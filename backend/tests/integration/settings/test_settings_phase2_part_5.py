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
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'bogus', 6311,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 5, 6312,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'not-bool', 6313,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'maybe', 6314,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'bogus', 6315,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 5, 6316,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', 'not-bool', 6317,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'maybe', 6318,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'bogus', 6319,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 5, 6320,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', 'not-bool', 6321,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'maybe', 6322,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'bogus', 6323,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 5, 6324,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', 'not-bool', 6325,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'maybe', 6326,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'bogus', 6327,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 5, 6328,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', 'not-bool', 6329,),
    ('EXPORT_RETENTION_DAYS', -5, 6330,),
    ('EXPORT_RETENTION_DAYS', -1, 6331,),
    ('EXPORT_RETENTION_DAYS', 0, 6332,),
    ('EXPORT_RETENTION_DAYS', 1000000000, 6333,),
    ('EXPORT_RETENTION_DAYS', 'not-a-number', 6334,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'maybe', 6335,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'bogus', 6336,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 5, 6337,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', 'not-bool', 6338,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'maybe', 6339,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'bogus', 6340,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 5, 6341,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', 'not-bool', 6342,),
    ('FRONTEND_DIST_PATH', '', 6343,),
    ('FUZZY_MAX_DISTANCE', '', 6344,),
    ('HF_ENDPOINT', '', 6345,),
    ('HF_MIRROR', '', 6346,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', -5, 6347,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', -1, 6348,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 0, 6349,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 1000000000, 6350,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 'not-a-number', 6351,),
    ('LOG_BACKUP_COUNT', -5, 6352,),
    ('LOG_BACKUP_COUNT', -1, 6353,),
    ('LOG_BACKUP_COUNT', 1000000000, 6354,),
    ('LOG_BACKUP_COUNT', 'not-a-number', 6355,),
    ('LOG_FILE_PATH', '', 6356,),
    ('LOG_LEVEL', '', 6357,),
    ('LOG_MAX_BYTES', -5, 6358,),
    ('LOG_MAX_BYTES', -1, 6359,),
    ('LOG_MAX_BYTES', 0, 6360,),
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
    ('SAFE_WORD_ENABLED', 'true', True, 6588,),
    ('SAFE_WORD_ENABLED', 'true', True, 6589,),
    ('SAFE_WORD_ENABLED', 'true', True, 6590,),
    ('SAFE_WORD_ENABLED', 'true', True, 6591,),
    ('SAFE_WORD_ENABLED', 'true', True, 6592,),
    ('SAFE_WORD_ENABLED', 'true', True, 6593,),
    ('SAFE_WORD_ENABLED', 'true', True, 6594,),
    ('SAFE_WORD_ENABLED', 'true', True, 6595,),
    ('SAFE_WORD_ENABLED', 'true', True, 6596,),
    ('SAFE_WORD_ENABLED', 'true', True, 6597,),
    ('SAFE_WORD_ENABLED', '1', True, 6598,),
    ('SAFE_WORD_ENABLED', '1', True, 6599,),
    ('SAFE_WORD_ENABLED', '1', True, 6600,),
    ('SAFE_WORD_ENABLED', '1', True, 6601,),
    ('SAFE_WORD_ENABLED', '1', True, 6602,),
    ('SAFE_WORD_ENABLED', '1', True, 6603,),
    ('SAFE_WORD_ENABLED', '1', True, 6604,),
    ('SAFE_WORD_ENABLED', '1', True, 6605,),
    ('SAFE_WORD_ENABLED', '1', True, 6606,),
    ('SAFE_WORD_ENABLED', '1', True, 6607,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6608,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6609,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6610,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6611,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6612,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6613,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6614,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6615,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6616,),
    ('SAFE_WORD_ENABLED', 'yes', True, 6617,),
    ('SAFE_WORD_ENABLED', 'false', False, 6618,),
    ('SAFE_WORD_ENABLED', 'false', False, 6619,),
    ('SAFE_WORD_ENABLED', 'false', False, 6620,),
    ('SAFE_WORD_ENABLED', 'false', False, 6621,),
    ('SAFE_WORD_ENABLED', 'false', False, 6622,),
    ('SAFE_WORD_ENABLED', 'false', False, 6623,),
    ('SAFE_WORD_ENABLED', 'false', False, 6624,),
    ('SAFE_WORD_ENABLED', 'false', False, 6625,),
    ('SAFE_WORD_ENABLED', 'false', False, 6626,),
    ('SAFE_WORD_ENABLED', 'false', False, 6627,),
    ('SAFE_WORD_ENABLED', '0', False, 6628,),
    ('SAFE_WORD_ENABLED', '0', False, 6629,),
    ('SAFE_WORD_ENABLED', '0', False, 6630,),
    ('SAFE_WORD_ENABLED', '0', False, 6631,),
    ('SAFE_WORD_ENABLED', '0', False, 6632,),
    ('SAFE_WORD_ENABLED', '0', False, 6633,),
    ('SAFE_WORD_ENABLED', '0', False, 6634,),
    ('SAFE_WORD_ENABLED', '0', False, 6635,),
    ('SAFE_WORD_ENABLED', '0', False, 6636,),
    ('SAFE_WORD_ENABLED', '0', False, 6637,),
)

class TestCoercionMatrix(BaseTest):
    """Typed coercion reproduces the golden value."""

    @pytest.mark.parametrize(('key', 'raw', 'expected', 'uid',), _COERCION_MATRIX_CASES)
    def test_coercion_matrix(self, engine: Any, key: str, raw: str, expected: object, uid: int) -> None:
        """Typed coercion reproduces the golden value."""
        service: SettingsService = engine._settings_service
        service.get(key)
        assert service._coerce(key, raw) == expected
