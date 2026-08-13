# Workbench API

The workbench API exposes the moderation engine's internal pipeline state to
the developer console. Every route is prefixed with `/test` and requires the
`X-API-Key` header set to `ADMIN_API_KEY`. Authentication is enforced at the
router level by a constant-time API-key dependency; a missing, empty, or
incorrect key returns HTTP 401.

Unlike the public `/moderate` endpoints, these routes are **not** rate limited
and are intended for developer and operations use.

## Endpoint Matrix

| Area | Endpoint | Method | Purpose |
| :--- | :--- | :--- | :--- |
| Traces | `/test/moderate-detail` | POST | Full pipeline trace (JSON, or SSE with `?stream=true`) |
| Traces | `/test/pipeline-status` | GET | Stream one moderation run over SSE |
| Load test | `/test/load-test` | POST | Concurrent load test, streamed over SSE |
| Dashboard | `/test/dashboard` | GET | Aggregate today's audit records |
| Config | `/test/config` | GET | Full settings catalog |
| Config | `/test/config` | POST | Apply a batch of settings immediately |
| Profiles | `/test/user-profile` | GET | One user's profiling history and ratio |
| Profiles | `/test/user-profile/seed` | POST | Record simulated user history |

## Authentication

All requests must carry the admin key:

```bash
curl -H "X-API-Key: $ADMIN_API_KEY" http://127.0.0.1:18427/test/dashboard
```

A missing, empty, or incorrect key returns:

```json
{
    "detail": "Invalid or missing API key"
}
```

with HTTP status `401`.

---

## Detailed Moderation

### `POST /test/moderate-detail`

Runs the three-stage pipeline and returns the response **and** the full trace.

#### Request Body

```json
{
    "id": "optional-caller-id",
    "app_name": "default",
    "user_id": "user-123",
    "text": "I will kill you tonight"
}
```

| Field | Type | Constraint | Default |
| :--- | :--- | :--- | :--- |
| `id` | string \| null | — | `null` |
| `app_name` | string \| null | — | `"default"` |
| `user_id` | string \| null | — | `null` |
| `text` | string | 1–8192 characters | required |

#### Non-Streaming Response (default)

Returns HTTP 200 with a JSON object:

```json
{
    "response": {
        "id": null,
        "verdict": "BLOCK",
        "allowed": false,
        "levelUsed": 2,
        "aiTriggered": true,
        "suspicionScore": 55.0,
        "reasons": ["Exact sensitive word matched in Aho-Corasick automaton"],
        "reason": "Exact sensitive word matched in Aho-Corasick automaton",
        "matchedWords": ["badword"],
        "matchedWord": "badword",
        "matchedLanguage": null,
        "confidenceScore": 1.0,
        "latencyMs": 3.2,
        "detectorChain": ["bloom_filter", "rolling_hash", "aho_corasick"]
    },
    "trace": {
        "request_id": null,
        "app_name": "default",
        "user_id": "user-123",
        "text": "I will kill you tonight",
        "verdict": "BLOCK",
        "suspicion_score": 55.0,
        "level_used": 2,
        "ai_triggered": true,
        "reasons": ["Exact sensitive word matched in Aho-Corasick automaton"],
        "matched_words": ["badword"],
        "matched_language": null,
        "confidence_score": 1.0,
        "total_latency_ms": 3.2,
        "stage_1": {
            "fast_path": false,
            "verdict": "BLOCK",
            "latency_ms": 0.11
        },
        "stage_2": {
            "detector_results": [
                {
                    "name": "bloom_filter",
                    "enabled": true,
                    "available": true,
                    "matched": true,
                    "blocking": false,
                    "confidence": 0.5,
                    "matched_words": ["badword"],
                    "matched_language": null,
                    "reason": "Token possibly present in word bank (Bloom hit)",
                    "latency_ms": 0.03,
                    "weight": 30
                }
            ],
            "semantic_similarities": {},
            "semantic_enabled": false,
            "user_profile": null,
            "suspicion_score": 55.0,
            "weight_contributions": [
                {
                    "kind": "detector",
                    "name": "aho_corasick",
                    "value": 1.0,
                    "weight": 30,
                    "contributed": 30
                }
            ],
            "latency_ms": 1.2
        },
        "stage_3": {
            "invoked": true,
            "trigger": "[or] score 55 > 50",
            "model_available": true,
            "prompt": "<|im_start|>system ...",
            "response": "BLOCK",
            "verdict": "BLOCK",
            "confidence": 0.9,
            "latency_ms": 1200.0
        }
    }
}
```

