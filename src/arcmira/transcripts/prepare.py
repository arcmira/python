# Maintained by hand. scripts/install-generated.py copies this to
# src/arcmira/transcripts/prepare.py and makes the generated transcripts
# clients inherit these mixins, so regeneration keeps prepare_and_wait.

from __future__ import annotations

import asyncio
import time
import typing
import uuid

from ..types.transcript_job import TranscriptJob
from ..types.transcript_result import TranscriptResult_Ready

if typing.TYPE_CHECKING:
    from .client import AsyncTranscriptsClient, TranscriptsClient

DEFAULT_POLL_SECONDS = 5


class PreparationError(Exception):
    """Base class for prepare_and_wait refusals that are not HTTP errors."""


class PreparationTimeoutError(PreparationError):
    """The Premium job was still pending when timeout_seconds ran out.

    The job keeps running. Read the transcript later, or poll `job.status_url`.
    """

    def __init__(self, job: TranscriptJob) -> None:
        super().__init__(f"Premium job {job.id} for {job.video_id} is still {job.status}")
        self.job = job


class PreparationFailedError(PreparationError):
    """The Premium job ended failed or refunded, or finished without a servable transcript."""

    def __init__(self, job: TranscriptJob) -> None:
        super().__init__(f"Premium job {job.id} for {job.video_id} ended {job.state}: {job.error or job.status}")
        self.job = job


class PremiumUnavailableError(PreparationError):
    """The account was served captions instead of Premium, so nothing can be prepared."""

    def __init__(self, transcript: TranscriptResult_Ready) -> None:
        super().__init__(f"Premium is not available for this account; the read returned {transcript.quality}")
        self.transcript = transcript


# One step of the plan. The sync and async clients run the same plan, so
# they cannot drift on when to submit, when to poll, or when to give up.
_READ, _SUBMIT, _STATUS, _SLEEP = "read", "submit", "status", "sleep"
_Step = typing.Tuple[str, typing.Any]


def _delay(response: typing.Any, job: TranscriptJob) -> float:
    header = response.response.headers.get("retry-after")
    if header is not None and header.strip().isdigit():
        return float(header)
    return float(job.next_poll_seconds if job.next_poll_seconds is not None else DEFAULT_POLL_SECONDS)


def _owned(transcript: typing.Any) -> TranscriptResult_Ready:
    if transcript.quality != "premium":
        raise PremiumUnavailableError(transcript)
    return transcript


def _plan(
    video_id: str, max_on_demand_cents: int, timeout_seconds: float
) -> typing.Generator[_Step, typing.Any, TranscriptResult_Ready]:
    if max_on_demand_cents < 0:
        raise ValueError("max_on_demand_cents cannot be negative")
    deadline = time.monotonic() + timeout_seconds
    read = yield (_READ, None)
    transcript = read.data
    if transcript.state == "ready":
        return _owned(transcript)
    if transcript.state == "pending":
        response, job = read, transcript.job
    else:
        submission: typing.Dict[str, typing.Any] = {"video_id": video_id}
        if max_on_demand_cents > 0:
            # Spending money is the only case that needs a key; one key serves this call and its own retries.
            submission.update(max_on_demand_cents=max_on_demand_cents, idempotency_key=str(uuid.uuid4()))
            if transcript.quote is not None:
                submission["max_rows"] = transcript.quote.rows
        response = yield (_SUBMIT, submission)
        job = response.data.job
    while job.state == "pending":
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise PreparationTimeoutError(job)
        yield (_SLEEP, min(_delay(response, job), remaining))
        response = yield (_STATUS, job.id)
        job = response.data
    if job.state != "ready":
        raise PreparationFailedError(job)
    final = (yield (_READ, None)).data
    if final.state != "ready":
        raise PreparationFailedError(job)
    return _owned(final)


class PrepareAndWait:
    def prepare_and_wait(
        self: TranscriptsClient,
        video_id: str,
        *,
        max_on_demand_cents: int = 0,
        timeout_seconds: float = 300,
    ) -> TranscriptResult_Ready:
        """
        Read the Premium transcript for a video, preparing it first when the account does not own it.

        Reads `quality="premium"`. A ready transcript is returned as is. When preparation is required,
        this posts `{video_id}` once, polls the job at the pace the API asks for, and returns the
        transcript when it is ready. The default spends included credits only and moves no money.
        A positive `max_on_demand_cents` authorizes that many cents of on-demand spend, and the call
        sends an Idempotency-Key and the quoted `max_rows`.

        Raises `PreparationTimeoutError` (carrying the job) when `timeout_seconds` pass first,
        `PreparationFailedError` when the job fails or is refunded, and `PremiumUnavailableError`
        when the plan has no Premium. API refusals raise `ApiError`.
        """
        plan = _plan(video_id, max_on_demand_cents, timeout_seconds)
        raw = self.with_raw_response
        try:
            step = next(plan)
            while True:
                kind, argument = step
                if kind == _SLEEP:
                    time.sleep(argument)
                    reply = None
                elif kind == _READ:
                    reply = raw.get(video_id, quality="premium")
                elif kind == _SUBMIT:
                    reply = raw.request(**argument)
                else:
                    reply = raw.status(argument)
                step = plan.send(reply)
        except StopIteration as done:
            return done.value


class AsyncPrepareAndWait:
    async def prepare_and_wait(
        self: AsyncTranscriptsClient,
        video_id: str,
        *,
        max_on_demand_cents: int = 0,
        timeout_seconds: float = 300,
    ) -> TranscriptResult_Ready:
        """
        Read the Premium transcript for a video, preparing it first when the account does not own it.

        The asynchronous twin of `Arcmira.transcripts.prepare_and_wait`; it takes the same arguments,
        follows the same plan and raises the same errors.
        """
        plan = _plan(video_id, max_on_demand_cents, timeout_seconds)
        raw = self.with_raw_response
        try:
            step = next(plan)
            while True:
                kind, argument = step
                if kind == _SLEEP:
                    await asyncio.sleep(argument)
                    reply = None
                elif kind == _READ:
                    reply = await raw.get(video_id, quality="premium")
                elif kind == _SUBMIT:
                    reply = await raw.request(**argument)
                else:
                    reply = await raw.status(argument)
                step = plan.send(reply)
        except StopIteration as done:
            return done.value
