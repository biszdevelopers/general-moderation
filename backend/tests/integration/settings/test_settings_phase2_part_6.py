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
    ('SAFE_WORD_ENABLED', 'no', False, 6598,),
    ('SAFE_WORD_ENABLED', 'no', False, 6599,),
    ('SAFE_WORD_ENABLED', 'no', False, 6600,),
    ('SAFE_WORD_ENABLED', 'no', False, 6601,),
    ('SAFE_WORD_ENABLED', 'no', False, 6602,),
    ('SAFE_WORD_ENABLED', 'no', False, 6603,),
    ('SAFE_WORD_ENABLED', 'no', False, 6604,),
    ('SAFE_WORD_ENABLED', 'no', False, 6605,),
    ('SAFE_WORD_ENABLED', 'no', False, 6606,),
    ('SAFE_WORD_ENABLED', 'no', False, 6607,),
    ('USER_WINDOW_DAYS', '91', 91, 6608,),
    ('USER_WINDOW_DAYS', '91', 91, 6609,),
    ('USER_WINDOW_DAYS', '91', 91, 6610,),
    ('USER_WINDOW_DAYS', '91', 91, 6611,),
    ('USER_WINDOW_DAYS', '91', 91, 6612,),
    ('USER_WINDOW_DAYS', '91', 91, 6613,),
    ('USER_WINDOW_DAYS', '91', 91, 6614,),
    ('USER_WINDOW_DAYS', '91', 91, 6615,),
    ('USER_WINDOW_DAYS', '91', 91, 6616,),
    ('USER_WINDOW_DAYS', '91', 91, 6617,),
    ('CACHE_MAX_SIZE', '500', 500, 6618,),
    ('CACHE_MAX_SIZE', '500', 500, 6619,),
    ('CACHE_MAX_SIZE', '500', 500, 6620,),
    ('CACHE_MAX_SIZE', '500', 500, 6621,),
    ('CACHE_MAX_SIZE', '500', 500, 6622,),
    ('CACHE_MAX_SIZE', '500', 500, 6623,),
    ('CACHE_MAX_SIZE', '500', 500, 6624,),
    ('CACHE_MAX_SIZE', '500', 500, 6625,),
    ('CACHE_MAX_SIZE', '500', 500, 6626,),
    ('CACHE_MAX_SIZE', '500', 500, 6627,),
    ('MODEL_MAX_TOKENS', '64', 64, 6628,),
    ('MODEL_MAX_TOKENS', '64', 64, 6629,),
    ('MODEL_MAX_TOKENS', '64', 64, 6630,),
    ('MODEL_MAX_TOKENS', '64', 64, 6631,),
    ('MODEL_MAX_TOKENS', '64', 64, 6632,),
    ('MODEL_MAX_TOKENS', '64', 64, 6633,),
    ('MODEL_MAX_TOKENS', '64', 64, 6634,),
    ('MODEL_MAX_TOKENS', '64', 64, 6635,),
    ('MODEL_MAX_TOKENS', '64', 64, 6636,),
    ('MODEL_MAX_TOKENS', '64', 64, 6637,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6638,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6639,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6640,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6641,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6642,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6643,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6644,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6645,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6646,),
    ('SEMANTIC_SIMILARITY_THRESHOLD', '0.9', 0.9, 6647,),
)

class TestCoercionMatrix(BaseTest):
    """Typed coercion reproduces the golden value."""

    @pytest.mark.parametrize(('key', 'raw', 'expected', 'uid',), _COERCION_MATRIX_CASES)
    def test_coercion_matrix(self, engine: Any, key: str, raw: str, expected: object, uid: int) -> None:
        """Typed coercion reproduces the golden value."""
        service: SettingsService = engine._settings_service
        service.get(key)
        assert service._coerce(key, raw) == expected
