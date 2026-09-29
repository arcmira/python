# Arcmira for Python

The official `arcmira` package: a typed client for the [Arcmira API](https://arcmira.com/docs). Arcmira is the search engine for the spoken web: it indexes YouTube and podcast transcripts and answers who said what, where, and when.

- Sync and async clients (`Arcmira`, `AsyncArcmira`) on `httpx`, with `pydantic` models and `py.typed`.
- Every list pages itself. Every error is a typed exception carrying the parsed API body.
- Full API scope: search, transcripts, mentions, momentum, sponsors and recommendations, monitors, trackers, team, transcriptions, corrections and feedback.
- Python 3.9 and later.

## Install

```sh
pip install arcmira
```

Get a key at [arcmira.com/docs/authentication](https://arcmira.com/docs/authentication) and set `ARCMIRA_API_KEY` before importing the package, or pass `api_key` to the client.

## Quickstart

```python
from arcmira import Arcmira, PaymentRequiredError

client = Arcmira()  # or Arcmira(api_key="...")

# Who is "Ramp"? Names, handles, URLs and channel ids resolve to typed rows with stable ids.
found = client.entities.search(q="Ramp", limit=3)
ramp = found.data[0]
print(ramp.id, ramp.type, ramp.page)

# Spoken slices that answer a phrase.
hits = client.transcripts.search(q="agent payments", limit=5)
for chunk in hits.chunks:
    print(chunk.channel_name, chunk.watch_url, chunk.text)

# Catalog rows page themselves: iterate and the client follows next_cursor.
for mention in client.mentions.list(entity_id=ramp.id, limit=50):
    print(mention.media.title, mention.start_seconds)

# Gates and failures are typed. The body is the API's error object.
try:
    momentum = client.entities.momentum(ramp.id)
    print(momentum.verdict, momentum.volume)
except PaymentRequiredError as err:
    print(err.body.error.gate, err.body.error.unlock and err.body.error.unlock.url)
```

Async, same surface:

```python
import asyncio
from arcmira import AsyncArcmira

async def main():
    client = AsyncArcmira()
    hits = await client.transcripts.search(q="agent payments", limit=5)
    print([c.watch_url for c in hits.chunks])

asyncio.run(main())
```

Every method is listed with its parameters and return types in [reference.md](./reference.md). The same operations, with `curl` samples, are in the [API reference](https://arcmira.com/docs/api-reference).

### Field names

Attributes are snake_case. Where the API sends camelCase (monitors, trackers, alerts and transcription rows) the model aliases it, so `monitor.notify_frequency` reads the wire's `notifyFrequency`.

### Errors

Every non-2xx answer raises a subclass of `arcmira.core.api_error.ApiError` named for the status: `BadRequestError`, `UnauthorizedError`, `PaymentRequiredError`, `ForbiddenError`, `NotFoundError`, `ConflictError`, `TooManyRequestsError`, `InternalServerError` and so on, importable from `arcmira`. `err.status_code` is the status and `err.body.error` the API's error object: `type`, `code`, `message`, `doc_url`, `request_id`, and on a plan gate `gate` and `unlock.url`. Switch on `type` and `gate` first; `code` is a string whose catalog is in the [errors page](https://arcmira.com/docs/errors).

### Options

`Arcmira(api_key=..., base_url=..., timeout=..., follow_redirects=..., httpx_client=...)`. The `api_key` default is read from `ARCMIRA_API_KEY` when the module is imported.

## Command line

The TypeScript package ships the `arcmira` command line, whose commands mirror the tools of the [Arcmira MCP server](https://github.com/arcmira/mcp): `npx arcmira search "agent payments"`. See [github.com/arcmira/arcmira](https://github.com/arcmira/arcmira#command-line).

## Links

- Docs: https://arcmira.com/docs
- API reference: https://arcmira.com/docs/api-reference
- TypeScript SDK and CLI: https://github.com/arcmira/arcmira (`npm install arcmira`)
- MCP server for agents: https://github.com/arcmira/mcp, what it does: https://arcmira.com/mcp
- Developers page: https://arcmira.com/developers
- Agent index: https://arcmira.com/llms.txt

## Development

`src/arcmira/` is generated from the Arcmira OpenAPI document by [Fern](https://github.com/fern-api/fern); do not edit it by hand, a regeneration overwrites it. `tests/` and this file are hand-written. `pytest` runs the tests against a local fake of the API (`tests/fake_v1.py`, bodies in `tests/fixtures/v1.json`).

## License

Apache-2.0. See [LICENSE](./LICENSE).
