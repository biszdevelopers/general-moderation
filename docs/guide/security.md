# Security

Every security-critical operation in this service is delegated to a compiled
C/C++/Rust library. Python is orchestration glue only.

## Security Function Mapping

| Function | Library | Python wrapper |
| :--- | :--- | :--- |
| Cryptography | OpenSSL / libsodium | `cryptography` (C) |
| Hashing | MurmurHash3 (C), SHA-256 (OpenSSL) | `mmh3`, `hashlib` (C) |
| TLS / mTLS | OpenSSL | `ssl` (stdlib, C) |
| Rate limiting | Redis + hiredis (C) | `slowapi` |
| Authentication | OpenSSL constant-time compare | `hmac.compare_digest` (C) |
| Encryption at rest | libsodium / OpenSSL | `cryptography.fernet` (C) |
| Input validation | Rust / C regex | `regex`, `re` (C) |
| JSON | Rust | `orjson` |
| String search | C Aho-Corasick | `pyahocorasick` (C) |
| Fuzzy matching | C edit distance | `python-Levenshtein` (C) |
| Bloom filter | C | `pybloom_live` (C) |

## Zero-Trust Principles

- **Least privilege** — every service runs with minimal permissions; the
  Docker images drop all capabilities.
- **Zero-trust network** — the FRP tunnel uses mutual TLS (OpenSSL).
- **Secrets management** — API keys are compared with a C constant-time
  comparison to prevent timing attacks.
- **Audit logging** — every decision is written as JSONL with `orjson`;
  logs contain only hashes and 50-character previews, never raw bodies.

## API Protection

- Admin endpoints require the `X-API-Key` header, validated by
  `hmac.compare_digest`.
- Rate limiting is applied to the public moderation endpoints via `slowapi`
  (in-memory by default; `RATE_LIMIT_STORAGE_URI=redis://...` switches to the
  C Redis client for multi-worker enforcement).
- CORS is restricted to `ALLOWED_ORIGINS`; wildcard origins are rejected.
- The service binds to `127.0.0.1` only.

## Security Headers

Every response carries:

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: default-src 'none'
Strict-Transport-Security: max-age=31536000; includeSubDomains
X-XSS-Protection: 1; mode=block
Referrer-Policy: no-referrer
```

## Sanitization and Injection Prevention

- **SQL** — all queries use parameterized SQL against the C sqlite3 module.
- **Commands** — no shell commands are executed; subprocesses always use
  `shell=False`.
- **Prompt injection (LLM)** — user text is sanitized before inference:
  chat control tokens (`<|im_start|>`, `<|im_end|>`) are stripped with C
  regex, XML metacharacters are escaped, the text is wrapped in
  `<user_text>` tags, and the model runs at `temperature=0.0`.

## Secure Defaults

- Placeholder secrets (`CHANGE_ME_...`) are replaced with strong random values
  on first startup and persisted to the gitignored `.env`. Regenerate them at
  any time with `npm run generate:secrets`.
- `ADMIN_API_KEY` comparison uses constant time.
- Health and metrics endpoints are admin-only and require a valid key.
