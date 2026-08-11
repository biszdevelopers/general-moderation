#!/usr/bin/env bash
# Build the backend and frontend for deployment.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "==> Building frontend"
cd "${ROOT_DIR}/frontend"
npm run build

echo "==> Verifying backend imports"
cd "${ROOT_DIR}/backend"
"${ROOT_DIR}/backend/.venv/bin/python" -c "import app.main; print('backend import OK')" \
    || python -c "import app.main; print('backend import OK')"

echo "==> Build complete"
