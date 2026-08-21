# Security & Supply-Chain Audit — Roadmap Item C

Date: 2026-08-15
Scope: `backend/` dependency scan, OWASP pass on the admin surface, secret
handling review, submodule pinning check, SBOM tooling.

---

## 1. Dependency vulnerability scan

| Check | Result |
|-------|--------|
| `uv lock --check` | PASS — lockfile in sync, 127 packages resolved |
| `uvx pip-audit --local` (against live `.venv`) | **0 known vulnerabilities** |
| `pip list --outdated` | Only newer-available versions, no CVE-driven bumps |

Notes:

- `uv run pip-audit` is not installed in the venv; `uvx pip-audit` was used
  instead (downloads its own tool env). Auditing a requirements freeze with
  `pip-audit -r` fails on Windows because pip tries to *build*
  `llama-cpp-python` (vendored llama.cpp contains a source path exceeding the
  MAX_PATH limit); `--local` against the installed venv avoids resolution and
  is the supported path.
- Outdated-but-clean: `aiohttp 3.12.0` (latest 3.14.3), `requests 2.32.3`
  (2.34.2), `orjson 3.11.9` (3.12.0), `uvicorn 0.52.1` (0.52.3),
  `pytest 8.4.1` (9.1.1). pip-audit reports none of these pinned versions as
  vulnerable, so **no dependency bumps were made**; the app-critical pins
  (`fastapi==0.141.1`, `orjson==3.11.9`, `mmh3==5.2.1`,
  `ahocorasick-rs==1.0.3`, `llama-cpp-python==0.3.34`, ...) are untouched.
- Recommended: run `uvx pip-audit --local` in CI on every lockfile change;
  review `aiohttp` upgrades next time the lockfile moves (it is the highest
  churn dependency with a historically large advisory surface).

## 2. OWASP pass — admin surface

### Fixed (concrete, low-risk)

1. **Path traversal in static asset serving (A01)** — `backend/app/static.py`:
   `serve_frontend` joined `dist_dir / full_path` and served any existing
   file, so `..` segments could read files outside the frontend build.
   Now resolved and verified with `candidate.is_relative_to(dist_dir)`.
2. **Secret exposure in export archives (A02/A07)** —
   `backend/app/settings_service.py::to_json()` serialized *every* setting,
   including `ADMIN_API_KEY`, `WEBUI_API_KEY`, `SECRET_KEY`,
   `ENCRYPTION_KEY` in plaintext into `config/settings_snapshot.json` inside
   the admin export ZIP (the `.env` copy was already redacted). Values with
   `_KEY`/`_SECRET` suffixes are now masked, matching the `describe()` API
   behavior. Verified golden-master export tests only assert `.env`
   redaction and custom-snapshot passthrough — no expectations broken.
3. **Missing security header (A05 hardening)** — added
   `Cross-Origin-Opener-Policy: same-origin` to the header middleware;
   previously only COEP-style framing protection existed.
4. **Unbounded query parameter (A01/A04)** — `GET /admin/spot-check?count=`
   accepted any integer; now capped `ge=1, le=1000`.
5. **Unbounded app name (A04)** — `AppConfigRequest.app_name` had only
   `min_length=1`; now capped at 128 chars.
6. **`.gitignore` gaps** — added `exports/`, `semantic/`, and SQLite WAL/SHM
   (`*.db-wal`, `*.db-shm`) to `backend/.gitignore` (WAL files carry the same
   sensitive rows as the main DB).

### Assessed — no change needed

- **Auth (A07)**: `hmac.compare_digest` constant-time comparison used for
  both admin and web-UI keys; missing header fails closed with 401. Good.
- **CORS (A02)**: allowlist from env, `allow_credentials=False`, explicit
  method/header lists. Good.
- **Injection (A05)**: all SQLite access is parameterized; the export CSV
  dumper interpolates table names only from `sqlite_master` (not user input).
  Pydantic v2 (Rust) validates every JSON input; bulk word import capped at
  1000 items. No raw SQL or shell/deserialization sinks found.
- **Path traversal in logs/export (A01)**: `logs.py` enforces a strict
  filename regex *and* a resolved-path containment check. Good.
- **Mass assignment (A01)**: `POST /admin/settings` and `/test/config`
  validate against a known-key catalog with a read-only set that includes
  the API keys/encryption key; unknown or read-only keys are rejected.
  `UpdateWordRequest`/`UpdatePhraseRequest` use `exclude_none=True` and only
  pass known fields. Good.
