#!/usr/bin/env bash
# Format the backend with ruff and the frontend with oxfmt.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "==> Formatting backend with ruff"
cd "${ROOT_DIR}/backend"
python -m ruff format app run.py gunicorn.conf.py

echo "==> Formatting frontend with oxfmt"
cd "${ROOT_DIR}/frontend"
npm run format

echo "==> Formatting complete"
