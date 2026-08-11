# General Moderation

A production-grade, multi-language content moderation microservice. A thin
Python (FastAPI) wrapper over C/C++/Rust libraries detects vulgar and
politically sensitive content in 20+ languages with sub-millisecond latency
on Level 1, backed by an optional llama.cpp (C++) inference engine on Level 2.

## Monorepo Layout

| Directory      | Contents                                              |
| :------------- | :---------------------------------------------------- |
| `backend/`     | Python FastAPI moderation service (thin wrapper)      |
| `frontend/`    | React + TypeScript + Ant Design admin UI              |
| `docs/`        | VitePress documentation                               |
| `deployment/`  | systemd, FRP, logrotate, Docker, nginx configs        |
| `scripts/`     | Build, test, deploy, and format scripts               |

## Highlights

- 7-layer detection pipeline, every layer backed by C/C++/Rust/WASM.
- 5 active multi-language detectors covering 26+ languages (plus 3 more
  guard-wired for environments that can provide them).
- Zero local word-bank text files; base dictionaries come from pip packages.
- Custom words stored in SQLite (C implementation).
- All security-critical operations delegated to compiled libraries
  (OpenSSL, libsodium, Rust regex, Redis hiredis).
- Well-structured Python: ABCs, frozen dataclasses, private fields, full typing.
- TypeScript/React admin UI with strict UI/logic separation.

## Detector Coverage

Five detectors are active on a standard install; three more are guard-wired
and activate only when a working index provides them.

| Detector | Languages | Key feature | Status |
| :--- | :--- | :--- | :--- |
| badwords | 26+ | Rust-based, fastest | Active |
| profanite | Universal | Anti-obfuscation | Active |
| glin-profanity | 25+ | Context-aware | Active |
| gangajal | All | WebAssembly | Active |
| PyProfane | Universal | Soundex-based | Active |
| safetext | 13 | Phrase detection | Guard-wired |
| sensitive-word-filter-cn | Chinese | Pinyin, symbols | Guard-wired |
| profanity-filter2 | Universal | Levenshtein automaton | Guard-wired |

`scheckbl` and `valx` are not wired (their documented APIs do not exist in
the installed versions); `datasketch` is a potential future semantic layer
that needs a pre-built toxic-signature database.

## Quick Start

Dependencies are managed with **uv** (the modern, Rust-based Python
toolchain). Install it from <https://astral.sh/uv/>.

### One-command orchestration (recommended)

From the repository root:

```bash
npm install          # installs concurrently (root tooling)
npm run install:all  # uv sync (backend) + npm deps (frontend)
npm run start        # runs backend (uvicorn :8080) + frontend (vite :5173)
```

Other root scripts: `npm run lint`, `npm run format`, `npm run build`,
`npm run install:backend`.

### Manual backend

```bash
cd backend
uv sync              # create .venv and install all locked dependencies
cp .env.example .env
uv run python run.py
```

See `docs/` for the full guide, API reference, and deployment instructions.

## Model Auto-Download

On first startup, General Moderation automatically downloads the
Qwen3.5-9B-Q4_K_M.gguf model (~5.78 GB) into `backend/models/`. The download
runs in the background so the service starts immediately; the model is loaded
once it is available.

**For users in China:** the system probes connectivity and falls back in
order:

1. `https://huggingface.co` (primary)
2. `https://hf-mirror.com` (primary mirror)
3. `https://www.modelscope.cn` (Alibaba-owned platform)
4. Manual download instructions if all endpoints fail

Downloads retry with exponential backoff (1s, 2s, 4s) and resume partial
transfers. The model unloads after `MODEL_IDLE_TIMEOUT_SECONDS` of inactivity
to free memory.

**To manually place the model:**

1. Download from:
   - Primary: <https://huggingface.co/bartowski/Qwen_Qwen3.5-9B-GGUF>
   - Mirror: <https://hf-mirror.com/bartowski/Qwen_Qwen3.5-9B-GGUF>
2. Place it at `backend/models/Qwen_Qwen3.5-9B-Q4_K_M.gguf`
3. Or set `MODEL_PATH=/path/to/model.gguf` in `.env`

## Performance Optimizations

| Optimization | Implementation | Benefit |
| :--- | :--- | :--- |
| KV Cache Quantization | Q8_0 (`type_k`/`type_v`) | ~50% KV memory reduction |
| Flash Attention | Enabled | Reduced memory bandwidth |
| Memory Locking (mlock) | Enabled | Prevents OS swapping |
| Idle Unloading | 300s timeout | Frees model memory when idle |
| Result Cache | LRU + TTL (mmh3 key) | <50ms for repeated requests |
| Parallel Detectors | ThreadPoolExecutor | Faster multi-package runs |
| CPU Offload | `run_in_threadpool` | Non-blocking async API |
| Worker Reduction | 3 gunicorn workers | Lower per-worker model memory |
| Garbage Collection | Tuned thresholds | Fewer GC pauses |
| Adaptive Short-Circuit | Hit-rate ordering | Faster common cases |
| Download Retry | Exponential backoff | Robust network recovery |

## License

[MIT](LICENSE)
