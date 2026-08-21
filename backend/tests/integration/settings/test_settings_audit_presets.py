"""Settings audit trail, presets, encryption, and catalog metadata tests."""

from __future__ import annotations

from typing import Any

import pytest

from app.settings_service import SettingsService
from tests.base_test import BaseTest


@pytest.fixture()
def service(engine: Any) -> SettingsService:
    """The runtime settings service of a sandboxed engine."""
    return engine._settings_service


class TestAuditTrail(BaseTest):
    """Every update lands in config_audit."""

    def test_update_records_old_and_new(self, service: SettingsService) -> None:
        """A change records both values, actor, and source."""
        before: Any = service.get("AI_TARGET_PERCENTAGE")
        service.update({"AI_TARGET_PERCENTAGE": 42})
        rows: list[dict[str, Any]] = service.history(key="AI_TARGET_PERCENTAGE", limit=5)
        assert rows[0]["new_value"] == "42"
        assert rows[0]["old_value"] == str(before)
        assert rows[0]["actor"] == "admin"
        assert rows[0]["source"] == "admin_api"

    def test_history_newest_first_and_limit(self, service: SettingsService) -> None:
        """Rows come back newest first honoring the limit."""
        for value in ("10", "20", "30"):
            service.update({"CACHE_TTL_SECONDS": value})
        rows: list[dict[str, Any]] = service.history(limit=2)
        assert len(rows) == 2
        assert rows[0]["new_value"] == "30"

    def test_history_filters_by_key(self, service: SettingsService) -> None:
        """The key filter restricts returned rows."""
        service.update({"CACHE_TTL_SECONDS": 120})
        rows: list[dict[str, Any]] = service.history(key="CACHE_TTL_SECONDS")
        assert rows and all(row["key"] == "CACHE_TTL_SECONDS" for row in rows)

    def test_secret_values_redacted_in_history(self, service: SettingsService) -> None:
        """Secret keys never leak through the audit query."""
        service.update({"OPENAI_API_KEY": "sk-super-secret"})
        rows: list[dict[str, Any]] = service.history(key="OPENAI_API_KEY")
        assert rows[0]["new_value"] == "********"

    def test_custom_actor_and_source(self, service: SettingsService) -> None:
        """Actor and source flow into audit rows."""
        service.update({"CACHE_TTL_SECONDS": 90}, actor="tester", source="preset:x")
        row: dict[str, Any] = service.history(key="CACHE_TTL_SECONDS")[0]
        assert row["actor"] == "tester"
        assert row["source"] == "preset:x"


class TestEncryptedSecrets(BaseTest):
    """Editable provider credentials encrypt at rest."""

    def test_roundtrip_through_database(self, service: SettingsService) -> None:
        """The stored blob is encrypted; reads return plaintext."""
        service.update({"OPENAI_API_KEY": "sk-roundtrip"})
        raw = service._connection.execute(
            "SELECT value FROM settings WHERE key = 'OPENAI_API_KEY'"
        ).fetchone()[0]
        assert raw.startswith("enc:v1:")
        assert service.get("OPENAI_API_KEY") == "sk-roundtrip"

    def test_describe_redacts_secret(self, service: SettingsService) -> None:
        """Catalog entries mask secret values but flag editability."""
        service.update({"OPENAI_API_KEY": "sk-visible"})
        entry: dict[str, Any] = next(e for e in service.describe() if e["key"] == "OPENAI_API_KEY")
        assert entry["value"] == "********"
        assert entry["secret"] is True
        assert entry["editable"] is True

    def test_read_only_secrets_stay_rejected(self, service: SettingsService) -> None:
        """ADMIN_API_KEY remains non-editable."""
        with pytest.raises(ValueError, match="read-only"):
            service.update({"ADMIN_API_KEY": "nope"})

    def test_legacy_plaintext_passthrough(self, service: SettingsService) -> None:
        """Values stored before encryption still read back."""
        service._connection.execute(
            "UPDATE settings SET value = ? WHERE key = 'OPENAI_API_KEY'",
            ("sk-legacy",),
        )
        service._load()
        assert service.get("OPENAI_API_KEY") == "sk-legacy"


class TestCatalogMetadata(BaseTest):
    """describe() enrichment for the admin UI."""

    def test_provider_keys_carry_choices(self, service: SettingsService) -> None:
        """Choice keys expose their allowed values."""
        entry: dict[str, Any] = next(e for e in service.describe() if e["key"] == "LLM_PROVIDER")
        assert "local_llama_cpp" in entry["choices"]
        assert entry["category"] == "Models & Providers"

    def test_range_keys_carry_bounds(self, service: SettingsService) -> None:
        """Range keys expose min and max."""
        entry: dict[str, Any] = next(
            e for e in service.describe() if e["key"] == "MODEL_HEALTH_INTERVAL_SECONDS"
        )
        assert entry["min"] == 5
        assert entry["max"] == 600
        assert entry["type"] == "integer"

    def test_read_only_flag_matches_restart_requirement(self, service: SettingsService) -> None:
        """APP_PORT is locked and flagged as restart-required."""
        entry: dict[str, Any] = next(e for e in service.describe() if e["key"] == "APP_PORT")
        assert entry["editable"] is False
        assert entry["restart_required"] is True

    def test_choice_validation_enforced(self, service: SettingsService) -> None:
        """Invalid choice values are rejected."""
        with pytest.raises(ValueError, match="must be one of"):
            service.update({"LLM_PROVIDER": "not_a_provider"})
        with pytest.raises(ValueError, match="must be one of"):
            service.update({"LLM_FAILURE_POLICY": "explode"})


