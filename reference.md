# Reference
## Health
<details><summary><code>client.health.<a href="src/arcmira/health/client.py">check</a>() -> HealthResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.health.check()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Me
<details><summary><code>client.me.<a href="src/arcmira/me/client.py">get</a>() -> MeResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Available even when the account has exhausted its usage allowance. Returns the credential making the request (key_id, key_label, credential_kind), the masked account email, the tier, scopes, rate limit, usage with period_resets_at, and account settings. usage.credits is the primary measure: credits from the plan, then the on-demand budget. The row fields restate it at 4 credits a row. settings.transcripts is what a transcript request that names no parameter of its own receives: every key of the account resolves against it.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.me.get()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.me.<a href="src/arcmira/me/client.py">update_settings</a>(...) -> MeSettingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the account defaults every key of the account resolves against. Send only the fields you are changing; an omitted field keeps the value it has. Resolution order for every transcript request is the explicit parameter, then these settings, then the platform default, so a default never overrides a parameter the caller sent. Defaults live on the account, never on a key: two keys of one account answer the same request the same way. The response echoes the resolved settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment
from arcmira.me import UpdateSettingsMeRequestTranscripts

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.me.update_settings(
    transcripts=UpdateSettingsMeRequestTranscripts(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcripts:** `UpdateSettingsMeRequestTranscripts` — Fields to change. An omitted field keeps the value the account already carries.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entities
<details><summary><code>client.entities.<a href="src/arcmira/entities/client.py">resolve</a>(...) -> EntityResolveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this before passing an id to about, by, entity_ids, channel_ids or channel; those filters refuse names with id_required. Pass context with the user's own words about the name ("the startup bank", "on My First Million"). The answer is one of three: best (the name means one entity: use it and name it), suggested (no entity is certain but one stands out, with reason and evidence: use it and tell the user you assumed it), or ask (several entities fit: show ask.options, or check every option id and answer per entity). For a show pass type=channel and use the youtube_channel_id; for a brand or a person use the id. Free; uses no credits.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.entities.resolve(
    q="q",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — A name, @handle, YouTube URL or channel id (UC...). One thing per call.

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ResolveEntitiesRequestType]` — Restrict candidates to one type. Pass channel for a show and read best.youtube_channel_id.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Candidates to return, 1 to 15. Default 8.

</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[str]` — What the user said about the name, in their words ("the startup bank", "Canada's prime minister", "on My First Million"). Ranks candidates by their description and by the episodes they share with what the context names; a clear winner comes back as suggested with reason context.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/arcmira/entities/client.py">get</a>(...) -> EntityDetailResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the canonical entity envelope for an ent_{n} or numeric id, following merge redirects. For organization and product entities, callers with Recommendations API access (a Pro+ plan) also receive a recommendations_summary commercial-intelligence rollup when a brand profile exists.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.entities.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Entity id, ent_{n} or the numeric id. Merged ids follow their redirect.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entities.<a href="src/arcmira/entities/client.py">momentum</a>(...) -> EntityMomentumResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mentions in the last 7 and 30 days against the prior 30, an absolute-delta verdict (accelerating, flat, fading, none), the newest media date, and the top shows in the window. It counts the shows we index, not the whole internet, and it is a count, not a score. On a Pro+ plan the card also carries paid_vs_organic; otherwise that field is absent and access names the gate. Free; uses no credits. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.entities.momentum(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Entity id, ent_{n} or the numeric id. Merged ids follow their redirect.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mentions
<details><summary><code>client.mentions.<a href="src/arcmira/mentions/client.py">list</a>(...) -> MentionListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cursor-paginated mentions filtered by entity (entity_id is required; resolve a name first with GET /v1/entities/resolve, or the call answers 400 id_required naming the parameter), channel (channel_id), text query, sentiment, appearance flag, and publication window [after, before). The signed continuation binds the route, filters, caller and visibility; invalid or old cursors return invalid_cursor. A first-page ID fence excludes later insertions, including old-date backfills. Edits and deletions to existing mentions remain live. Positions are start_seconds and end_seconds (integer seconds; 0 means full episode). is_appearance filtering applies to person entities only; passing is_appearance=true for any other type returns a 400 (appearances_person_only). details=full attaches per-mention commercial recommendations and requires a Pro+ plan.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.mentions.list(
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The entity, as an id like ent_14. Required. Ids only: a name answers 400 id_required. Resolve names first with GET /v1/entities/resolve.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to this route, normalized query, caller and visibility; invalid or old tokens return invalid_cursor.

</dd>
</dl>

<dl>
<dd>

**channel_id:** `typing.Optional[str]` — Only media from this YouTube channel id (UC plus 22 characters). Ids only: a name answers 400 id_required. Resolve names first with GET /v1/entities/resolve.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**sentiment:** `typing.Optional[ListMentionsRequestSentiment]`

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[bool]`

</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Only media published at or after this instant. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Only media published before this instant, so before=2026-09-02 includes all of 2026-09-01. Needs a paid plan: the free plan refuses it with filter_requires_paid. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**details:** `typing.Optional[ListMentionsRequestDetails]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.mentions.<a href="src/arcmira/mentions/client.py">count</a>(...) -> MentionCountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A small ranked table of entity and channel counts, all-time unless after is set. Pass channel_ids for what shows talk about and entity_types to match the question (topic for subjects, person for guests, organization,product for brands). Pass video_ids with one id from GET /v1/channels/{channel_id}/videos for what a single episode mentions. Two or more channel_ids also return shared, the entities on more than one of them ranked by the smallest per-channel count, which is true overlap. An after later than the plan's freshness gate is refused with freshness_requires_paid rather than widened. Uses 4 credits per ranked entry returned past the first 5. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.mentions.count()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel_ids:** `typing.Optional[str]` — Comma-separated YouTube channel ids (UC...), at most 8. Two or more also return shared, the entities on more than one of them.

</dd>
</dl>

<dl>
<dd>

**entity_ids:** `typing.Optional[str]` — Comma-separated entity ids (ent_{n}), at most 20. Counts only these entities.

</dd>
</dl>

<dl>
<dd>

**video_ids:** `typing.Optional[str]` — Comma-separated 11-character YouTube video ids, at most 20. Counts only these episodes; take the ids from GET /v1/channels/{channel_id}/videos.

</dd>
</dl>

<dl>
<dd>

**entity_types:** `typing.Optional[str]` — Comma-separated entity types to count: person, organization, product, topic, channel. Subjects are topic; guests are person; brands are organization,product. Omit and organizations dominate.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[CountMentionsRequestMode]` — mentions counts talk about an entity; appearances counts a person being present; both counts either. Default mentions.

</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Only media published at or after this instant. Counts are all-time without it. An after later than your plan's freshness gate is refused with freshness_requires_paid rather than widened. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Only media published before this instant, so before=2026-09-02 includes all of 2026-09-01. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Rows in the ranked table, 1 to 40. Default 20.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Recommendations
<details><summary><code>client.recommendations.<a href="src/arcmira/recommendations/client.py">list</a>(...) -> RecommendationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cursor-paginated commercial mentions (sponsored, organic and neutral mentions) filtered by entity (entity_id is required; resolve a name first with GET /v1/entities/resolve, or the call answers 400 id_required naming the parameter), channel (channel_id), class, confidence, and publication window [after, before). The signed continuation binds the route, filters, caller and visibility; invalid or old cursors return invalid_cursor. A first-page ID fence excludes later insertions, including old-date backfills. Edits and deletions to existing recommendations remain live. Requires a Pro+ plan. Positions are start_seconds and end_seconds (integer seconds).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.recommendations.list(
    entity_id="entity_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `str` — The entity, as an id like ent_14. Required. Ids only: a name answers 400 id_required. Resolve names first with GET /v1/entities/resolve.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to this route, normalized query, caller and visibility; invalid or old tokens return invalid_cursor.

</dd>
</dl>

<dl>
<dd>

**channel_id:** `typing.Optional[str]` — Only media from this YouTube channel id (UC plus 22 characters). Ids only: a name answers 400 id_required. Resolve names first with GET /v1/entities/resolve.

</dd>
</dl>

<dl>
<dd>

**class:** `typing.Optional[ListRecommendationsRequestClass]` — The commercial class to return. Omit for all three. Values: sponsored (an ad-style promotion heard at that moment: a paid sponsor read, promo code, affiliate plug, thanks for supplied goods or venue, or a show promoting its own product as an ad), organic (an unpaid personal recommendation), mention (a neutral commercial mention).

</dd>
</dl>

<dl>
<dd>

**min_confidence:** `typing.Optional[float]`

</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Only media published at or after this instant. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Only media published before this instant, so before=2026-09-02 includes all of 2026-09-01. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**include_disputed:** `typing.Optional[bool]`

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Feedback
<details><summary><code>client.feedback.<a href="src/arcmira/feedback/client.py">submit</a>(...) -> FeedbackResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attach corrections to the exact query you ran: pass the feedback type, the query object you sent, and optional per-item corrections. Public submissions are recorded for human review (status "logged"); nothing is auto-applied. Read the review status back later via GET /v1/feedback/{feedback_id}. recommendations and channel_sponsors feedback types require a Pro+ plan; every other type needs read. monitor_alert feedback targets fired alerts: query carries monitor_id and/or tracker_id and/or alert_id, corrections target the alert id, and every referenced alert must belong to the caller (otherwise 404 alert_not_found). missed_alert corrections are expectations with nothing to target: omit the correction id and put { source_url, approximate_timestamp_seconds?, entity_id? } in suggested_change. delivery_issue corrections may carry { channel } in suggested_change. experience feedback says how a task went as a whole rather than correcting a result: it requires category and notes, refuses corrections (400 invalid_feedback_request), and needs no query. category and mcp_call_id, when sent, are recorded in the stored query.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.feedback.submit(
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
    type="recommendations",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `SubmitFeedbackRequestType` — The surface being reviewed. Values: recommendations (/v1/recommendations results by com_* id; requires a Pro+ plan), channel_sponsors (sponsor entities on a channel; requires a Pro+ plan), mentions (/v1/mentions results by men_* id), entities_search (/v1/entities/resolve candidates), entities (/v1/entities/{id} payloads), channels (/v1/channels/{channel_id}/videos results), monitor_alert (fired alerts from /v1/monitors/{id}/alerts or /v1/trackers/{id}/alerts; corrections target the alert id), appearances (person appearances from /v1/mentions with is_appearance=true), search (/v1/search passages), experience (how a task went as a whole, not one result: requires category and notes, takes no corrections, and query is optional).

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Persist a unique key and the exact request before sending a logical mutation. A retry returns its stored response with Idempotency-Replayed: true. A changed intent under a finalized key returns 409 idempotency_conflict. Keys belong to the authenticated owner, credential and mutation domain. Current authorization still applies. Receipts have no general 24-hour expiry; signing-secret recovery alone expires after 24 hours or when the secret is displaced.

</dd>
</dl>

<dl>
<dd>

**query:** `typing.Optional[typing.Dict[str, typing.Any]]` — The query object that produced the result you are reviewing, echoed back verbatim so reviewers can replay it. For monitor_alert feedback, carry monitor_id and/or tracker_id and/or alert_id.

</dd>
</dl>

<dl>
<dd>

**endpoint:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**method:** `typing.Optional[SubmitFeedbackRequestMethod]`

</dd>
</dl>

<dl>
<dd>

**request_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**result_url:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**source_url:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**notes:** `typing.Optional[str]` — Free text for the reviewer. Required when type is experience: say what the user asked for and what went wrong, slow, or missing.

</dd>
</dl>

<dl>
<dd>

**corrections:** `typing.Optional[typing.List[SubmitFeedbackRequestCorrectionsItem]]` — Per-result corrections. Not allowed when type is experience.

</dd>
</dl>

<dl>
<dd>

**category:** `typing.Optional[SubmitFeedbackRequestCategory]` — What kind of problem this is. Values: wrong_entity (a name resolved to the wrong person, company or thing), bad_data (a result or field is wrong), missing (something that should exist was not found), slow (the task took too long), confusing (the answer or an error was hard to act on), other (anything else; say what in notes). Required when type is experience.

</dd>
</dl>

<dl>
<dd>

**mcp_call_id:** `typing.Optional[str]` — The MCP tool call this feedback is about, as the Arcmira MCP server names it (mcpc_ and 32 hex digits). Joins the feedback to that call in product analytics.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.feedback.<a href="src/arcmira/feedback/client.py">get</a>(...) -> FeedbackReadbackResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the submission (id, type, query, notes, created_at) plus its corrections, each with a review status in the public vocabulary: pending_review, needs_information, accepted, accepted_with_changes, rejected, withdrawn, applied, reverted (accepted means a reviewer agreed; applied means the change is live in the index). Only the submitting user's keys can read a submission; unknown ids and other users' submissions both return 404 (never 403).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.feedback.get(
    feedback_id="feedback_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**feedback_id:** `str` — The feedback submission id POST /v1/feedback returned, fbk_ and digits.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Transcripts
<details><summary><code>client.transcripts.<a href="src/arcmira/transcripts/client.py">search</a>(...) -> TranscriptSearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search indexed YouTube and podcast transcripts for short spoken slices. Each result includes spoken text, a watch URL, and a publish date. Scope with channel_ids (or channel) and entity_ids (a person id filters to that person's appearances); narrow to passages about entities with about, to a speaker with by, and to sponsored, organic or mention passages with kind. Every filter takes ids, never names: resolve a name first with GET /v1/entities/resolve, or the call answers 400 id_required naming the parameter. Results carry names beside ids (filters.about, filters.by, chunk about and speakers_by). Use one topic per call. Search results include text on every plan within the plan's publication-date window. Explicitly requesting source=arcmira_premium on a plan without Premium transcripts is refused with filter_requires_paid. An after later than the plan's freshness gate is refused with freshness_requires_paid rather than widened. Uses 4 credits per chunk returned past the first 5. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.transcripts.search(
    q="q",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — One topic or phrase. Do not concatenate unrelated names; make one call per topic.

</dd>
</dl>

<dl>
<dd>

**channel_ids:** `typing.Optional[str]` — Comma-separated YouTube channel ids (UC...), at most 8. Pass every show in scope unless drilling into one. Ids only: a name answers 400 id_required. Resolve names first with GET /v1/entities/resolve.

</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Alias of channel_ids for code-mode clients; the union of both is the scope.

</dd>
</dl>

<dl>
<dd>

**entity_ids:** `typing.Optional[str]` — Comma-separated entity ids (ent_{n}), at most 8. A person id filters to that person's appearances; a channel id widens channel_ids. Ids only: a name answers 400 id_required. Resolve names first with GET /v1/entities/resolve.

</dd>
</dl>

<dl>
<dd>

**about:** `typing.Optional[str]` — Comma-separated entity ids (ent_{n}), at most 8. Only passages about these entities: excerpt pins, exact-name mentions and ad verdicts. Ids only: a name answers 400 id_required. Resolve names first with GET /v1/entities/resolve.

</dd>
</dl>

<dl>
<dd>

**by:** `typing.Optional[str]` — Comma-separated person ids (ent_{n}), at most 8. Only passages where one of these people says the query words (each line of a chunk is labeled with its speaker); a non-person id is refused with invalid_query naming its type. Speaker labels cover a minority of shows; an empty result carries a note saying whether the person is labeled anywhere. Ids only: a name answers 400 id_required. Resolve names first with GET /v1/entities/resolve.

</dd>
</dl>

<dl>
<dd>

**kind:** `typing.Optional[str]` — Comma-separated passage classes: sponsored, organic, mention. Combine with about to read what was said about a brand in ad reads or in organic talk.

</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Only media published at or after this instant. An after later than your plan's freshness gate is refused with freshness_requires_paid rather than widened. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Only media published before this instant, so before=2026-09-02 includes all of 2026-09-01. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[SearchTranscriptsRequestSource]` — Restrict to one transcript source class. arcmira_premium on a plan without Premium transcripts is refused with filter_requires_paid.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Chunks to return, 1 to 20. Default 5.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transcripts.<a href="src/arcmira/transcripts/client.py">get</a>(...) -> TranscriptResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Caption reads use 4 credits per started 15 minutes. quality=premium is one read. An owned transcript answers 200 ready at no charge. Otherwise this call starts a Premium transcript of the whole video, 300 credits per started 15 minutes, using credits from the account's plan first and then the account's on-demand budget up to its limit, and answers 202 pending with the job and Retry-After until the transcript is ready. Read again after Retry-After; repeated reads join the same job and never charge twice. When the last Premium transcript for the video failed, the read answers 200 state failed with the job and last_attempt and charges nothing; retry=true starts a new one. When the plan or the budget blocks, 403 paid_plan_required (with unlock) or 402 quota_exceeded or spend_limit_exceeded carries the price in quote and nothing is charged. A default-premium account with nothing owned reads captions with a note. start/end only trim the returned content; language selects caption tracks, timestamps=false returns paragraphs. Premium lines carry speaker and index, and the body carries speakers and revision.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.transcripts.get(
    video_id="video_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**video_id:** `str` — YouTube video id, 11 characters.

</dd>
</dl>

<dl>
<dd>

**quality:** `typing.Optional[GetTranscriptsRequestQuality]` — captions reads creator or automatic captions at 4 credits per started 15 minutes. premium is one read. An owned transcript returns 200 state ready at no charge. Otherwise the read starts a Premium transcript of the whole video, 300 credits per started 15 minutes, using credits from the account's plan first and then the account's on-demand budget up to its limit, and returns 202 state pending with the job until it is ready. When the last Premium transcript for the video failed it answers 200 state failed and starts a new one only with retry=true. 402 quota_exceeded or spend_limit_exceeded and 403 paid_plan_required carry the price in quote. It never substitutes captions. Default captions unless changed in account settings.

</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` — Comma-separated caption language priority list, at most 5, tried in order (e.g. "de,en"). Use asr for the first automatic track and asr-<code> for a specific one. Default en. languages[] in the response lists every track the video offers.

</dd>
</dl>

<dl>
<dd>

**timestamps:** `typing.Optional[bool]` — false returns paragraphs[] of { start, text, speaker? } instead of lines[], for reading rather than citing. Default true.

</dd>
</dl>

<dl>
<dd>

**start:** `typing.Optional[float]` — Window start in seconds from the beginning of the video. Send start and end together. On captions the window bills only its own started 15-minute blocks; on Premium it trims the returned content. An explicit Premium read is charged for the whole video from the account's plan credits and then its on-demand budget; a window does not reduce that charge.

</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[float]` — Window end in seconds, greater than start and no greater than the video duration. Send start and end together.

</dd>
</dl>

<dl>
<dd>

**retry:** `typing.Optional[bool]` — Premium only; captions with retry=true returns invalid_query. When the last Premium transcript for this video failed, a read answers 200 state failed with the job and last_attempt and charges nothing; retry=true starts a new one under the same quote, budget and one-job-per-video rules as the first read. While that refund is still settling (job.status refund_pending) even retry=true answers state failed. Without a failed job it changes nothing.

</dd>
</dl>

<dl>
<dd>

**refresh:** `typing.Optional[bool]` — Captions only; Premium with refresh=true returns invalid_query. Refetch the caption track from YouTube instead of serving the stored copy. Available only for videos outside our index; a pipeline-owned video refuses it with invalid_query.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transcripts.<a href="src/arcmira/transcripts/client.py">quote</a>(...) -> PremiumQuote</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional free quote: what a Premium read of this video would use right now, as rows and credits (a row is 4 credits), where the credits would come from, and max_on_demand_cents, the on-demand budget the read would need beyond the plan's credits within the account limit. It does not reserve credits or budget and does not start a transcript. A video with no known duration, or one past the 12 hour cap, answers 400 invalid_query with param video_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.transcripts.quote(
    video_id="video_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**video_id:** `str` — YouTube video id, 11 characters.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.transcripts.<a href="src/arcmira/transcripts/client.py">list_requests</a>(...) -> TranscriptRequestListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Your transcription requests in descending creation time and id order. limit defaults to 20 and accepts 1–100. Follow next_cursor with the same video_id, limit and credential; has_more is false and next_cursor is null on the last page. A traversal excludes requests inserted after its first page. Each entry is a Premium transcript job with its processing and billing state, a `status_url` for the Premium transcript GET, and a `title` field (the video title, null when unknown). The scheduled reconciler advances requests; reading this list never dispatches work or changes billing. In-flight entries carry `eta_seconds` and `next_poll_seconds`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.transcripts.list_requests()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**video_id:** `typing.Optional[str]` — Filter to your requests for one video.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Requests per page, from 1 to 100. Default 20.

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Keep the same filter, limit and credential.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Channels
<details><summary><code>client.channels.<a href="src/arcmira/channels/client.py">coverage</a>(...) -> ChannelCoverageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

How many videos of a YouTube channel are searchable, the newest publish date among them, and the split by transcript source class. Call it when a search or mention lookup came back empty, before telling anyone we do not cover a show, and cite indexed_through as the as-of date for mentions and search_indexed_through for transcript search. It cannot request indexing; channel backfill is not available yet. Free; uses no credits. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.channels.coverage(
    channel_id="channel_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel_id:** `str` — YouTube channel id, the UC... form.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Monitors
<details><summary><code>client.monitors.<a href="src/arcmira/monitors/client.py">list</a>() -> MonitorListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All monitors for the account with tracker counts, alert counts for the current calendar month, and Slack display metadata. Single page, no pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/arcmira/monitors/client.py">create</a>(...) -> MonitorMutationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creating with notify_webhook: true and a webhook_url enables HMAC-signed webhook delivery and returns the signing secret (monitor.webhook_secret) in this response. Store it securely. A retry with the original Idempotency-Key recovers the same secret for up to 24 hours while it remains the current secret or the valid previous secret. An expired or displaced secret returns 409 idempotency_result_expired without rotating again. Reads do not expose the secret. All subsequent reads expose only webhook_secret_set and webhook_secret_hint. Creating monitors and trackers is free. Each alert uses 25 credits once, however many channels and recipients deliver it: credits from your plan, then your on-demand budget. When the account is out of credits, alerts wait instead of sending.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.create(
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Display name (1-100 characters). Required on create.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**notify_emails:** `typing.Optional[typing.List[str]]` — Desired email recipients. External recipients must confirm before delivery. Free includes one additional recipient per monitor; paid plans allow up to 20 total. Default [].

</dd>
</dl>

<dl>
<dd>

**notify_frequency:** `typing.Optional[CreateMonitorsRequestNotifyFrequency]` — Delivery cadence. Default realtime. Values: realtime (as analysis completes), hourly (hourly digest), daily (daily digest).

</dd>
</dl>

<dl>
<dd>

**digest_day:** `typing.Optional[str]` — Digest day of week. Default "monday". Consulted only by weekly digests, which are dashboard-configured today; inert for API-set frequencies.

</dd>
</dl>

<dl>
<dd>

**digest_time:** `typing.Optional[str]` — Digest send hour as HH:MM (account timezone). Default "09:00". Applies to daily digests.

</dd>
</dl>

<dl>
<dd>

**notify_webhook:** `typing.Optional[bool]` — Enable HMAC-signed webhook delivery (paid plans). When enabled together with webhook_url, the response returns the signing secret (monitor.webhook_secret), recoverable with the original Idempotency-Key during the valid recovery window. PATCHing true also re-enables an auto-disabled webhook and resets its failure counter.

</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Destination URL for webhook alert deliveries.

</dd>
</dl>

<dl>
<dd>

**notify_slack:** `typing.Optional[bool]` — Enable Slack delivery. Requires a Slack integration connected in the dashboard.

</dd>
</dl>

<dl>
<dd>

**slack_integration_id:** `typing.Optional[str]` — Slack integration id from the dashboard OAuth flow.

</dd>
</dl>

<dl>
<dd>

**slack_channel_id:** `typing.Optional[str]` — Slack channel id to deliver to.

</dd>
</dl>

<dl>
<dd>

**team_id:** `typing.Optional[str]` — Create the monitor in this team, which the caller must belong to. The team owner pays for it and its plan sets the limits. A member may not set a webhook. Create only.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/arcmira/monitors/client.py">delete</a>(...) -> MonitorDeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the monitor AND every tracker inside it (trackers_deleted reports how many). Cannot be undone. Retrying with the original Idempotency-Key returns the original deleted count without deleting again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.delete(
    id="id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Monitor id.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/arcmira/monitors/client.py">update</a>(...) -> MonitorMutationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

A PATCH that newly enables webhook signing (turns notify_webhook on, or sets a webhook_url where no secret existed before) returns the signing secret (monitor.webhook_secret) in this response. Store it securely. A retry with the original Idempotency-Key recovers the same secret for up to 24 hours while it remains the current secret or the valid previous secret. An expired or displaced secret returns 409 idempotency_result_expired without rotating again. Reads do not expose the secret. Unrelated PATCHes expose only webhook_secret_set and webhook_secret_hint. PATCHing notify_webhook: true also re-enables a webhook that was auto-disabled after repeated failures and resets its failure counter.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.update(
    id="id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Monitor id.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Display name (1-100 characters). Required on create.

</dd>
</dl>

<dl>
<dd>

**notify_emails:** `typing.Optional[typing.List[str]]` — Desired email recipients. External recipients must confirm before delivery. Free includes one additional recipient per monitor; paid plans allow up to 20 total. Default [].

</dd>
</dl>

<dl>
<dd>

**notify_frequency:** `typing.Optional[UpdateMonitorsRequestNotifyFrequency]` — Delivery cadence. Default realtime. Values: realtime (as analysis completes), hourly (hourly digest), daily (daily digest).

</dd>
</dl>

<dl>
<dd>

**digest_day:** `typing.Optional[str]` — Digest day of week. Default "monday". Consulted only by weekly digests, which are dashboard-configured today; inert for API-set frequencies.

</dd>
</dl>

<dl>
<dd>

**digest_time:** `typing.Optional[str]` — Digest send hour as HH:MM (account timezone). Default "09:00". Applies to daily digests.

</dd>
</dl>

<dl>
<dd>

**notify_webhook:** `typing.Optional[bool]` — Enable HMAC-signed webhook delivery (paid plans). When enabled together with webhook_url, the response returns the signing secret (monitor.webhook_secret), recoverable with the original Idempotency-Key during the valid recovery window. PATCHing true also re-enables an auto-disabled webhook and resets its failure counter.

</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Destination URL for webhook alert deliveries.

</dd>
</dl>

<dl>
<dd>

**notify_slack:** `typing.Optional[bool]` — Enable Slack delivery. Requires a Slack integration connected in the dashboard.

</dd>
</dl>

<dl>
<dd>

**slack_integration_id:** `typing.Optional[str]` — Slack integration id from the dashboard OAuth flow.

</dd>
</dl>

<dl>
<dd>

**slack_channel_id:** `typing.Optional[str]` — Slack channel id to deliver to.

</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` — Paused monitors accept config changes but do not deliver; alerts that would have fired are not queued.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.<a href="src/arcmira/monitors/client.py">rotate_webhook_secret</a>(...) -> WebhookSecretRotateResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generates a new signing secret and returns it in this response. Store it securely. A retry with the original Idempotency-Key recovers the same secret for up to 24 hours while it remains the current secret or the valid previous secret. An expired or displaced secret returns 409 idempotency_result_expired without rotating again. Reads do not expose the secret. Zero-downtime overlap: the previous secret remains valid until previous_secret_expires_at (24 hours); during the window every delivery carries an additional X-Arcmira-Signature-Previous header computed with the old secret over the same {timestamp}.{payload} string, so you can verify with either secret while you roll. After the window the old secret is dropped and the extra header disappears. Rotating again during the window replaces the previous secret and resets the window. Requires a configured webhook (webhook_url set); otherwise 409 with code webhook_not_configured. Auto-disable interplay: rotation resets webhook_failures but never re-enables a webhook that was auto-disabled after repeated failures; to resume delivery, also PATCH the monitor with notify_webhook: true. Requires the monitors:write scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.rotate_webhook_secret(
    id="id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Monitor id.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trackers
<details><summary><code>client.trackers.<a href="src/arcmira/trackers/client.py">list</a>() -> TrackerListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All trackers for the account, newest first, with per-channel delivery counts for the current billing period. Single page, no pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.trackers.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trackers.<a href="src/arcmira/trackers/client.py">create</a>(...) -> TrackerMutationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a standalone tracker watching one exact name and type, matched case-insensitively against entities in newly analyzed media, so a tracker can exist before the entity is indexed. To follow an entity you already have an id for, use POST /v1/monitors/{id}/entities. A channel is followed by its YouTube channel id (UC plus 22 characters); a channel name answers 400 id_required. Attach it to a monitor afterwards via POST /v1/monitors/{id}/trackers. Creating a duplicate (same entity name + type) returns 409 tracker_already_exists with the existing tracker id in error.details.existing_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.trackers.create(
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
    entity_name="entity_name",
    entity_type="person",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_name:** `str` — The exact name to watch, matched case-insensitively against analyzed media, so a tracker can exist before the entity is indexed. For a channel, the YouTube channel id (UC plus 22 characters), never a name: a channel name answers 400 id_required naming GET /v1/entities/resolve?q=...&type=channel and best.youtube_channel_id. Required on create. Creating a duplicate (same name, compared case-insensitively, and type) returns 409 tracker_already_exists with the existing tracker id in error.details.existing_id.

</dd>
</dl>

<dl>
<dd>

**entity_type:** `CreateTrackersRequestEntityType` — Entity type of the tracked entity. Required on create. org is accepted for organization, and the tracker answers organization.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Optional label shown in alerts and the dashboard.

</dd>
</dl>

<dl>
<dd>

**notify_email:** `typing.Optional[bool]` — Per-tracker email delivery. Default true.

</dd>
</dl>

<dl>
<dd>

**notify_webhook:** `typing.Optional[bool]` — Per-tracker webhook delivery override. Paid plans only.

</dd>
</dl>

<dl>
<dd>

**notify_slack:** `typing.Optional[bool]` — Per-tracker Slack delivery override. Paid plans only.

</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Per-tracker webhook destination override (http/https).

</dd>
</dl>

<dl>
<dd>

**slack_channel_id:** `typing.Optional[str]` — Per-tracker Slack channel override.

</dd>
</dl>

<dl>
<dd>

**slack_integration_id:** `typing.Optional[str]` — Per-tracker Slack integration override.

</dd>
</dl>

<dl>
<dd>

**person_match_mode:** `typing.Optional[CreateTrackersRequestPersonMatchMode]` — Person trackers only. Mentions (default) matches others talking about the person; appearances matches the person present as a speaker, host or guest; both accepts either. Non-person trackers reject this field. PATCH changes future and pending delivery eligibility, without backfill.

</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Stored filter object. personMatchMode is also accepted here for person trackers. Other filter keys are retained; do not assume they change matching.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trackers.<a href="src/arcmira/trackers/client.py">delete</a>(...) -> MessageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the tracker. Cannot be undone.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.trackers.delete(
    id="id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Tracker id, trk_ form.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trackers.<a href="src/arcmira/trackers/client.py">update</a>(...) -> TrackerMutationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partial update: send only the fields to change. The tracked entity itself (entity_name/entity_type) is immutable; delete and recreate to watch a different entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.trackers.update(
    id="id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Tracker id, trk_ form.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — Optional label shown in alerts and the dashboard.

</dd>
</dl>

<dl>
<dd>

**notify_email:** `typing.Optional[bool]` — Per-tracker email delivery. Default true.

</dd>
</dl>

<dl>
<dd>

**notify_webhook:** `typing.Optional[bool]` — Per-tracker webhook delivery override. Paid plans only.

</dd>
</dl>

<dl>
<dd>

**notify_slack:** `typing.Optional[bool]` — Per-tracker Slack delivery override. Paid plans only.

</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Per-tracker webhook destination override (http/https).

</dd>
</dl>

<dl>
<dd>

**slack_channel_id:** `typing.Optional[str]` — Per-tracker Slack channel override.

</dd>
</dl>

<dl>
<dd>

**slack_integration_id:** `typing.Optional[str]` — Per-tracker Slack integration override.

</dd>
</dl>

<dl>
<dd>

**person_match_mode:** `typing.Optional[UpdateTrackersRequestPersonMatchMode]` — Person trackers only. Mentions (default) matches others talking about the person; appearances matches the person present as a speaker, host or guest; both accepts either. Non-person trackers reject this field. PATCH changes future and pending delivery eligibility, without backfill.

</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Dict[str, typing.Any]]` — Stored filter object. personMatchMode is also accepted here for person trackers. Other filter keys are retained; do not assume they change matching.

</dd>
</dl>

<dl>
<dd>

**paused:** `typing.Optional[bool]` — Pause or resume the tracker. Paused trackers stop producing alerts; there is no backfill for the paused window.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Channels Sponsors
<details><summary><code>client.channels.sponsors.<a href="src/arcmira/channels/sponsors/client.py">list</a>(...) -> ChannelSponsorsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Rollup of recurring sponsors for a YouTube channel, ordered by ad read count. On a Pro+ plan the full list is served and min_ad_reads (default 3), status, and limit apply. Every other plan receives the free slice an anonymous visitor sees on arcmira.com, with meta.total naming the true count and access naming the gate; passing min_ad_reads, status, or limit on such a plan is refused with filter_requires_paid. Pass src=mcp-tool only from the Arcmira MCP server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.channels.sponsors.list(
    channel_id="channel_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel_id:** `str` — YouTube channel id, the UC... form.

</dd>
</dl>

<dl>
<dd>

**min_ad_reads:** `typing.Optional[int]` — Sponsors with fewer ad reads are excluded. Default 3. Pro+ only; on other plans passing it is refused with filter_requires_paid.

</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListSponsorsRequestStatus]` — Filter against the curated known-advertisers dataset. Pro+ only.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Sponsors to return. Default 100. Pro+ only; other plans receive the free slice.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Channels Videos
<details><summary><code>client.channels.videos.<a href="src/arcmira/channels/videos/client.py">list</a>(...) -> ChannelVideosResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The indexed videos of a YouTube channel, newest first, each with its video_id, title, publish date, duration, view count, and watch_url on arcmira.com. Pass next_cursor as cursor to continue. The signed token binds the route, filters, caller and visibility; invalid or old tokens return invalid_cursor. A first-page media ID fence excludes later insertions, including old-date backfills; edits and deletions to existing videos remain live. Call it for the latest or most recent episode of a show, or to list what a show published in a window, then pass a video_id to GET /v1/mentions/counts video_ids for what that episode mentions or to GET /v1/transcripts/{video_id} to read it. indexed_through is the newest date we hold for the channel. An empty list means nothing is indexed; channel backfill is not available yet. Uses 4 credits per video returned past the first 5. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.channels.videos.list(
    channel_id="channel_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**channel_id:** `str` — YouTube channel id, the UC... form.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Videos to return, 1 to 25, newest first. Default 10. Pass 1 for the latest episode.

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque continuation from next_cursor. Bound to the channel, filters, caller, and visibility; limit may change between pages. Invalid or old tokens return invalid_cursor.

</dd>
</dl>

<dl>
<dd>

**after:** `typing.Optional[str]` — Only media published at or after this instant. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**before:** `typing.Optional[str]` — Only media published before this instant, so before=2026-09-02 includes all of 2026-09-01. An ISO 8601 date (2026-09-01) or datetime with offset (2026-09-01T00:00:00Z), read in UTC. The window is half-open: after is inclusive, before is exclusive.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Integrations Slack
<details><summary><code>client.integrations.slack.<a href="src/arcmira/integrations/slack/client.py">list</a>() -> SlackIntegrationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The account's active Slack workspaces with the ids a monitor needs for Slack delivery: create or PATCH a monitor with notify_slack: true, slack_integration_id set to an id here, and optionally slack_channel_id (default_channel_id when omitted). Slack is connected in the dashboard, never through the API; an empty list means the user must connect it there first. Reads stored data only. Single page, no pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.integrations.slack.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Monitors Trackers
<details><summary><code>client.monitors.trackers.<a href="src/arcmira/monitors/trackers/client.py">list</a>(...) -> MonitorTrackersResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.trackers.list(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Monitor id.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.monitors.trackers.<a href="src/arcmira/monitors/trackers/client.py">add</a>(...) -> MonitorAddTrackersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attaches EXISTING trackers to the monitor by id ({ tracker_ids: ["trk_..."] }). It does not create trackers: create them first via POST /v1/trackers, then attach. Attached trackers use the monitor's delivery settings. Supply 1 to 90 IDs. Duplicate IDs count once. Every ID must belong to the account; a missing or foreign ID returns tracker_not_found and none are attached. attached_count reports the unique attached count.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.trackers.add(
    id="id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
    tracker_ids=[
        "tracker_ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Monitor id.

</dd>
</dl>

<dl>
<dd>

**tracker_ids:** `typing.List[str]` — Ids of existing trackers ("trk_...") to attach to this monitor. Create trackers first via POST /v1/trackers. At most 90 IDs per request; duplicates count once. All IDs must belong to the account or none are attached.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Monitors Alerts
<details><summary><code>client.monitors.alerts.<a href="src/arcmira/monitors/alerts/client.py">list</a>(...) -> AlertListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The newest limit alert deliveries for the monitor (default 25, at most 100), as a single page. has_more is true when older alerts exist past limit; this endpoint does not paginate, so next_cursor is always null and a larger limit reads further. entity_id ("ent_{n}") and mention_id ("men_{n}") are the ids GET /v1/entities/{id} and GET /v1/mentions use, and video_id is the YouTube video id that GET /v1/transcripts/{video_id} reads. Dispute a fired alert via POST /v1/feedback with type monitor_alert.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.alerts.list(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Monitor id.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Alerts to return, newest first, 1 to 100. Default 25.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Monitors Entities
<details><summary><code>client.monitors.entities.<a href="src/arcmira/monitors/entities/client.py">add</a>(...) -> MonitorAddEntitiesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Follows each entity ({ entity_ids: ["ent_..."] }) and each exact name ({ names: [{ name, type }] }) in the monitor: the monitor account's existing tracker for the entity or name (compared case-insensitively) is reused, else a tracker is created under the monitor's account (the team owner on a team monitor) for the canonical entity (a merged id follows its redirect) or the name as given, then the trackers are attached, all in one write. Use names for something not yet indexed; a channel is named by its YouTube channel id, and a channel name answers 400 id_required. Attached trackers use the monitor's delivery settings. Supply 1 to 90 ids and names together; duplicates count once. Each gets one result, ids first then names, in request order; a names result carries name and type in place of entity_id. An id that cannot be followed comes back with attached: false and a reason (entity_not_found, entity_type_not_trackable, tracker_limit_reached, tracked_in_another_monitor) while the rest still attach; a tracker already in another monitor is left there and named in current_monitor_id. Requires the monitors:write and trackers:write scopes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.monitors.entities.add(
    id="id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Monitor id.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — One key per intent, 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Keys are scoped to the account, credential and resource family. The same key and normalized method, path and body returns the committed response with Idempotency-Replayed: true. A changed intent within the same family returns 409 idempotency_conflict. Monitor and tracker families have independent namespaces. Secret recovery is limited as described by the operation.

</dd>
</dl>

<dl>
<dd>

**entity_ids:** `typing.Optional[typing.List[str]]` — Entity ids ("ent_...") to follow in this monitor, from GET /v1/entities/resolve or search. Duplicates count once. A merged id follows its redirect to the canonical entity.

</dd>
</dl>

<dl>
<dd>

**names:** `typing.Optional[typing.List[AddEntitiesRequestNamesItem]]` — Exact names to follow in this monitor, for a name not yet indexed or one you have no id for. The tracker is created under the monitor's account (the team owner on a team monitor) and attached in the same call; the account's tracker for the same name (compared case-insensitively) and type is reused. Duplicates count once.

</dd>
</dl>

<dl>
<dd>

**person_match_mode:** `typing.Optional[AddEntitiesRequestPersonMatchMode]` — For person trackers this request creates: mentions (default) matches others talking about the person; appearances matches the person present as a speaker, host or guest; both accepts either. Other types ignore it, and a tracker that already exists keeps its own setting (change it with PATCH /v1/trackers/{id}).

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trackers Alerts
<details><summary><code>client.trackers.alerts.<a href="src/arcmira/trackers/alerts/client.py">list</a>(...) -> AlertListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The newest limit alert deliveries for the tracker (default 25, at most 100), as a single page. has_more is true when older alerts exist past limit; this endpoint does not paginate, so next_cursor is always null and a larger limit reads further. entity_id ("ent_{n}") and mention_id ("men_{n}") are the ids GET /v1/entities/{id} and GET /v1/mentions use, and video_id is the YouTube video id that GET /v1/transcripts/{video_id} reads. Dispute a fired alert via POST /v1/feedback with type monitor_alert.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from arcmira import Arcmira
from arcmira.environment import ArcmiraEnvironment

client = Arcmira(
    api_key="<token>",
    environment=ArcmiraEnvironment.DEFAULT,
)

client.trackers.alerts.list(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Tracker id, trk_ form.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Alerts to return, newest first, 1 to 100. Default 25.

</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.

</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>
