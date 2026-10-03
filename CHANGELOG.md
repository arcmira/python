# Changelog

## 0.4.0

Generated from the v1 document of 2026-10-02. The document dropped from 88 operations to 36. Routes that left it still serve over HTTP, but the SDK no longer has methods for them.

Added.

- `client.monitors.entities.add(id, entity_ids=None, names=None, person_match_mode=None)` follows entities in a monitor by id, or by exact name and type for a name not yet indexed. It reuses the account's tracker for each entity or creates one, then attaches it. Each id or name gets one result, and one that cannot be followed comes back with `attached: false` and a reason.
- `trackers.create` and `names` accept `org` for `organization`, and the duplicate check ignores case.
- `client.integrations.slack.list()` lists the account's active Slack workspaces with the `slack_integration_id` and `slack_channel_id` values a monitor needs for Slack delivery. Slack is connected in the dashboard, not through the API.
- `monitors.create` takes `team_id`. `Monitor` carries `access`, `muted` and `team`.
- `feedback.submit` takes `category` and `mcp_call_id`, and `type="experience"` reports how a task went as a whole.
- List bodies for mentions, recommendations, search, counts and channel videos echo the applied date window as `window: { after, before }`.

Breaking changes from 0.3.

- Premium is one read. `transcripts.get(video_id, quality="premium")` answers `ready` (200) when the account owns the transcript. Otherwise it buys the whole video within the plan and the account's on-demand budget and answers `pending` (202) with the `job` and a `Retry-After` header. Read again after `Retry-After`. Repeated reads join the same purchase and never buy twice. When the last purchase for the video failed or was refunded, the read answers `failed` (200) with the `job` and `last_attempt` and buys nothing; pass `retry=True` to buy it again. `TranscriptResult` is now `TranscriptResult_Ready | TranscriptResult_Pending | TranscriptResult_Failed`. Priced refusals carry one `RefusedQuote` type. The `preparation_required` state and `TranscriptResult_PreparationRequired` are gone.
- `transcripts.prepare_and_wait` is removed, along with `PreparationError`, `PreparationFailedError`, `PreparationTimeoutError` and `PremiumUnavailableError`. Loop on `transcripts.get(..., quality="premium")` until `state == "ready"`. The README has the loop.
- `transcripts.request` and `transcripts.status` are removed, with the `TranscriptRequestSubmitResponse` type. The Premium read buys and reports its own job. `transcripts.list_requests` still lists past purchases.
- A Premium refusal raises from the read itself. `PaymentRequiredError` (402) carries `quota_exceeded` or `spend_limit_exceeded`, and `ForbiddenError` (403) carries `paid_plan_required`. Nothing is charged.
- Error extras moved under `error.details`. `body.quote` is now `body.error.details.quote`, `body.existing_request_id` is `body.error.details.existing_request_id`, and `body.existing_id` (409 `tracker_already_exists`) is `body.error.details.existing_id`.
- Reads take ids. `mentions.list` and `recommendations.list` require `entity_id` (`ent_N`), and `channel_id` takes a YouTube channel id (`UC` plus 22 characters). `entity_name`, `entity_type` and `channel_name` are gone. A name where an id belongs raises `BadRequestError` with code `id_required` and names the parameter. Resolve names first with `entities.resolve`.
- Dates are `after` and `before`, half-open `[after, before)`, on every dated read. `mentions.list` and `recommendations.list` replace `date_from` and `date_to`. `date_to` was an inclusive day, so `date_to="2026-09-01"` becomes `before="2026-09-02"`. `transcripts.search`, `mentions.count` and `channels.videos.list` replace `published_after` and `published_before`.
- `recommendations.list` takes `class_` (`sponsored`, `organic` or `mention`; omit it for all) in place of `mention_class` (`ad_read`, `endorsement`, `mention` or `all`). `Recommendation` and `RecommendationEnrichmentItem` carry `class_` in place of `mention_class`, and so does `WrongClassificationChange` in feedback corrections.
- `transcripts.search` calls `GET /v1/search`. Its `kind` takes `sponsored`, `organic` or `mention` in place of `mention`, `recommendation_sponsored` and `recommendation_organic`. The response renames `requested_k` to `limit` and `returned_n` to `returned`, and `filters.published_after` and `filters.published_before` move to `window`. `TranscriptSearchChunk.text_withheld` is gone.
- List bodies name their collection. `MentionListResponse.data` is `mentions`, `RecommendationListResponse.data` is `recommendations`, and `AlertListResponse.data` is `alerts`. Iterating a pager is unchanged.
- Integer ids and `MM:SS` strings are gone. `Mention` drops `appearance_id`, `start_timestamp` and `end_timestamp`, and `MentionMedia` drops `id`. `Recommendation` drops `recommendation_id`, `start_timestamp` and `end_timestamp`. Use `start_seconds`, `end_seconds` and `media.video_id`. `Alert` replaces `media_id` and `appearance_id` with `video_id`. `Entity.numeric_id` is gone. Premium `speakers[].entity_id` is an `ent_N` string, where 0.3 had an integer. Feedback ids are `fbk_N`.
- `monitors.update` takes `paused` in place of `is_paused`, and `is_collapsed` and `sort_order` are gone. `Monitor`, `Tracker` and monitor tracker rows carry `paused` in place of `is_paused`, and `Monitor` drops `is_collapsed` and `sort_order`.
- Models use the snake_case wire names. Attribute names were already snake_case in 0.3, but the camelCase aliases (`videoId`, `watchUrl`, `invitationStatus` and others) are gone, so `model_dump(by_alias=True)` and the JSON on the wire now match the attribute names.
- `MentionCountsResponse` replaces `published_after` and `published_before` with `window`. `FeedbackCorrectionResult` drops `new_mention_class`, `previous_mention_class`, `recommendation` and `rows_affected`.
- `feedback.submit` no longer requires `query`. `type` stays required.
- `trackers.create` follows a channel by its YouTube channel id in `entity_name`. A channel name raises `id_required`.
- `me.usage.hits` is gone. Monitor alerts cost credits now and count in `usage.credits`.

