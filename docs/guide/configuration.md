# Configuration

All configuration happens through environment variables loaded from `backend/.env`.
The complete, annotated template lives in `backend/.env.example`.

## Server

| Variable | Default | Description |
| :--- | :--- | :--- |
| `HOST` | `127.0.0.1` | Bind address. Never expose to the public network. |
| `PORT` | `8080` | HTTP port for the ASGI server. |
| `WORKERS` | `7` | Gunicorn worker count. Leave empty to auto-detect cores. |

## Level 2 AI (llama.cpp)

| Variable | Default | Description |
| :--- | :--- | :--- |
| `MODEL_PATH` | `/var/lib/.../mistral-7b-instruct.Q4_K_M.gguf` | Path to the GGUF model file. |
| `MODEL_CONTEXT_SIZE` | `4096` | Model context window. |
| `MODEL_THREADS` | `4` | CPU threads for inference. |
| `MODEL_BATCH_SIZE` | `512` | Prompt evaluation batch size. |
| `MODEL_MAX_TOKENS` | `10` | Maximum reply tokens (classification only). |

## Detector Thresholds

| Variable | Default | Description |
| :--- | :--- | :--- |
| `BLOOM_FILTER_CAPACITY` | `1000000` | Bloom filter capacity. |
| `BLOOM_FILTER_ERROR_RATE` | `0.001` | Bloom false-positive rate. |
| `SPAM_CACHE_SIZE` | `10000` | LRU spam cache entries. |
| `SPAM_CACHE_TTL_SECONDS` | `60` | Spam hash lifetime. |
| `FUZZY_MAX_DISTANCE` | `2` | BK-tree edit distance bound. |
| `MINHASH_NUM_PERM` | `128` | MinHash permutations. |
| `MINHASH_JACCARD_THRESHOLD` | `0.85` | Near-duplicate similarity bound. |

## Multi-Language Toggles

Each of the 11 packages can be disabled independently:

| Variable | Package |
| :--- | :--- |
| `ENABLE_BADWORDS_PY` | `badwords-py` (Rust) |
| `ENABLE_PROFANITE` | `profanite` (Rust) |
| `ENABLE_GLIN_PROFANITY` | `glin-profanity` (C) |
| `ENABLE_SAFETEXT` | `safetext` (C) |
| `ENABLE_SENSITIVE_WORD_FILTER_CN` | `sensitive-word-filter-cn` (C) |
| `ENABLE_PROFANITY_FILTER` | `profanity-filter2` (C) |
| `ENABLE_GANGAJAL` | `gangajal` (WebAssembly) |
| `ENABLE_SCHECKBL` | `scheckbl` (C) |
| `ENABLE_VALX` | `valx` (C + AI) |
| `ENABLE_SENSITIVE_WORD_FILTER` | `sensitive-word-filter` (C) |
| `ENABLE_PYPROFANE` | `pyprofane` (C) |

A package that is not installed or that is disabled is skipped at runtime; the
service stays fully operational.

## Security

| Variable | Default | Description |
| :--- | :--- | :--- |
| `ADMIN_API_KEY` | `CHANGE_ME_...` | Static key for `/admin/*`. Service refuses to start unchanged. |
| `SECRET_KEY` | `CHANGE_ME_...` | Session secret. |
| `ENCRYPTION_KEY` | `CHANGE_ME_...` | 32-byte hex key for encryption at rest. |
| `RATE_LIMIT_REQUESTS` | `100` | Allowed requests per period. |
| `RATE_LIMIT_PERIOD` | `60` | Rate limit window in seconds. |
| `ALLOWED_ORIGINS` | empty | Comma-separated CORS origins. No wildcard is permitted. |

## Logging

| Variable | Default | Description |
| :--- | :--- | :--- |
| `LOG_FILE_PATH` | `./logs/moderation.log` | JSONL audit file. |
| `LOG_LEVEL` | `INFO` | Minimum severity. |
| `LOG_MAX_BYTES` | `104857600` | Rotation size (100 MiB). |
| `LOG_BACKUP_COUNT` | `10` | Rotated files to keep. |
| `LOG_RETENTION_DAYS` | `30` | External retention window for logrotate. |

## Word Storage

| Variable | Default | Description |
| :--- | :--- | :--- |
| `CUSTOM_WORDS_STORAGE` | `sqlite` | `sqlite` or `json`. |
| `CUSTOM_WORDS_PATH` | `./data/custom_words.db` | Database or document file. |

## Performance

| Variable | Default | Description |
| :--- | :--- | :--- |
| `REQUEST_TIMEOUT_SECONDS` | `30` | Endpoint timeout. |
| `MAX_BATCH_SIZE` | `100` | Maximum items in a batch request. |

## Web UI

| Variable | Default | Description |
| :--- | :--- | :--- |
| `WEBUI_ENABLED` | `true` | Enable the admin console. |
| `WEBUI_HOST` | `127.0.0.1` | UI bind address. |
| `WEBUI_PORT` | `5173` | UI port. |
| `WEBUI_API_KEY` | `CHANGE_ME_...` | Key for UI-authenticated calls. |

## Monitoring

| Variable | Default | Description |
| :--- | :--- | :--- |
| `METRICS_ENABLED` | `true` | Enable Prometheus metrics. |
| `METRICS_PORT` | `9090` | Metrics port (exposed under `/admin/metrics`). |
