"""Phase 2 runtime settings tests (generated).

Catalog metadata, read-only protection, probed valid/invalid matrices
and typed coercion; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.settings_service import SettingsService
from tests.base_test import BaseTest

_INVALID_UPDATE_CASES: tuple[tuple[str, int, int], ...] = (
    ('AI_TARGET_PERCENTAGE', -5, 6176,),
    ('AI_TARGET_PERCENTAGE', -1, 6177,),
    ('AI_TARGET_PERCENTAGE', 1000000000, 6178,),
    ('AI_TARGET_PERCENTAGE', 'not-a-number', 6179,),
    ('ALLOWED_ORIGINS', '', 6180,),
    ('APP_CONFIG_DB_PATH', '', 6181,),
    ('APP_HOST', '', 6182,),
    ('AUTO_TUNING_BATCH_HOUR', -5, 6183,),
    ('AUTO_TUNING_BATCH_HOUR', -1, 6184,),
    ('AUTO_TUNING_BATCH_HOUR', 1000000000, 6185,),
    ('AUTO_TUNING_BATCH_HOUR', 'not-a-number', 6186,),
    ('AUTO_TUNING_ENABLED', 'maybe', 6187,),
    ('AUTO_TUNING_ENABLED', 'bogus', 6188,),
    ('AUTO_TUNING_ENABLED', 5, 6189,),
    ('AUTO_TUNING_ENABLED', 'not-bool', 6190,),
    ('BLOOM_FILTER_CAPACITY', '', 6191,),
    ('BLOOM_FILTER_ERROR_RATE', '', 6192,),
    ('CACHE_MAX_SIZE', -5, 6193,),
    ('CACHE_MAX_SIZE', -1, 6194,),
    ('CACHE_MAX_SIZE', 0, 6195,),
    ('CACHE_MAX_SIZE', 1000000000, 6196,),
    ('CACHE_MAX_SIZE', 'not-a-number', 6197,),
    ('CACHE_TTL_SECONDS', -5, 6198,),
    ('CACHE_TTL_SECONDS', -1, 6199,),
    ('CACHE_TTL_SECONDS', 0, 6200,),
    ('CACHE_TTL_SECONDS', 1000000000, 6201,),
    ('CACHE_TTL_SECONDS', 'not-a-number', 6202,),
    ('CRITICAL_PHRASES_DB_PATH', '', 6203,),
    ('CUSTOM_WORDS_PATH', '', 6204,),
    ('CUSTOM_WORDS_STORAGE', '', 6205,),
    ('DETECTOR_THREAD_POOL_SIZE', -5, 6206,),
    ('DETECTOR_THREAD_POOL_SIZE', -1, 6207,),
    ('DETECTOR_THREAD_POOL_SIZE', 0, 6208,),
    ('DETECTOR_THREAD_POOL_SIZE', 1000000000, 6209,),
    ('DETECTOR_THREAD_POOL_SIZE', 'not-a-number', 6210,),
    ('ENABLE_BADWORDS_PY', 'maybe', 6211,),
    ('ENABLE_BADWORDS_PY', 'bogus', 6212,),
    ('ENABLE_BADWORDS_PY', 5, 6213,),
    ('ENABLE_BADWORDS_PY', 'not-bool', 6214,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'maybe', 6215,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'bogus', 6216,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 5, 6217,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'not-bool', 6218,),
    ('ENABLE_DETECTOR_BK_TREE', 'maybe', 6219,),
    ('ENABLE_DETECTOR_BK_TREE', 'bogus', 6220,),
    ('ENABLE_DETECTOR_BK_TREE', 5, 6221,),
    ('ENABLE_DETECTOR_BK_TREE', 'not-bool', 6222,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'maybe', 6223,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'bogus', 6224,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 5, 6225,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'not-bool', 6226,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'maybe', 6227,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'bogus', 6228,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 5, 6229,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'not-bool', 6230,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'maybe', 6231,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'bogus', 6232,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 5, 6233,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'not-bool', 6234,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'maybe', 6235,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'bogus', 6236,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 5, 6237,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'not-bool', 6238,),
    ('ENABLE_GANGAJAL', 'maybe', 6239,),
    ('ENABLE_GANGAJAL', 'bogus', 6240,),
    ('ENABLE_GANGAJAL', 5, 6241,),
    ('ENABLE_GANGAJAL', 'not-bool', 6242,),
    ('ENABLE_GLIN_PROFANITY', 'maybe', 6243,),
    ('ENABLE_GLIN_PROFANITY', 'bogus', 6244,),
    ('ENABLE_GLIN_PROFANITY', 5, 6245,),
    ('ENABLE_GLIN_PROFANITY', 'not-bool', 6246,),
    ('ENABLE_PHRASE_DETECTOR', 'maybe', 6247,),
    ('ENABLE_PHRASE_DETECTOR', 'bogus', 6248,),
    ('ENABLE_PHRASE_DETECTOR', 5, 6249,),
    ('ENABLE_PHRASE_DETECTOR', 'not-bool', 6250,),
    ('ENABLE_PROFANITE', 'maybe', 6251,),
    ('ENABLE_PROFANITE', 'bogus', 6252,),
    ('ENABLE_PROFANITE', 5, 6253,),
    ('ENABLE_PROFANITE', 'not-bool', 6254,),
    ('ENABLE_PROFANITY_FILTER', 'maybe', 6255,),
    ('ENABLE_PROFANITY_FILTER', 'bogus', 6256,),
    ('ENABLE_PROFANITY_FILTER', 5, 6257,),
    ('ENABLE_PROFANITY_FILTER', 'not-bool', 6258,),
    ('ENABLE_PYPROFANE', 'maybe', 6259,),
    ('ENABLE_PYPROFANE', 'bogus', 6260,),
    ('ENABLE_PYPROFANE', 5, 6261,),
    ('ENABLE_PYPROFANE', 'not-bool', 6262,),
    ('ENABLE_SAFETEXT', 'maybe', 6263,),
    ('ENABLE_SAFETEXT', 'bogus', 6264,),
    ('ENABLE_SAFETEXT', 5, 6265,),
    ('ENABLE_SAFETEXT', 'not-bool', 6266,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'maybe', 6267,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'bogus', 6268,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 5, 6269,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'not-bool', 6270,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'maybe', 6271,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'bogus', 6272,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 5, 6273,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'not-bool', 6274,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'maybe', 6275,),
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
