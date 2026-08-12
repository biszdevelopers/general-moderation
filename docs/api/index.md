# API Overview

The moderation service exposes a small public API for moderation and a larger
admin API guarded by a static API key. All request and response bodies are
JSON. Responses are serialized with Rust `orjson`.

## Base URL

- Backend: `http://127.0.0.1:18427`
- Public VPS: `http://127.0.0.1:9000`

## Authentication

| Scope | Mechanism |
| :--- | :--- |
| Public moderation | None (rate limited) |
| Admin endpoints | `X-API-Key: <ADMIN_API_KEY>` header |

## API Groups

| Group | Base path | Auth |
| :--- | :--- | :--- |
| [Public moderation](/api/public) | `/moderate`, `/moderate/batch` | None |
| [Admin](/api/admin) | `/admin` | API key |

## Error Format

Errors follow the standard FastAPI shape:

```json
{
    "detail": "Invalid or missing API key"
}
```

Rate limiting returns HTTP 429 with `{"detail": "Rate limit exceeded"}`.

## Common Concepts

- **Verdict**: `PASS`, `BLOCK`, or `REVIEW`.
- **Level 1**: the C/C++/Rust rule-based pipeline.
- **Level 2**: the llama.cpp model, used when the trigger policy fires.
- **detector_chain**: the ordered names of detectors that ran, e.g.
  `["bloom_filter", "rolling_hash", "aho_corasick"]`.
