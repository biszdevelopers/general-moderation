"""Unit tests for the confidence calibrator, prompt store, and registry."""

from __future__ import annotations

from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import pytest

from app.ai.calibration import ConfidenceCalibrator
from app.ai.model_registry import ModelRegistryService
from app.ai.prompt import SYSTEM_PROMPT
from app.ai.prompt_store import PromptStore
from app.ai.providers.interface import ProviderResult


class _StubSettings:
    """Canned settings values."""

    def __init__(self, values: dict[str, Any] | None = None) -> None:
        self.values: dict[str, Any] = values or {}

    def get(self, key: str, default: Any = None) -> Any:
        """Return the stored value or the default."""
        return self.values.get(key, default)

    def update(self, values: dict[str, Any], **kwargs: Any) -> dict[str, Any]:
        """Record updates like the real service."""
        self.values.update(values)
        return values


class TestConfidenceCalibrator:
    """Calibration math and toggle behavior."""

    def test_block_confidence_rises_with_suspicion(self) -> None:
        """A BLOCK verdict lands between base and 1.0 as suspicion grows."""
        calibrator = ConfidenceCalibrator(_StubSettings())
        low: float = calibrator.calibrate(ProviderResult(True, 0.9, "", 1.0), 0.0)
        high: float = calibrator.calibrate(ProviderResult(True, 0.9, "", 1.0), 100.0)
        assert low == pytest.approx(0.9)
        assert high == pytest.approx(0.95)
        assert low < high < 1.0

    def test_allow_confidence_falls_with_suspicion(self) -> None:
        """An ALLOW verdict loses confidence as suspicion grows."""
        calibrator = ConfidenceCalibrator(_StubSettings())
        low: float = calibrator.calibrate(ProviderResult(False, 0.5, "", 1.0), 0.0)
        high: float = calibrator.calibrate(ProviderResult(False, 0.5, "", 1.0), 100.0)
        assert low == pytest.approx(0.35)
        assert low > high > 0.0

    def test_disabled_passthrough_clamps(self) -> None:
        """Disabled calibration returns the raw value clamped to 0-1."""
        calibrator = ConfidenceCalibrator(_StubSettings({"CALIBRATION_ENABLED": False}))
        result = calibrator.calibrate(ProviderResult(False, 7.5, "", 1.0), 50.0)
        assert result == 1.0

    def test_configurable_bounds(self) -> None:
        """Block/allow bounds come from settings."""
        calibrator = ConfidenceCalibrator(
            _StubSettings(
                {"CALIBRATION_BLOCK_CONFIDENCE": 0.8, "CALIBRATION_ALLOW_CONFIDENCE": 0.2}
            )
        )
        blocked: float = calibrator.calibrate(ProviderResult(True, 1.0, "", 1.0), 0.0)
        allowed: float = calibrator.calibrate(ProviderResult(False, 1.0, "", 1.0), 0.0)
        assert blocked == pytest.approx(0.8)
        assert allowed == pytest.approx(0.2)


class TestPromptStore:
    """Versioned prompt storage."""

    def test_default_prompt_when_empty(self, tmp_path: Path) -> None:
        """An empty store returns the built-in system prompt."""
        store = PromptStore(str(tmp_path / "prompts.db"))
        assert store.get_active() == SYSTEM_PROMPT
        assert store.list_versions() == []
        store.close()

    def test_save_creates_active_version(self, tmp_path: Path) -> None:
        """Saving creates one active version retrievable verbatim."""
        store = PromptStore(str(tmp_path / "prompts.db"))
        version_id: int = store.save("custom rules v1")
        assert version_id >= 1
        assert store.get_active() == "custom rules v1"
        assert store.list_versions()[0]["active"] is True
        store.close()

    def test_save_new_version_deactivates_previous(self, tmp_path: Path) -> None:
        """Only the newest save stays active."""
        store = PromptStore(str(tmp_path / "prompts.db"))
        first: int = store.save("v1")
        store.save("v2")
        versions: list[dict[str, Any]] = store.list_versions()
        assert len(versions) == 2
        assert store.get_active() == "v2"
        flags: dict[int, bool] = {int(v["id"]): bool(v["active"]) for v in versions}
        assert flags[first] is False
        store.close()

    def test_activate_rollback(self, tmp_path: Path) -> None:
        """Reactivating an old version rolls the active template back."""
        store = PromptStore(str(tmp_path / "prompts.db"))
        first: int = store.save("v1")
        second: int = store.save("v2")
        store.activate(first)
        assert store.get_active() == "v1"
        assert store.get_version(second) == "v2"
        store.close()

    def test_empty_template_rejected(self, tmp_path: Path) -> None:
        """Blank templates raise ValueError."""
        store = PromptStore(str(tmp_path / "prompts.db"))
        with pytest.raises(ValueError):
            store.save("   ")
        store.close()

    def test_unknown_activation_rejected(self, tmp_path: Path) -> None:
        """Activating a missing version raises ValueError."""
        store = PromptStore(str(tmp_path / "prompts.db"))
        with pytest.raises(ValueError):
            store.activate(999)
        store.close()

    def test_get_version_missing_returns_none(self, tmp_path: Path) -> None:
        """Unknown ids return None."""
        store = PromptStore(str(tmp_path / "prompts.db"))
        assert store.get_version(42) is None
        store.close()


