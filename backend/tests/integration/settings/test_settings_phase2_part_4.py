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
    ('AI_TARGET_PERCENTAGE', -5, 6211,),
    ('AI_TARGET_PERCENTAGE', -1, 6212,),
    ('AI_TARGET_PERCENTAGE', 1000000000, 6213,),
    ('AI_TARGET_PERCENTAGE', 'not-a-number', 6214,),
    ('ALLOWED_ORIGINS', '', 6215,),
    ('APP_CONFIG_DB_PATH', '', 6216,),
    ('APP_HOST', '', 6217,),
    ('AUTO_TUNING_BATCH_HOUR', -5, 6218,),
    ('AUTO_TUNING_BATCH_HOUR', -1, 6219,),
    ('AUTO_TUNING_BATCH_HOUR', 1000000000, 6220,),
    ('AUTO_TUNING_BATCH_HOUR', 'not-a-number', 6221,),
    ('AUTO_TUNING_ENABLED', 'maybe', 6222,),
    ('AUTO_TUNING_ENABLED', 'bogus', 6223,),
    ('AUTO_TUNING_ENABLED', 5, 6224,),
    ('AUTO_TUNING_ENABLED', 'not-bool', 6225,),
    ('BLOOM_FILTER_CAPACITY', '', 6226,),
    ('BLOOM_FILTER_ERROR_RATE', '', 6227,),
    ('CACHE_MAX_SIZE', -5, 6228,),
    ('CACHE_MAX_SIZE', -1, 6229,),
    ('CACHE_MAX_SIZE', 0, 6230,),
    ('CACHE_MAX_SIZE', 1000000000, 6231,),
    ('CACHE_MAX_SIZE', 'not-a-number', 6232,),
    ('CACHE_TTL_SECONDS', -5, 6233,),
    ('CACHE_TTL_SECONDS', -1, 6234,),
    ('CACHE_TTL_SECONDS', 0, 6235,),
    ('CACHE_TTL_SECONDS', 1000000000, 6236,),
    ('CACHE_TTL_SECONDS', 'not-a-number', 6237,),
    ('CRITICAL_PHRASES_DB_PATH', '', 6238,),
    ('CUSTOM_WORDS_PATH', '', 6239,),
    ('CUSTOM_WORDS_STORAGE', '', 6240,),
    ('DETECTOR_THREAD_POOL_SIZE', -5, 6241,),
    ('DETECTOR_THREAD_POOL_SIZE', -1, 6242,),
    ('DETECTOR_THREAD_POOL_SIZE', 0, 6243,),
    ('DETECTOR_THREAD_POOL_SIZE', 1000000000, 6244,),
    ('DETECTOR_THREAD_POOL_SIZE', 'not-a-number', 6245,),
    ('ENABLE_BADWORDS_PY', 'maybe', 6246,),
    ('ENABLE_BADWORDS_PY', 'bogus', 6247,),
    ('ENABLE_BADWORDS_PY', 5, 6248,),
    ('ENABLE_BADWORDS_PY', 'not-bool', 6249,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'maybe', 6250,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'bogus', 6251,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 5, 6252,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'not-bool', 6253,),
    ('ENABLE_DETECTOR_BK_TREE', 'maybe', 6254,),
    ('ENABLE_DETECTOR_BK_TREE', 'bogus', 6255,),
    ('ENABLE_DETECTOR_BK_TREE', 5, 6256,),
    ('ENABLE_DETECTOR_BK_TREE', 'not-bool', 6257,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'maybe', 6258,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'bogus', 6259,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 5, 6260,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'not-bool', 6261,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'maybe', 6262,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'bogus', 6263,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 5, 6264,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'not-bool', 6265,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'maybe', 6266,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'bogus', 6267,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 5, 6268,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'not-bool', 6269,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'maybe', 6270,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'bogus', 6271,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 5, 6272,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'not-bool', 6273,),
    ('ENABLE_GANGAJAL', 'maybe', 6274,),
    ('ENABLE_GANGAJAL', 'bogus', 6275,),
    ('ENABLE_GANGAJAL', 5, 6276,),
    ('ENABLE_GANGAJAL', 'not-bool', 6277,),
    ('ENABLE_GLIN_PROFANITY', 'maybe', 6278,),
    ('ENABLE_GLIN_PROFANITY', 'bogus', 6279,),
    ('ENABLE_GLIN_PROFANITY', 5, 6280,),
    ('ENABLE_GLIN_PROFANITY', 'not-bool', 6281,),
    ('ENABLE_PHRASE_DETECTOR', 'maybe', 6282,),
    ('ENABLE_PHRASE_DETECTOR', 'bogus', 6283,),
    ('ENABLE_PHRASE_DETECTOR', 5, 6284,),
    ('ENABLE_PHRASE_DETECTOR', 'not-bool', 6285,),
    ('ENABLE_PROFANITE', 'maybe', 6286,),
    ('ENABLE_PROFANITE', 'bogus', 6287,),
    ('ENABLE_PROFANITE', 5, 6288,),
    ('ENABLE_PROFANITE', 'not-bool', 6289,),
    ('ENABLE_PROFANITY_FILTER', 'maybe', 6290,),
    ('ENABLE_PROFANITY_FILTER', 'bogus', 6291,),
    ('ENABLE_PROFANITY_FILTER', 5, 6292,),
    ('ENABLE_PROFANITY_FILTER', 'not-bool', 6293,),
    ('ENABLE_PYPROFANE', 'maybe', 6294,),
    ('ENABLE_PYPROFANE', 'bogus', 6295,),
    ('ENABLE_PYPROFANE', 5, 6296,),
    ('ENABLE_PYPROFANE', 'not-bool', 6297,),
    ('ENABLE_SAFETEXT', 'maybe', 6298,),
    ('ENABLE_SAFETEXT', 'bogus', 6299,),
    ('ENABLE_SAFETEXT', 5, 6300,),
    ('ENABLE_SAFETEXT', 'not-bool', 6301,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'maybe', 6302,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'bogus', 6303,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 5, 6304,),
    ('ENABLE_SENSITIVE_STOP_WORDS', 'not-bool', 6305,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'maybe', 6306,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'bogus', 6307,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 5, 6308,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', 'not-bool', 6309,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', 'maybe', 6310,),
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
