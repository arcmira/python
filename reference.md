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

Available even when the account has exhausted its usage allowance. Returns the credential making the request (key_id, key_label, credential_kind), the masked account email, the tier, scopes, rate limit, row usage with period_resets_at, and account settings. settings.transcripts is what a transcript request that names no parameter of its own receives: every key of the account resolves against it.
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
<details><summary><code>client.entities.<a href="src/arcmira/entities/client.py">search</a>(...) -> EntitySearchResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Substring name search returning up to 25 entities ordered by appearance count, each with a suggested flag: true on an exact match with far more traction than any other row of its type. A q that is a YouTube channel id (UC...), an @handle, or a YouTube URL carrying either resolves to that one channel row, suggested, with its youtube_channel_id. Callers with Recommendations API access (a Pro+ plan) also receive a recommendations_summary per result when a brand profile exists.
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

client.entities.search(
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

**q:** `str`

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[SearchEntitiesRequestType]`

</dd>
</dl>

<dl>
<dd>

**has_recommendations_data:** `typing.Optional[bool]`

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

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

<details><summary><code>client.entities.<a href="src/arcmira/entities/client.py">resolve</a>(...) -> EntityResolveResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Call this before passing an id to about, by, entity_ids, channel_ids or channel; those filters refuse names with id_required. Pass context with the user's own words about the name ("the startup bank", "on My First Million"). The answer is one of three: best (the name means one row: use it and name it), suggested (no row is certain but one stands out, with reason and evidence: use it and tell the user you assumed it), or ask (several rows fit: show ask.options, or check every option id and answer per row). For a show pass type=channel and use the youtube_channel_id; for a brand or a person use the id. Free; bills no rows.
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

<details><summary><code>client.entities.<a href="src/arcmira/entities/client.py">lookup</a>(...) -> EntityLookupResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Resolves an id or name to the canonical entity record, following merge redirects. Pass either id (ent_{n} or numeric) or name, optionally constrained by type.
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

client.entities.lookup()

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

**id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[LookupEntitiesRequestType]`

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

<details><summary><code>client.entities.<a href="src/arcmira/entities/client.py">cards</a>(...) -> EntityCardsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Free endpoint (0 rows). Batched compact lookups for UI hover cards: name, slug, type, image, and index counts for up to 50 raw integer entity ids per request. Merged ids resolve to their canonical entity but are returned under the requested id; unknown ids are silently dropped. The response is identical for all viewers and CDN-cacheable.
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

client.entities.cards(
    ids="ids",
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

**ids:** `str` — Comma-separated raw integer entity ids, 1 to 50 of them (e.g. "12,844,1032"). Merged ids resolve to their canonical entity; unknown ids are silently dropped from the response.

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

Mentions in the last 7 and 30 days against the prior 30, an absolute-delta verdict (accelerating, flat, fading, none), the newest media date, and the top shows in the window. It counts the shows we index, not the whole internet, and it is a count, not a score. On a Pro+ plan the card also carries paid_vs_organic; otherwise that field is absent and access names the gate. Bills one row. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
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

Cursor-paginated mentions filtered by entity (entity_id or entity_name is required), channel, text query, sentiment, appearance flag, and date range. The signed continuation binds the route, filters, caller and visibility; invalid or old cursors return invalid_cursor. A first-page ID fence excludes later insertions, including old-date backfills. Edits and deletions to existing rows remain live. Read timestamps from start_seconds / end_seconds (integer seconds; 0 means full episode); the MM:SS (or HH:MM:SS) string fields are deprecated. is_appearance filtering applies to person entities only; passing is_appearance=true for any other type returns a 400 (appearances_person_only). details=full attaches per-mention commercial recommendations and requires a Pro+ plan.
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

client.mentions.list()

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

**entity_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**entity_name:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[ListMentionsRequestEntityType]`

</dd>
</dl>

<dl>
<dd>

**channel_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**channel_name:** `typing.Optional[str]`

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

**date_from:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[str]`

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

A small ranked table of entity and channel counts, all-time unless published_after is set. Pass channel_ids for what shows talk about and entity_types to match the question (topic for subjects, person for guests, organization,product for brands). Pass video_ids with one id from GET /v1/channels/{channel_id}/videos for what a single episode mentions. Two or more channel_ids also return shared, the entities on more than one of them ranked by the smallest per-channel count, which is true overlap. A published_after narrower than the plan's freshness gate is refused with freshness_requires_paid rather than widened. Bills one row per table row returned. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
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

**published_after:** `typing.Optional[str]` — ISO date. Counts are all-time without it. A window narrower than your plan's freshness gate is refused with freshness_requires_paid rather than widened.

</dd>
</dl>

<dl>
<dd>

**published_before:** `typing.Optional[str]` — ISO date. Only media published before this day.

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

Cursor-paginated commercial mentions (ad reads, endorsements, neutral mentions) filtered by entity (entity_id or entity_name is required), channel, mention_class, confidence, and date range. The signed continuation binds the route, filters, caller and visibility; invalid or old cursors return invalid_cursor. A first-page ID fence excludes later insertions, including old-date backfills. Edits and deletions to existing rows remain live. Requires a Pro+ plan. Read timestamps from start_seconds / end_seconds (integer seconds); the MM:SS string fields are deprecated.
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

client.recommendations.list()

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

**entity_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**entity_name:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**entity_type:** `typing.Optional[ListRecommendationsRequestEntityType]`

</dd>
</dl>

<dl>
<dd>

**channel_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**channel_name:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**mention_class:** `typing.Optional[ListRecommendationsRequestMentionClass]`

</dd>
</dl>

<dl>
<dd>

**min_confidence:** `typing.Optional[float]`

</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[str]`

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

Attach corrections to the exact query you ran: pass the feedback type, the query object you sent, and optional per-item corrections. Public submissions are recorded for human review (status "logged"); nothing is auto-applied. Read the review status back later via GET /v1/feedback/{feedback_id}. recommendations and channel_sponsors feedback types require a Pro+ plan; every other type needs read. monitor_alert feedback targets fired alert rows: query carries monitor_id and/or tracker_id and/or alert_id, corrections target the alert row id, and every referenced alert row must belong to the caller (otherwise 404 alert_not_found). missed_alert corrections are expectations with no row to target: omit the correction id and put { source_url, approximate_timestamp_seconds?, entity_id? } in suggested_change. delivery_issue corrections may carry { channel } in suggested_change.
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
    query={
        "key": "value"
    },
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

**type:** `SubmitFeedbackRequestType` — The surface being reviewed. Values: recommendations (/v1/recommendations rows by com_* id; requires a Pro+ plan), channel_sponsors (sponsor entities on a channel; requires a Pro+ plan), mentions (/v1/mentions rows by men_* id), entities_search (/v1/entities/search hits), entities (/v1/entities/lookup and /v1/entities/{id} payloads), channels (/v1/channels/{slug} payloads), monitor_alert (fired alert rows from /v1/monitors/{id}/alerts or /v1/trackers/{id}/alerts; corrections target the alert row id), appearances (person appearance rows), search (rows from /v1/search or /v1/entities/search).

</dd>
</dl>

<dl>
<dd>

**query:** `typing.Dict[str, typing.Any]` — The query object that produced the result you are reviewing, echoed back verbatim so reviewers can replay it. For monitor_alert feedback, carry monitor_id and/or tracker_id and/or alert_id.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Persist a unique key and the exact request before sending a logical mutation. A retry returns its stored response with Idempotency-Replayed: true. A changed intent under a finalized key returns 409 idempotency_conflict. Keys belong to the authenticated owner, credential and mutation domain. Current authorization still applies. Receipts have no general 24-hour expiry; signing-secret recovery alone expires after 24 hours or when the secret is displaced.

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

**notes:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**corrections:** `typing.Optional[typing.List[SubmitFeedbackRequestCorrectionsItem]]`

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

Returns the submission (id, type, query, notes, created_at) plus its per-correction rows, each with a review status in the public vocabulary: pending_review, needs_information, accepted, accepted_with_changes, rejected, withdrawn, applied, reverted (accepted means a reviewer agreed; applied means the change is live in the index). Only the submitting user's keys can read a submission; unknown ids and other users' submissions both return 404 (never 403).
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

**feedback_id:** `str` — The feedback submission id POST /v1/feedback returned.

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

Search indexed YouTube and podcast transcripts for short spoken slices. Each result includes spoken text, a watch URL, and a publish date. Scope with channel_ids (or channel) and entity_ids (a person id filters to that person's appearances); narrow to passages about entities with about, to a speaker with by, and to mention, recommendation_sponsored or recommendation_organic passages with kind. Every filter takes ids, never names: resolve a name first with GET /v1/entities/resolve, or the call answers 400 id_required naming the parameter. Results carry names beside ids (filters.about, filters.by, chunk about and speakers_by). Use one topic per call. Search results include text on every plan within the plan's publication-date window. Explicitly requesting source=arcmira_premium on a plan without Premium transcripts is refused with filter_requires_paid. A published_after narrower than the plan's freshness gate is refused with freshness_requires_paid rather than widened. Bills one row per chunk returned. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
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

**kind:** `typing.Optional[str]` — Comma-separated passage kinds: mention, recommendation_sponsored, recommendation_organic. Combine with about to read what was said about a brand in ad reads or in organic talk.

</dd>
</dl>

<dl>
<dd>

**published_after:** `typing.Optional[str]` — ISO date. Only media published on or after this day. A window narrower than your plan's freshness gate is refused with freshness_requires_paid rather than widened.

</dd>
</dl>

<dl>
<dd>

**published_before:** `typing.Optional[str]` — ISO date. Only media published before this day.

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

Caption retrieval costs one row per started 15 minutes. Premium retrieval is free and never buys, generates, or returns fallback captions. Branch on state: 200 ready is owned content; 202 pending carries the job, with Retry-After; 200 preparation_required carries the whole-video quote and the action to take, POST /v1/transcriptions with { video_id }, plus last_attempt when the previous purchase failed. Plans without Premium read captions with an access gate instead. start/end only trim the returned content; language selects caption tracks, timestamps=false returns paragraphs. Premium responses retain revision and line indexes for corrections.
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

**quality:** `typing.Optional[GetTranscriptsRequestQuality]` — captions reads creator or automatic captions at 1 row per started 15 minutes. premium is read-only: an owned transcript returns 200 state ready at zero rows, an active purchase returns 202 state pending with its job, and an unowned transcript on a plan with Premium returns 200 state preparation_required with the quote and the POST /v1/transcriptions action. It never purchases or substitutes captions. Default captions unless changed in account settings.

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

**start:** `typing.Optional[float]` — Window start in seconds from the beginning of the video. Send start and end together. On captions the window bills only its own started 15-minute blocks; on Premium it trims an already purchased transcript; this GET does not charge.

</dd>
</dl>

<dl>
<dd>

**end:** `typing.Optional[float]` — Window end in seconds, greater than start and no greater than the video duration. Send start and end together.

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

<details><summary><code>client.transcripts.<a href="src/arcmira/transcripts/client.py">quote</a>(...) -> TranscriptPurchaseQuote</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Optional free quote. It does not reserve funds or start generation. max_rows authorizes rows, while max_on_demand_cents separately authorizes new money and defaults to zero on purchase. The accepted purchase stores its pricing mode. A video with no known duration, or one past the 12 hour cap, answers 400 invalid_query with param video_id.
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

<details><summary><code>client.transcripts.<a href="src/arcmira/transcripts/client.py">captions</a>(...) -> VideoCaptionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Free (0 rows), any key. Returns the video metadata and every caption track YouTube lists for it, each as { code, name, generated }. Call it when GET /v1/transcripts/{video_id} answered transcript_unavailable without languages, or before asking for a specific track. Listing is served from a day-long cache; a cold listing answers 503 transcript_fetching with Retry-After while the fetch continues in the background.
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

client.transcripts.captions(
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

Your transcription requests in descending creation time and id order. limit defaults to 20 and accepts 1–100. Follow next_cursor with the same video_id, limit and credential; has_more is false and next_cursor is null on the last page. A traversal excludes requests inserted after its first page. Each entry has the same shape as the status poll plus a `title` field (the video title, null when unknown). The scheduled reconciler advances requests; reading this list never dispatches work or changes billing. In-flight entries carry `eta_seconds` and `next_poll_seconds`.
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

<details><summary><code>client.transcripts.<a href="src/arcmira/transcripts/client.py">request</a>(...) -> TranscriptRequestSubmitResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Explicit whole-video Premium purchase in one request: POST { video_id }. With no max_rows the purchase is capped at the current quote, and max_on_demand_cents defaults to zero, so it spends included rows or credits only and moves no money. Idempotency-Key is optional: without one, a purchase already open or owned for this video is returned with existing: true, and two simultaneous requests buy once. max_on_demand_cents above 0 is the only way to move money and requires both Idempotency-Key and max_rows (400 invalid_body names the missing one in param). A video with no known duration or longer than 12 hours answers 400 invalid_query with param video_id. A plan without Premium answers 403 forbidden with unlock. Accepted price, mode, and debit identity persist across retries. Included rows or credits are reserved up front; monetary on-demand usage is reserved until Premium is ready. Existing owned unlocks cost zero. A terminal generation failure refunds the exact original debit and period before reporting refunded. A repeated key returns the same request; different intent with that key returns idempotency_conflict. The body is { job, existing }. Poll job.status_url after Retry-After. A pending job returns 202; a ready, failed or refunded job returns 200. Idempotency-Replayed: true marks a replay of the same key; a different key joined onto the active purchase answers existing: true without it.
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

client.transcripts.request(
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

**idempotency_key:** `typing.Optional[str]` — 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Persist a unique key and the exact request before sending a logical mutation. A retry returns its stored response with Idempotency-Replayed: true. A changed intent under a finalized key returns 409 idempotency_conflict. Keys belong to the authenticated owner, credential and mutation domain. Current authorization still applies. Receipts have no general 24-hour expiry; signing-secret recovery alone expires after 24 hours or when the secret is displaced.

</dd>
</dl>

<dl>
<dd>

**video_id:** `typing.Optional[str]` — YouTube video id (11 characters). Either video_id or url is required.

</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — A YouTube watch/short/live URL. Either video_id or url is required.

</dd>
</dl>

<dl>
<dd>

**max_rows:** `typing.Optional[int]` — Maximum whole-video rows authorized. Credit mode charges four credits per row. Omit it to cap the purchase at the current quote. Required with max_on_demand_cents above 0.

</dd>
</dl>

<dl>
<dd>

**max_on_demand_cents:** `typing.Optional[int]` — Maximum new monetary on-demand charge in whole cents. Defaults to 0, which moves no money. Above 0 it requires Idempotency-Key and max_rows.

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

<details><summary><code>client.transcripts.<a href="src/arcmira/transcripts/client.py">status</a>(...) -> TranscriptJob</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Agent-friendly polling contract: while the request is in flight the response carries a Retry-After header (seconds) and body fields `eta_seconds` and `next_poll_seconds`. Sleep on Retry-After and re-poll. `status` walks queued → downloading → transcribing → analyzing → complete (user-facing `stage` folds downloading into transcribing). refund_pending retains Retry-After and next_poll_seconds until reversal completes; it has no completion ETA. Terminal statuses (`complete`, `failed`, `refunded`) drop Retry-After. On `complete`, fetch the transcript via GET /v1/transcripts/{video_id}; the successful purchase owns the permanent unlock. `refunded` means the pipeline failed and the rows were returned. A caller with no account holds no jobs: it is refused with 401 job_requires_account, whose unlock points at sign-up.
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

client.transcripts.status(
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

**id:** `str` — Transcription request id, the UUID POST /v1/transcriptions returned.

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

How many videos of a YouTube channel are searchable, the newest publish date among them, and the split by transcript source class. Call it when a search or mention lookup came back empty, before telling anyone we do not cover a show, and cite indexed_through as the as-of date for mentions and search_indexed_through for transcript search. It cannot request indexing; channel backfill is not available yet. Free (0 rows). Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
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

<details><summary><code>client.channels.<a href="src/arcmira/channels/client.py">get</a>(...) -> ChannelPageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Channel pages include a recommendations_summary teaser: sponsor_count for all callers; top_sponsors additionally requires a Pro+ plan.
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

client.channels.get(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

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

## People
<details><summary><code>client.people.<a href="src/arcmira/people/client.py">get</a>(...) -> PersonPageResponse</code></summary>
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

client.people.get(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

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

## Topics
<details><summary><code>client.topics.<a href="src/arcmira/topics/client.py">get</a>(...) -> TopicPageResponse</code></summary>
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

client.topics.get(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

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

## Organizations
<details><summary><code>client.organizations.<a href="src/arcmira/organizations/client.py">get</a>(...) -> OrganizationPageResponse</code></summary>
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

client.organizations.get(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

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

## Products
<details><summary><code>client.products.<a href="src/arcmira/products/client.py">get</a>(...) -> ProductPageResponse</code></summary>
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

client.products.get(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

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

Creating with notifyWebhook: true and a webhookUrl enables HMAC-signed webhook delivery and returns the signing secret (monitor.webhookSecret) in this response. Store it securely. A retry with the original Idempotency-Key recovers the same secret for up to 24 hours while it remains the current secret or the valid previous secret. An expired or displaced secret returns 409 idempotency_result_expired without rotating again. Reads do not expose the secret. All subsequent reads expose only webhookSecretSet and webhookSecretHint.
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

**notify_frequency:** `typing.Optional[CreateMonitorsRequestNotifyFrequency]` — Delivery cadence. Default realtime. Values: realtime (as analysis completes), hourly (hourly digest), daily (daily digest). Free-tier email delivery is coerced to daily regardless of the value sent.

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

**notify_webhook:** `typing.Optional[bool]` — Enable HMAC-signed webhook delivery (paid plans). When enabled together with webhookUrl, the response returns the signing secret (monitor.webhookSecret), recoverable with the original Idempotency-Key during the valid recovery window. PATCHing true also re-enables an auto-disabled webhook and resets its failure counter.

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

Deletes the monitor AND every tracker inside it (trackersDeleted reports how many). Cannot be undone. Retrying with the original Idempotency-Key returns the original deleted count without deleting again.
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

A PATCH that newly enables webhook signing (turns notifyWebhook on, or sets a webhookUrl where no secret existed before) returns the signing secret (monitor.webhookSecret) in this response. Store it securely. A retry with the original Idempotency-Key recovers the same secret for up to 24 hours while it remains the current secret or the valid previous secret. An expired or displaced secret returns 409 idempotency_result_expired without rotating again. Reads do not expose the secret. Unrelated PATCHes expose only webhookSecretSet and webhookSecretHint. PATCHing notifyWebhook: true also re-enables a webhook that was auto-disabled after repeated failures and resets its failure counter.
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

**notify_frequency:** `typing.Optional[UpdateMonitorsRequestNotifyFrequency]` — Delivery cadence. Default realtime. Values: realtime (as analysis completes), hourly (hourly digest), daily (daily digest). Free-tier email delivery is coerced to daily regardless of the value sent.

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

**notify_webhook:** `typing.Optional[bool]` — Enable HMAC-signed webhook delivery (paid plans). When enabled together with webhookUrl, the response returns the signing secret (monitor.webhookSecret), recoverable with the original Idempotency-Key during the valid recovery window. PATCHing true also re-enables an auto-disabled webhook and resets its failure counter.

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

**is_paused:** `typing.Optional[bool]` — Paused monitors accept config changes but do not deliver; alerts that would have fired are not queued.

</dd>
</dl>

<dl>
<dd>

**is_collapsed:** `typing.Optional[bool]` — Dashboard display state.

</dd>
</dl>

<dl>
<dd>

**sort_order:** `typing.Optional[int]` — Dashboard sort position.

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

Generates a new signing secret and returns it in this response. Store it securely. A retry with the original Idempotency-Key recovers the same secret for up to 24 hours while it remains the current secret or the valid previous secret. An expired or displaced secret returns 409 idempotency_result_expired without rotating again. Reads do not expose the secret. Zero-downtime overlap: the previous secret remains valid until previousSecretExpiresAt (24 hours); during the window every delivery carries an additional X-Arcmira-Signature-Previous header computed with the old secret over the same {timestamp}.{payload} string, so you can verify with either secret while you roll. After the window the old secret is dropped and the extra header disappears. Rotating again during the window replaces the previous secret and resets the window. Requires a configured webhook (webhookUrl set); otherwise 409 with code webhook_not_configured. Auto-disable interplay: rotation resets webhook_failures but never re-enables a webhook that was auto-disabled after repeated failures; to resume delivery, also PATCH the monitor with notifyWebhook: true. Requires the monitors:write scope.
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

Creates a standalone tracker watching one entity (name + type, resolved with the same entity resolution Search uses). Attach it to a monitor afterwards via POST /v1/monitors/{id}/trackers. Creating a duplicate (same entity name + type) returns 409 with the existingId.
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
    entity_name="entityName",
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

**entity_name:** `str` — The entity name to resolve and watch. Required on create. Creating a duplicate (same name + type) returns 409 with the existingId.

</dd>
</dl>

<dl>
<dd>

**entity_type:** `CreateTrackersRequestEntityType` — Entity type of the tracked entity. Required on create.

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

Partial update: send only the fields to change. The tracked entity itself (entityName/entityType) is immutable; delete and recreate to watch a different entity.
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

## Team
<details><summary><code>client.team.<a href="src/arcmira/team/client.py">members</a>() -> TeamMembersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Active members of the team the key is scoped to, with role and seat type, earliest join first. Single page, no pagination. Requires a team-scoped API key whose owner is still an active team admin. Personal keys and keys whose owner lost team authority receive 403 (team_key_required).
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

client.team.members()

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

<details><summary><code>client.team.<a href="src/arcmira/team/client.py">spend</a>() -> TeamSpendResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Account-wide rows consumed and on-demand overage spend for every active member in the current period. Totals include personal-key use and activity before joining; they are not a team-attributed invoice. Single page, no pagination. Requires a team-scoped API key whose owner is still an active team admin. Personal keys and keys whose owner lost team authority receive 403 (team_key_required).
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

client.team.spend()

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

## Corrections
<details><summary><code>client.corrections.<a href="src/arcmira/corrections/client.py">submit</a>(...) -> CorrectionAcceptedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unified corrections ingestion for all kinds: line_edit, speaker_reassign, speaker_identify, add_person, entity_tag, segment_rewrite. Corrections are free (0 rows) and land as pending-review rows attributed to your API key; speaker_identify/add_person also create a community-flagged appearance immediately. segment_rewrite is the structural primitive: it replaces an inclusive segment range with new segments (an empty replacements array deletes the range); timestamps can be pinned per replacement with optional start/end seconds, and unpinned times are repaired by char-proportional interpolation between pins. Anchored kinds (line_edit, speaker_reassign, entity_tag, segment_rewrite) must echo the `revision` from a Premium transcript read and an `anchor` ({ segmentIndex, contentHash: djb2 of the covered segment text }); `anchor.segmentIndex` is the line's `index` in that read. Every refusal uses the shared error envelope. Error semantics for outbox-style clients: a 409 revision_mismatch or anchor_mismatch means the transcript changed, and error.current_revision is the revision to re-read; create a new event and key after re-anchoring, because the original refusal consumed its sequence and is replayable. A 409 idempotency_conflict means a finalized key was reused for changed intent; recover the original request instead of rebasing that key. A 412 sequence_mismatch stores no receipt or effect; error.expected_seq is the next seq, so synchronize local counters and resend under the same key.
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

client.corrections.submit(
    video_id="video_id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
    kind="line_edit",
    payload={
        "key": "value"
    },
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

**kind:** `SubmitCorrectionsRequestKind`

</dd>
</dl>

<dl>
<dd>

**payload:** `typing.Dict[str, typing.Any]` — Kind-specific payload. line_edit: { segmentIndex, originalText, correctedText }. speaker_reassign: { selection: { startIndex, startChar, endIndex, endChar }, target: { kind: existing|new|role, speakerId, label?, role? } }. speaker_identify: { speakerId, entityId }. add_person: { speakerId, name }. entity_tag: { segmentIndex, charStart, charEnd, entityId } or { segmentIndex, charStart, charEnd, proposedName, proposedType }. segment_rewrite: { startIndex, endIndex, replacements: [{ text, speaker?, start?, end? }] }. replaces the inclusive segment range with the replacements (max 50 source segments, 50 replacements, 2000 chars each); an empty array deletes the range. Timestamps: optional start/end pins (seconds, non-decreasing across the list) fix times explicitly; every unpinned time is interpolated char-proportionally between the surrounding pins (outer bounds default to the source time range). A replacement without speaker inherits from the source segment its repaired start time falls in; startIndex must equal anchor.segmentIndex and the anchor contentHash covers startIndex through endIndex.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Persist a unique client event key with the HTTP method, public path and parsed body. The same finalized intent replays its original response with Idempotency-Replayed: true; changed finalized input returns 409 idempotency_conflict. Receipts have no expiry. A 412 stores no receipt or effect, so synchronize the sequence and resend under the same key. Other finalized refusals consume the eligible sequence once.

</dd>
</dl>

<dl>
<dd>

**seq:** `typing.Optional[int]` — Per-video monotonic sequence number (strict FIFO per user+video). Optional for one-off submissions; required for outbox-style clients that depend on ordering. Any mismatch returns 412 with the expected value.

</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[str]` — The revision from the Premium transcript read this correction was made against. Required for every kind. Speaker ids in the payload are the speakers[].id values of that read.

</dd>
</dl>

<dl>
<dd>

**anchor:** `typing.Optional[SubmitCorrectionsRequestAnchor]` — Required for line_edit, speaker_reassign, entity_tag, and segment_rewrite.

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

<details><summary><code>client.corrections.<a href="src/arcmira/corrections/client.py">withdraw_speaker_edit</a>(...) -> WithdrawnResponse</code></summary>
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

client.corrections.withdraw_speaker_edit(
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

**id:** `str` — The pending row id, as result.id of the response that accepted it.

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

<details><summary><code>client.corrections.<a href="src/arcmira/corrections/client.py">withdraw_entity_tag</a>(...) -> WithdrawnResponse</code></summary>
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

client.corrections.withdraw_entity_tag(
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

**id:** `str` — The pending row id, as result.id of the response that accepted it.

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

<details><summary><code>client.corrections.<a href="src/arcmira/corrections/client.py">withdraw_segment_rewrite</a>(...) -> WithdrawnResponse</code></summary>
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

client.corrections.withdraw_segment_rewrite(
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

**id:** `str` — The pending row id, as result.id of the response that accepted it.

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

The indexed videos of a YouTube channel, newest first, each with its video_id, title, publish date, duration, view count, and watch_url on arcmira.com. Pass next_cursor as cursor to continue. The signed token binds the route, filters, caller and visibility; invalid or old tokens return invalid_cursor. A first-page media ID fence excludes later insertions, including old-date backfills; edits and deletions to existing rows remain live. Call it for the latest or most recent episode of a show, or to list what a show published in a window, then pass a video_id to GET /v1/mentions/counts video_ids for what that episode mentions or to GET /v1/transcripts/{video_id} to read it. indexed_through is the newest date we hold for the channel. An empty list means nothing is indexed; channel backfill is not available yet. Bills one row per video returned. Every gate is a typed error whose error.unlock.url names the plan that lifts it; pass src=mcp-tool only from the Arcmira MCP server.
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

**published_after:** `typing.Optional[str]` — ISO date. Only videos published on or after this day.

</dd>
</dl>

<dl>
<dd>

**published_before:** `typing.Optional[str]` — ISO date. Only videos published before this day.

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

## Channels Related
<details><summary><code>client.channels.related.<a href="src/arcmira/channels/related/client.py">topics</a>(...) -> EntityTopicListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The topics that co-occur with this channel in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.channels.related.topics(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[TopicsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[TopicsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[TopicsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.channels.related.<a href="src/arcmira/channels/related/client.py">people</a>(...) -> EntityPeopleListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The people that co-occur with this channel in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.channels.related.people(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PeopleRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[PeopleRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[PeopleRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.channels.related.<a href="src/arcmira/channels/related/client.py">organizations</a>(...) -> EntityOrganizationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The organizations that co-occur with this channel in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.channels.related.organizations(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrganizationsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[OrganizationsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[OrganizationsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.channels.related.<a href="src/arcmira/channels/related/client.py">products</a>(...) -> EntityProductListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The products that co-occur with this channel in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.channels.related.products(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ProductsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ProductsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ProductsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.channels.related.<a href="src/arcmira/channels/related/client.py">channels</a>(...) -> EntityChannelListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The channels that co-occur with this channel in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.channels.related.channels(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ChannelsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ChannelsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ChannelsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

## Channels Guests
<details><summary><code>client.channels.guests.<a href="src/arcmira/channels/guests/client.py">list</a>(...) -> ChannelGuestListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

People who appeared as guests on the channel, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.channels.guests.list(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListGuestsRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ListGuestsRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ListGuestsRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

## Entities Mentions
<details><summary><code>client.entities.mentions.<a href="src/arcmira/entities/mentions/client.py">list</a>(...) -> MentionListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cursor-paginated mentions for one entity, newest media first. Read timestamps from start_seconds / end_seconds (integer seconds; 0 means full episode); the MM:SS (or HH:MM:SS) string fields are deprecated. is_appearance filtering applies to person entities only; passing is_appearance=true for any other type returns a 400 (appearances_person_only). details=full attaches per-mention commercial recommendations and requires a Pro+ plan.
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

client.entities.mentions.list(
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

**channel_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**channel_name:** `typing.Optional[str]`

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

**date_from:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[str]`

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

## Entities Recommendations
<details><summary><code>client.entities.recommendations.<a href="src/arcmira/entities/recommendations/client.py">list</a>(...) -> RecommendationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cursor-paginated commercial mentions (ad reads, endorsements, neutral mentions) for one entity, newest media first. The signed continuation binds the route, filters, caller and visibility; invalid or old cursors return invalid_cursor. A first-page ID fence excludes later insertions, including old-date backfills. Edits and deletions to existing rows remain live. Requires a Pro+ plan. Read timestamps from start_seconds / end_seconds (integer seconds); the MM:SS string fields are deprecated. Rows below min_confidence (default 0.7) and disputed rows (unless include_disputed=true) are excluded.
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

client.entities.recommendations.list(
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

**channel_id:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**channel_name:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**mention_class:** `typing.Optional[ListRecommendationsRequestMentionClass]`

</dd>
</dl>

<dl>
<dd>

**min_confidence:** `typing.Optional[float]`

</dd>
</dl>

<dl>
<dd>

**date_from:** `typing.Optional[str]`

</dd>
</dl>

<dl>
<dd>

**date_to:** `typing.Optional[str]`

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

Attaches EXISTING trackers to the monitor by id ({ trackerIds: ["trk_..."] }). It does not create trackers: create them first via POST /v1/trackers, then attach. Attached trackers use the monitor's delivery settings. Supply 1 to 90 IDs. Duplicate IDs count once. Every ID must belong to the account; a missing or foreign ID returns tracker_not_found and none are attached. attachedCount reports the unique attached count.
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
        "trackerIds"
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

The newest limit alert deliveries for the monitor (default 25, at most 100), as a single page. has_more is true when older alerts exist past limit; this endpoint does not paginate, so next_cursor is always null and a larger limit reads further. entity_id ("ent_{n}") and mention_id ("men_{n}") are public-ID forms that join directly against entity and mention rows; media_id and appearance_id are raw integer ids, matching the numeric ids used elsewhere in the API. Dispute a fired alert via POST /v1/feedback with type monitor_alert.
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

## Organizations Related
<details><summary><code>client.organizations.related.<a href="src/arcmira/organizations/related/client.py">topics</a>(...) -> EntityTopicListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The topics that co-occur with this organization in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.organizations.related.topics(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[TopicsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[TopicsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[TopicsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.organizations.related.<a href="src/arcmira/organizations/related/client.py">people</a>(...) -> EntityPeopleListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The people that co-occur with this organization in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.organizations.related.people(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PeopleRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[PeopleRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[PeopleRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.organizations.related.<a href="src/arcmira/organizations/related/client.py">organizations</a>(...) -> EntityOrganizationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The organizations that co-occur with this organization in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.organizations.related.organizations(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrganizationsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[OrganizationsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[OrganizationsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.organizations.related.<a href="src/arcmira/organizations/related/client.py">products</a>(...) -> EntityProductListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The products that co-occur with this organization in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.organizations.related.products(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ProductsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ProductsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ProductsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.organizations.related.<a href="src/arcmira/organizations/related/client.py">channels</a>(...) -> EntityChannelListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The channels that co-occur with this organization in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.organizations.related.channels(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ChannelsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ChannelsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ChannelsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

## People Appearances
<details><summary><code>client.people.appearances.<a href="src/arcmira/people/appearances/client.py">list</a>(...) -> PersonAppearanceListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Appearances (the person was actually present in the media) for one person, newest first. Person-only: the equivalent route for any other entity type returns a 400 (appearances_person_only). Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied. The rows are display-oriented. For programmatic pagination, date filtering, and the standard mention-row shape, use GET /v1/mentions?entity_id=...&is_appearance=true instead.
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

client.people.appearances.list(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ListAppearancesRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ListAppearancesRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ListAppearancesRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

## People Related
<details><summary><code>client.people.related.<a href="src/arcmira/people/related/client.py">topics</a>(...) -> EntityTopicListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The topics that co-occur with this person in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.people.related.topics(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[TopicsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[TopicsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[TopicsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.people.related.<a href="src/arcmira/people/related/client.py">people</a>(...) -> EntityPeopleListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The people that co-occur with this person in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.people.related.people(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PeopleRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[PeopleRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[PeopleRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.people.related.<a href="src/arcmira/people/related/client.py">organizations</a>(...) -> EntityOrganizationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The organizations that co-occur with this person in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.people.related.organizations(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrganizationsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[OrganizationsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[OrganizationsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.people.related.<a href="src/arcmira/people/related/client.py">products</a>(...) -> EntityProductListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The products that co-occur with this person in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.people.related.products(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ProductsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ProductsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ProductsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.people.related.<a href="src/arcmira/people/related/client.py">channels</a>(...) -> EntityChannelListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The channels that co-occur with this person in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.people.related.channels(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ChannelsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ChannelsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ChannelsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

## Products Related
<details><summary><code>client.products.related.<a href="src/arcmira/products/related/client.py">topics</a>(...) -> EntityTopicListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The topics that co-occur with this product in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.products.related.topics(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[TopicsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[TopicsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[TopicsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.products.related.<a href="src/arcmira/products/related/client.py">people</a>(...) -> EntityPeopleListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The people that co-occur with this product in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.products.related.people(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PeopleRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[PeopleRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[PeopleRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.products.related.<a href="src/arcmira/products/related/client.py">organizations</a>(...) -> EntityOrganizationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The organizations that co-occur with this product in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.products.related.organizations(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrganizationsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[OrganizationsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[OrganizationsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.products.related.<a href="src/arcmira/products/related/client.py">products</a>(...) -> EntityProductListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The products that co-occur with this product in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.products.related.products(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ProductsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ProductsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ProductsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.products.related.<a href="src/arcmira/products/related/client.py">channels</a>(...) -> EntityChannelListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The channels that co-occur with this product in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.products.related.channels(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ChannelsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ChannelsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ChannelsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

## Team UsageEvents
<details><summary><code>client.team.usage_events.<a href="src/arcmira/team/usage_events/client.py">list</a>(...) -> TeamUsageEventsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Account usage log across every active team member, including personal-key use and activity before joining. Ordered by created_at and id descending, bounded to a 90-day look-back. Continuation preserves the first page's time window and excludes subsequently inserted events, including backfills. Removed members and deleted events disappear during traversal; this is not a historical membership snapshot. Cursors expire after 24 hours and bind the team, caller, days and limit; invalid or changed-query cursors return invalid_cursor rather than restarting. The aggregated analytics chart data is not exposed on this API (Enterprise). Requires a team-scoped API key whose owner is still an active team admin. Personal keys and keys whose owner lost team authority receive 403 (team_key_required).
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

client.team.usage_events.list()

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

**limit:** `typing.Optional[int]` — Events per page, 1 to 100.

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Opaque cursor from a previous page's next_cursor.

</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Look-back window in days, bounded at 90.

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

## Topics Related
<details><summary><code>client.topics.related.<a href="src/arcmira/topics/related/client.py">topics</a>(...) -> EntityTopicListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The topics that co-occur with this topic in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.topics.related.topics(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[TopicsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[TopicsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[TopicsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.topics.related.<a href="src/arcmira/topics/related/client.py">people</a>(...) -> EntityPeopleListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The people that co-occur with this topic in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.topics.related.people(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[PeopleRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[PeopleRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[PeopleRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.topics.related.<a href="src/arcmira/topics/related/client.py">organizations</a>(...) -> EntityOrganizationListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The organizations that co-occur with this topic in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.topics.related.organizations(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[OrganizationsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[OrganizationsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[OrganizationsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.topics.related.<a href="src/arcmira/topics/related/client.py">products</a>(...) -> EntityProductListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The products that co-occur with this topic in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.topics.related.products(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ProductsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ProductsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ProductsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

<details><summary><code>client.topics.related.<a href="src/arcmira/topics/related/client.py">channels</a>(...) -> EntityChannelListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The channels that co-occur with this topic in indexed media, with q/field/sort/order filtering. Signed cursor pagination: rows are in items, and next_cursor (null on the last page) feeds cursor. A token binds route, filters, caller and visibility; malformed or old tokens return invalid_cursor. Aggregate and display lists are live: changed ranks or deleted rows may shift later pages. total counts every matching row and limit is the page size applied.
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

client.topics.related.channels(
    slug="slug",
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

**slug:** `str` — The entity slug: the last segment of its arcmira.com page URL, as EntityRef.slug carries it.

</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]`

</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Signed continuation from next_cursor. Bound to route, filters, caller and visibility; invalid or old tokens return invalid_cursor. Person appearance publication pages use a media-id insertion fence; aggregate sorts remain live.

</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Substring filter over the row's text columns (e.g. video title, channel name, description).

</dd>
</dl>

<dl>
<dd>

**field:** `typing.Optional[str]` — Restrict the q filter to one column. Default "any" (all searchable columns).

</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort key. Rows default to newest first; supported values vary by list (e.g. "date", "channel").

</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[ChannelsRelatedRequestOrder]` — Sort direction. Default desc.

</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[ChannelsRelatedRequestMode]` — Person relationship lens: guest appearances or inbound mentions.

</dd>
</dl>

<dl>
<dd>

**is_appearance:** `typing.Optional[ChannelsRelatedRequestIsAppearance]` — For person appearances, true lists guest episodes and false lists inbound mentions.

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

The newest limit alert deliveries for the tracker (default 25, at most 100), as a single page. has_more is true when older alerts exist past limit; this endpoint does not paginate, so next_cursor is always null and a larger limit reads further. entity_id ("ent_{n}") and mention_id ("men_{n}") are public-ID forms that join directly against entity and mention rows; media_id and appearance_id are raw integer ids, matching the numeric ids used elsewhere in the API. Dispute a fired alert via POST /v1/feedback with type monitor_alert.
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

## Transcripts Edits
<details><summary><code>client.transcripts.edits.<a href="src/arcmira/transcripts/edits/client.py">submit</a>(...) -> TranscriptEditSubmittedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Purpose-built wrapper for the line_edit kind. The edit is pending review: visible to you immediately (returned in the transcript GET `edits[]`), applied for everyone once approved. Free (0 rows), attributed to your API key.
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

client.transcripts.edits.submit(
    video_id="video_id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
    segment_index=1,
    original_text="originalText",
    corrected_text="correctedText",
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

**segment_index:** `int`

</dd>
</dl>

<dl>
<dd>

**original_text:** `str` — The current segment text you are correcting (guards against applying to a changed segment).

</dd>
</dl>

<dl>
<dd>

**corrected_text:** `str`

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Persist a unique key and the exact request before sending a logical mutation. A retry returns its stored response with Idempotency-Replayed: true. A changed intent under a finalized key returns 409 idempotency_conflict. Keys belong to the authenticated owner, credential and mutation domain. Current authorization still applies. Receipts have no general 24-hour expiry; signing-secret recovery alone expires after 24 hours or when the secret is displaced.

</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[str]` — The revision from the Premium transcript read.

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

<details><summary><code>client.transcripts.edits.<a href="src/arcmira/transcripts/edits/client.py">withdraw</a>(...) -> WithdrawnResponse</code></summary>
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

client.transcripts.edits.withdraw(
    video_id="video_id",
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

**video_id:** `str` — YouTube video id, 11 characters.

</dd>
</dl>

<dl>
<dd>

**id:** `str` — The pending row id, as result.id of the response that accepted it.

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

## Transcripts Speakers
<details><summary><code>client.transcripts.speakers.<a href="src/arcmira/transcripts/speakers/client.py">identify</a>(...) -> SpeakerIdentificationSubmittedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Links a diarization speaker id to a person entity (or proposes a new person via `name`). Creates a community-attributed appearance immediately. It shows on the person page right away, flagged pending review; reviewers can revert it. Free (0 rows).
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

client.transcripts.speakers.identify(
    video_id="video_id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
    speaker_id=1,
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

**speaker_id:** `int` — A speakers[].id from the Premium transcript read that revision names.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Persist a unique key and the exact request before sending a logical mutation. A retry returns its stored response with Idempotency-Replayed: true. A changed intent under a finalized key returns 409 idempotency_conflict. Keys belong to the authenticated owner, credential and mutation domain. Current authorization still applies. Receipts have no general 24-hour expiry; signing-secret recovery alone expires after 24 hours or when the secret is displaced.

</dd>
</dl>

<dl>
<dd>

**entity_id:** `typing.Optional[int]` — Existing person entity id. Either entityId or name is required.

</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Propose a person not in the index yet. Reuses an existing same-name person or creates a provisional one. Either entityId or name is required.

</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[str]` — The revision of the transcript read speakerId came from. Required.

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

<details><summary><code>client.transcripts.speakers.<a href="src/arcmira/transcripts/speakers/client.py">withdraw</a>(...) -> WithdrawnResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Withdrawing also removes the community-attributed appearance the identification created.
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

client.transcripts.speakers.withdraw(
    video_id="video_id",
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

**video_id:** `str` — YouTube video id, 11 characters.

</dd>
</dl>

<dl>
<dd>

**id:** `str` — The pending row id, as result.id of the response that accepted it.

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

## Transcripts Merges
<details><summary><code>client.transcripts.merges.<a href="src/arcmira/transcripts/merges/client.py">list</a>(...) -> VideoMergeListResponse</code></summary>
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

client.transcripts.merges.list(
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

<details><summary><code>client.transcripts.merges.<a href="src/arcmira/transcripts/merges/client.py">submit</a>(...) -> VideoMergeSubmittedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asserts that a name in this video refers to a specific entity, for misattributed name mentions in one video (e.g. a first-name-only mention resolved to the wrong entity). Optionally respells the transcript text via `replaceWith`. Pending review; applied optimistically for you. Mentions of the same name in other videos are untouched. Free (0 rows).
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

client.transcripts.merges.submit(
    video_id="video_id",
    idempotency_key="8b2f6c3e-4d1a-4e7b-9c05-2f6a1b7d3e90",
    source_name="sourceName",
    target_entity_id=1,
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

**source_name:** `str` — The name as it appears in this video (e.g. a first-name-only mention).

</dd>
</dl>

<dl>
<dd>

**target_entity_id:** `int` — The canonical entity these mentions actually refer to.

</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — 1 to 255 printable ASCII characters (0x21 to 0x7E); anything else is 400 invalid_idempotency_key. Persist a unique key and the exact request before sending a logical mutation. A retry returns its stored response with Idempotency-Replayed: true. A changed intent under a finalized key returns 409 idempotency_conflict. Keys belong to the authenticated owner, credential and mutation domain. Current authorization still applies. Receipts have no general 24-hour expiry; signing-secret recovery alone expires after 24 hours or when the secret is displaced.

</dd>
</dl>

<dl>
<dd>

**replace_with:** `typing.Optional[str]` — Optional respelling applied to the transcript text (e.g. "Imad" → "Emad").

</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[str]`

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

<details><summary><code>client.transcripts.merges.<a href="src/arcmira/transcripts/merges/client.py">withdraw</a>(...) -> WithdrawnResponse</code></summary>
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

client.transcripts.merges.withdraw(
    video_id="video_id",
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

**video_id:** `str` — YouTube video id, 11 characters.

</dd>
</dl>

<dl>
<dd>

**id:** `str` — The pending row id, as result.id of the response that accepted it.

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
