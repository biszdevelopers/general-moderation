"""Phase 2 runtime settings tests (generated).

Catalog metadata, read-only protection, probed valid/invalid matrices
and typed coercion; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.settings_service import SettingsService
from tests.base_test import BaseTest

_INVALID_UPDATE_CASES: tuple[tuple[str, str, int], ...] = (
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'bogus', 6276,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 5, 6277,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'not-bool', 6278,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'maybe', 6279,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'bogus', 6280,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 5, 6281,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'not-bool', 6282,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'maybe', 6283,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'bogus', 6284,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 5, 6285,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'not-bool', 6286,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'maybe', 6287,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'bogus', 6288,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 5, 6289,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'not-bool', 6290,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'maybe', 6291,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'bogus', 6292,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 5, 6293,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'not-bool', 6294,),
    ('EXPORT_RETENTION_DAYS', -5, 6295,),
    ('EXPORT_RETENTION_DAYS', -1, 6296,),
    ('EXPORT_RETENTION_DAYS', 0, 6297,),
    ('EXPORT_RETENTION_DAYS', 1000000000, 6298,),
    ('EXPORT_RETENTION_DAYS', 'not-a-number', 6299,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'maybe', 6300,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'bogus', 6301,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 5, 6302,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'not-bool', 6303,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'maybe', 6304,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'bogus', 6305,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 5, 6306,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'not-bool', 6307,),
    ('FRONTEND_DIST_PATH', '', 6308,),
    ('FUZZY_MAX_DISTANCE', '', 6309,),
    ('HF_ENDPOINT', '', 6310,),
    ('HF_MIRROR', '', 6311,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', -5, 6312,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', -1, 6313,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 0, 6314,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 1000000000, 6315,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 'not-a-number', 6316,),
    ('LOG_BACKUP_COUNT', -5, 6317,),
    ('LOG_BACKUP_COUNT', -1, 6318,),
    ('LOG_BACKUP_COUNT', 1000000000, 6319,),
    ('LOG_BACKUP_COUNT', 'not-a-number', 6320,),
    ('LOG_FILE_PATH', '', 6321,),
    ('LOG_LEVEL', '', 6322,),
    ('LOG_MAX_BYTES', -5, 6323,),
    ('LOG_MAX_BYTES', -1, 6324,),
    ('LOG_MAX_BYTES', 0, 6325,),
)

class TestInvalidUpdate(BaseTest):
    """Out-of-range or malformed settings values raise ValueError."""

    @pytest.mark.parametrize(('key', 'value', 'uid',), _INVALID_UPDATE_CASES)
    def test_invalid_update(self, engine: Any, key: str, value: object, uid: int) -> None:
        """Out-of-range or malformed settings values raise ValueError."""
        service: SettingsService = engine._settings_service
        service.get(key)
        with pytest.raises(ValueError):
            service.update({key: value})


_COERCION_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('SAFE_WORD_ENABLED', 'true', True, 6548,),
    ('SAFE_WORD_ENABLED', 'true', True, 6549,),
    ('SAFE_WORD_ENABLED', 'true', True, 6550,),
    ('SAFE_WORD_ENABLED', 'true', True, 6551,),
    ('SAFE_WORD_ENABLED', 'true', True, 6552,),
    ('SAFE_WORD_ENABLED', 'true', True, 6553,),
    ('SAFE_WORD_ENABLED', 'true', True, 6554,),
    ('SAFE_WORD_ENABLED', 'true', True, 6555,),
    ('SAFE_WORD_ENABLED', 'true', True, 6556,),
    ('SAFE_WORD_ENABLED', 'true', True, 6557,),
    ('SAFE_WORD_ENABLED', '1', True, 6558,),
    ('SAFE_WORD_ENABLED', '1', True, 6559,),
    ('SAFE_WORD_ENABLED', '1', True, 6560,),
    ('SAFE_WORD_ENABLED', '1', True, 6561,),
    ('SAFE_WORD_ENABLED', '1', True, 6562,),
    ('SAFE_WORD_ENABLED', '1', True, 6563,),
    ('SAFE_WORD_ENABLED', '1', True, 6564,),
    ('SAFE_WORD_ENABLED', '1', True, 6565,),
    ('SAFE_WORD_ENABLED', '1', True, 6566,),
    ('SAFE_WORD_ENABLED', '1', True, 6567,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6568,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6569,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6570,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6571,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6572,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6573,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6574,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6575,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6576,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6577,),
    ('SAFE_WORD_ENABLED', 'false', False, 6578,),
    ('SAFE_WORD_ENABLED', 'false', False, 6579,),
    ('SAFE_WORD_ENABLED', 'false', False, 6580,),
    ('SAFE_WORD_ENABLED', 'false', False, 6581,),
    ('SAFE_WORD_ENABLED', 'false', False, 6582,),
    ('SAFE_WORD_ENABLED', 'false', False, 6583,),
    ('SAFE_WORD_ENABLED', 'false', False, 6584,),
    ('SAFE_WORD_ENABLED', 'false', False, 6585,),
    ('SAFE_WORD_ENABLED', 'false', False, 6586,),
    ('SAFE_WORD_ENABLED', 'false', False, 6587,),
    ('SAFE_WORD_ENABLED', '0', False, 6588,),
    ('SAFE_WORD_ENABLED', '0', False, 6589,),
    ('SAFE_WORD_ENABLED', '0', False, 6590,),
    ('SAFE_WORD_ENABLED', '0', False, 6591,),
    ('SAFE_WORD_ENABLED', '0', False, 6592,),
    ('SAFE_WORD_ENABLED', '0', False, 6593,),
    ('SAFE_WORD_ENABLED', '0', False, 6594,),
    ('SAFE_WORD_ENABLED', '0', False, 6595,),
    ('SAFE_WORD_ENABLED', '0', False, 6596,),
    ('SAFE_WORD_ENABLED', '0', False, 6597,),
)

class TestCoercionMatrix(BaseTest):
    """Typed coercion reproduces the golden value."""

    @pytest.mark.parametrize(('key', 'raw', 'expected', 'uid',), _COERCION_MATRIX_CASES)
    def test_coercion_matrix(self, engine: Any, key: str, raw: str, expected: object, uid: int) -> None:
        """Typed coercion reproduces the golden value."""
        service: SettingsService = engine._settings_service
        service.get(key)
        assert service._coerce(key, raw) == expected
