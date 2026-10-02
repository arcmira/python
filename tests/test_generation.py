import copy
import json
import runpy
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = runpy.run_path(str(ROOT / 'scripts/prepare-openapi.py'))

class GenerationTests(unittest.TestCase):
    def test_unknown_and_ambiguous_cursor_collections_fail(self):
        for props in ({'mystery': {'type':'array'}}, {'requests':{'type':'array'}, 'episodes':{'type':'array'}}):
            with self.assertRaisesRegex(ValueError, 'Unknown or ambiguous'):
                TOOLS['collection']({}, {'properties': props})

    def test_actual_contract_generates_union_key_and_collections(self):
        doc = json.loads((ROOT / 'fern/openapi.json').read_text())
        before = copy.deepcopy(doc)
        prepared = TOOLS['prepare'](doc, json.loads((ROOT / 'fern/method-names.json').read_text()))
        self.assertEqual(doc, before)
        union = prepared['components']['schemas']['TranscriptResult']
        self.assertEqual(union['discriminator']['propertyName'], 'state')
        self.assertEqual(set(union['discriminator']['mapping']), {'ready','preparation_required','pending'})
        for path, collection in [('/v1/transcriptions','requests'),('/v1/channels/{channel_id}/videos','episodes')]:
            self.assertEqual(prepared['paths'][path]['get']['x-fern-pagination']['results'], '$response.'+collection)
        post = prepared['paths']['/v1/transcriptions']['post']
        self.assertFalse(next(p for p in post['parameters'] if p['name']=='Idempotency-Key').get('required'))
        body = post['requestBody']['content']['application/json']['schema']
        self.assertNotIn('videoId', body['properties'])
        self.assertNotIn('max_rows', body.get('required', []))
        self.assertEqual(post['x-fern-sdk-method-name'], 'request')

    def test_installed_api_error_matches_the_preserved_override(self):
        self.assertEqual((ROOT / 'src/arcmira/core/api_error.py').read_text(), (ROOT / 'scripts/overrides/api_error.py').read_text())
        self.assertIn('overrides/api_error.py', (ROOT / 'scripts/install-generated.py').read_text())

    def test_installed_prepare_and_wait_matches_the_preserved_override(self):
        self.assertEqual((ROOT / 'src/arcmira/transcripts/prepare.py').read_text(), (ROOT / 'scripts/overrides/prepare.py').read_text())
        client = (ROOT / 'src/arcmira/transcripts/client.py').read_text()
        self.assertIn('class TranscriptsClient(PrepareAndWait):', client)
        self.assertIn('class AsyncTranscriptsClient(AsyncPrepareAndWait):', client)

if __name__ == '__main__': unittest.main()
