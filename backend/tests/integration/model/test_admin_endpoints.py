"""Admin endpoint integration tests for models, prompts, and settings v2.

Exercises the new HTTP surface through the wired test app: model registry
CRUD and activation, prompt versioning, settings history, and presets.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from tests.base_test import BaseTest


@pytest.fixture()
def gguf(tmp_path: Path) -> Path:
    """A fake GGUF file on the server disk."""
    file_path: Path = tmp_path / "fake.gguf"
    file_path.write_bytes(b"fake-gguf")
    return file_path


class TestModelEndpoints(BaseTest):
    """/admin/models surface."""

    def test_list_models_empty(self, client: Any, admin_headers: dict[str, str]) -> None:
        """An empty registry lists nothing but reports provider status."""
        response = client.get("/admin/models", headers=admin_headers)
        assert response.status_code == 200
        body: dict[str, Any] = response.json()
        assert body["models"] == []
        assert "active" in body["providers"]

    def test_register_and_activate(
        self, client: Any, admin_headers: dict[str, str], gguf: Path
    ) -> None:
        """Registering then activating points ACTIVE_GGUF_PATH at the file."""
        created = client.post(
            "/admin/models/register",
            json={"name": "local-test", "path": str(gguf)},
            headers=admin_headers,
        )
        assert created.status_code == 201
        model_id: int = created.json()["model"]["id"]
        activated = client.post(f"/admin/models/{model_id}/activate", headers=admin_headers)
        assert activated.status_code == 200
        listed = client.get("/admin/models", headers=admin_headers).json()["models"]
        assert listed[0]["active"] is True

    def test_register_missing_file_rejected(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Registration of a non-existent path returns 400."""
        response = client.post(
            "/admin/models/register",
            json={"name": "ghost", "path": "/nowhere/x.gguf"},
            headers=admin_headers,
        )
        assert response.status_code == 400

    def test_duplicate_download_name_rejected(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """A duplicate name returns 400."""
        payload = {"name": "dup", "repo": "r", "filename": "x.gguf"}
        first = client.post("/admin/models/download", json=payload, headers=admin_headers)
        second = client.post("/admin/models/download", json=payload, headers=admin_headers)
        assert first.status_code == 202
        assert second.status_code == 400

    def test_upload_registers_model(
        self, client: Any, admin_headers: dict[str, str], tmp_path: Path
    ) -> None:
        """A multipart GGUF upload registers as a ready model."""
        response = client.post(
            "/admin/models/upload?name=uploaded",
            files={"file": ("model.gguf", b"gguf-data", "application/octet-stream")},
            headers=admin_headers,
        )
        assert response.status_code == 201
        assert response.json()["model"]["status"] == "ready"

    def test_upload_rejects_non_gguf(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Non-GGUF uploads return 400."""
        response = client.post(
            "/admin/models/upload?name=bad",
            files={"file": ("model.txt", b"text", "text/plain")},
            headers=admin_headers,
        )
        assert response.status_code == 400

    def test_delete_unknown_returns_400(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Deleting an unknown id returns 400."""
        response = client.delete("/admin/models/999999", headers=admin_headers)
        assert response.status_code == 400

    def test_health_endpoint(self, client: Any, admin_headers: dict[str, str]) -> None:
        """/admin/models/health reports active and backup entries."""
        body: dict[str, Any] = client.get("/admin/models/health", headers=admin_headers).json()
        assert set(body) >= {"active", "backup", "consecutive_failures"}


class TestPromptEndpoints(BaseTest):
    """/admin/prompt surface."""

    def test_default_prompt_roundtrip(self, client: Any, admin_headers: dict[str, str]) -> None:
        """PUT creates an active version; GET returns it."""
        saved = client.put(
            "/admin/prompt", json={"template": "Be extremely strict."}, headers=admin_headers
        )
        assert saved.status_code == 200
        fetched = client.get("/admin/prompt", headers=admin_headers).json()
        assert fetched["template"] == "Be extremely strict."

    def test_empty_template_rejected(self, client: Any, admin_headers: dict[str, str]) -> None:
        """An empty template returns 400."""
        response = client.put("/admin/prompt", json={"template": "   "}, headers=admin_headers)
        assert response.status_code == 400

    def test_versions_and_activation(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Version history lists saves; reactivation rolls back."""
        client.put("/admin/prompt", json={"template": "v1"}, headers=admin_headers)
        client.put("/admin/prompt", json={"template": "v2"}, headers=admin_headers)
        versions: list[dict[str, Any]] = client.get(
            "/admin/prompt/versions", headers=admin_headers
        ).json()["versions"]
        assert len(versions) >= 2
        oldest: int = versions[-1]["id"]
        activated = client.post(f"/admin/prompt/versions/{oldest}/activate", headers=admin_headers)
        assert activated.status_code == 200
        current = client.get("/admin/prompt", headers=admin_headers).json()["template"]
        assert current == "v1"

    def test_activate_unknown_version_400(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Unknown version ids return 400."""
        response = client.post("/admin/prompt/versions/424242/activate", headers=admin_headers)
        assert response.status_code == 400


class TestSettingsHistoryAndPresetEndpoints(BaseTest):
    """Settings history and preset endpoints."""

    def test_history_endpoint_redacts_secrets(
        self, engine: Any, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """The API never exposes secret values from history."""
        engine._settings_service.update({"OPENAI_API_KEY": "sk-http-secret"})
        rows: list[dict[str, Any]] = client.get(
            "/admin/settings/history?key=OPENAI_API_KEY", headers=admin_headers
        ).json()["history"]
        assert rows[0]["new_value"] == "********"

    def test_presets_flow(self, client: Any, admin_headers: dict[str, str]) -> None:
        """List, apply, create, and delete presets over HTTP."""
        names: list[str] = [
            p["name"] for p in client.get("/admin/presets", headers=admin_headers).json()["presets"]
        ]
        assert "Strict" in names
        applied = client.post("/admin/presets/Strict/apply", headers=admin_headers)
        assert applied.status_code == 200
        assert "LLM_FAILURE_POLICY" in applied.json()["updated"]
        created = client.post(
            "/admin/presets",
            json={"name": "HTTP", "description": "d", "payload": {"AI_TARGET_PERCENTAGE": 2}},
            headers=admin_headers,
        )
        assert created.status_code == 201
        deleted = client.delete("/admin/presets/HTTP", headers=admin_headers)
        assert deleted.status_code == 200

    def test_apply_unknown_preset_400(self, client: Any, admin_headers: dict[str, str]) -> None:
        """Unknown preset application returns 400."""
        response = client.post("/admin/presets/Missing/apply", headers=admin_headers)
        assert response.status_code == 400

    def test_update_settings_audited(self, client: Any, admin_headers: dict[str, str]) -> None:
        """POST /admin/settings writes auditable history."""
        updated = client.post(
            "/admin/settings",
            json={"settings": {"AI_TARGET_PERCENTAGE": 33}},
            headers=admin_headers,
        )
        assert updated.status_code == 200
        rows: list[dict[str, Any]] = client.get(
            "/admin/settings/history?key=AI_TARGET_PERCENTAGE", headers=admin_headers
        ).json()["history"]
        assert rows[0]["new_value"] == "33"

    def test_read_only_setting_rejected_over_http(
        self, client: Any, admin_headers: dict[str, str]
    ) -> None:
        """Restart-required fields return 400 with a read-only detail."""
        response = client.post(
            "/admin/settings",
            json={"settings": {"APP_HOST": "10.0.0.1"}},
            headers=admin_headers,
        )
        assert response.status_code == 400
        assert "read-only" in response.json()["detail"]

    def test_endpoints_require_auth(self, client: Any) -> None:
        """Every new route rejects missing credentials."""
        for method, path in (
            ("get", "/admin/models"),
            ("post", "/admin/models/register"),
            ("put", "/admin/prompt"),
            ("get", "/admin/settings/history"),
            ("get", "/admin/presets"),
        ):
            call = getattr(client, method)
            assert call(path).status_code == 401