class TestPresets(BaseTest):
    """Preset CRUD and atomic application."""

    def test_defaults_seeded(self, service: SettingsService) -> None:
        """The three built-in presets exist."""
        names: list[str] = [p["name"] for p in service.presets()]
        assert {"High Accuracy", "Low Cost", "Strict"}.issubset(set(names))

    def test_apply_preset_changes_settings(self, service: SettingsService) -> None:
        """Applying Strict flips the failure policy and thresholds."""
        updated: dict[str, Any] = service.apply_preset("Strict")
        assert "LLM_FAILURE_POLICY" in updated
        assert service.get("LLM_FAILURE_POLICY") == "block"
        assert service.get("SEVERITY_HARD_BLOCK_THRESHOLD") == 3

    def test_apply_records_preset_source(self, service: SettingsService) -> None:
        """Preset application is audited with its source."""
        service.apply_preset("Low Cost")
        rows: list[dict[str, Any]] = service.history(key="AI_TARGET_PERCENTAGE")
        assert rows[0]["source"] == "preset:Low Cost"

    def test_create_and_delete_preset(self, service: SettingsService) -> None:
        """Custom presets persist and delete cleanly."""
        service.create_preset("Quiet", "minimal load", {"AI_TARGET_PERCENTAGE": 1})
        names: list[str] = [p["name"] for p in service.presets()]
        assert "Quiet" in names
        service.delete_preset("Quiet")
        assert "Quiet" not in [p["name"] for p in service.presets()]

    def test_create_duplicate_rejected(self, service: SettingsService) -> None:
        """Duplicate names raise ValueError."""
        with pytest.raises(ValueError, match="already exists"):
            service.create_preset("Strict", "dup", {})

    def test_create_with_unknown_key_rejected(self, service: SettingsService) -> None:
        """Payloads referencing unknown keys raise ValueError."""
        with pytest.raises(ValueError, match="Unknown setting"):
            service.create_preset("Bad", "", {"NOT_A_KEY": 1})

    def test_create_with_invalid_value_rejected(self, service: SettingsService) -> None:
        """Payloads failing validation raise ValueError."""
        with pytest.raises(ValueError):
            service.create_preset("Bad2", "", {"AI_TARGET_PERCENTAGE": 9999})

    def test_create_with_readonly_key_rejected(self, service: SettingsService) -> None:
        """Read-only keys cannot enter presets."""
        with pytest.raises(ValueError, match="read-only"):
            service.create_preset("Bad3", "", {"APP_PORT": 1234})

    def test_apply_unknown_preset_rejected(self, service: SettingsService) -> None:
        """Unknown preset names raise ValueError."""
        with pytest.raises(ValueError, match="Unknown preset"):
            service.apply_preset("Missing")

    def test_delete_unknown_preset_rejected(self, service: SettingsService) -> None:
        """Deleting a missing preset raises ValueError."""
        with pytest.raises(ValueError, match="Unknown preset"):
            service.delete_preset("Missing")


class TestNewSettingKeys(BaseTest):
    """Provider and calibration keys seed and validate correctly."""

    def test_provider_defaults_present(self, service: SettingsService) -> None:
        """Every new key seeds with its documented default."""
        assert service.get("LLM_PROVIDER") == "local_llama_cpp"
        assert service.get("BACKUP_LLM_PROVIDER") == ""
        assert service.get("LLM_FAILURE_POLICY") == "rule_based"
        assert service.get("OLLAMA_BASE_URL").startswith("http")
        assert service.get("ACTIVE_GGUF_PATH") == ""

    def test_calibration_range_validation(self, service: SettingsService) -> None:
        """Calibration bounds stay within 0..1."""
        with pytest.raises(ValueError):
            service.update({"CALIBRATION_BLOCK_CONFIDENCE": 1.5})
        service.update({"CALIBRATION_BLOCK_CONFIDENCE": 0.75})
        assert service.get("CALIBRATION_BLOCK_CONFIDENCE") == 0.75

    def test_health_ranges_validate(self, service: SettingsService) -> None:
        """Health probe settings respect their ranges."""
        with pytest.raises(ValueError):
            service.update({"MODEL_HEALTH_INTERVAL_SECONDS": 1})
        service.update({"MODEL_HEALTH_FAILURE_THRESHOLD": 5})
        assert service.get("MODEL_HEALTH_FAILURE_THRESHOLD") == 5
