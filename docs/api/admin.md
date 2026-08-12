# Admin API

All admin endpoints are prefixed with `/admin` and require the
`X-API-Key` header set to `ADMIN_API_KEY`. Authentication is enforced at the
router level by a constant-time API-key dependency; a missing, empty, or
incorrect key returns HTTP 401.

## Endpoint Matrix

| Area | Endpoint | Method | Purpose |
| :--- | :--- | :--- | :--- |
| Word bank | `/admin/wordbank/words` | POST | Add a custom word |
| Word bank | `/admin/wordbank/words` | GET | List / search custom words |
| Word bank | `/admin/wordbank/words/{id}` | PUT | Update a custom word |
| Word bank | `/admin/wordbank/words` | DELETE | Remove a custom word by `word_id` |
| Word bank | `/admin/wordbank/import` | POST | Bulk import words |
| Word bank | `/admin/wordbank/export` | GET | Export all custom words |
| Word bank | `/admin/wordbank/audit` | GET | Read recent audit records |
| Word bank | `/admin/wordbank/stats` | GET | Word bank statistics |
| Word bank | `/admin/wordbank/languages` | GET | Distinct languages |
| Word bank | `/admin/wordbank/categories` | GET | Distinct categories |
| Service | `/admin/reload` | POST | Rebuild word bank structures |
| Service | `/admin/shutdown` | POST | Graceful shutdown |
| Service | `/admin/health` | GET | Health report |
| Service | `/admin/metrics` | GET | Prometheus metrics |
| Logs | `/admin/logs` | GET | List log files |
| Logs | `/admin/logs/{filename}` | GET | Download a log tail |
| Settings | `/admin/settings` | GET | Full settings catalog |
| Settings | `/admin/settings` | POST | Update settings |
| Export | `/admin/export` | GET | Download a full data ZIP |
| Feedback | `/admin/feedback` | POST | Record an administrator correction |
| Tuning | `/admin/tune` | POST | Run the tuning batch on demand |
| App config | `/admin/app-config` | GET | List app trigger policies |
| App config | `/admin/app-config/{app}` | GET | Effective policy for one app |
| App config | `/admin/app-config` | POST | Set an app trigger policy |
| Semantic | `/admin/semantic` | GET | Semantic stage status |
| Semantic | `/admin/semantic/categories` | GET | Supported categories |
| Semantic | `/admin/semantic` | POST | Add / delete a sensitive example |
| Stats | `/admin/stats` | GET | Dashboard statistics |
| Stats | `/admin/spot-check` | GET | Random audit sample |

## Word Bank

### Add a Custom Word

`POST /admin/wordbank/words`

```json
{
    "word": "badword",
    "language": "en",
    "category": "profanity",
    "severity": 5
}
```

Returns `201` with the stored record. Duplicates return `409`.

### Remove a Custom Word

`DELETE /admin/wordbank/words?word_id=1`

Returns `{"removed": true}`.

### List Custom Words

`GET /admin/wordbank/words?search=foo`

Returns the matching words as an array.

### Update a Custom Word

`PUT /admin/wordbank/words/{id}`

Accepts any subset of `word`, `language`, `category`, `severity`.

### Bulk Import

`POST /admin/wordbank/import`

```json
{
    "items": [
        { "word": "w1", "language": "de", "category": "profanity", "severity": 3 }
    ]
}
```

Returns `{"imported": 1}`.

### Bulk Export

`GET /admin/wordbank/export`

Returns every custom word as a JSON array.

### Audit

`GET /admin/wordbank/audit`

Returns the last 100 parsed JSONL audit records.

### Statistics

`GET /admin/wordbank/stats`

```json
{
    "totalWords": 1024,
    "customWords": 24,
    "baseWords": 1000,
    "languages": 26,
    "categories": 6
}
```

### Languages and Categories

- `GET /admin/wordbank/languages`
- `GET /admin/wordbank/categories`

## Service Control

### Reload Word Bank

`POST /admin/reload`

Rebuilds the Aho-Corasick automaton and Bloom filter atomically. Returns
`{"status": "reloaded"}`.

### Graceful Shutdown

`POST /admin/shutdown`

Releases the model, storage, and logger, then stops the process. Returns
`202 {"status": "shutting_down"}`.

### Health

`GET /admin/health`

```json
{
    "status": "ok",
    "uptimeSeconds": 4321.5,
    "wordCount": { "totalWords": 1024, "customWords": 24, "baseWords": 1000, "languages": 26, "categories": 6 },
    "llamaAvailable": true,
    "detectors": [
        { "name": "bloom_filter", "available": true },
        { "name": "aho_corasick", "available": true }
    ]
}
```

### Metrics

`GET /admin/metrics`

Prometheus text exposition. Includes:

- `moderation_requests_total`
- `moderation_requests_pass_total` / `_block_total` / `_review_total`
- `moderation_ai_requests_total`
- `moderation_rate_limit_hits_total`
- `detector_<name>_seconds_total`

