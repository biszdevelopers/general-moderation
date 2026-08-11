# Deployment

The service is designed to run on a **private server without a public IP**.
An FRP tunnel exposes it to a public VPS on port `9000`, where your
application calls the moderation API over `127.0.0.1`.

## Network Architecture

```
User → Next.js (VPS) → FRP Tunnel (mTLS) → Python FastAPI (Private Server)
```

## Node.js Requirements

- Node.js 20.19+ is required (Vite 8 requires Node.js 20.19+)
- npm 10.0+ is required

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
