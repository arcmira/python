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
from arcmira.errors import ForbiddenError, PaymentRequiredError
from arcmira.monitors import AddEntitiesRequestNamesItem
from arcmira.types.transcript_result import TranscriptResult_Pending, TranscriptResult_Ready

FIXTURES = json.loads((Path(__file__).parent / 'fixtures/transcription-responses.json').read_text())
PENDING = FIXTURES['pending_premium']['body']
REFUSED = FIXTURES['refused_quota']['body']
PAID_PLAN = FIXTURES['paid_plan_required']['body']
QUOTE = FIXTURES['quote_transcription']['body']
REQUEST = FIXTURES['list_transcriptions']['body']['requests'][0]
REFUNDED = {**FIXTURES['job_refunded']['body'], 'title': None}
ME = dict(user_id='usr_1', key_id='key_1', key_label='laptop', credential_kind='account_key', email_masked='z***@example.com', period_resets_at='2026-11-01T00:00:00Z', tier='ultra', scopes=['read'], rate_limit=60, recommendations_api_enabled=True, usage=dict(rows_used=1, rows_remaining=1, monthly_rows=1, current_spend_cents=0), settings=dict(transcripts=dict(quality='captions', language='en', timestamps=True)))

PAGE_CAP = 5
CURSOR = 'signed+/opaque==&cursor'
ENTITY = dict(id='ent_14', canonical_id='ent_14', name='Ramp', type='organization', is_canonical=True)
ENTITY_REF = dict(id='ent_14', name='Ramp', type='organization')
WINDOW = dict(after=None, before=None)
CALLS = []


def page(query, first, second):
    continued = 'cursor' in query
    return [second if continued else first], dict(has_more=not continued, next_cursor=None if continued else CURSOR)


def mention(video_id):
    return dict(id='men_' + video_id, entity=ENTITY_REF, media=dict(video_id=video_id), is_appearance=False, sentiment='neutral', start_seconds=0, end_seconds=20)


def monitor(id, body):
    return dict(id=id, name='Fixture', paused=body.get('paused', False), notify_emails=[], notify_webhook=False, notify_slack=False, created_at='2026-10-01T00:00:00Z', updated_at='2026-10-02T00:00:00Z', access='account', tracker_count=1)


def transcript(video_id, query):
    if video_id == 'pending0000':
        return 202, PENDING
    if video_id == 'quota000000':
        return 402, REFUSED
    if video_id == 'plan0000000':
        return 403, PAID_PLAN
    if query.get('quality') == ['premium']:
        return 200, FIXTURES['premium_ready']['body']
    return 200, FIXTURES['get_transcript']['body']


def route(method, path, query, body):
    parts = path.strip('/').split('/')
    if method == 'GET' and path.endswith('/quote'):
        return 200, QUOTE
    if method == 'GET' and parts[:2] == ['v1', 'transcripts']:
        return transcript(parts[2], query)
    if method == 'GET' and path == '/v1/entities/resolve':
        best = dict(ENTITY_REF, match='exact')
        return 200, dict(query=query['q'][0], context=None, confidence='exact', best=best, suggested=None, ask=None, candidates=[best], note='Fixture')
    if method == 'GET' and path == '/v1/transcriptions':
        requests, more = page(query, REQUEST, REFUNDED)
        return 200, dict(requests=requests, **more)
    if method == 'GET' and path.endswith('/videos'):
        episodes, more = page(query, *[dict(video_id=v, channel_id='UC-test', watch_url='https://arcmira.com/video/' + v) for v in ('video-1', 'video-2')])
        return 200, dict(channel=dict(youtube_channel_id='UC-test', name='Fixture'), episodes=episodes, returned=1, window=WINDOW, note='Fixture', **more)
    if method == 'GET' and path == '/v1/mentions':
        mentions, more = page(query, mention('video-1'), mention('video-2'))
        return 200, dict(mentions=mentions, entity=ENTITY, window=WINDOW, **more)
    if method == 'GET' and path == '/v1/recommendations':
        row = dict(id='com_1', entity=ENTITY_REF, media=dict(video_id='video-1'), confidence=0.9, speaker_role='host', start_seconds=10, end_seconds=40, **{'class': 'sponsored'})
        return 200, dict(recommendations=[row], entity=ENTITY, window=WINDOW, has_more=False, next_cursor=None)
    if method == 'POST' and parts[:2] == ['v1', 'monitors'] and parts[3:] == ['entities']:
        results = [dict(name=item['name'], type=item['type'], tracker_id='trk_' + str(index + 1), created=True, attached=True) for index, item in enumerate(body['names'])]
        return 200, dict(monitor_id=parts[2], results=results)
    if method == 'GET' and path == '/v1/me':
        return 200, dict(ME, account=dict(id='acc_1', name='Acme', kind='team', plan='ultra'), role='admin')
    if method == 'PATCH' and parts[:2] == ['v1', 'monitors']:
        return 200, dict(monitor=monitor(parts[2], body), message='Monitor updated.')
    return 404, dict(error=dict(type='not_found', code='not_found', message=f'No fixture for {method} {path}', doc_url='https://arcmira.com/docs/errors', request_id='fixture'))


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        self.answer()

    def do_POST(self):
        self.answer()

    def do_PATCH(self):
        self.answer()

    def answer(self):
        url = urlparse(self.path)
        query = parse_qs(url.query)
        raw = self.rfile.read(int(self.headers.get('Content-Length', 0))).decode()
        body = json.loads(raw) if raw else {}
        CALLS.append(dict(method=self.command, path=url.path, query=query, body=body))
        status, result = route(self.command, url.path, query, body)
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        if status == 202:
            self.send_header('Retry-After', str(result['job']['next_poll_seconds']))
        self.end_headers()
        self.wfile.write(json.dumps(result).encode())


