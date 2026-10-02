# Arcmira Python SDK

The official Python client for the [Arcmira API](https://arcmira.com/docs), with synchronous and asynchronous clients, typed responses, and cursor pagination.

```sh
pip install arcmira
```

Set `ARCMIRA_API_KEY` or pass `api_key` to the client.

## Premium quickstart

```python
from arcmira import Arcmira

transcript = Arcmira().transcripts.prepare_and_wait("dQw4w9WgXcQ")
print(transcript.lines)
```

`prepare_and_wait(video_id, *, max_on_demand_cents=0, timeout_seconds=300)` reads the Premium transcript and returns it. When your account does not own it yet, the call posts `{video_id}` to `/v1/transcriptions` once, polls the job at the pace the API sets with `Retry-After` and `next_poll_seconds`, and reads the finished transcript. The default spends included credits only and sends no `Idempotency-Key`. Preparation purchases the whole video, even if you only read a window.

`AsyncArcmira` has the same method: `await client.transcripts.prepare_and_wait(video_id)`.

Errors you can handle:

- `PreparationTimeoutError` when the job outlasts `timeout_seconds`. It carries `.job`, and the job keeps running.
- `PreparationFailedError` when the job fails or is refunded. It carries `.job`.
- `PremiumUnavailableError` when the plan has no Premium. The read returned captions, and they are never returned as Premium.
- `ApiError` for any API refusal, such as `quota_exceeded`, with the public error and recovery URLs in `body`.

To spend money, pass a cents ceiling you have approved. The call then sends the quoted `max_rows` and a generated `Idempotency-Key`.

```python
client = Arcmira()
transcript = client.transcripts.prepare_and_wait("dQw4w9WgXcQ", max_on_demand_cents=25)
```

## Lower-level calls

A quote is free. GET never purchases Premium, and each state is typed.

```python
client = Arcmira()
quote = client.transcripts.quote(video_id="dQw4w9WgXcQ")
print(quote.quote.rows, quote.charge)

result = client.transcripts.with_raw_response.get(video_id="dQw4w9WgXcQ", quality="premium")
if result.data.state == "ready":
    print(result.data.lines)
elif result.data.state == "preparation_required":
    print(result.data.quote, result.data.action)
else:
    print(result.data.job.status_url, result.data.job.next_poll_seconds)
print(result.status_code, result.headers)
```

To prepare without waiting, post the purchase and poll the job yourself. Every purchase answers one `Job`. `idempotency_key` is optional while `max_on_demand_cents` is 0: without one, a purchase already open or owned for the video is returned with `existing: true`. `max_on_demand_cents` defaults to zero. A positive amount requires both `idempotency_key` and `max_rows`, and a retry with the same saved key and exact input returns the same job with the `Idempotency-Replayed` header.

```python
order = client.transcripts.with_raw_response.request(video_id="dQw4w9WgXcQ")
print(order.status_code, order.data.job.state)
job = client.transcripts.status(order.data.job.id)
```

A refusal raises a typed error derived from `arcmira.core.api_error.ApiError`. Its `body` retains the public error, quote, and recovery URLs. `refund_pending` is unfinished; a refund is complete only when the job reports `refunded`.

```python
for job in client.transcripts.list_requests(limit=10):
    print(job.id, job.state)
for episode in client.channels.videos.list(channel_id="UC-DRzaGnL_vtBUpCFH5M0tg", limit=10):
    print(episode.video_id)
```

Pagination follows the actual `requests` and `episodes` arrays. Cursors remain opaque and filters stay the same between pages.

For asynchronous calls, use `AsyncArcmira` and await the same methods. Paginated methods return async iterators after awaiting the initial page.

```python
from arcmira import AsyncArcmira

async def history():
    client = AsyncArcmira()
    async for request in await client.transcripts.list_requests(limit=10):
        print(request.id)
```

See the [generated reference](reference.md) for all endpoints.

## Regenerate and verify

Run `bash scripts/generate.sh` with Node 22 or newer, Python 3, Docker, and Fern access for the `arcmira` organization. Generation pins Fern CLI 5.131.1 and Python generator 5.31.0, disables CLI version redirection and telemetry, and reads `fern/openapi.json`. The overlay combines distinct success schemas and rejects unknown or ambiguous cursor collections. Generated source is never edited by hand. `scripts/overrides/` holds the hand-written pieces the installer copies back after every generation: the `ApiError` text and `prepare_and_wait`.

```sh
uv sync
uv run python -m unittest discover -s tests -v
uv build
```

The tests use a local HTTP server that returns the bodies the API sends. They check both client variants, state discrimination, `prepare_and_wait`, response status, quotes, refusals, replay input, and opaque pagination. No live API key or purchase is required.

Version 0.3.0 replaces the earlier URL-only placeholder with a usable SDK. The public URL constants remain available.

## License

Apache-2.0. See [LICENSE](./LICENSE).
