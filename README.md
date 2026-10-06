# Arcmira: YouTube Transcript Search

The official Python SDK for searching indexed YouTube transcripts. Find timestamped quotes, speaker appearances, mentions, sponsors and recommendations with synchronous and asynchronous clients, typed responses and cursor pagination.

[Arcmira](https://arcmira.com) · [API docs](https://arcmira.com/docs) · [OpenAPI schema](https://api.arcmira.com/v1/openapi.json) · [MCP setup](https://arcmira.com/docs/mcp-server)

```sh
pip install arcmira
```

Set `ARCMIRA_API_KEY` before you import the client, or pass `api_key` to it.

## First call

Reads take ids. Resolve a name to an id, then read with the id.

```python
from arcmira import Arcmira

client = Arcmira()
match = client.entities.resolve(q="Ramp", type="organization")
ramp = match.best or match.suggested
if ramp is None:
    raise LookupError(match.note)
for mention in client.mentions.list(entity_id=ramp.id, after="2026-09-01", before="2026-10-01"):
    print(mention.media.video_id, mention.start_seconds, mention.description)
```

`entities.resolve` answers one of three ways. `best` is a certain match. `suggested` is the likeliest row, with a reason, when no row is certain. `ask` lists the options when several rows fit, and `best` and `suggested` are both `None`. For a show, pass `type="channel"` and use `best.youtube_channel_id` as `channel_id`.

A name where an id belongs raises `BadRequestError` with the code `id_required`. Its message names the parameter and the resolve call.

## Dates

Every dated read takes `after` and `before`. The window is half-open, `[after, before)`. Each accepts an ISO date (`2026-09-01`) or a datetime with an offset (`2026-09-01T00:00:00Z`), read in UTC. Each dated read echoes the window it applied in `window`.

## Premium transcripts

A Premium read is one call. It answers 200 `ready` when the account owns the transcript. Otherwise it starts transcribing the whole video and answers 202 `pending` with the job. The read uses credits from your plan, then your on-demand budget. You set that budget in the dashboard, and it is the approval, so the call takes no price ceiling.

Read again after `Retry-After`. Repeated reads join the same job and never use credits twice.

```python
import time
from arcmira import Arcmira

client = Arcmira()
for _ in range(60):
    read = client.transcripts.with_raw_response.get("dQw4w9WgXcQ", quality="premium")
    if read.data.state == "ready":
        for line in read.data.lines:
            print(line.start, line.text)
        break
    if read.data.state == "failed":
        raise RuntimeError(f"{read.data.last_attempt.status}: {read.data.last_attempt.error}")
    time.sleep(int(read.headers.get("retry-after") or read.data.job.next_poll_seconds or 10))
else:
    raise TimeoutError("Still processing. Resume the same Premium read later.")
```

The timeout only stops this polling loop. It does not cancel the job. Resume with the same video id and `quality="premium"`; do not set `retry=True` while the job is pending.

`read.data` is a `TranscriptResult`, discriminated on `state`. `ready` carries the transcript. `pending` carries `job`, with `eta_seconds`, `next_poll_seconds` and `charge`. `failed` means the last transcription failed or was refunded; it carries `job` and `last_attempt` and uses no credits. `retry=True` transcribes it again and uses credits again. Without `with_raw_response`, `client.transcripts.get(...)` returns the same union without the status and headers.

A quote is free and changes nothing.

```python
quote = client.transcripts.quote("dQw4w9WgXcQ")
print(quote.quote.rows, quote.charge.amount, quote.charge.from_, quote.max_on_demand_cents)
```

`client.transcripts.list_requests()` lists past Premium transcriptions with their state.

A read without `quality="premium"` returns captions and starts no transcription.

## Errors

A refusal raises a typed error from `arcmira.errors`. Each derives from `arcmira.core.api_error.ApiError` and carries `status_code`, `headers` and `body`. `body.error` holds `type`, `code`, `message`, `param`, `gate`, `unlock`, `details`, `doc_url` and `request_id`. Switch on `type` and `gate` first. Codes inside a type can grow.

| Status | Error | Example codes |
|---|---|---|
| 400 | `BadRequestError` | `invalid_query`, `id_required`, `invalid_cursor` |
| 401 | `UnauthorizedError` | `invalid_api_key` |
| 402 | `PaymentRequiredError` | `quota_exceeded`, `spend_limit_exceeded` |
| 403 | `ForbiddenError` | `paid_plan_required`, `freshness_requires_paid` |
| 404 | `NotFoundError` | `entity_not_found` |
| 409 | `ConflictError` | `tracker_already_exists` |
| 429 | `TooManyRequestsError` | `rate_limited` |
| 500, 503 | `InternalServerError`, `ServiceUnavailableError` | |

A priced refusal carries the price in `error.details.quote`. Nothing is charged.

```python
from arcmira.errors import ForbiddenError, PaymentRequiredError

try:
    client.transcripts.get("dQw4w9WgXcQ", quality="premium")
except (PaymentRequiredError, ForbiddenError) as refusal:
    error = refusal.body.error
    print(error.code, error.details.quote.rows, error.unlock.url)
```

`str(refusal)` reads `402 quota_exceeded: <message>`. A duplicate tracker carries the existing id in `error.details.existing_id`.

## Pagination

`mentions.list`, `recommendations.list`, `channels.videos.list` and `transcripts.list_requests` return pagers. Iterate them and they follow `next_cursor` for you. Cursors are opaque. Keep the filters the same between pages.

```python
for episode in client.channels.videos.list("UC-DRzaGnL_vtBUpCFH5M0tg", limit=10):
    print(episode.video_id)
```

Each page body names its rows: `mentions`, `recommendations`, `episodes` or `requests`. The alert lists (`monitors.alerts.list`, `trackers.alerts.list`) return one page of `alerts`, newest first. Pass a larger `limit` to read further.

## Async

`AsyncArcmira` has the same methods to await. Paginated methods return async iterators after you await the first page.

```python
from arcmira import AsyncArcmira

async def ramp_sponsorships():
    client = AsyncArcmira()
    async for row in await client.recommendations.list(entity_id="ent_14", class_="sponsored"):
        print(row.class_, row.media.video_id, row.start_seconds)
```

`class` is a Python keyword, so the parameter and the field are spelled `class_`. The wire name stays `class`.

## Methods

Each method has the full parameter list in the [generated reference](reference.md).

| Group | Methods |
|---|---|
| `entities` | `resolve`, `get`, `momentum` |
| `mentions` | `list`, `count` |
| `recommendations` | `list` |
| `transcripts` | `search`, `get`, `quote`, `list_requests` |
| `channels` | `coverage`, `videos.list`, `sponsors.list` |
| `monitors` | `list`, `create`, `update`, `delete`, `rotate_webhook_secret`, `trackers.list`, `trackers.add`, `entities.add`, `alerts.list` |
| `trackers` | `list`, `create`, `update`, `delete`, `alerts.list` |
| `integrations` | `slack.list` |
| `feedback` | `submit`, `get` |
| `me` | `get`, `update_settings` |
| `health` | `check` |

`transcripts.search` returns spoken passages from `GET /v1/search`. Its filters take ids too.

To follow an entity you have an id for, call `monitors.entities.add(monitor_id, entity_ids=["ent_14"])`. To watch an exact name before it is indexed, call `trackers.create(entity_name="Ramp", entity_type="organization")`. A channel tracker takes the YouTube channel id as `entity_name`.

See [CHANGELOG.md](CHANGELOG.md) for what changed from 0.3.

## Agents

The [Arcmira MCP server](https://github.com/arcmira/mcp) gives AI agents the same data at `https://mcp.arcmira.com/mcp`. [llms.txt](llms.txt) describes this package for agents.

## Regenerate and verify

Run `bash scripts/generate.sh` with Node 22 or newer, Python 3, Docker, and Fern access for the `arcmira` organization. Generation pins Fern CLI 5.131.1 and Python generator 5.31.0, disables CLI version redirection and telemetry, and reads `fern/openapi.json`. `fern/method-names.json` names the group and method of every operation by operationId. An operation without a name, or a name for an operation the document lacks, fails the build. The overlay combines the transcript read's success schemas into `TranscriptResult` and rejects unknown or ambiguous cursor collections. Generated source is never edited by hand. `scripts/overrides/api_error.py` holds the `ApiError` text, and the installer copies it back after every generation.

```sh
uv sync
uv run python -m unittest discover -s tests -v
uv build
```

The tests use a local HTTP server that returns the bodies the API sends. They check both client variants, the ready and pending reads, typed refusals with their quote, the query and body each call sends, and opaque pagination. They need no live API key and use no credits.

## License

Apache-2.0. See [LICENSE](./LICENSE).
