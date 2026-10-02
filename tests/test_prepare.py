import asyncio
import json
import threading
import types
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest import mock
from urllib.parse import parse_qs, urlparse

from arcmira import (
    Arcmira,
    AsyncArcmira,
    PreparationFailedError,
    PreparationTimeoutError,
    PremiumUnavailableError,
)
from arcmira.core.api_error import ApiError
from arcmira.transcripts import prepare
from arcmira.types.transcript_result import TranscriptResult_Ready

FIXTURES = json.loads((Path(__file__).parent / 'fixtures/transcription-responses.json').read_text())
body = lambda name: FIXTURES[name]['body']
VIDEO = 'dQw4w9WgXcQ'
JOB = body('get_transcription')['id']
READ = f'/v1/transcripts/{VIDEO}'
SUBMIT = '/v1/transcriptions'
POLL = f'/v1/transcriptions/{JOB}'
PRICE_REFUSED = {'error': {'type': 'permission_error', 'code': 'spend_limit_exceeded', 'message': 'The spend limit would be exceeded.', 'doc_url': 'https://arcmira.com/docs/errors', 'request_id': 'fixture-request'}}


def reply(name, status=200, retry_after=None):
    return status, retry_after, body(name)


class Handler(BaseHTTPRequestHandler):
    script = {}
    calls = []

    def log_message(self, *args):
        pass

    def do_GET(self):
        self.answer()

    def do_POST(self):
        self.answer()

    def answer(self):
        path = urlparse(self.path).path
        payload = self.rfile.read(int(self.headers.get('Content-Length', 0))).decode()
        Handler.calls.append((self.command, path, parse_qs(urlparse(self.path).query), dict(self.headers), payload))
        queue = Handler.script[(self.command, path)]
        status, retry_after, result = queue.pop(0) if len(queue) > 1 else queue[0]
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        if retry_after is not None:
            self.send_header('Retry-After', str(retry_after))
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())


class FakeClock:
    def __init__(self):
        self.now = 0.0
        self.slept = []

    def monotonic(self):
        return self.now

    def sleep(self, seconds):
        self.slept.append(seconds)
        self.now += seconds


class PrepareAndWaitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'
        cls.client = Arcmira(api_key='local-test-key', base_url=cls.base, max_retries=0, timeout=5)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        Handler.calls = []
        self.clock = FakeClock()
        patches = [
            mock.patch.object(prepare, 'time', self.clock),
            mock.patch.object(prepare, 'asyncio', types.SimpleNamespace(sleep=self.async_sleep)),
        ]
        for patch in patches:
            patch.start()
            self.addCleanup(patch.stop)

    async def async_sleep(self, seconds):
        self.clock.sleep(seconds)

    def script(self, **routes):
        Handler.script = {
            ('GET', READ): routes['read'],
            ('POST', SUBMIT): routes.get('submit', [reply('submit_pending', 202)]),
            ('GET', POLL): routes.get('poll', [reply('job_ready')]),
        }

    def requests(self, method, path):
        return [call for call in Handler.calls if call[0] == method and call[1] == path]

    def assert_zero_dollar_post(self):
        (_, _, _, headers, payload), = self.requests('POST', SUBMIT)
        self.assertEqual(json.loads(payload), {'video_id': VIDEO})
        self.assertNotIn('Idempotency-Key', headers)

    def test_ready_returns_the_owned_transcript_without_posting(self):
        self.script(read=[reply('premium_ready')])
        transcript = self.client.transcripts.prepare_and_wait(VIDEO)
        self.assertIsInstance(transcript, TranscriptResult_Ready)
        self.assertEqual((transcript.quality, transcript.rows_billed), ('premium', 0))
        self.assertEqual([line.speaker for line in transcript.lines], [0, 1])
        self.assertEqual(self.requests('GET', READ)[0][2], {'quality': ['premium']})
        self.assertEqual(self.requests('POST', SUBMIT), [])
        self.assertEqual(self.clock.slept, [])

    def test_preparation_required_posts_once_polls_and_reads_the_transcript(self):
        self.script(
            read=[reply('preparation_required'), reply('premium_ready')],
            poll=[reply('get_transcription', retry_after=3), reply('job_ready')],
        )
        transcript = self.client.transcripts.prepare_and_wait(VIDEO)
        self.assertEqual(transcript.quality, 'premium')
        self.assert_zero_dollar_post()
        self.assertEqual(len(self.requests('GET', POLL)), 2)
        self.assertEqual(len(self.requests('GET', READ)), 2)
        self.assertEqual(self.clock.slept, [29, 3])

    def test_a_pending_read_polls_the_job_without_posting(self):
        self.script(
            read=[reply('pending_premium', 202, retry_after=5), reply('premium_ready')],
            poll=[reply('job_ready')],
        )
        self.assertEqual(self.client.transcripts.prepare_and_wait(VIDEO).quality, 'premium')
        self.assertEqual(self.requests('POST', SUBMIT), [])
        self.assertEqual(self.clock.slept, [5])

    def test_a_ready_submission_skips_polling(self):
        self.script(read=[reply('preparation_required'), reply('premium_ready')], submit=[reply('submit_ready')])
        self.client.transcripts.prepare_and_wait(VIDEO)
        self.assertEqual(self.requests('GET', POLL), [])
        self.assertEqual(self.clock.slept, [])

    def test_money_sends_the_quoted_max_rows_and_one_idempotency_key(self):
        self.script(read=[reply('preparation_required'), reply('premium_ready')])
        self.client.transcripts.prepare_and_wait(VIDEO, max_on_demand_cents=25)
        (_, _, _, headers, payload), = self.requests('POST', SUBMIT)
        self.assertEqual(json.loads(payload), {'video_id': VIDEO, 'max_rows': 300, 'max_on_demand_cents': 25})
        self.assertRegex(headers['Idempotency-Key'], r'^[0-9a-f-]{36}$')

    def test_a_pending_job_that_outlasts_the_timeout_raises_with_the_job(self):
        self.script(read=[reply('preparation_required')], poll=[reply('get_transcription')])
        with self.assertRaises(PreparationTimeoutError) as caught:
            self.client.transcripts.prepare_and_wait(VIDEO, timeout_seconds=40)
        self.assertEqual(caught.exception.job.id, JOB)
        self.assertEqual(caught.exception.job.state, 'pending')
        self.assertEqual(self.clock.slept, [29, 11])

    def test_a_refunded_job_raises_and_never_reposts(self):
        self.script(read=[reply('preparation_required')], poll=[reply('job_refunded')])
        with self.assertRaises(PreparationFailedError) as caught:
            self.client.transcripts.prepare_and_wait(VIDEO)
        self.assertEqual((caught.exception.job.state, caught.exception.job.error), ('refunded', 'Transcription timed out.'))
        self.assertEqual(len(self.requests('POST', SUBMIT)), 1)

    def test_captions_are_never_returned_for_a_premium_ask(self):
        self.script(read=[reply('get_transcript')])
        with self.assertRaises(PremiumUnavailableError) as caught:
            self.client.transcripts.prepare_and_wait(VIDEO)
        self.assertEqual(caught.exception.transcript.quality, 'captions')

    def test_an_api_refusal_surfaces_as_api_error(self):
        self.script(read=[reply('preparation_required')], submit=[(402, None, PRICE_REFUSED)])
        with self.assertRaises(ApiError) as caught:
            self.client.transcripts.prepare_and_wait(VIDEO, max_on_demand_cents=25)
        self.assertEqual(str(caught.exception), '402 spend_limit_exceeded: The spend limit would be exceeded.')

    def test_negative_cents_are_refused_before_any_request(self):
        with self.assertRaises(ValueError):
            self.client.transcripts.prepare_and_wait(VIDEO, max_on_demand_cents=-1)
        self.assertEqual(Handler.calls, [])

    def test_async_client_follows_the_same_plan(self):
        async def run():
            client = AsyncArcmira(api_key='local-test-key', base_url=self.base, max_retries=0, timeout=5)
            self.script(
                read=[reply('preparation_required'), reply('premium_ready')],
                poll=[reply('get_transcription', retry_after=3), reply('job_ready')],
            )
            transcript = await client.transcripts.prepare_and_wait(VIDEO)
            self.assertEqual(transcript.quality, 'premium')
            self.assert_zero_dollar_post()
            self.assertEqual(self.clock.slept, [29, 3])

            self.script(read=[reply('preparation_required')], poll=[reply('get_transcription')])
            Handler.calls.clear()
            self.clock.slept.clear()
            with self.assertRaises(PreparationTimeoutError) as caught:
                await client.transcripts.prepare_and_wait(VIDEO, timeout_seconds=40)
            self.assertEqual(caught.exception.job.id, JOB)

            self.script(read=[reply('preparation_required'), reply('premium_ready')])
            Handler.calls.clear()
            await client.transcripts.prepare_and_wait(VIDEO, max_on_demand_cents=25)
            (_, _, _, headers, payload), = self.requests('POST', SUBMIT)
            self.assertEqual(json.loads(payload)['max_rows'], 300)
            self.assertIn('Idempotency-Key', headers)
        asyncio.run(run())


if __name__ == '__main__':
    unittest.main()
