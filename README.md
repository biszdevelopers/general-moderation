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

- 8-layer detection pipeline, every layer backed by C/C++/Rust/WASM.
- 11 multi-language pip packages covering 26+ languages.
- Zero local word-bank text files; base dictionaries come from pip packages.
- Custom words stored in SQLite (C implementation).
- All security-critical operations delegated to compiled libraries
  (OpenSSL, libsodium, Rust regex, Redis hiredis).
- Java-flavored Python: ABCs, frozen dataclasses, private fields, full typing.
- TypeScript/React admin UI with strict UI/logic separation.

## Quick Start

```bash
cd backend
python -m venv .venv
pip install -r requirements.txt
cp .env.example .env
python run.py
```

See `docs/` for the full guide, API reference, and deployment instructions.

## License

[MIT](LICENSE)
