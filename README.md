# Arcmira Python SDK

The official Python client for the [Arcmira API](https://arcmira.com/docs), with synchronous and asynchronous clients, typed responses, and cursor pagination.

```sh
pip install arcmira
```

Set `ARCMIRA_API_KEY` or pass `api_key` to the client.

```python
from arcmira import Arcmira

client = Arcmira()
quote = client.transcripts.quote(video_id="dQw4w9WgXcQ")
print(quote.quote.rows, quote.charge)
```

A quote is free. Preparation purchases the whole video, even if you later read a short window. Persist the intent before submitting it. Choose ceilings after reviewing the quote and authorizing the cost.

```python
intent = dict(
    video_id="dQw4w9WgXcQ",
    max_rows=300,
    max_on_demand_cents=0,
    idempotency_key="saved-order-dQw4w9WgXcQ-1",
)
order = client.transcripts.with_raw_response.request(**intent)
print(order.status_code, order.data.request.state)
```

`idempotency_key` and `max_rows` are required. `max_on_demand_cents` defaults to zero. If the response is lost, retry with the same saved key and exact input. The response retains `{request, existing?}` and the `Idempotency-Replayed` header. A changed intent with the same key returns `409 idempotency_conflict`.

GET never purchases Premium. A ready read includes transcript lines. A pending read includes a status URL and polling delay.

```python
result = client.transcripts.with_raw_response.get(
    video_id="dQw4w9WgXcQ", quality="premium"
)
if result.data.state == "ready":
    print(result.data.lines)
else:
    print(result.data.status_url, result.data.next_poll_seconds)
print(result.status_code, result.headers)
```

A refusal raises a typed error derived from `arcmira.core.api_error.ApiError`. Its `body` retains the public error, quote, and recovery URLs. `refund_pending` is unfinished; a refund is complete only when the request reports `refunded`.

```python
for request in client.transcripts.list_requests(limit=10):
    print(request.id, request.state)
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

Run `bash scripts/generate.sh` with Node 22 or newer, Python 3, Docker, and Fern access for the `arcmira` organization. Generation pins Fern CLI 5.131.1 and Python generator 5.31.0, disables CLI version redirection and telemetry, and reads `fern/openapi.json`. The overlay combines distinct success schemas and rejects unknown or ambiguous cursor collections. Generated source is never edited by hand.

```sh
uv sync
uv run python -m unittest discover -s tests -v
uv build
```

The tests use a local HTTP server. They check both client variants, state discrimination, response status, quotes, refusals, exact replay input, and opaque pagination. No live API key or purchase is required.

Version 0.3.0 replaces the earlier URL-only placeholder with a usable SDK. The public URL constants remain available.