- **Logging (A09)**: moderation records log a SHA-256 hash + 50-char preview
  of text, never the raw body, keys, or headers. Good.
- **Rate limiting (A07)**: public `/moderate` routes are slowapi-limited;
  admin routes are intentionally exempt (documented) — mitigated by the
  constant-time API key and the dedicated export limiter.

### Recommended-only (not fixed)

- `GET /metrics` (root) is public and unauthenticated; counters are low
  sensitivity, but consider moving behind the admin key or a proxy.
- Export rate limiter stores one entry per client IP forever (unbounded
  dict, admin-only surface).
- `X-XSS-Protection: 1; mode=block` is deprecated by modern browsers
  (harmless, kept for legacy).
- `Permissions-Policy` header not set (informational).
- Free-form `language`/`category` on word/phrase add — no enum validation
  (admin-only; the UI constrains choices already).

## 3. Secret handling review

- **No real secrets are committed.** `git ls-files` shows only
  `.env.example` files (root, `backend/`, `frontend/`); no `.env`, `*.db`,
  `exports/`, or `logs/` are tracked. All matches for key material are the
  `CHANGE_ME_*` placeholders in `.env.example` and the documented defaults
  in `app/config.py`.
- `app/config.py::ensure_secrets` replaces empty/`CHANGE_ME*` values with
  `secrets.token_urlsafe(32)` / `secrets.token_hex(32)` and persists them to
  a local (untracked) `.env` via `atomicwrites`. `app/secret_gen.py` exposes
  the same path for `npm run generate:secrets`. Correct usage of the stdlib
  CSPRNG.
- `backend/.gitignore` now covers `.env`, DBs (+ WAL/SHM), `exports/`,
  `semantic/`, and `logs/`. The root `.gitignore` already covered the same
  paths.
- Logging never writes API keys; the export `.env` copy and settings
  snapshot are redacted.

## 4. Submodule pinning

`.gitmodules` declares 4 subrepos (all in `backend/data/`):
`sensitive-stop-words`, `sensitive`, `sensitive-lexicon`,
`sensitive-word-data`.

- Pinning is by commit SHA in the superproject's gitlink (the `.gitmodules`
  file stores only URL+path, which is standard); `git submodule status`
  confirms every submodule is initialized and checked out at a pinned
  commit:
  - `sensitive` → `42d1c505be7b2d2a3f7fe106e3b02499975b2f24`
  - `sensitive-lexicon` → `5a8da94c61c160e203a6b2fcfafbea642404d50c`
  - `sensitive-stop-words` → `a7d06bb1c321e669943b6841570d9da6dad8ce2b`
  - `sensitive-word-data` → `fe6fc2921836217b8c90619db81b24af8b22d80f`
- **Recommendation**: these are word-list data repos; treat them as
  supply-chain inputs — review diffs on upgrade, and consider
  `git config submodule.recurse true` so updates are deliberate. No action
  required today (SHAs are pinned).

## 5. SBOM usage

- New `backend/tools/sbom.py` — runs `pip list --format=json` in the active
  venv, attaches best-effort licenses via
  `importlib.metadata.metadata(pkg, 'License')` (with classifier fallback),
  writes a compact JSON SBOM to `backend/exports/sbom.json`.
- Root `package.json` gains `"sbom": "cd backend && uv run python tools/sbom.py"`.
- Example run: **106 packages** exported with licenses (e.g.
  `ahocorasick_rs 1.0.3 → Apache 2.0`, `aiohttp 3.12.0 → Apache-2.0`).
- Usage: `npm run sbom` before a release, or in CI, to capture the exact
  dependency graph; pair with the pip-audit scan for vulnerability posture.

## Files changed

- `backend/app/static.py` — path-traversal containment
- `backend/app/settings_service.py` — redact secrets in `to_json()`
- `backend/app/security/headers.py` — added COOP header
- `backend/app/admin/stats_router.py` — cap `spot-check` count
- `backend/app/admin/appconfig_router.py` — cap `app_name`
- `backend/.gitignore` — add `exports/`, `semantic/`, `*.db-wal`, `*.db-shm`
- `backend/tools/sbom.py` — new SBOM exporter
- `package.json` — `sbom` npm script
- `backend/security_report.md` — this report

## Verification performed

- `uv lock --check` — pass
- `uv run python -c "import fastapi, orjson"` — resolves
- `uv run ruff check` on all changed files — pass
- `uv run python tools/sbom.py` — writes 106-package SBOM
- Golden-master test expectations untouched (no test files modified, no
  goldens regenerated).