class TestModelRegistry:
    """GGUF registry lifecycle."""

    @pytest.fixture()
    def registry(self, tmp_path: Path) -> ModelRegistryService:
        """Registry wired to sandboxed paths."""
        settings = MagicMock()
        settings.model_dir = str(tmp_path / "models")
        settings.model_registry_db_path = str(tmp_path / "models.db")
        settings.hf_endpoint = "http://127.0.0.1:1"
        settings.hf_mirror = "http://127.0.0.1:2"
        runtime = _StubSettings()
        return ModelRegistryService(settings, runtime)

    def test_register_and_list(self, registry: ModelRegistryService, tmp_path: Path) -> None:
        """A registered file appears with ready status and size."""
        gguf: Path = tmp_path / "models" / "a.gguf"
        gguf.parent.mkdir(parents=True, exist_ok=True)
        gguf.write_bytes(b"gguf-bytes")
        model_id: int = registry.register_path("a", str(gguf))
        models: list[dict[str, Any]] = registry.list_models()
        assert models[0]["id"] == model_id
        assert models[0]["status"] == "ready"
        assert models[0]["size_bytes"] == 10
        assert models[0]["exists"] is True
        assert registry.get_model(model_id)["name"] == "a"

    def test_register_rejects_missing_file(self, registry: ModelRegistryService) -> None:
        """Non-existent paths raise ValueError."""
        with pytest.raises(ValueError):
            registry.register_path("ghost", "/nowhere/a.gguf")

    def test_register_rejects_non_gguf(
        self, registry: ModelRegistryService, tmp_path: Path
    ) -> None:
        """Only .gguf files are accepted."""
        other: Path = tmp_path / "x.bin"
        other.write_bytes(b"x")
        with pytest.raises(ValueError):
            registry.register_path("bin", str(other))

    def test_duplicate_name_rejected(self, registry: ModelRegistryService, tmp_path: Path) -> None:
        """The same name cannot register twice."""
        gguf: Path = tmp_path / "a.gguf"
        gguf.write_bytes(b"x")
        registry.register_path("dup", str(gguf))
        with pytest.raises(ValueError):
            registry.register_path("dup", str(gguf))

    def test_activate_updates_runtime_setting(
        self, registry: ModelRegistryService, tmp_path: Path
    ) -> None:
        """Activation writes ACTIVE_GGUF_PATH through the runtime service."""
        gguf: Path = tmp_path / "a.gguf"
        gguf.write_bytes(b"x")
        model_id: int = registry.register_path("act", str(gguf))
        runtime: _StubSettings = registry._settings_service
        activated: dict[str, Any] = registry.activate(model_id)
        assert activated["name"] == "act"
        assert runtime.values["ACTIVE_GGUF_PATH"] == str(gguf)
        assert registry.list_models()[0]["active"] is True

    def test_activate_missing_file_rejected(
        self, registry: ModelRegistryService, tmp_path: Path
    ) -> None:
        """Activation refuses rows whose file disappeared."""
        gguf: Path = tmp_path / "gone.gguf"
        gguf.write_bytes(b"x")
        model_id: int = registry.register_path("gone", str(gguf))
        gguf.unlink()
        with pytest.raises(ValueError):
            registry.activate(model_id)

    def test_delete_clears_active_pointer(
        self, registry: ModelRegistryService, tmp_path: Path
    ) -> None:
        """Deleting the active model clears ACTIVE_GGUF_PATH."""
        gguf: Path = tmp_path / "del.gguf"
        gguf.write_bytes(b"x")
        model_id: int = registry.register_path("del", str(gguf))
        registry.activate(model_id)
        runtime: _StubSettings = registry._settings_service
        registry.delete(model_id)
        assert runtime.values["ACTIVE_GGUF_PATH"] == ""
        assert registry.list_models() == []

    def test_delete_unknown_rejected(self, registry: ModelRegistryService) -> None:
        """Deleting an unknown id raises ValueError."""
        with pytest.raises(ValueError):
            registry.delete(12345)

    def test_probe_url_failure_is_false(self) -> None:
        """Unreachable URLs report False."""
        assert ModelRegistryService.probe_url("http://127.0.0.1:1", timeout=0.5) is False
