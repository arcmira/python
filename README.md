# Arcmira for Python

Pull YouTube transcripts, search spoken passages, and monitor company mentions with Arcmira. Results include timestamps and source links for research, citations, and agent workflows.

[Get an API key](https://arcmira.com/docs/authentication) · [API docs](https://arcmira.com/docs) · [Pricing](https://arcmira.com/pricing)

## Install

```sh
uv add arcmira
```

`pip install arcmira` works too. Set `ARCMIRA_API_KEY` to your API key. Save an example as `example.py` and run `python example.py` in your environment.

## Search YouTube videos and podcast transcripts for quotes and clips

Find what people are saying about a company, product, or idea across YouTube videos and podcasts. Search phrases such as `GPU demand`, `GPU financing`, or `inference costs`; narrow by speaker, company, channel, or date as your question develops. Start with GPU demand over the last 60 days.

```python
from datetime import datetime, timedelta, timezone
from urllib.parse import urljoin
from arcmira import Arcmira

client = Arcmira()
query = "GPU demand"

# Search the last 60 days.
now = datetime.now(timezone.utc)
after = (now - timedelta(days=60)).isoformat()
before = now.isoformat()

hits = client.transcripts.search(q=query, after=after, before=before, limit=20)
print(f"\n{query} ({len(hits.chunks)} passages)")
print(
    f"{(hits.window.after or 'unknown')[:10]} - "
    f"{(hits.window.before or 'unknown')[:10]}\n"
)
for i, hit in enumerate(hits.chunks, 1):
    print(f"{i:02d}\n{hit.text}\n")
    print(f"Video:      {hit.video_title or hit.video_id}")
    print(f"Channel:    {hit.channel_name or 'Unknown'}")
    print(f"Published:  {(hit.published_at or 'Unknown')[:10]}")
    print(f"Transcript: {hit.source_label or 'Unknown'}")
    print(f"Watch:      {urljoin('https://arcmira.com', hit.watch_url)}\n--\n")

```

**Sample console output**

The script prints every returned passage in full. Below is an excerpt from result 13 of the October 16, 2026 run, wrapped for readability. `...` marks omitted output. Your results will vary.

```text
GPU demand (20 passages)
2026-08-17 - 2026-10-16

...

13
...
John Coogan: What is the next couple months even look like for CPU demand in the
data center?
Cristiano Amon: Okay, let me separate that conversation into— I think one, one
topic is there's so much more demand for compute than availability right now and
across the board.
Cristiano Amon: So I think what we're seeing this right now and by the way, as a
semiconductor company, I'll tell you, this supply chain, it's operating at 100%
capacity, everything Everything is short because there's so much more demand

Video:      Jensen vs NYT, New Model Reactions, Saudi EVs, You Can See
            Everything
Channel:    TBPN
Published:  2026-09-23
Transcript: Arcmira Premium
Watch:      https://arcmira.com/watch?v=wDWgNOpna90&t=2428
--

...
```


Use `hits.chunks` directly for further analysis; the logging above is for inspection.

**Find evidence that could change your mind.** Strong demand is the beginning of the investigation. Follow the other results into customer commitments, margins, and financing, compare conflicting claims, and build a research brief with timestamped sources.

Learn how to [investigate a research question with YouTube video and podcast transcript search in our Guide](https://github.com/arcmira/python/blob/master/GUIDE.md#investigate-a-research-question-with-youtube-video-and-podcast-transcript-search).

Give your agent access to the latest indexed conversations, speaker-labeled Premium transcripts, and company alerts. The most up-to-date coverage is only available via paid plans, starting at $20/month. [Try Pro free for 7 days at no risk.](https://arcmira.com/pricing) Put Arcmira to work on a real research question, then keep it only if it earns a place in your research stack.

Not ready for a paid plan? [Tell us why and what you would pay for](https://arcmira.com/docs/feedback#not-ready-for-a-paid-plan). Feedback is free to give and helps us build what you want.

Search covers indexed transcripts within your plan's date window. Missing a source you care about? [Help shape the index](https://arcmira.com/docs/feedback#help-shape-the-index) with the channels or industries you need and what better coverage would make possible.

## Transcribe a YouTube video

Start free with 1,000 credits a month, enough for up to 250 caption transcripts of videos up to 15 minutes each. Captions use 4 credits per started 15 minutes from the same balance as search and alerts. [Plans and usage](https://arcmira.com/pricing).

Pull an available YouTube caption track with timestamps. Replace the video id below with yours.

**Keep the names your research depends on.** Misheard company and product names can send an agent to the wrong entity. In a spelling-based review across 167 tech and finance videos, name disagreements favored Premium over YouTube automatic captions by about 21:1. Use Premium for speaker labels and research where names matter.

This measures the tested name disagreements, not overall word accuracy. [How we measured this](https://arcmira.com/docs/transcript-name-comparison).

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

Follow 2 names and get up to 40 alerts a month on a free account, if you use all 1,000 monthly credits for alerts. Each alert uses 25 credits once per occurrence, regardless of delivery channels or recipients. Get alerts as new mentions are analyzed, by email or [Slack](https://arcmira.com/docs/monitors#delivery), or use a [webhook](https://arcmira.com/docs/monitors#verify-webhooks) on a paid plan.

Follow your company or a competitor in newly analyzed YouTube videos and podcasts. Replace `PlanetScale` and `you@example.com` below. External email recipients must confirm before delivery.

```python
from arcmira import Arcmira
from arcmira.monitors import AddEntitiesRequestNamesItem

client = Arcmira()
created = client.monitors.create(
    name="Company watch",
    notify_frequency="realtime",
    notify_emails=["you@example.com"],
)
added = client.monitors.entities.add(
    created.monitor.id,
    names=[AddEntitiesRequestNamesItem(name="PlanetScale", type="organization")],
)
for result in added.results:
    print(result.tracker_id if result.attached else result.reason)
```

This creates a monitor and tracker in your account. Check each `attached` result. Alerts cover newly analyzed episodes published within the last 14 days. For retries of writes, reuse the same `idempotency_key`.

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

## Use Arcmira with an AI agent

For tasks such as "pull YouTube transcripts", "find quotes with timestamps", "research podcast sponsors", or "monitor company mentions", connect the [Arcmira MCP server](https://github.com/arcmira/mcp). The [agent index](https://arcmira.com/llms.txt) links to current API and citation guidance.

## Reference

- [SDK guide](https://github.com/arcmira/python/blob/master/GUIDE.md): async examples, typed errors, pagination, and Premium polling.
- [Method reference](https://github.com/arcmira/python/blob/master/reference.md): request and response types for every method.
- [TypeScript and JavaScript SDK](https://github.com/arcmira/arcmira).
- [Release notes](https://github.com/arcmira/python/blob/master/CHANGELOG.md).

Requires Python 3.9+. Apache-2.0. [Source](https://github.com/arcmira/python) · [License](https://github.com/arcmira/python/blob/master/LICENSE).
