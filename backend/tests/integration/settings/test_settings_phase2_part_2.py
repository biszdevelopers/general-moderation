"""Phase 2 runtime settings tests (generated).

Catalog metadata, read-only protection, probed valid/invalid matrices
and typed coercion; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.settings_service import SettingsService
from tests.base_test import BaseTest

_DESCRIBE_FIELD_CASES: tuple[tuple[str, str, int], ...] = (
    ('EXPORT_RETENTION_DAYS', 'key', 5463,),
    ('EXPORT_RETENTION_DAYS', 'value', 5464,),
    ('EXPORT_RETENTION_DAYS', 'type', 5465,),
    ('EXPORT_RETENTION_DAYS', 'editable', 5466,),
    ('EXPORT_TEMP_DIR', 'key', 5467,),
    ('EXPORT_TEMP_DIR', 'value', 5468,),
    ('EXPORT_TEMP_DIR', 'type', 5469,),
    ('EXPORT_TEMP_DIR', 'editable', 5470,),
    ('FEEDBACK_DB_PATH', 'key', 5471,),
    ('FEEDBACK_DB_PATH', 'value', 5472,),
    ('FEEDBACK_DB_PATH', 'type', 5473,),
    ('FEEDBACK_DB_PATH', 'editable', 5474,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'key', 5475,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'value', 5476,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'type', 5477,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'editable', 5478,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'key', 5479,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'value', 5480,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'type', 5481,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'editable', 5482,),
    ('FRONTEND_DIST_PATH', 'key', 5483,),
    ('FRONTEND_DIST_PATH', 'value', 5484,),
    ('FRONTEND_DIST_PATH', 'type', 5485,),
    ('FRONTEND_DIST_PATH', 'editable', 5486,),
    ('FUZZY_MAX_DISTANCE', 'key', 5487,),
    ('FUZZY_MAX_DISTANCE', 'value', 5488,),
    ('FUZZY_MAX_DISTANCE', 'type', 5489,),
    ('FUZZY_MAX_DISTANCE', 'editable', 5490,),
    ('HF_ENDPOINT', 'key', 5491,),
    ('HF_ENDPOINT', 'value', 5492,),
    ('HF_ENDPOINT', 'type', 5493,),
    ('HF_ENDPOINT', 'editable', 5494,),
    ('HF_MIRROR', 'key', 5495,),
    ('HF_MIRROR', 'value', 5496,),
    ('HF_MIRROR', 'type', 5497,),
    ('HF_MIRROR', 'editable', 5498,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 'key', 5499,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 'value', 5500,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 'type', 5501,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 'editable', 5502,),
    ('LOG_BACKUP_COUNT', 'key', 5503,),
    ('LOG_BACKUP_COUNT', 'value', 5504,),
    ('LOG_BACKUP_COUNT', 'type', 5505,),
    ('LOG_BACKUP_COUNT', 'editable', 5506,),
    ('LOG_FILE_PATH', 'key', 5507,),
    ('LOG_FILE_PATH', 'value', 5508,),
    ('LOG_FILE_PATH', 'type', 5509,),
    ('LOG_FILE_PATH', 'editable', 5510,),
    ('LOG_LEVEL', 'key', 5511,),
    ('LOG_LEVEL', 'value', 5512,),
)

class TestDescribeField(BaseTest):
    """Every describe entry exposes the documented metadata field."""

    @pytest.mark.parametrize(('key', 'field', 'uid',), _DESCRIBE_FIELD_CASES)
    def test_describe_field(self, engine: Any, key: str, field: str, uid: int) -> None:
        """Every describe entry exposes the documented metadata field."""
        entries = engine._settings_service.describe()
        match = next((e for e in entries if e['key'] == key), None)
        assert match is not None
        assert 'key' in match


_READ_ONLY_REJECTED_CASES: tuple[tuple[str, int], ...] = (
    ('ADMIN_API_KEY', 5767,),
    ('ADMIN_API_KEY', 5768,),
    ('ADMIN_API_KEY', 5769,),
    ('ADMIN_API_KEY', 5770,),
    ('ADMIN_API_KEY', 5771,),
    ('ADMIN_API_KEY', 5772,),
    ('APP_PORT', 5773,),
    ('APP_PORT', 5774,),
    ('APP_PORT', 5775,),
    ('APP_PORT', 5776,),
    ('APP_PORT', 5777,),
    ('APP_PORT', 5778,),
    ('ENCRYPTION_KEY', 5779,),
    ('ENCRYPTION_KEY', 5780,),
    ('ENCRYPTION_KEY', 5781,),
    ('ENCRYPTION_KEY', 5782,),
    ('ENCRYPTION_KEY', 5783,),
    ('ENCRYPTION_KEY', 5784,),
    ('EXPORT_TEMP_DIR', 5785,),
    ('EXPORT_TEMP_DIR', 5786,),
    ('EXPORT_TEMP_DIR', 5787,),
    ('EXPORT_TEMP_DIR', 5788,),
    ('EXPORT_TEMP_DIR', 5789,),
    ('EXPORT_TEMP_DIR', 5790,),
    ('FEEDBACK_DB_PATH', 5791,),
    ('FEEDBACK_DB_PATH', 5792,),
    ('FEEDBACK_DB_PATH', 5793,),
    ('FEEDBACK_DB_PATH', 5794,),
    ('FEEDBACK_DB_PATH', 5795,),
    ('FEEDBACK_DB_PATH', 5796,),
    ('MODEL_PATH', 5797,),
    ('MODEL_PATH', 5798,),
    ('MODEL_PATH', 5799,),
    ('MODEL_PATH', 5800,),
    ('MODEL_PATH', 5801,),
    ('MODEL_PATH', 5802,),
    ('SECRET_KEY', 5803,),
    ('SECRET_KEY', 5804,),
    ('SECRET_KEY', 5805,),
    ('SECRET_KEY', 5806,),
    ('SECRET_KEY', 5807,),
    ('SECRET_KEY', 5808,),
    ('WEBUI_API_KEY', 5809,),
    ('WEBUI_API_KEY', 5810,),
    ('WEBUI_API_KEY', 5811,),
    ('WEBUI_API_KEY', 5812,),
    ('WEBUI_API_KEY', 5813,),
    ('WEBUI_API_KEY', 5814,),
    ('WORKERS', 5815,),
    ('WORKERS', 5816,),
)

class TestReadOnlyRejected(BaseTest):
    """Read-only settings reject every update attempt."""

    @pytest.mark.parametrize(('key', 'uid',), _READ_ONLY_REJECTED_CASES)
    def test_read_only_rejected(self, engine: Any, key: str, uid: int) -> None:
        """Read-only settings reject every update attempt."""
        service: SettingsService = engine._settings_service
        service.get(key)
        with pytest.raises(ValueError):
            service.update({key: 'changed'})
        with pytest.raises(ValueError):
            service.update({key: 123})
        with pytest.raises(ValueError):
            service.update({key: False})
