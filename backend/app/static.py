"""Static asset and SPA fallback serving for the built frontend.

The built frontend is served by the FastAPI application on a single port. Real
files (``logo.svg``, ``favicon.svg``, any ``public/`` asset) are served
directly; client-side routes (``/dashboard``, ``/word-bank``, ...) fall back to
``index.html`` so the React router owns them; unknown API-prefixed paths return
404 so they never silently return the SPA shell.
"""

from __future__ import annotations

from pathlib import Path

from fastapi import HTTPException, status
from fastapi.responses import FileResponse, Response

_API_PREFIXES: tuple[str, ...] = ("admin", "test", "moderate", "health", "metrics")


def serve_frontend(dist_dir: Path, full_path: str) -> Response:
    """Return a real built asset, the SPA entry, or a 404.

    :param dist_dir: the built frontend directory
    :param full_path: the requested path without the leading slash
    :return: the matched file or the SPA ``index.html``
    :raises HTTPException: 404 for unknown API-prefixed paths or a missing build
    """
    if full_path.startswith(_API_PREFIXES):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if full_path:
        candidate: Path = dist_dir / full_path
        if candidate.is_file():
            return FileResponse(candidate)
    index_file: Path = dist_dir / "index.html"
    if index_file.is_file():
        return FileResponse(index_file)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
