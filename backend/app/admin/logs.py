"""Log management admin endpoints.

Filenames are validated against a strict C-regex pattern to prevent path
traversal; log content is serialized and returned as JSONL text.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException, status

_FILENAME_PATTERN = re.compile(r"^[A-Za-z0-9._-]+$")
_TAIL_LINES: int = 200


def create_logs_router(log_dir: str, auth_dependency: Any) -> APIRouter:
    """Build the log management router.

    :param log_dir: directory containing the log files
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    router: APIRouter = APIRouter(
        prefix="/admin/logs", tags=["logs"], dependencies=[auth_dependency]
    )

    @router.get("")
    def list_log_files() -> list[dict[str, Any]]:
        """List every log file in the logs directory.

        :return: file name and size in bytes for each log file
        """
        directory: Path = Path(log_dir)
        if not directory.exists():
            return []
        files: list[dict[str, Any]] = []
        for path in sorted(directory.glob("*.log")):
            if path.is_file():
                files.append({"name": path.name, "size": path.stat().st_size})
        return files

    @router.get("/{filename}")
    def download_log(filename: str) -> dict[str, Any]:
        """Return the tail of a log file.

        :param filename: the log file name
        :return: the log content and its metadata
        :raises HTTPException: 400 for invalid names, 404 for missing files
        """
        if not _FILENAME_PATTERN.match(filename):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid log file name",
            )
        path: Path = (Path(log_dir) / filename).resolve()
        if not path.is_file() or path.parent != Path(log_dir).resolve():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Log file not found"
            )
        lines: list[str] = path.read_text(encoding="utf-8").splitlines()
        return {
            "name": filename,
            "lines": len(lines),
            "tail": lines[-_TAIL_LINES:],
        }

    return router
