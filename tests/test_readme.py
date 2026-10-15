import contextlib
import io
import json
import re
import unittest
from pathlib import Path
from unittest.mock import patch

import httpx
from arcmira import Arcmira

ROOT = Path(__file__).resolve().parents[1]
RESPONSES = json.loads((ROOT / 'tests/fixtures/readme-responses.json').read_text())


class ReadmeTests(unittest.TestCase):
    def test_examples_return_quotes_captions_and_attached_tracker(self):
        requests = []
        routes = {
            ('GET', '/v1/search'): 'search',
            ('GET', '/v1/transcripts/dQw4w9WgXcQ'): 'get_transcript',
            ('POST', '/v1/monitors'): 'create_monitor',
            ('POST', '/v1/monitors/mon_2/entities'): 'add_entities',
        }
        def respond(request):
            requests.append(request)
            return httpx.Response(200, json=RESPONSES[routes[(request.method, request.url.path)]])
        with httpx.Client(transport=httpx.MockTransport(respond)) as http:
            client = Arcmira(api_key='fixture-key', httpx_client=http, max_retries=0)
            output = io.StringIO()
            examples = re.findall(r'```python\n(.*?)```', (ROOT / 'README.md').read_text(), re.S)
            self.assertEqual(len(examples), 3)
            with patch('arcmira.Arcmira', return_value=client), contextlib.redirect_stdout(output):
                for code in examples:
                    exec(compile(code, 'README.md', 'exec'), {})
        printed = output.getvalue().splitlines()
        self.assertIn('agent payments on air', printed)
        self.assertIn('https://arcmira.com/watch?v=dQw4w9WgXcQ&t=1', printed)
        self.assertIn('0.0 Welcome back to the show.', printed)
        self.assertIn('trk_200', printed)
        self.assertEqual([(r.method, r.url.path) for r in requests], list(routes))
        self.assertEqual(dict(requests[0].url.params), dict(q='agent payments', limit='5'))
        self.assertEqual(json.loads(requests[2].content), dict(name='Company watch', notify_frequency='daily', notify_emails=['you@example.com']))
        self.assertEqual(json.loads(requests[3].content), dict(names=[dict(name='Ramp', type='organization')]))
        self.assertTrue(all(r.headers['Authorization'] == 'Bearer fixture-key' for r in requests))
