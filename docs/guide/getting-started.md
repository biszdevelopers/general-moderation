# Getting Started

## Prerequisites

- Python 3.11 or newer
- Node.js 20.19+ (Vite 8 requirement) and npm 10+
- [uv](https://astral.sh/uv/) (the Python package manager used by the backend)
- A Linux server or Docker for production deployments

## Repository Layout

```
moderation-monorepo/
├── backend/       # Python FastAPI service (thin wrapper)
├── frontend/      # React + TypeScript + Ant Design admin UI
├── docs/          # This documentation
├── deployment/    # systemd, FRP, logrotate, Docker, nginx
└── scripts/       # Build, test, deploy, format scripts
```

## Backend Setup

Dependencies are managed with `uv`; `uv sync` creates the virtual environment
and installs every locked dependency.

```bash
cd backend
uv sync
cp .env.example .env
```

Security secrets are auto-generated on first startup and written to the
gitignored `.env`; regenerate them at any time with
`npm run generate:secrets` from the repository root.

### Development Server

```bash
uv run python run.py
```

The service now listens on `http://127.0.0.1:8080`. Try the health endpoint:

```bash
curl http://127.0.0.1:8080/admin/health \
    -H "X-API-Key: your-admin-key"
```

### Production Server

```bash
gunicorn -c gunicorn.conf.py app.main:app
```

See [Deployment](/guide/deployment) for systemd, FRP, and Docker recipes.

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The admin UI runs on `http://127.0.0.1:5173` and proxies `/admin` requests to
the backend. Open the **Settings** page, enter your admin API key, and start
managing the word bank.

## First Moderation

```bash
curl -X POST http://127.0.0.1:8080/moderate \
    -H "Content-Type: application/json" \
    -d '{"id":"1","user_id":"u1","text":"hello world"}'
```

Response:

```json
{
    "id": "1",
    "verdict": "PASS",
    "level_used": 1,
    "reasons": [],
    "matched_words": [],
    "matched_language": null,
    "confidence_score": null,
    "latency_ms": 0.31,
    "detector_chain": ["bloom_filter", "rolling_hash", "aho_corasick"]
}
```

## Next Steps

- [Configuration](/guide/configuration) — every environment variable
- [Word Banks](/guide/wordbanks) — managing custom words
- [Security](/guide/security) — how C/C++ libraries protect the service
- [API Reference](/api/index) — full endpoint documentation