def capped(pager):
    return list(itertools.islice(pager, PAGE_CAP))


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

    def calls_since(self, before, path):
        return [call for call in CALLS[before:] if call['path'] == path]

    def test_ready_read(self):
        ready = self.client.transcripts.with_raw_response.get('dQw4w9WgXcQ')
        self.assertEqual(ready.status_code, 200)
        self.assertIsInstance(ready.data, TranscriptResult_Ready)
        self.assertEqual(ready.data.quality, 'captions')
        self.assertEqual(ready.data.lines[0].text, FIXTURES['get_transcript']['body']['lines'][0]['text'])
        premium = self.client.transcripts.get('dQw4w9WgXcQ', quality='premium')
        self.assertIsInstance(premium, TranscriptResult_Ready)
        self.assertEqual(premium.quality, 'premium')
        self.assertEqual(premium.revision, FIXTURES['premium_ready']['body']['revision'])

    def test_premium_pending_carries_the_job_and_retry_after(self):
        before = len(CALLS)
        pending = self.client.transcripts.with_raw_response.get('pending0000', quality='premium')
        self.assertEqual(pending.status_code, 202)
        self.assertIsInstance(pending.data, TranscriptResult_Pending)
        self.assertEqual(pending.data.job.id, PENDING['job']['id'])
        self.assertEqual(pending.data.job.next_poll_seconds, PENDING['job']['next_poll_seconds'])
        self.assertEqual(pending.headers['retry-after'], str(PENDING['job']['next_poll_seconds']))
        sent = self.calls_since(before, '/v1/transcripts/pending0000')
        self.assertEqual([(call['method'], call['query']) for call in sent], [('GET', {'quality': ['premium']})])

    def test_premium_refusals_are_typed_errors_with_the_quote(self):
        for video_id, error_type, fixture in (('quota000000', PaymentRequiredError, REFUSED), ('plan0000000', ForbiddenError, PAID_PLAN)):
            with self.subTest(code=fixture['error']['code']):
                with self.assertRaises(error_type) as caught:
                    self.client.transcripts.get(video_id, quality='premium')
                error = caught.exception.body.error
                expected = fixture['error']
                self.assertIsInstance(caught.exception, ApiError)
                self.assertEqual((error.type, error.code, error.gate), (expected['type'], expected['code'], expected['gate']))
                self.assertEqual(error.unlock.tier, expected['unlock']['tier'])
                quote = error.details.quote
                self.assertEqual(quote.rows, expected['details']['quote']['rows'])
                self.assertEqual(quote.charge.amount, expected['details']['quote']['charge']['amount'])
                self.assertEqual(quote.max_on_demand_cents, expected['details']['quote']['max_on_demand_cents'])
                self.assertEqual(str(caught.exception), f"{caught.exception.status_code} {expected['code']}: {expected['message']}")

    def test_resolve_with_best_and_no_suggestion(self):
        before = len(CALLS)
        match = self.client.entities.resolve(q='Ramp', type='organization')
        self.assertEqual(self.calls_since(before, '/v1/entities/resolve')[0]['query'], {'q': ['Ramp'], 'type': ['organization']})
        self.assertEqual(match.best.id, 'ent_14')
        self.assertIsNone(match.suggested)

    def test_quote_passes_through(self):
        quote = self.client.transcripts.quote('dQw4w9WgXcQ')
        self.assertEqual(quote.quote.rows, QUOTE['quote']['rows'])
        self.assertEqual(quote.charge.amount, QUOTE['charge']['amount'])
        self.assertEqual(quote.max_on_demand_cents, QUOTE['max_on_demand_cents'])

    def test_pagers_follow_the_opaque_cursor(self):
        cases = (
            ('/v1/transcriptions', lambda: self.client.transcripts.list_requests(limit=1), lambda row: row.id, [REQUEST['id'], REFUNDED['id']]),
            ('/v1/channels/UC-test/videos', lambda: self.client.channels.videos.list('UC-test', limit=1), lambda row: row.video_id, ['video-1', 'video-2']),
            ('/v1/mentions', lambda: self.client.mentions.list(entity_id='ent_14', limit=1), lambda row: row.media.video_id, ['video-1', 'video-2']),
        )
        for path, pager, key, expected in cases:
            with self.subTest(path=path):
                before = len(CALLS)
                self.assertEqual([key(row) for row in capped(pager())], expected)
                continued = [call['query'] for call in self.calls_since(before, path) if 'cursor' in call['query']]
                self.assertEqual(len(continued), 1)
                self.assertEqual(continued[0]['cursor'], [CURSOR])
                self.assertEqual(continued[0]['limit'], ['1'])

    def test_refunded_request_row_parses(self):
        rows = capped(self.client.transcripts.list_requests(limit=1))
        self.assertEqual([row.state for row in rows], ['pending', 'refunded'])

    def test_mentions_send_entity_id_and_the_half_open_window(self):
        before = len(CALLS)
        rows = capped(self.client.mentions.list(entity_id='ent_14', channel_id='UC-test', after='2026-09-01', before='2026-09-02'))
        self.assertEqual(len(rows), 2)
        first = self.calls_since(before, '/v1/mentions')[0]['query']
        self.assertEqual(first, {'entity_id': ['ent_14'], 'channel_id': ['UC-test'], 'after': ['2026-09-01'], 'before': ['2026-09-02']})

    def test_recommendations_send_class(self):
        before = len(CALLS)
        rows = capped(self.client.recommendations.list(entity_id='ent_14', class_='sponsored'))
        self.assertEqual([row.class_ for row in rows], ['sponsored'])
        query = self.calls_since(before, '/v1/recommendations')[0]['query']
        self.assertEqual(query, {'entity_id': ['ent_14'], 'class': ['sponsored']})

    def test_monitor_entities_follow_an_exact_name(self):
        before = len(CALLS)
        added = self.client.monitors.entities.add('mon_1', names=[AddEntitiesRequestNamesItem(name='Ramp', type='organization')])
        self.assertEqual(self.calls_since(before, '/v1/monitors/mon_1/entities')[0]['body'], {'names': [{'name': 'Ramp', 'type': 'organization'}]})
        self.assertEqual([(row.name, row.attached) for row in added.results], [('Ramp', True)])
        self.assertFalse(hasattr(self.client.trackers, 'create'))

    def test_me_names_the_account_and_the_role(self):
        me = self.client.me.get()
        self.assertEqual((me.account.name, me.account.kind, me.role), ('Acme', 'team', 'admin'))

    def test_monitors_update_sends_paused(self):
        before = len(CALLS)
        updated = self.client.monitors.update('mon_1', paused=True)
        self.assertEqual(self.calls_since(before, '/v1/monitors/mon_1')[0]['body'], {'paused': True})
        self.assertTrue(updated.monitor.paused)

    def test_async_read_and_pagination(self):
        async def run():
            client = AsyncArcmira(api_key='local-test-key', base_url=self.base, max_retries=0, timeout=5)
            ready = await client.transcripts.get('dQw4w9WgXcQ')
            self.assertIsInstance(ready, TranscriptResult_Ready)
            pending = await client.transcripts.with_raw_response.get('pending0000', quality='premium')
            self.assertEqual(pending.status_code, 202)
            self.assertIsInstance(pending.data, TranscriptResult_Pending)
            self.assertEqual(pending.headers['retry-after'], str(PENDING['job']['next_poll_seconds']))
            with self.assertRaises(PaymentRequiredError) as caught:
                await client.transcripts.get('quota000000', quality='premium')
            self.assertEqual(caught.exception.body.error.details.quote.rows, REFUSED['error']['details']['quote']['rows'])
            rows = []
            async for row in await client.mentions.list(entity_id='ent_14', limit=1):
                rows.append(row.media.video_id)
                if len(rows) >= PAGE_CAP:
                    break
            self.assertEqual(rows, ['video-1', 'video-2'])
        asyncio.run(run())


if __name__ == '__main__':
    unittest.main()
