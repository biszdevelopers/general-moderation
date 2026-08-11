#!/usr/bin/env bash
# Deploy the monorepo to the private server and install the systemd unit.
# Usage: scripts/deploy.sh USER@SERVER
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${1:-}"

if [[ -z "${TARGET}" ]]; then
    echo "Usage: $0 USER@SERVER" >&2
    exit 1
fi

echo "==> Syncing repository to ${TARGET}"
rsync -az --delete \
    --exclude "backend/.venv" \
    --exclude "backend/data" \
    --exclude "backend/logs" \
    --exclude "backend/models" \
    --exclude "frontend/node_modules" \
    --exclude "frontend/dist" \
    --exclude "docs/.vitepress/cache" \
    "${ROOT_DIR}/" "${TARGET}:/opt/moderation-monorepo/"

echo "==> Installing systemd unit"
ssh "${TARGET}" 'sudo cp /opt/moderation-monorepo/deployment/systemd/moderation.service /etc/systemd/system/moderation.service && sudo systemctl daemon-reload && sudo systemctl enable --now moderation'

echo "==> Installing logrotate rule"
ssh "${TARGET}" 'sudo cp /opt/moderation-monorepo/deployment/logrotate/moderation /etc/logrotate.d/moderation'

echo "==> Deployment complete"
