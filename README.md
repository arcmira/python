# Arcmira for Python

Pull YouTube transcripts, search spoken passages, and monitor company mentions with Arcmira. Results include timestamps and source links for research, citations, and agent workflows.

[Get an API key](https://arcmira.com/docs/authentication) · [API docs](https://arcmira.com/docs) · [Pricing](https://arcmira.com/pricing)

## Install

```sh
uv add arcmira
```

`pip install arcmira` works too. Set `ARCMIRA_API_KEY` to your API key. Save an example as `example.py` and run `python example.py` in your environment.

## Search clips and quotes in YouTube videos

Find spoken passages in YouTube videos and podcasts, then jump to the matching moment. Search a topic, company, or phrase.

```python
from urllib.parse import urljoin
from arcmira import Arcmira

client = Arcmira()
hits = client.transcripts.search(q="TSMC", limit=5)
for hit in hits.chunks:
    print(hit.text)
    print(urljoin("https://arcmira.com", hit.watch_url))
print(hits.note)
```

For a research workflow, [compare what Jensen Huang said about TSMC across two months](https://github.com/arcmira/python/blob/master/GUIDE.md#compare-a-speakers-comments-over-time). Filter by speaker and date, then inspect the quoted passages in context.

Search covers indexed transcripts within your plan's date window. Check `window`, `search_index`, and `note` before drawing conclusions from missing results.

## Transcribe a YouTube video

Start free with 1,000 credits a month, enough for up to 250 caption transcripts of videos up to 15 minutes each. Captions use 4 credits per started 15 minutes from the same balance as search and alerts. [Plans and usage](https://arcmira.com/pricing).

Pull an available YouTube caption track with timestamps. Replace the video id below with yours. For a new transcription of the audio with speaker labels, use Premium on a paid plan.

```python
from arcmira import Arcmira

client = Arcmira()
transcript = client.transcripts.get("dQw4w9WgXcQ")
if transcript.state == "ready":
    for line in transcript.lines or []:
        print(line.start, line.text)
```

Get a free cost estimate with `client.transcripts.quote(video_id)`, then read with `quality="premium"`. Premium uses credits from your plan, then your on-demand budget. If `pending`, poll after `job.next_poll_seconds`. [Premium states, polling, and retries](https://github.com/arcmira/python/blob/master/GUIDE.md#premium-transcripts).

## Set up YouTube monitoring for your company

Follow 2 names and get up to 40 alert deliveries a month on a free account, if you use all 1,000 monthly credits for alerts. Each delivery uses 25 credits. Get alerts by email or [Slack](https://arcmira.com/docs/monitors#delivery), or use a [webhook](https://arcmira.com/docs/monitors#verify-webhooks) on a paid plan.

Follow your company or a competitor in newly analyzed YouTube videos and podcasts. Replace `Ramp` and `you@example.com` below. External email recipients must confirm before delivery.

```python
from arcmira import Arcmira
from arcmira.monitors import AddEntitiesRequestNamesItem

client = Arcmira()
created = client.monitors.create(
    name="Company watch",
    notify_frequency="daily",
    notify_emails=["you@example.com"],
)
added = client.monitors.entities.add(
    created.monitor.id,
    names=[AddEntitiesRequestNamesItem(name="Ramp", type="organization")],
)
for result in added.results:
    print(result.tracker_id if result.attached else result.reason)
```

This creates a monitor and tracker in your account. Check each `attached` result. Alerts cover newly analyzed episodes published within the last 14 days. Multiple recipients or channels can use multiple deliveries per mention. For retries of writes, reuse the same `idempotency_key`.

## Choose the next task

| Task | SDK call |
| --- | --- |
| Find a company, person, or show | `entities.resolve(q=..., context=...)` |
| Read mentions of an entity | `mentions.list(entity_id=...)` |
| Find a channel's sponsors | `channels.sponsors.list(channel_id)` |
| Separate recommendations from paid mentions | `recommendations.list(entity_id=..., class_="organic")` |
| Read alerts from a monitor | `monitors.alerts.list(monitor_id)` |

Entity filters take ids. Resolve names first; explain a `suggested` match and ask the user when the resolver returns `ask`. Use `after` inclusive and `before` exclusive for date windows. Paginated methods fetch more rows as you iterate, so stop when you have enough.

`AsyncArcmira` provides the same methods asynchronously. Await the first page, then use `async for` for paginated results.

## Use with an AI agent

For tasks such as "pull YouTube transcripts", "find quotes with timestamps", "research podcast sponsors", or "monitor company mentions", connect the [Arcmira MCP server](https://github.com/arcmira/mcp). The [agent index](https://arcmira.com/llms.txt) links to current API and citation guidance.

## Reference

- [SDK guide](https://github.com/arcmira/python/blob/master/GUIDE.md): async examples, typed errors, pagination, and Premium polling.
- [Method reference](https://github.com/arcmira/python/blob/master/reference.md): request and response types for every method.
- [TypeScript and JavaScript SDK](https://github.com/arcmira/arcmira).
- [Release notes](https://github.com/arcmira/python/blob/master/CHANGELOG.md).

Requires Python 3.9+. Apache-2.0. [Source](https://github.com/arcmira/python) · [License](https://github.com/arcmira/python/blob/master/LICENSE).
