# Admin API

All admin endpoints are prefixed with `/admin` and require the
`X-API-Key` header set to `ADMIN_API_KEY`.

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
