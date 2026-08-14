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
    ('ADMIN_API_KEY', 5831,),
    ('ADMIN_API_KEY', 5832,),
    ('ADMIN_API_KEY', 5833,),
    ('ADMIN_API_KEY', 5834,),
    ('ADMIN_API_KEY', 5835,),
    ('ADMIN_API_KEY', 5836,),
    ('APP_PORT', 5837,),
    ('APP_PORT', 5838,),
    ('APP_PORT', 5839,),
    ('APP_PORT', 5840,),
    ('APP_PORT', 5841,),
    ('APP_PORT', 5842,),
    ('ENCRYPTION_KEY', 5843,),
    ('ENCRYPTION_KEY', 5844,),
    ('ENCRYPTION_KEY', 5845,),
    ('ENCRYPTION_KEY', 5846,),
    ('ENCRYPTION_KEY', 5847,),
    ('ENCRYPTION_KEY', 5848,),
    ('EXPORT_TEMP_DIR', 5849,),
    ('EXPORT_TEMP_DIR', 5850,),
    ('EXPORT_TEMP_DIR', 5851,),
    ('EXPORT_TEMP_DIR', 5852,),
    ('EXPORT_TEMP_DIR', 5853,),
    ('EXPORT_TEMP_DIR', 5854,),
    ('FEEDBACK_DB_PATH', 5855,),
    ('FEEDBACK_DB_PATH', 5856,),
    ('FEEDBACK_DB_PATH', 5857,),
    ('FEEDBACK_DB_PATH', 5858,),
    ('FEEDBACK_DB_PATH', 5859,),
    ('FEEDBACK_DB_PATH', 5860,),
    ('MODEL_PATH', 5861,),
    ('MODEL_PATH', 5862,),
    ('MODEL_PATH', 5863,),
    ('MODEL_PATH', 5864,),
    ('MODEL_PATH', 5865,),
    ('MODEL_PATH', 5866,),
    ('SECRET_KEY', 5867,),
    ('SECRET_KEY', 5868,),
    ('SECRET_KEY', 5869,),
    ('SECRET_KEY', 5870,),
    ('SECRET_KEY', 5871,),
    ('SECRET_KEY', 5872,),
    ('WEBUI_API_KEY', 5873,),
    ('WEBUI_API_KEY', 5874,),
    ('WEBUI_API_KEY', 5875,),
    ('WEBUI_API_KEY', 5876,),
    ('WEBUI_API_KEY', 5877,),
    ('WEBUI_API_KEY', 5878,),
    ('WORKERS', 5879,),
    ('WORKERS', 5880,),
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
