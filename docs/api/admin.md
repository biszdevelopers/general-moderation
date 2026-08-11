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
    "total_words": 1024,
    "custom_words": 24,
    "base_words": 1000,
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
    "uptime_seconds": 4321.5,
    "word_count": { "total_words": 1024, "custom_words": 24, "base_words": 1000, "languages": 26, "categories": 6 },
    "llama_available": true,
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