The `response` object uses camelCase aliases; the `trace` uses snake_case
field names. See the [trace structure](/guide/test-workbench#the-pipeline-trace)
for every field.

#### Streaming Response (`?stream=true`)

Returns `text/event-stream`. The pipeline runs in a worker thread and each
stage completion is pushed to the stream as it happens.

| Event | Payload |
| :--- | :--- |
| `stage1_complete` | `{"stage":1,"fast_path":false,"verdict":"REVIEW","latency_ms":0.11}` |
| `detector_result` | `{"name":"bloom_filter","matched":true,"blocking":false,"confidence":0.5,"matched_words":["badword"],"reason":"Token possibly present in word bank (Bloom hit)","latency_ms":0.03}` |
| `stage2_complete` | `{"stage":2,"suspicion_score":55.0,"latency_ms":1.2,"semantic_similarities":{},"user_profile":null,"weight_contributions":[...]}` |
| `stage3_complete` | `{"stage":3,"invoked":true,"trigger":"[or] score 55 > 50","model_available":true,"prompt":"...","response":"BLOCK","verdict":"BLOCK","confidence":0.9,"latency_ms":1200.0}` |
| `complete` | `{"response":{...},"trace":{...}}` |
| `error` | `{"detail":"message"}` — replaces `complete` when the pipeline raises |

The final `complete` payload is byte-for-byte identical to the non-streaming
response.

#### Example

```bash
curl -X POST "http://127.0.0.1:18427/test/moderate-detail?stream=true" \
     -H "X-API-Key: $ADMIN_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"text":"hello world","user_id":"u1","app_name":"default"}'
```

#### Validation

| Constraint | Failure |
| :--- | :--- |
| `text` shorter than 1 character | `422` |
| `text` longer than 8192 characters | `422` |
| missing `X-API-Key` | `401` |

---

### `GET /test/pipeline-status`

Streams one moderation run as Server-Sent Events. The message is passed as a
query parameter, making the endpoint convenient for scripts and simple browser
clients that want the live pipeline without a POST body. It emits the exact
same event sequence as `POST /test/moderate-detail?stream=true` and finishes
with an identical `complete` payload.

#### Query Parameters

| Parameter | Type | Constraint | Default |
| :--- | :--- | :--- | :--- |
| `text` | string | 1–8192 characters | required |
| `user_id` | string \| null | 1–256 characters | `null` |
| `app_name` | string \| null | 1–64 characters | `null` |

#### Response

`text/event-stream` with the same events as
[`moderate-detail` streaming](#streaming-response-streamtrue):

| Event | Payload |
| :--- | :--- |
| `stage1_complete` | `{"stage":1,"fast_path":false,"verdict":"REVIEW","latency_ms":0.11}` |
| `detector_result` | one frame per detector |
| `stage2_complete` | `{"stage":2,"suspicion_score":55.0,...}` |
| `stage3_complete` | `{"stage":3,"invoked":true,...}` |
| `complete` | `{"response":{...},"trace":{...}}` |
| `error` | `{"detail":"message"}` — replaces `complete` when the pipeline raises |

#### Example

```bash
curl -N "http://127.0.0.1:18427/test/pipeline-status?text=hello+world&user_id=u1" \
     -H "X-API-Key: $ADMIN_API_KEY"
```

#### Validation

| Constraint | Failure |
| :--- | :--- |
| missing or empty `text` | `422` |
| `text` longer than 8192 characters | `422` |
| missing `X-API-Key` | `401` |

---

## Load Test

### `POST /test/load-test`

Runs a concurrent load test against the engine and streams progress over SSE.

#### Request Body

```json
{
    "concurrent_users": 10,
    "requests_per_user": 10,
    "text_source": "random",
    "corpus": [],
    "custom_texts": [],
    "app_name": "default",
    "user_prefix": "loadtest"
}
```

| Field | Type | Constraint | Default |
| :--- | :--- | :--- | :--- |
| `concurrent_users` | integer | 1–1000 | 10 |
| `requests_per_user` | integer | 1–100 | 10 |
| `text_source` | string | `random` \| `corpus` \| `custom` | `random` |
| `corpus` | string[] | used when `text_source` is `corpus` | `[]` |
| `custom_texts` | string[] | used when `text_source` is `custom` | `[]` |
| `app_name` | string | — | `"default"` |
| `user_prefix` | string | — | `"loadtest"` |

Total requests = `concurrent_users × requests_per_user`.

#### SSE Events

| Event | Payload |
| :--- | :--- |
| `progress` | `{"completed":50,"total":100,"elapsed_ms":2500.5,"rps":20.0,"p50":12.4,"p95":40.2,"p99":60.1,"errors":0,"llm_invocations":3,"verdicts":{"PASS":40,"REVIEW":7,"BLOCK":3}}` |
| `complete` | The full result object below |

Progress events are emitted at least every `max(1, total / 100)` completed
requests and at least every 500 ms.

#### Result Object

```json
{
    "total_requests": 100,
    "successful_requests": 99,
    "failed_requests": 1,
    "total_duration_ms": 8200.5,
    "requests_per_second": 12.07,
    "latency_percentiles": {
        "p50": 12.4,
        "p95": 40.2,
        "p99": 60.1
    },
    "max_concurrency_reached": 10,
    "llm_invocation_count": 5,
    "error_distribution": {
        "RuntimeError": 1
    },
    "verdicts": {
        "PASS": 80,
        "REVIEW": 14,
        "BLOCK": 5
    }
}
```

#### Example

```bash
curl -N -X POST "http://127.0.0.1:18427/test/load-test" \
     -H "X-API-Key: $ADMIN_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"concurrent_users":20,"requests_per_user":10,"text_source":"corpus","corpus":["hello world","I will kill you tonight"]}'
```

#### Validation

| Constraint | Failure |
| :--- | :--- |
| `concurrent_users` outside 1–1000 | `422` |
| `requests_per_user` outside 1–100 | `422` |
| `text_source` not one of the three literals | `422` |
| missing `X-API-Key` | `401` |

---

## Dashboard

### `GET /test/dashboard`

Returns aggregated metrics for the current UTC day, parsed from the audit log.

```json
{
    "total_requests_today": 1234,
    "blocked_today": 120,
    "block_rate": 0.0972,
    "avg_latency_ms": 15.3,
    "llm_invocations_today": 49,
    "llm_invocation_rate": 0.0397,
    "top_detectors": [
        { "name": "aho_corasick", "count": 890 },
        { "name": "bloom_filter", "count": 620 }
    ],
    "requests_over_time": [
        { "bucket": "08:00", "count": 12 },
        { "bucket": "08:01", "count": 9 }
    ],
    "metrics": {
        "requests_total": 1234.0,
        "requests_block_total": 120.0,
        "ai_requests_total": 49.0,
        "semantic_queries_total": 0.0,
        "rate_limit_hits_total": 0.0
    }
}
```

| Field | Description |
| :--- | :--- |
| `total_requests_today` | `moderation_decision` records whose timestamp starts with today's UTC date |
| `blocked_today` | Records with `verdict == "BLOCK"` |
| `block_rate` | `blocked / total` (0.0 when no records) |
| `avg_latency_ms` | Mean of `latencyMs` (0.0 when no records) |
| `llm_invocations_today` | Records with `aiTriggered == true` |
| `llm_invocation_rate` | `llm_invocations / total` |
| `top_detectors` | Ranked detector name → count from `detectorChain`, top 8 |
| `requests_over_time` | Per-minute `HH:MM` → request count, oldest to newest |
| `metrics` | Live engine runtime counters |

Only records whose `message` is `moderation_decision` are counted. The scan
starts at the newest log line and stops at the first record older than today,
because the log is written chronologically.

#### Example

```bash
curl -H "X-API-Key: $ADMIN_API_KEY" http://127.0.0.1:18427/test/dashboard
```

---

## Configuration

### `GET /test/config`

Returns the full settings catalog, identical in shape to `/admin/settings`:

```json
{
    "settings": [
        {
            "key": "ENABLE_DETECTOR_AHO_CORASICK",
            "value": true,
            "type": "boolean",
            "description": "Enable the Aho-Corasick exact matcher",
            "editable": true
        }
    ]
}
```

Each entry has `key`, `value`, `type` (`boolean`, `integer`, `float`, or
`string`), `description`, and `editable`. Secret (`*_KEY`, `*_SECRET`) and
restart-required values are not editable.

### `POST /test/config`

Applies a batch of settings immediately.

```json
{
    "settings": {
        "WEIGHT_DETECTOR_AHO": 35,
        "ENABLE_DETECTOR_ROLLING_HASH": false,
        "SEMANTIC_SIMILARITY_THRESHOLD": 0.88
    }
}
```

#### Response

```json
{
    "status": "ok",
    "updated": ["WEIGHT_DETECTOR_AHO", "ENABLE_DETECTOR_ROLLING_HASH", "SEMANTIC_SIMILARITY_THRESHOLD"]
}
```

Keys are uppercased before matching. Values are validated (type, range) and
the settings cache reloads immediately, so the next interactive moderation
reflects the change.

#### Validation

| Condition | Failure |
| :--- | :--- |
| Unknown key | `400 {"detail": "Unknown setting: <KEY>"}` |
| Read-only key (secret or restart-required) | `400 {"detail": "Setting is read-only: <KEY>"}` |
| Value fails type or range validation | `400 {"detail": "<KEY> must be a boolean"}` etc. |
| Missing `X-API-Key` | `401` |

#### Examples

```bash
curl -H "X-API-Key: $ADMIN_API_KEY" http://127.0.0.1:18427/test/config
```

```bash
curl -X POST http://127.0.0.1:18427/test/config \
     -H "X-API-Key: $ADMIN_API_KEY" \
     -H "Content-Type: application/json" \
     -d '{"settings":{"WEIGHT_DETECTOR_AHO":35}}'
```

---

## User Profiles

### `GET /test/user-profile`

Returns one user's profiling history, aggregates, and ratio.

```
GET /test/user-profile?app_name=default&user_id=user-123
```

#### Response

```json
{
    "app_name": "default",
    "user_id": "user-123",
    "ratio": 0.4,
    "total_msgs": 50,
    "flagged_msgs": 20,
    "blocked_msgs": 0,
    "daily": [
        {
            "day_offset": 1,
            "total_msgs": 50,
            "flagged_msgs": 20,
            "blocked_msgs": 0,
            "reviewed_msgs": 0,
            "date": "2026-08-13"
        }
    ],
    "summaries": [
        {
            "cycle_id": 1,
            "start_day": "2025-10-01",
            "end_day": "2025-12-30",
            "total_msgs": 100,
            "flagged_msgs": 40,
            "blocked_msgs": 5,
            "reviewed_msgs": 0,
            "next_cycle_id": null
        }
    ]
}
```

| Field | Description |
| :--- | :--- |
| `ratio` | `(flagged + blocked) / total` across the live window and every archived summary |
| `total_msgs` / `flagged_msgs` / `blocked_msgs` | Aggregates across `daily` and `summaries` |
| `daily` | Live 91-day window rows from `user_daily_stats` |
| `summaries` | Archived cycle summaries from `user_summaries`, oldest cycle first |

#### Validation

| Condition | Failure |
| :--- | :--- |
| Missing `user_id` | `400 {"detail": "user_id is required"}` |
| Missing `X-API-Key` | `401` |

### `POST /test/user-profile/seed`

Records simulated user history through the profiler so experiments have a
meaningful ratio. Rows are real and persist; load tests do **not** call this.

```json
{
    "app_name": "default",
    "user_id": "sim-user",
    "total_msgs": 50,
    "flagged_msgs": 40
}
```

| Field | Type | Constraint | Default |
| :--- | :--- | :--- | :--- |
| `app_name` | string | — | `"default"` |
| `user_id` | string | 1–256 characters | required |
| `total_msgs` | integer | 1–1000 | 50 |
| `flagged_msgs` | integer | 0–1000 | 0 |

#### Response

```json
{
    "status": "seeded"
}
```

#### Validation

| Condition | Failure |
| :--- | :--- |
| Empty `user_id` | `422` |
| `total_msgs` or `flagged_msgs` out of range | `422` |
| Missing `X-API-Key` | `401` |

---

## Trace Data Structures

The trace is returned by `moderate-detail` and is documented field-by-field in
the [Test Workbench guide](/guide/test-workbench#the-pipeline-trace). Summary:

| Structure | Fields |
| :--- | :--- |
| `PipelineTrace` | `request_id`, `app_name`, `user_id`, `text`, `verdict`, `suspicion_score`, `level_used`, `ai_triggered`, `reasons`, `matched_words`, `matched_language`, `confidence_score`, `stage_1`, `stage_2`, `stage_3`, `total_latency_ms` |
| `Stage1Trace` | `fast_path`, `verdict`, `latency_ms` |
| `Stage2Trace` | `detector_results`, `semantic_similarities`, `semantic_enabled`, `user_profile`, `suspicion_score`, `weight_contributions`, `latency_ms` |
| `DetectorRunTrace` | `name`, `enabled`, `available`, `matched`, `blocking`, `confidence`, `matched_words`, `matched_language`, `reason`, `latency_ms`, `weight` |
| `WeightContribution` | `kind`, `name`, `value`, `weight`, `contributed` |
| `Stage3Trace` | `invoked`, `trigger`, `model_available`, `prompt`, `response`, `verdict`, `confidence`, `latency_ms` |

---

## Error Codes

| Status | Meaning |
| :--- | :--- |
| `401` | Missing or invalid `X-API-Key` |
| `400` | Valid JSON, semantically rejected (empty user ID, invalid settings key or value) |
| `422` | Validation failure at the `pydantic-core` boundary (missing text, out-of-range load test values, empty user ID on seed) |
| `500` | Unexpected pipeline exception (streamed as an `error` SSE event in streaming mode) |

## Authentication and Security

- Every `/test` route is guarded by `RequireAdminApiKey` using constant-time
  comparison.
- Security headers (`nosniff`, `DENY` framing, strict CSP, HSTS) are applied to
  every response by the security-headers middleware.
- The settings catalog redacts `*_KEY` and `*_SECRET` values.
- Load tests bypass the response cache and skip profile and feedback writes so
  a stress run does not pollute tuning data.
- Audit records store only a text hash and a 50-character preview, never the
  full message body.
