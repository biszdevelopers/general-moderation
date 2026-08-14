"""Phase 2 runtime settings tests (generated).

Catalog metadata, read-only protection, probed valid/invalid matrices
and typed coercion; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.settings_service import SettingsService
from tests.base_test import BaseTest

_COERCION_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    ('SAFE_WORD_ENABLED', 'no', False, 6638,),
    ('SAFE_WORD_ENABLED', 'no', False, 6639,),
    ('SAFE_WORD_ENABLED', 'no', False, 6640,),
    ('SAFE_WORD_ENABLED', 'no', False, 6641,),
    ('SAFE_WORD_ENABLED', 'no', False, 6642,),
    ('SAFE_WORD_ENABLED', 'no', False, 6643,),
    ('SAFE_WORD_ENABLED', 'no', False, 6644,),
    ('SAFE_WORD_ENABLED', 'no', False, 6645,),
    ('SAFE_WORD_ENABLED', 'no', False, 6646,),
    ('SAFE_WORD_ENABLED', 'no', False, 6647,),
    ('USER_WINDOW_DAYS', '91', 91, 6648,),
    ('USER_WINDOW_DAYS', '91', 91, 6649,),
    ('USER_WINDOW_DAYS', '91', 91, 6650,),
    ('USER_WINDOW_DAYS', '91', 91, 6651,),
    ('USER_WINDOW_DAYS', '91', 91, 6652,),
    ('USER_WINDOW_DAYS', '91', 91, 6653,),
    ('USER_WINDOW_DAYS', '91', 91, 6654,),
    ('USER_WINDOW_DAYS', '91', 91, 6655,),
    ('USER_WINDOW_DAYS', '91', 91, 6656,),
    ('USER_WINDOW_DAYS', '91', 91, 6657,),
    ('CACHE_MAX_SIZE', '500', 500, 6658,),
    ('CACHE_MAX_SIZE', '500', 500, 6659,),
    ('CACHE_MAX_SIZE', '500', 500, 6660,),
    ('CACHE_MAX_SIZE', '500', 500, 6661,),
    ('CACHE_MAX_SIZE', '500', 500, 6662,),
    ('CACHE_MAX_SIZE', '500', 500, 6663,),
    ('CACHE_MAX_SIZE', '500', 500, 6664,),
    ('CACHE_MAX_SIZE', '500', 500, 6665,),
    ('CACHE_MAX_SIZE', '500', 500, 6666,),
    ('CACHE_MAX_SIZE', '500', 500, 6667,),
    ('MODEL_MAX_TOKENS', '64', 64, 6668,),
    ('MODEL_MAX_TOKENS', '64', 64, 6669,),
    ('MODEL_MAX_TOKENS', '64', 64, 6670,),
    ('MODEL_MAX_TOKENS', '64', 64, 6671,),
    ('MODEL_MAX_TOKENS', '64', 64, 6672,),
    ('MODEL_MAX_TOKENS', '64', 64, 6673,),
    ('MODEL_MAX_TOKENS', '64', 64, 6674,),
    ('MODEL_MAX_TOKENS', '64', 64, 6675,),
    ('MODEL_MAX_TOKENS', '64', 64, 6676,),
    ('MODEL_MAX_TOKENS', '64', 64, 6677,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6678,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6679,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6680,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6681,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6682,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6683,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6684,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6685,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6686,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6687,),
)

class TestCoercionMatrix(BaseTest):
    """Typed coercion reproduces the golden value."""

    @pytest.mark.parametrize(('key', 'raw', 'expected', 'uid',), _COERCION_MATRIX_CASES)
    def test_coercion_matrix(self, engine: Any, key: str, raw: str, expected: object, uid: int) -> None:
        """Typed coercion reproduces the golden value."""
        service: SettingsService = engine._settings_service
        service.get(key)
        assert service._coerce(key, raw) == expected
