# Arcmira for Python

Pull YouTube transcripts, search spoken passages, and monitor company mentions with Arcmira. Results include timestamps and source links for research, citations, and agent workflows.

[Get an API key](https://arcmira.com/docs/authentication) · [API docs](https://arcmira.com/docs) · [Pricing](https://arcmira.com/pricing)

## Install

```sh
uv add arcmira
```

`pip install arcmira` works too. Set `ARCMIRA_API_KEY` to your API key. Save an example as `example.py` and run `python example.py` in your environment.

## Find quotes with source links

Search YouTube and podcast transcripts by topic. Keep the source link beside each quote so readers can check the original.

```python
from urllib.parse import urljoin
from arcmira import Arcmira

client = Arcmira()
hits = client.transcripts.search(q="agent payments", limit=5)
for hit in hits.chunks:
    print(hit.text)
    print(urljoin("https://arcmira.com", hit.watch_url))
print(hits.note)
```

Search covers indexed transcripts within your plan's date window. Check `window`, `search_index`, and `note` before treating an empty result as evidence that nobody said it.

## Pull a YouTube transcript

Read available captions with timestamps. Replace the video id with the video you need.

```python
from arcmira import Arcmira

client = Arcmira()
transcript = client.transcripts.get("dQw4w9WgXcQ")
if transcript.state == "ready":
    for line in transcript.lines or []:
        print(line.start, line.text)
```

For a Premium transcript with speaker labels, first call `client.transcripts.quote(video_id)` for a free quote, then read with `quality="premium"`. A Premium read uses credits from your plan, then your on-demand budget. It may return `pending`; poll after `job.next_poll_seconds`. A `failed` result needs an explicit retry. [Premium states and polling](https://github.com/arcmira/python/blob/master/GUIDE.md#premium-transcripts).

## Monitor company mentions

Follow an exact name in newly analyzed media, even before it is indexed. Replace `you@example.com` with your alert address. External recipients must confirm before delivery.

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

This creates a monitor and tracker in your account. Creation is free; delivered alerts use credits from your plan, then your on-demand budget. Check each `attached` result because a name may already belong to another monitor. For retries of writes, reuse the same `idempotency_key`.

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
