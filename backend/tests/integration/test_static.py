"""Static asset and SPA fallback serving (Phase 1).

Covers the single-port frontend serving helper: real public assets are served
with their own content type, client-side routes fall back to ``index.html``,
and unknown API-prefixed paths return 404 instead of the SPA shell.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from fastapi import HTTPException

from app.static import serve_frontend
from tests.base_test import BaseTest


def _build_dist(root: Path) -> Path:
    """Create a minimal built frontend directory."""
    dist: Path = root / "dist"
    dist.mkdir()
    (dist / "index.html").write_text("<html>spa</html>", encoding="utf-8")
    (dist / "logo.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding="utf-8")
    (dist / "favicon.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"/>', encoding="utf-8")
    return dist


class TestServeFrontend(BaseTest):
    """The built frontend serving helper."""

    def test_serves_public_assets(self, tmp_path: Path) -> None:
        """Real files like the logo and favicon keep their content type."""
        dist: Path = _build_dist(tmp_path)
        response: Any = serve_frontend(dist, "logo.svg")
        assert Path(response.path) == dist / "logo.svg"
        assert response.headers["content-type"] == "image/svg+xml"

        favicon: Any = serve_frontend(dist, "favicon.svg")
        assert Path(favicon.path) == dist / "favicon.svg"
        assert favicon.headers["content-type"] == "image/svg+xml"

    def test_spa_fallback_for_client_routes(self, tmp_path: Path) -> None:
        """Client-side routes receive index.html."""
        dist: Path = _build_dist(tmp_path)
        response: Any = serve_frontend(dist, "dashboard")
        assert Path(response.path) == dist / "index.html"
        assert response.headers["content-type"].startswith("text/html")

    def test_missing_asset_falls_back_to_spa(self, tmp_path: Path) -> None:
        """An unknown non-API path still returns the SPA shell."""
        dist: Path = _build_dist(tmp_path)
        response: Any = serve_frontend(dist, "not-a-real-file")
        assert Path(response.path) == dist / "index.html"

    def test_api_prefixes_return_404(self, tmp_path: Path) -> None:
        """API paths never silently return the SPA shell."""
        dist: Path = _build_dist(tmp_path)
        for path in ("admin/health", "test/config", "moderate", "health", "metrics"):
            with pytest.raises(HTTPException) as excinfo:
                serve_frontend(dist, path)
            assert excinfo.value.status_code == 404

    def test_missing_build_returns_404(self, tmp_path: Path) -> None:
        """Without a build there is nothing to serve."""
        with pytest.raises(HTTPException) as excinfo:
            serve_frontend(tmp_path, "dashboard")
        assert excinfo.value.status_code == 404
