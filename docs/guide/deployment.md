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
git submodule update --init          # fetch sensitive-stop-words word lists
npm run start:prod                   # build frontend, then gunicorn on APP_PORT
```

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

The `backend/data/sensitive-stop-words` submodule provides Chinese political,
pornographic, gun/explosive, advertising, and URL word lists loaded by the
`sensitive-stop-words` detector. Fetch it after cloning:

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
start the FRP client on the private server. Port `8080` is published as
`9000` on the public VPS. Use mTLS between the FRP server and client.

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
  memory cap, and 7 CPUs.
- Runs the frontend (built and served by nginx) on port `5173`.
- Mounts `backend/models`, `backend/logs`, and `backend/data` as volumes.

## Nginx (Frontend + API)

`deployment/nginx/nginx.conf` serves the built frontend and proxies `/api/`
to the backend. Point `YOUR_DOMAIN` at your VPS and terminate TLS with
Certbot or your certificate authority.

## Multi-Language Detection

The service runs **five active detectors** on a standard PyPI install:

1. **badwords** – Rust, 26+ languages (`filter_text`)
2. **profanite** – Rust, anti-obfuscation (`contains_profanity`)
3. **glin-profanity** – C, 25+ languages, context-aware (`is_profane`)
4. **gangajal** – WebAssembly, all languages (`validate`)
5. **PyProfane** – C, Soundex-based (`isProfane`)

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
