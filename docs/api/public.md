# Public Moderation API

The public API moderates single messages and batches. Responses use camelCase
aliases, validated by Rust `pydantic-core`, and serialized with Rust `orjson`.
All endpoints are rate-limited per client address but require no API key.

## Validation and Limits

| Rule | Value | Enforced by |
| :--- | :--- | :--- |
| `text` length | 1–8192 characters | `pydantic-core` (Rust) |
| batch size | 1–100 items | `pydantic-core` (Rust) |
| rate limit | configurable requests per window per client | slowapi |
| app isolation | `app_name` defaults to `"default"` | application glue |

## Moderate a Message

`POST /moderate`

```json
{
    "text": "string",
    "user_id": "string",
    "app_name": "string",
    "id": "string"
}
```

`app_name` is optional and defaults to `"default"`; it isolates user
profiling per application.

### Response

```json
{
    "id": null,
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
    "latencyMs": 12.4,
    "detectorChain": ["sensitive_stop_words", "bloom_filter", "rolling_hash", "aho_corasick"]
}
```

| Field | Type | Description |
| :--- | :--- | :--- |
| `verdict` | `PASS` \| `BLOCK` \| `REVIEW` | the final decision |
| `allowed` | boolean | whether the message may be published |
| `levelUsed` | integer | detection level that decided (1 or 2) |
| `aiTriggered` | boolean | whether the LLM was invoked |
| `suspicionScore` | number | the 0-100 suspicion score |
| `reason` | string \| null | the primary reason |
| `matchedWord` | string \| null | the primary matched word |
| `matchedLanguage` | string \| null | ISO code of the detected language |
| `confidenceScore` | number \| null | overall confidence |
| `severity` | integer \| null | severity of the strongest match (0–10) |
| `category` | string \| null | semantic bucket of the strongest match |

## Moderate a Batch

`POST /moderate/batch`

```json
{
    "items": [
        { "text": "clean message", "user_id": "u1" },
        { "text": "another message", "user_id": "u2" }
    ]
}
```

Returns `{"results": [...], "totalLatencyMs": 42.1}`.

## Error Responses

| Status | Meaning |
| :--- | :--- |
| `422` | Validation failure — missing/empty `text`, non-string `text`, `text` over the length cap, empty/missing/oversized batch, item without `text` |
| `429` | Rate limit exceeded |
| `500` | Internal error |

## Behavior Contract

- **Determinism** — identical requests return identical verdicts; repeated
  requests are served from the `mmh3`-keyed LRU result cache.
- **Profiling** — `user_id` drives the per-app profiling window; the same
  user in different `app_name`s is tracked separately.
- **Audit** — every decision is written to the JSONL audit log for the
  dashboard and spot-check sampling.
- **CamelCase responses** — `levelUsed`, `suspicionScore`, `latencyMs`,
  `detectorChain`, `totalLatencyMs`, `matchedWords`, `matchedLanguage`,
  `confidenceScore`, `aiTriggered`, `allowed`.
