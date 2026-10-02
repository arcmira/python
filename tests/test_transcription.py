import asyncio
import itertools
import json
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from arcmira import Arcmira, AsyncArcmira
from arcmira.core.api_error import ApiError
from arcmira.types.transcript_result import TranscriptResult_Ready, TranscriptResult_Pending

FIXTURES = json.loads((Path(__file__).parent / 'fixtures/transcription-responses.json').read_text())
QUOTE = FIXTURES['quote_transcription']['body']
REQUEST = FIXTURES['get_transcription']['body']
def error(code, kind):
    return dict(type=kind, code=code, message=code, doc_url='https://arcmira.com/docs/errors', request_id='fixture-request')

PAGE_CAP = 5
CURSOR = 'signed+/opaque==&cursor'
PENDING = dict(state='pending', quality='premium', premium_job=dict(job_id=REQUEST['id'], status='queued', next_poll_seconds=5), status_url='/v1/transcriptions/'+REQUEST['id'], next_poll_seconds=5)
CALLS = []
RECEIPTS = {}

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        self.answer()

    def do_POST(self):
        self.answer()

    def answer(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)
        body = self.rfile.read(int(self.headers.get('Content-Length', 0))).decode()
        CALLS.append((url.path, query, dict(self.headers), body, self.command))
        status, extra = 200, {}
        if url.path.endswith('/quote'):
            result = QUOTE
        elif url.path == '/v1/transcriptions' and self.command == 'POST':
            key = self.headers['Idempotency-Key']
            replay = key in RECEIPTS
            if key is None:
                status, result = 400, {'error': error('idempotency_key_required', 'invalid_request_error')}
            elif replay and RECEIPTS[key] != body:
                status, result = 409, {'error': error('idempotency_conflict', 'conflict_error')}
            else:
                RECEIPTS[key] = body
                status = 200 if replay else 202
                result = {'request': REQUEST, **({'existing': True} if replay else {})}
                if replay: extra['Idempotency-Replayed'] = 'true'
        elif url.path == '/v1/transcriptions':
            result = {'requests': [{**REQUEST, 'id': 'request-2' if 'cursor' in query else 'request-1'}], 'has_more': 'cursor' not in query, 'next_cursor': None if 'cursor' in query else CURSOR}
        elif '/channels/' in url.path:
            episode = dict(video_id='video-2' if 'cursor' in query else 'video-1', channel_id='UC-test', watch_url='https://arcmira.com/video/test')
            result = dict(channel={'youtube_channel_id':'UC-test','name':'Fixture'}, episodes=[episode], returned=1, has_more='cursor' not in query, next_cursor=None if 'cursor' in query else CURSOR, indexed_through=None, index_age_days=None, as_of=None, note='Fixture')
        elif url.path.endswith('/pending0000'):
            status, result = 202, PENDING
        elif url.path.endswith('/refused0000'):
            status, result = 403, {'error': error('purchase_required', 'permission_error'), 'quote': QUOTE, 'prepare_url': '/v1/transcriptions'}
        else:
            result = FIXTURES['get_transcript']['body']
        self.send_response(status)
        for name, value in {'Content-Type': 'application/json', 'Retry-After': '5', **extra}.items(): self.send_header(name, value)
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())

class GeneratedClientTests(unittest.TestCase):
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

    def test_ready_pending_status_and_union(self):
        ready = self.client.transcripts.with_raw_response.get(video_id='dQw4w9WgXcQ')
        self.assertIsInstance(ready.data, TranscriptResult_Ready)
        self.assertEqual(ready.status_code, 200)
        self.assertTrue(ready.data.lines)
        pending = self.client.transcripts.with_raw_response.get(video_id='pending0000', quality='premium')
        self.assertIsInstance(pending.data, TranscriptResult_Pending)
        self.assertEqual(pending.status_code, 202)
        self.assertEqual(pending.data.status_url, PENDING['status_url'])
        self.assertEqual(pending.headers['retry-after'], '5')

    def test_quote_and_refusal(self):
        quote = self.client.transcripts.quote(video_id='dQw4w9WgXcQ')
        self.assertEqual(quote.quote.rows, QUOTE['quote']['rows'])
        with self.assertRaises(ApiError) as caught:
            self.client.transcripts.get(video_id='refused0000', quality='premium')
        self.assertEqual(caught.exception.status_code, 403)
        self.assertEqual(caught.exception.body.quote, QUOTE)
        self.assertEqual(str(caught.exception), '403 purchase_required: purchase_required')
        self.assertNotIn('headers', str(caught.exception))

    def test_preparation_exact_intent_replay_and_required_key(self):
        intent = dict(video_id='dQw4w9WgXcQ', max_rows=300, max_on_demand_cents=0, idempotency_key='python-saved-intent')
        first = self.client.transcripts.with_raw_response.request(**intent)
        replay = self.client.transcripts.with_raw_response.request(**intent)
        sent = [call[2]['Idempotency-Key'] for call in CALLS if call[0] == '/v1/transcriptions' and call[4] == 'POST' and 'Idempotency-Key' in call[2]]
        self.assertEqual(sent[-2:], ['python-saved-intent', 'python-saved-intent'])
        self.assertEqual(first.status_code, 202)
        self.assertEqual(replay.status_code, 200)
        self.assertEqual(replay.data.request.id, first.data.request.id)
        self.assertTrue(replay.data.existing)
        self.assertEqual(replay.headers['idempotency-replayed'], 'true')
        self.assertEqual(json.loads(CALLS[-1][3]), dict(videoId='dQw4w9WgXcQ', max_rows=300, max_on_demand_cents=0))
        with self.assertRaises(ApiError) as caught:
            self.client.transcripts.request(**{**intent, 'max_rows':600})
        self.assertEqual(caught.exception.status_code, 409)
        with self.assertRaises(TypeError):
            self.client.transcripts.request(video_id='dQw4w9WgXcQ', max_rows=300)

    def test_request_and_episode_arrays_preserve_opaque_cursor(self):
        before = len(CALLS)
        capped = lambda pager: list(itertools.islice(pager, PAGE_CAP))
        self.assertEqual([x.id for x in capped(self.client.transcripts.list_requests(limit=1))], ['request-1','request-2'])
        self.assertEqual([x.video_id for x in capped(self.client.channels.videos.list(channel_id='UC-test', limit=1))], ['video-1','video-2'])
        continued = [call for call in CALLS[before:] if 'cursor' in call[1]]
        self.assertEqual(len(continued), 2)
        for call in continued:
            self.assertEqual(call[1]['cursor'], [CURSOR])
            self.assertEqual(call[1]['limit'], ['1'])

    def test_async_pending_and_pagination(self):
        async def run():
            client = AsyncArcmira(api_key='local-test-key', base_url=self.base, max_retries=0, timeout=5)
            pending = await client.transcripts.with_raw_response.get(video_id='pending0000', quality='premium')
            self.assertEqual(pending.status_code, 202)
            self.assertIsInstance(pending.data, TranscriptResult_Pending)
            rows = []
            async for row in await client.transcripts.list_requests(limit=1):
                rows.append(row.id)
                if len(rows) >= PAGE_CAP: break
            self.assertEqual(rows, ['request-1','request-2'])
        asyncio.run(run())

if __name__ == '__main__': unittest.main()
