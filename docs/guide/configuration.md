# Configuration

All configuration happens through environment variables loaded from `backend/.env`.
The complete, annotated template lives in `backend/.env.example`.

## Python Version Requirements

- Python 3.11+ is required (many packages have dropped Python 3.9 support)
- Recommended: Python 3.13

## Package Management (uv)

Dependencies are managed with [uv](https://astral.sh/uv/). The backend uses
`pyproject.toml` with a committed `uv.lock` for reproducible installs:

```bash
cd backend
uv sync
```

The optional Level 2 engine (`llama-cpp-python==0.3.23`) is an optional extra
because it has no Windows/cp314 wheel; install it with:

```bash
uv sync --extra ai
```

## Package Versions

All versions are verified and available on PyPI as of August 2026:

- fastapi: 0.141.1
- uvicorn: 0.52.1
- gunicorn: 26.0.0
- python-Levenshtein: 0.27.4
- cryptography: 50.0.0
- badwords-py: 2.1.0 (2.2.0/2.3.1 have no installable artifact for cp314)
- profanite: 0.1.9 (0.1.10 does not exist)
- slowapi: 0.1.10 (not 0.2.0)
- python-json-logger: 4.1.0 (not 3.2.0)
- python-multipart: 0.0.32

## Server

| Variable | Default | Description |
| :--- | :--- | :--- |
| `APP_HOST` | `0.0.0.0` | Bind address for the single-port deployment. |
| `APP_PORT` | `18427` | Single port serving both the API and the built frontend. |
| `FRONTEND_DIST_PATH` | `../frontend/dist` | Directory of the built React SPA. |
| `WORKERS` | `3` | Gunicorn worker count. Leave empty to auto-detect cores. |

## Level 2 AI (llama.cpp, auto-download)

The GGUF model is downloaded automatically on first use when `MODEL_PATH` is
`auto`.

| Variable | Default | Description |
| :--- | :--- | :--- |
| `MODEL_PATH` | `auto` | `auto` to auto-download, or a full path to an existing GGUF. |
| `MODEL_PRIMARY_REPO` | `bartowski/Qwen_Qwen3.5-9B-GGUF` | Primary Hugging Face repository. |
| `MODEL_FALLBACK_REPO` | `lmstudio-community/Qwen3.5-9B-GGUF` | Fallback repository. |
| `MODEL_FILENAME` | `Qwen_Qwen3.5-9B-Q4_K_M.gguf` | File to download. |
| `MODEL_DIR` | `./models` | Local model directory. |
| `MODEL_CONTEXT_SIZE` | `16384` | Model context window. |
| `MODEL_THREADS` | `auto` | `auto` uses CPU cores minus one, or a fixed count. |
| `MODEL_BATCH_SIZE` | `512` | Prompt evaluation batch size. |
| `MODEL_MAX_TOKENS` | `10` | Maximum reply tokens (classification only). |
| `MODEL_CACHE_TYPE_K` | `q8_0` | KV cache quantization for keys. |
| `MODEL_CACHE_TYPE_V` | `q8_0` | KV cache quantization for values. |
| `MODEL_FLASH_ATTN` | `true` | Enable flash attention. |
| `MODEL_MLOCK` | `true` | Lock model memory to prevent swapping. |
| `MODEL_IDLE_TIMEOUT_SECONDS` | `300` | Unload the model after this many idle seconds. |

### Hugging Face Endpoints

Endpoints are probed in order and the first reachable one is used:

| Variable | Default | Description |
| :--- | :--- | :--- |
| `HF_ENDPOINT` | `https://huggingface.co` | Primary endpoint. |
| `HF_MIRROR` | `https://hf-mirror.com` | China mirror. |
| `MODELSCOPE_ENDPOINT` | `https://www.modelscope.cn` | ModelScope fallback. |

## Result Cache

| Variable | Default | Description |
| :--- | :--- | :--- |
| `CACHE_MAX_SIZE` | `500` | Maximum cached moderation results. |
| `CACHE_TTL_SECONDS` | `60` | How long a cached result stays valid. |

## Concurrency

| Variable | Default | Description |
| :--- | :--- | :--- |
| `DETECTOR_THREAD_POOL_SIZE` | `4` | Worker threads for the multi-language detector pool. |

## Detector Thresholds

| Variable | Default | Description |
| :--- | :--- | :--- |
| `BLOOM_FILTER_CAPACITY` | `1000000` | Bloom filter capacity. |
| `BLOOM_FILTER_ERROR_RATE` | `0.001` | Bloom false-positive rate. |
| `SPAM_CACHE_SIZE` | `10000` | LRU spam cache entries. |
| `SPAM_CACHE_TTL_SECONDS` | `60` | Spam hash lifetime. |
| `FUZZY_MAX_DISTANCE` | `2` | BK-tree edit distance bound. |

## Multi-Language Toggles

Each registered package can be disabled independently:

| Variable | Package |
| :--- | :--- |
| `ENABLE_BADWORDS_PY` | `badwords` (Rust) |
| `ENABLE_PROFANITE` | `profanite` (Rust) |
| `ENABLE_GLIN_PROFANITY` | `glin-profanity` (C) |
| `ENABLE_SAFETEXT` | `safetext` (guard-wired) |
| `ENABLE_SENSITIVE_WORD_FILTER_CN` | `sensitive-word-filter-cn` (guard-wired) |
| `ENABLE_PROFANITY_FILTER` | `profanity-filter2` (guard-wired) |
| `ENABLE_GANGAJAL` | `gangajal` (WebAssembly) |
| `ENABLE_PYPROFANE` | `PyProfane` (C) |
| `ENABLE_SENSITIVE_STOP_WORDS` | `sensitive-stop-words` (submodule word lists) |

`badwords`, `profanite`, `glin-profanity`, `gangajal`, and `PyProfane`
activate on a standard install. `sensitive-stop-words` activates when the
`backend/data/sensitive-stop-words` submodule is initialized
(`git submodule update --init`); its directory is configurable with
`SENSITIVE_STOP_WORDS_DIR`. `safetext`, `sensitive-word-filter-cn`,
and `profanity-filter2` are guard-wired but no reachable index (pypi.org,
Tsinghua, Aliyun) provides an installable release; they activate only when a
working index provides them:

```bash
uv add safetext==0.3.3
uv add sensitive-word-filter-cn==0.1.6
uv add profanity-filter2==1.4.3
```

`scheckbl` and `valx` are not registered (their documented APIs do not exist
in the installed versions). `datasketch` is installed as a dependency but not
wired; MinHash semantic similarity is not a direct profanity detector.

A package that is not installed or that is disabled is skipped at runtime; the
service stays fully operational.

## Security

| Variable | Default | Description |
| :--- | :--- | :--- |
| `ADMIN_API_KEY` | auto-generated | Static key for `/admin/*`. Generated on first run. |
| `SECRET_KEY` | auto-generated | Session secret. Generated on first run. |
| `ENCRYPTION_KEY` | auto-generated | 32-byte hex key for encryption at rest. Generated on first run. |
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
