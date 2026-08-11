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

## License

[MIT](LICENSE)
