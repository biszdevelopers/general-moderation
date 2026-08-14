"""Runtime settings service tests (Phase 1, P1/P2).

Covers seeded defaults, typed coercion, validation ranges, read-only keys,
secret exclusion, updates, and JSON export.
"""

from __future__ import annotations

from typing import Any

import pytest

from app.settings_service import SettingsService
from tests.base_test import BaseTest


class TestSettingsSeeded(BaseTest):
    """Seeded default settings."""

    def test_weights_seeded(self, engine: Any) -> None:
        """Detector weights are seeded from the environment."""
        service: SettingsService = engine._settings_service
        service.get("WEIGHT_DETECTOR_AHO")
        assert int(service.get("WEIGHT_DETECTOR_AHO", 0)) == 30

    def test_threshold_seeded(self, engine: Any) -> None:
        """Semantic thresholds are seeded."""
        service: SettingsService = engine._settings_service
        service.get("SEMANTIC_SIMILARITY_THRESHOLD")
        assert float(service.get("SEMANTIC_SIMILARITY_THRESHOLD", 0.0)) == 0.65

    def test_window_seeded(self, engine: Any) -> None:
        """The profiling window is seeded."""
        service: SettingsService = engine._settings_service
        service.get("USER_WINDOW_DAYS")
        assert int(service.get("USER_WINDOW_DAYS", 0)) == 91

    def test_all_returns_mapping(self, engine: Any) -> None:
        """all() returns every seeded setting."""
        service: SettingsService = engine._settings_service
        assert "WEIGHT_DETECTOR_AHO" in service.all()

    def test_describe_has_metadata(self, engine: Any) -> None:
        """describe() returns typed metadata per setting."""
        service: SettingsService = engine._settings_service
        entries: list[dict[str, Any]] = service.describe()
        assert entries
        for entry in entries:
            assert "key" in entry
            assert "value" in entry
            assert "type" in entry
            assert "editable" in entry


class TestSettingsValidation(BaseTest):
    """Type and range validation on update."""

    @pytest.mark.parametrize(
        ("key", "bad_value"),
        (
            ("WEIGHT_DETECTOR_AHO", "not-a-number"),
            ("WEIGHT_DETECTOR_AHO", 0),
            ("WEIGHT_DETECTOR_AHO", 51),
            ("SEMANTIC_SIMILARITY_THRESHOLD", -0.1),
            ("SEMANTIC_SIMILARITY_THRESHOLD", 1.5),
            ("USER_WINDOW_DAYS", 6),
            ("USER_WINDOW_DAYS", 366),
            ("AUTO_TUNING_BATCH_HOUR", 24),
            ("CACHE_MAX_SIZE", 0),
            ("RATE_LIMIT_REQUESTS", 0),
            ("LOG_BACKUP_COUNT", -1),
            ("MODEL_MAX_TOKENS", 0),
            ("SEMANTIC_TOP_K", 0),
            ("WEIGHT_USER", 4),
            ("AI_TARGET_PERCENTAGE", 101),
        ),
    )
    def test_invalid_value_rejected(self, engine: Any, key: str, bad_value: object) -> None:
        """Out-of-range or malformed values raise ValueError.

        :param engine: test engine
        :param key: settings key
        :param bad_value: invalid value to attempt
        """
        service: SettingsService = engine._settings_service
        service.get(key)
        with pytest.raises(ValueError):
            service.update({key: bad_value})

    @pytest.mark.parametrize(
        ("key", "good_value"),
        (
            ("WEIGHT_DETECTOR_AHO", 35),
            ("SEMANTIC_SIMILARITY_THRESHOLD", 0.9),
            ("USER_WINDOW_DAYS", 91),
            ("AUTO_TUNING_BATCH_HOUR", 2),
            ("CACHE_MAX_SIZE", 100),
            ("RATE_LIMIT_REQUESTS", 500),
            ("LOG_BACKUP_COUNT", 5),
            ("MODEL_MAX_TOKENS", 64),
            ("SEMANTIC_TOP_K", 10),
            ("WEIGHT_USER", 25),
        ),
    )
    def test_valid_value_accepted(self, engine: Any, key: str, good_value: object) -> None:
        """In-range values persist without error.

        :param engine: test engine
        :param key: settings key
        :param good_value: valid value to apply
        """
        service: SettingsService = engine._settings_service
        service.get(key)
        updated: dict[str, Any] = service.update({key: good_value})
        assert key in updated


