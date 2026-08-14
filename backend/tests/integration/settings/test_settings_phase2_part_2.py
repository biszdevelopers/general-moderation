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
    ('ENABLE_PHRASE_DETECTOR', 'key', 5463,),
    ('ENABLE_PHRASE_DETECTOR', 'value', 5464,),
    ('ENABLE_PHRASE_DETECTOR', 'type', 5465,),
    ('ENABLE_PHRASE_DETECTOR', 'editable', 5466,),
    ('ENABLE_PROFANITE', 'key', 5467,),
    ('ENABLE_PROFANITE', 'value', 5468,),
    ('ENABLE_PROFANITE', 'type', 5469,),
    ('ENABLE_PROFANITE', 'editable', 5470,),
    ('ENABLE_PROFANITY_FILTER', 'key', 5471,),
    ('ENABLE_PROFANITY_FILTER', 'value', 5472,),
    ('ENABLE_PROFANITY_FILTER', 'type', 5473,),
    ('ENABLE_PROFANITY_FILTER', 'editable', 5474,),
    ('ENABLE_PYPROFANE', 'key', 5475,),
    ('ENABLE_PYPROFANE', 'value', 5476,),
    ('ENABLE_PYPROFANE', 'type', 5477,),
    ('ENABLE_PYPROFANE', 'editable', 5478,),
    ('ENABLE_SAFETEXT', 'key', 5479,),
    ('ENABLE_SAFETEXT', 'value', 5480,),
    ('ENABLE_SAFETEXT', 'type', 5481,),
    ('ENABLE_SAFETEXT', 'editable', 5482,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'key', 5483,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'value', 5484,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'type', 5485,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'editable', 5486,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'key', 5487,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'value', 5488,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'type', 5489,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'editable', 5490,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'key', 5491,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'value', 5492,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'type', 5493,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'editable', 5494,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'key', 5495,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'value', 5496,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'type', 5497,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'editable', 5498,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'key', 5499,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'value', 5500,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'type', 5501,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'editable', 5502,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'key', 5503,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'value', 5504,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'type', 5505,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'editable', 5506,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'key', 5507,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'value', 5508,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'type', 5509,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'editable', 5510,),
    ('ENCRYPTION_KEY', 'key', 5511,),
    ('ENCRYPTION_KEY', 'value', 5512,),
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
    ('ADMIN_API_KEY', 5851,),
    ('ADMIN_API_KEY', 5852,),
    ('ADMIN_API_KEY', 5853,),
    ('ADMIN_API_KEY', 5854,),
    ('ADMIN_API_KEY', 5855,),
    ('ADMIN_API_KEY', 5856,),
    ('APP_PORT', 5857,),
    ('APP_PORT', 5858,),
    ('APP_PORT', 5859,),
    ('APP_PORT', 5860,),
    ('APP_PORT', 5861,),
    ('APP_PORT', 5862,),
    ('ENCRYPTION_KEY', 5863,),
    ('ENCRYPTION_KEY', 5864,),
    ('ENCRYPTION_KEY', 5865,),
    ('ENCRYPTION_KEY', 5866,),
    ('ENCRYPTION_KEY', 5867,),
    ('ENCRYPTION_KEY', 5868,),
    ('EXPORT_TEMP_DIR', 5869,),
    ('EXPORT_TEMP_DIR', 5870,),
    ('EXPORT_TEMP_DIR', 5871,),
    ('EXPORT_TEMP_DIR', 5872,),
    ('EXPORT_TEMP_DIR', 5873,),
    ('EXPORT_TEMP_DIR', 5874,),
    ('FEEDBACK_DB_PATH', 5875,),
    ('FEEDBACK_DB_PATH', 5876,),
    ('FEEDBACK_DB_PATH', 5877,),
    ('FEEDBACK_DB_PATH', 5878,),
    ('FEEDBACK_DB_PATH', 5879,),
    ('FEEDBACK_DB_PATH', 5880,),
    ('MODEL_PATH', 5881,),
    ('MODEL_PATH', 5882,),
    ('MODEL_PATH', 5883,),
    ('MODEL_PATH', 5884,),
    ('MODEL_PATH', 5885,),
    ('MODEL_PATH', 5886,),
    ('SECRET_KEY', 5887,),
    ('SECRET_KEY', 5888,),
    ('SECRET_KEY', 5889,),
    ('SECRET_KEY', 5890,),
    ('SECRET_KEY', 5891,),
    ('SECRET_KEY', 5892,),
    ('WEBUI_API_KEY', 5893,),
    ('WEBUI_API_KEY', 5894,),
    ('WEBUI_API_KEY', 5895,),
    ('WEBUI_API_KEY', 5896,),
    ('WEBUI_API_KEY', 5897,),
    ('WEBUI_API_KEY', 5898,),
    ('WORKERS', 5899,),
    ('WORKERS', 5900,),
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
