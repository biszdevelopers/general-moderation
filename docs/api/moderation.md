# Moderation API

Public endpoints for moderating single messages and batches. Requests and
responses are JSON; response fields use camelCase aliases and are serialized
with Rust `orjson`.

## Endpoint Overview

| Endpoint | Purpose | Rate limited |
| :--- | :--- | :--- |
| `POST /moderate` | Moderate a single message | yes |
| `POST /moderate/batch` | Moderate a batch of messages | yes |

All public endpoints are unauthenticated but rate-limited per client address.
No API key is required; application isolation is expressed via `app_name`.

## Moderate a Single Message

`POST /moderate`

### Request

```json
{
    "id": "msg-123",
    "app_name": "game",
    "user_id": "user-456",
    "text": "your message here"
}
```

| Field | Type | Required | Constraints | Description |
| :--- | :--- | :--- | :--- | :--- |
| `text` | string | **yes** | 1–8192 chars | The message body to moderate |
| `id` | string | no | — | Caller identifier, echoed back verbatim |
| `app_name` | string | no | — | Isolates user profiling per application; defaults to `"default"` |
| `user_id` | string | no | — | Author identifier; drives the profiling window and audit log |

Validation is enforced by `pydantic-core` (Rust) at the boundary: missing or
empty `text`, non-string `text`, and `text` over the length limit are rejected
with HTTP 422 before any application logic runs.

### Response 200

```json
{
    "id": "msg-123",
    "verdict": "BLOCK",
    "allowed": false,
    "levelUsed": 1,
    "aiTriggered": false,
    "suspicionScore": 60.0,
    "reasons": ["Sensitive stop word matched from submodule lists"],
    "reason": "Sensitive stop word matched from submodule lists",
    "matchedWords": ["敏感词"],
    "matchedWord": "敏感词",
    "matchedLanguage": "zh-CN",
    "confidenceScore": 0.85,
    "severity": 8,
    "category": "political",
    "latencyMs": 0.42,
    "detectorChain": ["sensitive_stop_words", "bloom_filter", "rolling_hash", "aho_corasick"]
}
```

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | string \| null | Echoed caller identifier |
| `verdict` | `PASS` \| `BLOCK` \| `REVIEW` | The final decision |
| `allowed` | boolean | `true` when the message may be published |
| `levelUsed` | integer | Detection level that decided: `1` (rules) or `2` (LLM) |
| `aiTriggered` | boolean | Whether the LLM was invoked |
| `suspicionScore` | number | Weighted 0–100 score (clamped) |
| `reasons` | array&lt;string&gt; | Human-readable per-detector reasons |
| `reason` | string \| null | The primary reason |
| `matchedWords` | array&lt;string&gt; | Every matched dictionary word (deduplicated) |
| `matchedWord` | string \| null | The primary matched word |
| `matchedLanguage` | string \| null | ISO language code when a package reported one |
| `confidenceScore` | number \| null | Overall confidence, 0–1 |
| `severity` | integer \| null | Severity of the strongest match (0–10), when known |
| `category` | string \| null | Semantic bucket of the strongest match, when known |
| `latencyMs` | number | Wall-clock time for this request |
| `detectorChain` | array&lt;string&gt; | Ordered detectors that ran, e.g. `["sensitive_stop_words", "bloom_filter", "aho_corasick"]` |

### Verdict Semantics

| Verdict | Meaning |
| :--- | :--- |
| `PASS` | No sensitive content detected; safe to publish |
| `BLOCK` | A decisive exact match (Level 1), a severity hard-block, **or** the LLM confirmed sensitivity (Level 2) |
| `REVIEW` | A probabilistic or fuzzy hit awaiting human review |

`BLOCK` verdicts are preserved even when the LLM is unavailable after a
trigger fires (fail-open); only ambiguous content becomes `REVIEW`. `REVIEW`
escalates to `BLOCK` when the llama.cpp model is available and classifies the
content as sensitive, or when the suspicion score crosses
`REVIEW_ESCALATION_THRESHOLD` (default 40) and the model confirms it; without
the model the verdict stays `REVIEW`.

## Moderate a Batch

`POST /moderate/batch`

### Request

```json
{
    "items": [
        { "id": "a", "user_id": "u1", "text": "message one" },
        { "id": "b", "user_id": "u2", "text": "message two" }
    ]
}
```

| Field | Type | Required | Constraints | Description |
| :--- | :--- | :--- | :--- | :--- |
| `items` | array | **yes** | 1–100 items | Messages to moderate |

Each item accepts the same fields as a single request (`id`, `app_name`,
`user_id`, `text`). An empty list, a missing list, an item without `text`, or
more than the batch cap is rejected with 422.

### Response 200

```json
{
    "results": [
        {
            "id": "a",
            "verdict": "PASS",
            "allowed": true,
            "levelUsed": 1,
            "aiTriggered": false,
            "suspicionScore": 0.0,
            "reasons": [],
            "reason": null,
            "matchedWords": [],
            "matchedWord": null,
            "matchedLanguage": null,
            "confidenceScore": null,
            "severity": null,
            "category": null,
            "latencyMs": 0.31,
            "detectorChain": ["sensitive_stop_words", "bloom_filter", "rolling_hash"]
        }
    ],
    "totalLatencyMs": 0.64
}
```

| Field | Type | Description |
| :--- | :--- | :--- |
| `results` | array | One response object per item, **in request order** |
| `totalLatencyMs` | number | Cumulative latency across the batch |

Results are always returned in the order of the request items, and each item's
`id` is echoed into its result for correlation.

## Error Responses

| Status | Meaning | Detail example |
| :--- | :--- | :--- |
| `422` | Validation failure (Rust `pydantic-core`) | `{"detail": [{"loc": ["body","text"], "msg": "Field required", ...}]}` |
| `429` | Rate limit exceeded for this client address | `{"detail": "Rate limit exceeded"}` |
| `500` | Internal error | `{"detail": "Internal Server Error"}` |

## Behavior Details

- **Caching** — repeated identical requests are served from an in-memory LRU
  result cache keyed by `mmh3` over the request; a cache hit skips the
  pipeline. Entries are fingerprint-validated against the runtime settings
  that affect detection, and admin settings/app-config/phrase edits clear it.
- **Profiling** — requests carrying a `user_id` update the per-app profiling
  window; the same `user_id` in different `app_name`s is profiled separately.
- **Audit log** — every moderation decision is appended to the JSONL audit
  log (including severity and category) and feeds the admin dashboard and
  spot-check sampling.
- **Level assignment** — `levelUsed` is `1` whenever rule detectors are
  decisive (including the top-priority sensitive-stop-words and phrase
  detectors), and `2` only when the conditional LLM actually runs.
- **Long messages** — when the LLM is invoked, long messages are processed in
  chunks; the final verdict is `BLOCK` if any chunk blocks.