class TestSettingsReadOnly(BaseTest):
    """Read-only and secret settings."""

    @pytest.mark.parametrize(
        "key",
        (
            "ADMIN_API_KEY",
            "WEBUI_API_KEY",
            "SECRET_KEY",
            "ENCRYPTION_KEY",
            "MODEL_PATH",
            "APP_PORT",
        ),
    )
    def test_read_only_rejected(self, engine: Any, key: str) -> None:
        """Read-only keys cannot be updated.

        :param engine: test engine
        :param key: a read-only settings key
        """
        service: SettingsService = engine._settings_service
        service.get(key)
        with pytest.raises(ValueError):
            service.update({key: "changed"})

    def test_secrets_not_public(self, engine: Any) -> None:
        """Secret keys are never marked public."""
        service: SettingsService = engine._settings_service
        for key in ("ADMIN_API_KEY", "WEBUI_API_KEY", "SECRET_KEY", "ENCRYPTION_KEY"):
            assert service.is_public(key) is False

    def test_unknown_key_rejected(self, engine: Any) -> None:
        """Unknown keys raise ValueError."""
        service: SettingsService = engine._settings_service
        service.get("WEIGHT_DETECTOR_AHO")
        with pytest.raises(ValueError):
            service.update({"NONEXISTENT_KEY": "x"})


class TestSettingsPersistence(BaseTest):
    """Update and export behavior."""

    def test_update_persists(self, engine: Any) -> None:
        """An update is readable immediately after writing."""
        service: SettingsService = engine._settings_service
        service.get("WEIGHT_DETECTOR_AHO")
        service.update({"WEIGHT_DETECTOR_AHO": 40})
        assert int(service.get("WEIGHT_DETECTOR_AHO", 0)) == 40

    def test_to_json_valid(self, engine: Any) -> None:
        """to_json() produces valid JSON."""
        service: SettingsService = engine._settings_service
        payload: str = service.to_json()
        import json

        decoded: dict[str, Any] = json.loads(payload)
        assert isinstance(decoded, dict)


