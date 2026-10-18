# Arcmira SDK Guide (Python)

Search YouTube video and podcast transcripts, read the surrounding conversation, and follow company mentions with the Arcmira Python SDK. Use synchronous or asynchronous clients with typed responses.

[Arcmira](https://arcmira.com) · [API docs](https://arcmira.com/docs) · [OpenAPI schema](https://api.arcmira.com/v1/openapi.json) · [MCP setup](https://arcmira.com/docs/mcp-server)

We recommend [uv](https://docs.astral.sh/uv/) as your Python package manager:

```sh
uv add arcmira
```

(`pip install arcmira` works too.)

Set `ARCMIRA_API_KEY` before you import the client, or pass `api_key` to it.

[Investigate a research question](#investigate-a-research-question-with-youtube-video-and-podcast-transcript-search) · [Read a Premium transcript](#premium-transcripts) · [SDK building blocks](#arcmira-sdk-building-blocks)

## Investigate a research question with YouTube video and podcast transcript search

Find evidence that could change your mind. Continue the [README](README.md#search-youtube-videos-and-podcast-transcripts-for-quotes-and-clips)'s `GPU demand` search. The TBPN passage gives you a starting claim: compute demand exceeds supply. The next question is whether that demand becomes profitable, funded capacity. Search company mentions, executive interviews, and expert commentary to test what could support or challenge that thesis.

With the [Arcmira MCP server](https://arcmira.com/docs/mcp-server) connected, ask your agent:

> Investigate the semiconductor investment thesis using the last 60 days of public conversations. Look for changes in demand, customer commitments, financing, and usable capacity. Find evidence for and against each explanation, cite the original moments, and verify material claims against filings and earnings disclosures.

### Search the next question

Keep the search broad enough to find customers and suppliers outside the first interview. Start with `GPU financing`, then try `compute margins` or `capacity commitments` as the evidence develops. This example searches the latest 60 days and prints up to 20 full passages, using the same layout as the [README](README.md#search-youtube-videos-and-podcast-transcripts-for-quotes-and-clips).

```python
from datetime import datetime, timedelta, timezone
from urllib.parse import urljoin
from arcmira import Arcmira

client = Arcmira()
query = "GPU financing"

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

Excerpt from result 20 of the October 17, 2026 run. The script prints full passages; `...` marks omitted output here.

```text
GPU financing (20 passages)
2026-08-18 - 2026-10-17

...

20
...
Gavin Baker: And then also, like, we should also talk if particularly if you're
buying NVIDIA GPUs to a lesser extent TPUs, you can finance these.
David George: Yes.
David George: And there's a very sophisticated, you know, yeah, it's a very low
cost of capital to finance 'em today.
Gavin Baker: Yeah.
Gavin Baker: And everybody's, you know, worked up about, you know, circularity
and it's like, well, I don't know.
Gavin Baker: I know a lot of smart people who work at Blackstone and KKR and
Apollo, and they're the ones that are financing it.

Video:      Why AI Demand Is Outrunning Compute Supply
Channel:    a16z
Published:  2026-08-31
Transcript: Arcmira Premium
Watch:      https://arcmira.com/watch?v=FGC4ofTcg2k&t=760
--
```

### Read the surrounding exchange

Result 20 in this capture points to a financing counterargument. Choose the result number you want from your own output; ranks and results change. The next block continues the same script and prints the surrounding transcript with speaker names and start/end seconds.

Premium uses credits from your plan, then your on-demand budget. It reads the full video even though this example prints only nearby lines. Get a free estimate with `client.transcripts.quote` first; see [Premium states, polling, and retries](https://arcmira.com/docs/transcripts).

```python
# Choose a result from the output above. This capture uses result 20.
selected_number = 20
if not 1 <= selected_number <= len(hits.chunks):
    raise ValueError("Choose a result number from your search.")
selected = hits.chunks[selected_number - 1]

transcript = client.transcripts.get(
    selected.video_id, quality="premium", timestamps=True,
)
if transcript.state == "ready":
    names = {speaker.id: speaker.name for speaker in transcript.speakers or []}
    start = max(0, (selected.start_seconds or 0) - 30)
    end = (selected.start_seconds or 0) + 120
    print(f"Video: {transcript.video.title}\n")
    for line in transcript.lines or []:
        if line.end <= start or line.start >= end:
            continue
        speaker = names.get(line.speaker, "Unknown speaker")
        print(f"{line.start} - {line.end} seconds | {speaker}")
        print(f"{line.text}\n")
elif transcript.state == "pending":
    print(f"Try again in {transcript.job.next_poll_seconds} seconds.")
else:
    print(transcript.last_attempt.error)
```

**Sample transcript output**

Excerpt from the same video, beyond the search passage. Wording is unchanged; lines are wrapped for readability.

```text
Video: Why AI Demand Is Outrunning Compute Supply

...

825.1 - 827.32 seconds | David George
They're the ones who are financing it at a relatively low cost.

827.32 - 829.28 seconds | Gavin Baker
At a relatively low cost.

829.28 - 833.94 seconds | Gavin Baker
And I think one reason that's happening is useful lives just keep getting
extended.

833.94 - 843.42 seconds | Gavin Baker
And as these models get better and better and better and the ROI on token spend
goes up, you know, the monetization rate per gigawatt goes up.

843.42 - 852.53 seconds | Gavin Baker
So I mean, the true equity payback like might be way inside of a year.

...
```

The surrounding exchange adds an assumption: useful GPU lifetimes keep extending. That gives you something concrete to test against depreciation schedules, rental prices, utilization, and financing terms. Preserve the distinction between what the speakers claim and what you have verified.

### Follow the speaker

The captured result identifies Gavin Baker as `ent_158280`. Resolve the name to get the current ID rather than guessing it, then use `by` to find his comments on the same topic. The returned `speakers_by` field is another source of these public person IDs.

```python
person = client.entities.resolve(
    q="Gavin Baker",
    type="person",
    context="Technology investor discussing GPU financing",
)
if person.best is None:
    raise LookupError("Confirm the person before continuing.")
print(f"Speaker: {person.best.name} ({person.best.id})")

related = client.transcripts.search(
    q=query, by=person.best.id, after=after, before=before, limit=20,
)
print(f"{query} ({len(related.chunks)} passages)")
for hit in related.chunks:
    print(f"\n{hit.text}\n")
    print(f"Published: {(hit.published_at or 'Unknown')[:10]}")
    print(f"Watch:     {hit.watch_url}\n--")
```

```text
Speaker: Gavin Baker (ent_158280)
GPU financing (3 passages)
...
```

This output is from the same captured window; your count may differ. A search filter uses the public entity ID. In a transcript response, `line.speaker` is a local numeric ID joined to `transcript.speakers`, as the preceding example shows.

Follow the companies and terms you discover, seek counterevidence, and deduplicate repeated clips before comparing sources.

Search and transcript reads use credits from your plan. See [Plans and usage](https://arcmira.com/docs/usage-and-billing). Publication dates can differ from recording dates. An empty search does not prove that a risk is absent. If coverage leaves a gap in your research, [tell us what you need](#help-shape-the-index).

Give your agent access to the latest indexed conversations, speaker-labeled Premium transcripts, and company alerts. The most up-to-date coverage is only available via paid plans, starting at $20/month. [Try Pro free for 7 days at no risk.](https://arcmira.com/pricing) Put Arcmira to work on a real research question, then keep it only if it earns a place in your research stack.

Not ready for a paid plan? [Tell us why and what you would pay for](https://arcmira.com/docs/feedback#not-ready-for-a-paid-plan). Feedback is free to give and helps us build what you want.

[Continue this investment research example workflow](https://arcmira.com/docs/workflows/investment-research). You will learn how to test competing explanations, compare demand with margins and financing, verify claims against disclosures, and turn the evidence into a research brief.

## Compare a speaker's comments over time

Resolve Jensen Huang as NVIDIA's CEO, then compare several topics across two adjacent 30-day windows. Replace the person and topics to investigate another executive, expert, or supplier.

```python
from datetime import datetime, timedelta, timezone
from urllib.parse import urljoin
from arcmira import Arcmira

client = Arcmira()
match = client.entities.resolve(
    q="Jensen Huang", type="person", context="NVIDIA CEO",
)
if match.best is None:
    raise LookupError(match.ask or match.suggested or match.note)

now = datetime.now(timezone.utc)
day = timedelta(days=1)
windows = [
    (now - 60 * day, now - 30 * day),
    (now - 30 * day, now),
]
for start, end in windows:
    for q in ["TSMC", "GPU demand", "capacity"]:
        hits = client.transcripts.search(
            q=q, by=match.best.id, limit=20,
            after=start.isoformat(), before=end.isoformat(),
        )
        print(f"\n{q} ({len(hits.chunks)} passages)")
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

If there is no certain match, confirm the person before continuing. The `by` filter relies on speaker labels, which cover only part of the index. Want better coverage of a speaker or show? [Help us prioritize it](#help-shape-the-index).

Ask whether the newer passages add a commitment, name a constraint, or repeat an existing view. Check recording dates and earlier disclosures before concluding that a position changed.

## Help shape the index

We want to build the index around work that matters to you. Use [`client.feedback.submit`](https://github.com/arcmira/python/blob/master/reference.md#feedback) with `type: "experience"`, `category: "missing"`, and `notes` describing the coverage you need. Include source links, your workflow, and how much better coverage would be worth to you and others doing similar work. Use `category: "other"` for a broader capability request.

Feedback is free to give and helps us prioritize the coverage and workflows you need. Keep it coming as your needs evolve. Your requests help us decide what to index and improve next. You can also [ask your agent to send feedback](https://arcmira.com/docs/feedback#help-shape-the-index).

## Dates

Every dated read takes `after` and `before`. The window is half-open, `[after, before)`. Each accepts an ISO date (`2026-09-01`) or a datetime with an offset (`2026-09-01T00:00:00Z`), read in UTC. Each dated read echoes the window it applied in `window`.

## Premium transcripts

A Premium read is one call. It answers 200 `ready` when the account owns the transcript. Otherwise it starts transcribing the whole video and answers 202 `pending` with the job. The read uses credits from your plan, then your on-demand budget. You set that budget in the dashboard, and Arcmira enforces it, so the call takes no spending amount.

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

Check `read.data.state` before using the result:

| State | Next step |
| --- | --- |
| `ready` | Use the transcript and speaker labels. |
| `pending` | Wait for `Retry-After` or `job.next_poll_seconds`, then repeat the same read. The `job` also carries `eta_seconds` and `charge`. |
| `failed` | Inspect `last_attempt`. To start a new transcription, pass `retry=True` once, then omit it while polling. This uses credits again. |

A failed or refunded attempt returns `failed` without using credits until you request a retry. Without `with_raw_response`, `client.transcripts.get(...)` returns the same result without status and headers.

A quote is free and changes nothing.

```python
quote = client.transcripts.quote("dQw4w9WgXcQ")
print(quote.quote.rows, quote.charge.amount, quote.charge.from_, quote.max_on_demand_cents)
```

`client.transcripts.list_requests()` lists past Premium transcriptions with their state.

A read without `quality="premium"` returns captions and starts no transcription.

<a id="first-call"></a>

## Arcmira SDK building blocks

### Find mentions of an entity

Find where people discuss a person, company, product, or topic. This example uses a company, PlanetScale.

```python
from datetime import datetime, timedelta, timezone
from urllib.parse import urlencode, urljoin
from arcmira import Arcmira

client = Arcmira()
resolved = client.entities.resolve(
    q="PlanetScale", type="organization", context="Database platform",
)
company = resolved.best or resolved.suggested
if company is None:
    raise LookupError("Confirm the company before continuing.")
if resolved.suggested:
    print(f"Assuming {company.name}.")
print(f"Company: {company.name} ({company.id})")

# Look back over the last 60 days.
now = datetime.now(timezone.utc)
after = (now - timedelta(days=60)).isoformat()
before = now.isoformat()

for i, mention in enumerate(client.mentions.list(
    entity_id=company.id, after=after, before=before, limit=5,
), 1):
    print(f"\n{mention.description or 'No description available.'}\n")
    print(f"Video:     {mention.media.title or mention.media.video_id}")
    print(f"Published: {(mention.media.published_at or 'Unknown')[:10]}")
    params = {"v": mention.media.video_id}
    if mention.start_seconds is not None:
        params["t"] = str(mention.start_seconds)
    print(f"Watch:     https://arcmira.com/watch?{urlencode(params)}\n--")
    if i == 5:
        break
```

`best` is a certain match. `suggested` is a likely match; state the assumption when using it. If the resolver returns `ask`, confirm the company before continuing. Entity filters take IDs. Date windows include `after` and exclude `before`.

List methods fetch more pages as you iterate. This example stops after five mentions.

### Find a person's appearances

Find a person's media appearances across YouTube and podcasts. Arcmira records appearances as a type of mention, so the same `mentions.list` method finds both appearances and mentions by others.

| `is_appearance` | For a person, returns |
| --- | --- |
| `True` | Their appearances |
| `False` | Mentions of them by others |
| Omitted | Both |

Continue with the same `client`, `after`, and `before` to find Scott Wu's appearances in the last 60 days. Each result is an indexed video; separate clips from an interview can appear as separate results.

```python
person_match = client.entities.resolve(q="Scott Wu", type="person")
person = person_match.best or person_match.suggested
if person is None:
    raise LookupError("Confirm the person before continuing.")
if person_match.suggested:
    print(f"Assuming {person.name}.")
print(f"\nAppearances: {person.name}\n")

for i, appearance in enumerate(client.mentions.list(
    entity_id=person.id, is_appearance=True, after=after, before=before, limit=5,
), 1):
    media = appearance.media
    channel = media.source_channel
    print(f"Video:     {media.title or media.video_id}")
    print(f"Channel:   {channel.name if channel else 'Unknown'}")
    print(f"Published: {(media.published_at or 'Unknown')[:10]}")
    params = {"v": media.video_id}
    print(f"Watch:     https://arcmira.com/watch?{urlencode(params)}\n--\n")
    if i == 5:
        break
```

### Narrow your search

Search transcript passages mentioning that subject for specific words or phrases. Continue with the same `client`, `company`, `after`, and `before` to search for "database" in passages associated with PlanetScale.

```python
query = "database"
hits = client.transcripts.search(
    q=query, about=company.id, after=after, before=before, limit=20,
)
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

### Find organic endorsements

Continue with the same `client` and `company`. The `organic` filter selects unpaid personal recommendations. This example uses Pro+ commercial data.

```python
for i, row in enumerate(client.recommendations.list(
    entity_id=company.id, class_="organic", after=after, before=before, limit=5,
), 1):
    print(f"\n{row.verbatim_quote}\n")
    print(f"Type: {row.class_}\n--")
    if i == 5:
        break
```

### Find ad reads and sponsors

Find a brand's ad reads, inspect the pitch, and discover which sponsors recur on a channel. These examples use Pro+ commercial data.

Continue with the same `client`, `company`, `after`, and `before` to find PlanetScale promotions in the last 60 days. `sponsored` includes ad reads, affiliate promotions, and other ad-style pitches.

```python
for i, row in enumerate(client.recommendations.list(
    entity_id=company.id, class_="sponsored", after=after, before=before, limit=5,
), 1):
    media = row.media
    channel = media.source_channel
    print(f"\n{row.verbatim_quote or 'No quote available.'}\n")
    print(f"Video:     {media.title or media.video_id}")
    print(f"Channel:   {channel.name if channel else 'Unknown'}")
    print(f"Published: {(media.published_at or 'Unknown')[:10]}")
    params = {"v": media.video_id}
    if row.start_seconds is not None:
        params["t"] = str(row.start_seconds)
    print(f"Watch:     https://arcmira.com/watch?{urlencode(params)}\n--")
    if i == 5:
        break
```

To explore sponsorship opportunities, list a channel's recurring sponsors, ordered by ad-read count. This rollup covers its indexed history rather than the date window above.

```python
channel_match = client.entities.resolve(q="ThePrimeTime", type="channel")
channel = channel_match.best or channel_match.suggested
if channel is None or not channel.youtube_channel_id:
    raise LookupError("Confirm the channel before continuing.")
if channel_match.suggested:
    print(f"Assuming {channel.name}.")
sponsors = client.channels.sponsors.list(channel.youtube_channel_id, limit=5)
print(f"\nSponsors on {sponsors.channel.name or channel.name}\n")
for sponsor in sponsors.sponsors:
    print(f"{sponsor.entity.name}: {sponsor.ad_reads} ad reads")
    print(f"Videos: {sponsor.videos}")
    print(f"Latest: {(sponsor.last_seen or 'Unknown')[:10]}\n")
```

Other plans can preview the channel sponsor list by omitting `limit`. See [plans and usage](https://arcmira.com/docs/usage-and-billing) for access and credit usage. Missing a show or seeing a misclassified promotion? [Send feedback](#help-shape-the-index) to help us improve the coverage and classifications.

### Check mention momentum

See whether a company is gaining attention, which shows mention it most, and where to look next. Compare a competitor's mentions with the previous period, then search its transcripts to understand what changed.

Continue with the same `client`. This example investigates Cloudflare. Choose a rolling window of 7 to 365 days. Momentum returns an `accelerating`, `flat`, `fading`, or `none` verdict, mention counts for both periods, the change, the latest source date, and the top shows.

```python
match = client.entities.resolve(
    q="Cloudflare", type="organization",
    context="Internet infrastructure and developer platform",
)
subject = match.best or match.suggested
if subject is None:
    raise LookupError("Confirm the company before continuing.")
if match.suggested:
    print(f"Assuming {subject.name}.")

# Compare the latest 7 days available on your plan with the prior 7 days.
momentum = client.entities.momentum(subject.id, days=7)
volume = momentum.volume
start = (momentum.window.after or "Unknown")[:10]
end = (momentum.window.before or "Unknown")[:10]
print(f"\nCompany:   {momentum.entity.name}")
print(f"Momentum:  {momentum.verdict}")
print(f"Window:    {start} - {end}")
print(
    f"Mentions:  {volume.mentions_window} vs "
    f"{volume.mentions_prior_window} prior"
)
delta = volume.delta_window_absolute
percent = volume.delta_window_pct
percentage = f" ({'+' if percent > 0 else ''}{percent:g}%)" if percent is not None else ""
print(f"Change:    {'+' if delta > 0 else ''}{delta} mentions{percentage}")
print(f"Latest:    {(momentum.as_of or 'No dated source')[:10]}")
```

Output captured on October 17, 2026. The code samples a new rolling window each time you run it; `window` records the dates actually returned. Save the response with your research brief to preserve the counts you used.

```text
Company:   Cloudflare
Momentum:  accelerating
Window:    2026-10-10 - 2026-10-17
Mentions:  22 vs 17 prior
Change:    +5 mentions (+29.4%)
Latest:    2026-10-16
```

Available on every plan. Free coverage ends 30 days ago; paid plans include the latest indexed conversations. Pro+ and higher also return `paid_vs_organic`, with separate counts for ad reads, endorsements, and organic recommendations. Each momentum lookup uses 10 credits from your plan. See [plans and usage](https://arcmira.com/docs/usage-and-billing).

Search Cloudflare transcripts to find what drove the increase and whether people are enthusiastic, critical, or concerned. The response also includes `top_shows` when you want to choose which shows to investigate first.

[See which companies are gaining attention in Famous Rankings](https://arcmira.com/famous/companies/view/rising). Explore rising companies, the shows discussing them, and eight weeks of history to find your next research lead.

Momentum measures mention volume across indexed shows. Famous Rankings uses its own [ranking method](https://arcmira.com/famous/method) to compare companies. Follow the mentions to learn whether an increase reflects a product launch, customer enthusiasm, sponsorships, or controversy. Need more coverage for your market? [Help shape the index](#help-shape-the-index).

### Set up YouTube monitoring

Set up YouTube monitoring for a person, company, product, or topic to get alerts when they are mentioned across videos and podcasts.

This example creates a monitor in your account for PlanetScale, using the company resolved above. A monitor sets delivery preferences; each tracker follows a name or channel. See [monitor delivery options](https://arcmira.com/docs/monitors#delivery) to choose email, Slack or a webhook.

```python
created = client.monitors.create(
    name=f"{company.name} mentions", notify_frequency="daily",
)
added = client.monitors.entities.add(created.monitor.id, entity_ids=[company.id])
for result in added.results:
    print(f"Tracker: {result.tracker_id}" if result.attached else result.reason)
```

Every method is listed with its request and response types in [reference.md](reference.md). The same operations, with `curl` samples, are in the [API reference](https://arcmira.com/docs/api-reference).

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

`str(refusal)` reads `402 quota_exceeded: <message>`. `member_limit` and `fair_use_cap` are 402 refusals with no `unlock`: an admin of the account raises the limit, or it resets with the month. `on_demand_paused` is a 402 refusal with no `unlock` too: a payment for on-demand usage was declined, and an admin of the account updates the card at https://arcmira.com/dashboard/billing.

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
| `trackers` | `list`, `update`, `delete`, `alerts.list` |
| `integrations` | `slack.list` |
| `feedback` | `submit`, `get` |
| `me` | `get`, `update_settings` |
| `health` | `check` |

`transcripts.search` returns spoken passages from `GET /v1/search`. Its filters take ids too.

Every tracker lives in a monitor, which sets how it alerts. To follow an entity you have an id for, call `monitors.entities.add(monitor_id, entity_ids=["ent_14"])`. To watch an exact name before it is indexed, pass `names=[AddEntitiesRequestNamesItem(name="Ramp", type="organization")]` (from `arcmira.monitors`) to the same call. A channel is named by its YouTube channel id.

`me.get()` names the account the key spends as `account` (`id`, `name`, `kind`, `plan`) and your `role` there; `email_masked` is you.

See [CHANGELOG.md](CHANGELOG.md) for what changed from 0.3.

## Agents

The [Arcmira MCP server](https://github.com/arcmira/mcp) gives AI agents the same data at `https://mcp.arcmira.com/mcp`. [llms.txt](llms.txt) describes this package for agents.

## Contributing

We are hiring. ASI-pilled technical people only. Figure it out.

## License

Apache-2.0. See [LICENSE](./LICENSE).