## Logs

### List Log Files

`GET /admin/logs`

Returns `[{"name": "moderation.log", "size": 12345}]`.

### Download a Log File

`GET /admin/logs/{filename}`

Returns the file name, total line count, and the last 200 lines. Filenames
are validated against a strict pattern to prevent path traversal.

## Runtime Settings

### List Settings

`GET /admin/settings`

Returns the full setting catalog with `key`, `value`, `type`,
`description`, and `editable` flags. Secrets and restart-required values are
excluded from editing.

### Update Settings

`POST /admin/settings`

```json
{
    "settings": {
        "MODEL_CONTEXT_SIZE": 16384,
        "CACHE_MAX_SIZE": 600
    }
}
```

Values are validated; invalid or read-only keys return `400`. See the
[Admin Settings](/guide/admin-settings) guide for the editable groups.

## Data Export

`GET /admin/export`

Returns a ZIP archive of all databases, CSV dumps, logs, a redacted
configuration snapshot, and semantic indexes. Rate-limited to one request per
ten minutes per client. See the [Data Export](/guide/data-export) guide.

## Feedback and Auto-Tuning

### Submit Feedback

`POST /admin/feedback`

```json
{
    "request_id": "uuid",
    "verdict": "BLOCK",
    "is_correct": true,
    "actual_action": "BLOCK"
}
```

Returns `{"status": "ok"}`.

### Run the Tuning Batch

`POST /admin/tune`

Runs the daily weight and threshold tuning on demand and returns a report
with the adjusted weights and threshold.

## Per-Application Trigger Policy

### List Apps

`GET /admin/app-config`

### Get One App

`GET /admin/app-config/{app_name}`

### Set an App Policy

`POST /admin/app-config`

```json
{
    "app_name": "myapp",
    "score_threshold": 50,
    "semantic_boost": true,
    "user_ratio_boost": true,
    "logic_type": "or"
}
```

## Semantic Index Management

### Status

`GET /admin/semantic`

Returns availability, model name, and per-category entry counts.

### Categories

`GET /admin/semantic/categories`

### Add or Delete an Example

`POST /admin/semantic`

```json
{
    "action": "add",
    "category": "violence",
    "text": "example sensitive phrase"
}
```

## Statistics and Spot-Check

### Dashboard Statistics

`GET /admin/stats`

Returns runtime counters, profiling stats, word bank totals, and semantic
status.

### Spot-Check

`GET /admin/spot-check?count=50`

Returns a random sample of recent audit entries with verdicts and suspicion
scores.

## Validation Rules

| Endpoint | Constraint | Failure |
| :--- | :--- | :--- |
| `POST /admin/wordbank/words` | `word` length 1–200; `severity` 0–10 | 422 (empty, over-length, out-of-range severity) |
| `POST /admin/wordbank/words` | duplicate word | 409 |
| `DELETE /admin/wordbank/words` | `word_id` ≥ 1 | 422 |
| `POST /admin/wordbank/import` | 1–1000 items, each with `word` | 422 (empty, over-cap, missing key) |
| `PUT /admin/wordbank/words/{id}` | unknown `id` | 404 |
| `GET /admin/app-config/{app}` | empty app name | 400 |
| `POST /admin/app-config` | `score_threshold` 0–100; `logic_type` `and`\|`or` | 422 |
| `POST /admin/settings` | unknown, invalid, or read-only key | 400 |
| `GET /admin/logs/{filename}` | filename must match `[A-Za-z0-9._-]+` | 400; missing file 404 |
| `POST /admin/semantic` | unknown category or empty text | 400; deleting a missing example 404 |
| `POST /admin/feedback` | `verdict` ∈ `BLOCK`\|`PASS`\|`REVIEW`; `actual_action` ∈ `BLOCK`\|`PASS`; `request_id` non-empty | 422 |
| `POST /admin/tune` | auto-tuning disabled | 400 |

## Error Codes

| Status | Meaning |
| :--- | :--- |
| `401` | Missing or invalid `X-API-Key` |
| `400` | Valid JSON, semantically rejected (bad app name, disabled tuning, invalid settings key) |
| `404` | Resource not found (unknown word id, missing log file, missing semantic example) |
| `409` | Conflict (duplicate word) |
| `422` | Validation failure at the Rust `pydantic-core` boundary |
| `429` | Export rate limit (once per ten minutes per client) |

## Authentication and Security

- Every admin route is guarded by `RequireAdminApiKey`, which compares the
  `X-API-Key` header using constant-time comparison.
- Security headers (`nosniff`, `DENY` framing, strict CSP, HSTS) are applied
  to every admin response by the security-headers middleware.
- Log filenames are validated against a compiled regex before touching the
  filesystem, blocking path traversal.
- The full export endpoint redacts all `*_KEY`, `*_SECRET`, `PASSWORD`, and
  `TOKEN` environment values before archiving.
