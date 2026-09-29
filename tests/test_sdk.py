import os
import subprocess
import sys

import pytest

from arcmira import Arcmira, NotFoundError, PaymentRequiredError
from arcmira.core.api_error import ApiError

from fake_v1 import Fake


@pytest.fixture(scope="module")
def fake():
    server = Fake()
    yield server
    server.close()


@pytest.fixture(scope="module")
def client(fake):
    return Arcmira(api_key="test-key", base_url=fake.base_url)


def test_sends_the_bearer_key_and_the_sdk_user_agent(fake, client):
    client.me.get()
    assert fake.last["headers"]["authorization"] == "Bearer test-key"
    assert fake.last["headers"]["user-agent"] == "arcmira/0.2.0"
    assert fake.last["headers"]["x-fern-sdk-version"] == "0.2.0"


def test_falls_back_to_arcmira_api_key_from_the_environment(fake):
    # The default is read when arcmira is imported, so the variable is set in a fresh interpreter.
    code = f"from arcmira import Arcmira; Arcmira(base_url={fake.base_url!r}).me.get()"
    subprocess.run([sys.executable, "-c", code], check=True, env={**os.environ, "ARCMIRA_API_KEY": "env-key"})
    assert fake.last["headers"]["authorization"] == "Bearer env-key"


def test_search_returns_typed_chunks(fake, client):
    hits = client.transcripts.search(q="agent payments", limit=5)
    assert hits.query == "agent payments"
    assert hits.chunks[0].text == "agent payments on air"
    assert fake.last["query"] == {"q": "agent payments", "limit": "5"}


def test_a_paged_list_walks_next_cursor_to_the_end(fake, client):
    before = len(fake.requests)
    ids = [m.id for m in client.mentions.list(entity_id="ent_14")]
    assert ids == ["men_1", "men_2", "men_3"]
    pages = fake.requests[before:]
    assert len(pages) == 2
    assert pages[1]["query"]["cursor"] == "c2"


def test_a_write_sends_a_json_body(fake, client):
    created = client.monitors.create(name="Ramp", notify_frequency="daily")
    assert fake.last["method"] == "POST"
    assert fake.last["body"] == {"name": "Ramp", "notifyFrequency": "daily"}
    assert created.monitor.name == "Ramp"


def test_a_plan_gate_is_a_typed_payment_required_error(client):
    with pytest.raises(PaymentRequiredError) as raised:
        client.entities.momentum("ent_gated")
    err = raised.value
    assert isinstance(err, ApiError)
    assert err.status_code == 402
    assert err.body.error.gate == "plan"
    assert err.body.error.code == "usage_limit_exceeded"
    assert err.body.error.unlock.url == "https://arcmira.com/pricing?src=sdk"


def test_a_404_is_a_typed_not_found_error(client):
    with pytest.raises(NotFoundError) as raised:
        client.transcripts.get("missingvid0")
    assert raised.value.body.error.code == "transcript_unavailable"


def test_an_entity_page_list_404_carries_the_v1_envelope(client):
    with pytest.raises(NotFoundError) as raised:
        client.people.related.topics("nobody")
    assert raised.value.body.error.type == "not_found"
    assert raised.value.body.error.code == "entity_not_found"


def test_transcript_requests_live_on_transcripts(fake, client):
    assert not hasattr(client, "transcriptions")
    order = client.transcripts.request(video_id="dQw4w9WgXcQ", idempotency_key="order-1")
    assert fake.last["method"] == "POST"
    assert fake.last["path"] == "/v1/transcriptions"
    assert fake.last["headers"]["idempotency-key"] == "order-1"
    assert fake.last["body"] == {"videoId": "dQw4w9WgXcQ"}
    assert order.request.id is not None
    state = client.transcripts.status(order.request.id)
    assert fake.last["path"] == f"/v1/transcriptions/{order.request.id}"
    assert state.next_poll_seconds == 30
