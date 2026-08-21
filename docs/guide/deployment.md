# Deployment

The service is designed to run on a **private server without a public IP**.
An FRP tunnel exposes it to a public VPS on port `9000`, where your
application calls the moderation API over `127.0.0.1`.

## Network Architecture

```
User → Next.js (VPS) → FRP Tunnel (mTLS) → Python FastAPI (Private Server)
```

## Single-Port Production

In production the FastAPI service serves both the API and the built React
frontend on one port (`APP_HOST:APP_PORT`, default `0.0.0.0:18427`):

```
┌─────────────────────────────────────────────┐
│         SINGLE PORT (e.g. 18427)             │
│  ┌───────────────────────────────────────┐  │
│  │      Uvicorn + Gunicorn (C-uvloop)    │  │
│  │  /admin/*   → Admin Routes            │  │
│  │  /moderate  → Moderation API          │  │
│  │  /health    → Health Check            │  │
│  │  /metrics   → Prometheus              │  │
│  │  /*         → Static Files (React SPA)│  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

Deploy from the repository root:

```bash
npm install
npm run install:all
git submodule update --init          # fetch the Chinese sensitive-word lists
npm run build                        # build the frontend once
npm run start:prod                   # serve everything on APP_PORT (no build)
```

Start scripts never rebuild the frontend; re-run `npm run build` after any UI
change.

Verify:

```bash
curl http://127.0.0.1:18427/health    # {"status":"healthy"}
curl http://127.0.0.1:18427/          # the React admin app
curl http://127.0.0.1:18427/admin/health -H "X-API-Key: $KEY"
```

`npm run start` (alias for `start:dev`) keeps the two-port development
setup: Vite on `5173` proxying API calls to uvicorn on `8080`.

### Platform Notes

`start:prod` runs **Gunicorn on Linux** (`-c gunicorn.conf.py`, 3 preloaded
workers on `APP_HOST:APP_PORT`) and **a single uvicorn worker through
`run.py` on Windows**, because Gunicorn and its `fcntl` dependency are
Unix-only. Both read the same `backend/.env`, so `APP_HOST`, `APP_PORT`, and
`WORKERS` behave identically; on Windows the worker count is always one.

### Sensitive Stop Words Submodule

The `backend/data/` subrepos provide Chinese political, pornographic,
gun/explosive, advertising, URL, and general word lists loaded by the
top-priority `sensitive-stop-words` detector. The sources are
`sensitive-stop-words`, `sensitive`, `sensitive-lexicon`, and
`sensitive-word-data` (see [Credits](/guide/credits)). Fetch them after
cloning:

```bash
git submodule update --init
```

The lists are cached at startup and rebuilt on `/admin/reload`.

## Node.js Requirements

- Node.js 20.19+ is required (Vite 8 requires Node.js 20.19+)
- npm 10.0+ is required

## Model Requirements

- **Disk space**: at least 6 GB free for the Q4_K_M GGUF model (~5.78 GB)
  plus the tokenized context cache.
- **Network**: outbound HTTPS access to `huggingface.co` (or a mirror) for
  the first-run auto-download.
- **Memory**: with `MODEL_MLOCK=true` and Q8_0 KV cache, plan for roughly
  6-8 GB RSS per worker when the model is loaded.
- **llama-cpp-python 0.3.34**: required to parse the Qwen3.5 architecture.
  See [Configuration](/guide/configuration) for the `ai` extra and the
  Windows prebuilt-wheel install.

### China Mirror Configuration

The model downloader probes endpoints in order and uses the first reachable
one:

1. `https://huggingface.co`
2. `https://hf-mirror.com`
3. `https://www.modelscope.cn`

Override the defaults in `.env` with `HF_ENDPOINT`, `HF_MIRROR`, and
`MODELSCOPE_ENDPOINT`. If no endpoint is reachable, the service logs manual
download instructions and continues with Level 2 disabled.

### Manual Model Placement

To avoid the auto-download entirely:

1. Download the GGUF from
   <https://huggingface.co/bartowski/Qwen_Qwen3.5-9B-GGUF> (or the
   hf-mirror.com equivalent).
2. Place it at `backend/models/Qwen_Qwen3.5-9B-Q4_K_M.gguf`.
3. The service detects the file on startup and loads it directly.

## systemd

Install `deployment/systemd/moderation.service` as
`/etc/systemd/system/moderation.service`:

```bash
sudo cp deployment/systemd/moderation.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now moderation
```

The unit runs as the `moderation` user from `/opt/moderation-monorepo/backend`,
restarts on failure, and caps memory at 20 GiB with a 700% CPU quota.

## FRP Client

Configure `deployment/frp/frpc.ini` with your VPS address and token, then
start the FRP client on the private server. Port `APP_PORT` (`18427`) is
published as `9000` on the public VPS. Use mTLS between the FRP server and
client.