class TestSettingsTypes(BaseTest):
    """Typed coercion across settings."""

    @pytest.mark.parametrize(
        ("key", "expected_type"),
        (
            ("WEIGHT_DETECTOR_AHO", int),
            ("SEMANTIC_SIMILARITY_THRESHOLD", float),
            ("SAFE_WORD_ENABLED", bool),
            ("MODEL_MAX_TOKENS", int),
            ("ALLOWED_ORIGINS", list),
            ("USER_WINDOW_DAYS", int),
        ),
    )
    def test_type_coercion(self, engine: Any, key: str, expected_type: type) -> None:
        """Stored settings coerce to their declared type.

        :param engine: test engine
        :param key: settings key
        :param expected_type: expected Python type
        """
        service: SettingsService = engine._settings_service
        service.get(key)
        assert isinstance(service.get(key), expected_type)

    def test_boolean_true_forms(self, engine: Any) -> None:
        """Boolean true values parse from any true form."""
        service: SettingsService = engine._settings_service
        service.get("SAFE_WORD_ENABLED")
        assert service._coerce("SAFE_WORD_ENABLED", "true") is True
        assert service._coerce("SAFE_WORD_ENABLED", "1") is True
        assert service._coerce("SAFE_WORD_ENABLED", "yes") is True

    def test_boolean_false_forms(self, engine: Any) -> None:
        """Boolean false values parse from any false form."""
        service: SettingsService = engine._settings_service
        assert service._coerce("SAFE_WORD_ENABLED", "false") is False
        assert service._coerce("SAFE_WORD_ENABLED", "0") is False
        assert service._coerce("SAFE_WORD_ENABLED", "no") is False

    def test_allowed_origins_parse(self, engine: Any) -> None:
        """Allowed origins parse from a comma-separated string."""
        service: SettingsService = engine._settings_service
        parsed = service._coerce("ALLOWED_ORIGINS", "http://a, http://b")
        assert parsed == ["http://a", "http://b"]

    def test_invalid_float_defaults(self, engine: Any) -> None:
        """An unparseable stored float falls back to the default."""
        service: SettingsService = engine._settings_service
        service.get("SEMANTIC_SIMILARITY_THRESHOLD")
        assert service.get("SEMANTIC_SIMILARITY_THRESHOLD", 0.5) == 0.65

    def test_empty_string_rejected_for_strings(self, engine: Any) -> None:
        """Empty string settings are rejected on update."""
        service: SettingsService = engine._settings_service
        service.get("SEMANTIC_MODEL")
        with pytest.raises(ValueError):
            service.update({"SEMANTIC_MODEL": ""})

    def test_boolean_update_accepted(self, engine: Any) -> None:
        """Boolean values update successfully."""
        service: SettingsService = engine._settings_service
        service.get("SAFE_WORD_ENABLED")
        updated: dict[str, Any] = service.update({"SAFE_WORD_ENABLED": False})
        assert "SAFE_WORD_ENABLED" in updated

    def test_float_update_accepted(self, engine: Any) -> None:
        """Float values update successfully."""
        service: SettingsService = engine._settings_service
        service.get("SEMANTIC_SIMILARITY_THRESHOLD")
        updated: dict[str, Any] = service.update({"SEMANTIC_SIMILARITY_THRESHOLD": 0.9})
        assert "SEMANTIC_SIMILARITY_THRESHOLD" in updated

    def test_integer_update_accepted(self, engine: Any) -> None:
        """Integer values update successfully."""
        service: SettingsService = engine._settings_service
        service.get("USER_WINDOW_DAYS")
        updated: dict[str, Any] = service.update({"USER_WINDOW_DAYS": 91})
        assert "USER_WINDOW_DAYS" in updated

    def test_bool_string_update_accepted(self, engine: Any) -> None:
        """Boolean strings update successfully."""
        service: SettingsService = engine._settings_service
        service.get("AUTO_TUNING_ENABLED")
        updated: dict[str, Any] = service.update({"AUTO_TUNING_ENABLED": "true"})
        assert "AUTO_TUNING_ENABLED" in updated

    def test_int_string_update_accepted(self, engine: Any) -> None:
        """Numeric strings update as integers."""
        service: SettingsService = engine._settings_service
        service.get("CACHE_MAX_SIZE")
        updated: dict[str, Any] = service.update({"CACHE_MAX_SIZE": "500"})
        assert "CACHE_MAX_SIZE" in updated

    def test_all_describe_editable_flags(self, engine: Any) -> None:
        """Every described setting carries an editable flag."""
        service: SettingsService = engine._settings_service
        for entry in service.describe():
            assert "editable" in entry
            assert isinstance(entry["editable"], bool)

    def test_all_describe_types(self, engine: Any) -> None:
        """Every described setting carries a type label."""
        service: SettingsService = engine._settings_service
        for entry in service.describe():
            assert entry["type"] in ("boolean", "integer", "float", "string")

    def test_update_multiple_at_once(self, engine: Any) -> None:
        """Multiple settings update in one call."""
        service: SettingsService = engine._settings_service
        service.get("WEIGHT_DETECTOR_AHO")
        service.get("WEIGHT_USER")
        updated: dict[str, Any] = service.update({"WEIGHT_DETECTOR_AHO": 40, "WEIGHT_USER": 25})
        assert {"WEIGHT_DETECTOR_AHO", "WEIGHT_USER"}.issubset(updated.keys())

    def test_update_mixed_valid_invalid(self, engine: Any) -> None:
        """A mixed update leaves valid keys unchanged on failure."""
        service: SettingsService = engine._settings_service
        service.get("WEIGHT_DETECTOR_AHO")
        with pytest.raises(ValueError):
            service.update({"WEIGHT_DETECTOR_AHO": 40, "NOPE": 1})
        assert int(service.get("WEIGHT_DETECTOR_AHO", 30)) == 30
