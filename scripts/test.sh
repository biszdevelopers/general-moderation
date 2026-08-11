#!/usr/bin/env bash
# Run linting and type checks for both codebases.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "==> Backend: ruff check"
cd "${ROOT_DIR}/backend"
python -m ruff check app run.py gunicorn.conf.py
python -m ruff format --check app run.py gunicorn.conf.py

echo "==> Frontend: oxlint and typecheck"
cd "${ROOT_DIR}/frontend"
npm run lint
npx tsc --noEmit

echo "==> All checks passed"