## Log Rotation

Install the logrotate rule:

```bash
sudo cp deployment/logrotate/moderation /etc/logrotate.d/moderation
```

Logs rotate daily, compress after a one-day delay, and retain 30 rotations.
The unit is reloaded after each rotation.

## Docker

```bash
cd deployment/docker
docker compose up -d --build
```

The compose file:

- Runs the backend with dropped capabilities, `no-new-privileges`, a 20 GiB
  memory cap, and 7 CPUs on port `18427`.
- Runs the frontend (built and served by nginx, proxying the API prefixes)
  on port `5173`.
- Mounts `backend/models`, `backend/logs`, and `backend/data` as volumes.

## Nginx (Frontend + API)

`deployment/nginx/nginx.conf` serves the built frontend and proxies `/api/`
to the backend. Point `YOUR_DOMAIN` at your VPS and terminate TLS with
Certbot or your certificate authority.

## Multi-Language Detection

The service runs **five active package detectors** on a standard PyPI install:

1. **badwords** – Rust, 26+ languages (`filter_text`)
2. **profanite** – Rust, anti-obfuscation (`contains_profanity`)
3. **glin-profanity** – C, 25+ languages, context-aware (`check_profanity`)
4. **gangajal** – WebAssembly, all languages (`validate`)
5. **PyProfane** – C, Soundex-based (`isProfane`)

These sit inside the `multi_language` detector (priority 6), which serializes
each native/WASM package behind a per-adapter lock. Before it, the dedicated
`SensitiveStopWordsDetector` (priority 0) runs the Chinese subrepo lists with a
native Rust/C Aho-Corasick engine, and the severity-aware `PhraseDetector`
(priority 7) runs the critical-phrase table.

Three more packages are guard-wired (`safetext`, `sensitive-word-filter-cn`,
`profanity-filter2`) but no reachable index provides an installable release.
They activate automatically if a working index provides them
(e.g. `cd backend && uv add safetext==0.3.3`).

`scheckbl` and `valx` are not wired (their documented APIs do not exist in
the installed versions). `datasketch` is a potential future semantic layer
but requires a pre-built toxic-signature database and is not enabled.

## Backups

| Component | Frequency | Retention |
| :--- | :--- | :--- |
| Custom word DB | Daily | 30 days |
| Logs | Daily | 90 days (compressed) |
| Configuration | On change | Indefinite (Git) |
| Model file | On update | Indefinite (encrypted storage) |

## Failover

Run a hot standby on a second private server with identical configuration.
Monitor `GET /admin/health` externally; on failure, start the FRP client on
the standby server so traffic flows to it.

## Multi-Worker Scaling

`start:prod` runs **3 preloaded Gunicorn workers** on Linux (override with
`WORKERS`). Each worker holds its own in-memory result cache, semantic
indexes, and LLM handle, so the model load is amortized once per worker.

### Worker count guidance

The dominant memory cost is the LLM: roughly 6-8 GB RSS per worker with
`MODEL_MLOCK=true` and a Q8_0 KV cache, plus the SentenceTransformer model
(~470 MB) and its Faiss indexes. A rule of thumb:

```
workers = floor((RAM_GB - 4) / 8)     # conservative, model per worker
```

For 64 GB RAM that is 7 workers; for 32 GB, 3. Each worker also spawns one
detector thread pool (`DETECTOR_THREAD_POOL_SIZE`, default 4) plus the
semantic preload thread.

### Cross-worker consistency (Redis)

Without Redis each worker's result cache is independent: an admin edit clears
the cache only in the worker that received the request, so the other workers
keep serving cached verdicts until their TTL expires (the config fingerprint
heals them on the next miss). To make invalidation immediate across all
workers, set `REDIS_URI`:

```
REDIS_URI=redis://localhost:6379/0
```

This does two things:

- **Rate limiting** — slowapi stores rate-limit counters in Redis, so the
  per-IP budget is enforced across workers instead of per process.
- **Cache invalidation** — every worker subscribes to a `moderation:cache`
  channel; when any worker clears its cache (settings, app-config, or phrase
  edits) it publishes a clear and every worker drops its cache at once.

The bus is fail-open: if the `redis` package is missing or the server is
unreachable the service starts normally with per-worker semantics.

### Graceful shutdown

Gunicorn is configured with `graceful_timeout = 30`, so `SIGTERM` lets the
in-flight requests drain before the worker exits. The FastAPI lifespan runs
`ENGINE.shutdown()`, which releases the model, closes the detectors, word
bank, profiler, settings, app-config, and feedback connections, and stops the
cache-invalidation listener. On Windows the single uvicorn worker handles the
same shutdown through the same lifespan.