Removed methods and their replacements.

| 0.3 | 0.4 |
|---|---|
| `entities.search`, `entities.lookup`, `entities.cards` | `entities.resolve`, then `entities.get` |
| `entities.mentions.list(id)` | `mentions.list(entity_id=id)` |
| `entities.recommendations.list(id)` | `recommendations.list(entity_id=id)` |
| `people.get`, `topics.get`, `organizations.get`, `products.get`, `channels.get` | `entities.resolve`, then `entities.get`. For a channel, `channels.coverage` and `channels.videos.list` |
| `people.appearances.list` | `mentions.list(entity_id=..., is_appearance=True)` |
| `channels.related.*` | `mentions.count(channel_ids=..., entity_types=...)` |
| `channels.guests.list` | `mentions.count(channel_ids=..., entity_types="person", mode="appearances")` |
| `people.related.*`, `topics.related.*`, `organizations.related.*`, `products.related.*` | No direct replacement. `mentions.list(entity_id=...)` gives the episodes, and `mentions.count(video_ids=...)` counts what else they mention |
| `transcripts.captions` | `transcripts.get(video_id)`. `languages` lists every caption track and `language` selects one |
| `transcripts.request`, `transcripts.status`, `transcripts.prepare_and_wait` | `transcripts.get(video_id, quality="premium")`, read again on 202 |
| `corrections.*`, `transcripts.edits.*`, `transcripts.speakers.*`, `transcripts.merges.*` | No SDK method. Report a wrong row with `feedback.submit` |
| `team.members`, `team.spend`, `team.usage_events.list` | None. The routes are deleted |

## 0.3.0

The first usable SDK, replacing the URL-only placeholder. The public URL constants remain available.

- Generated synchronous `Arcmira` and asynchronous `AsyncArcmira` clients with typed responses and cursor pagination.
- `transcripts.get` returns a union discriminated on `state`. The Premium purchase is one job, created by `transcripts.request` and polled with `transcripts.status`.
- `transcripts.prepare_and_wait` reads Premium, posts the purchase once when needed, polls at the pace the API sets and returns the transcript.
- `ApiError` text leads with the status, code and message.
- Licensed under Apache-2.0.
