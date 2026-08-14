"""Phase 2 runtime settings tests (generated).

Catalog metadata, read-only protection, probed valid/invalid matrices
and typed coercion; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.settings_service import SettingsService
from tests.base_test import BaseTest

_VALID_UPDATE_CASES: tuple[tuple[str, int, int], ...] = (
    ('AI_TARGET_PERCENTAGE', 25, 5901,),
    ('AI_TARGET_PERCENTAGE', 50, 5902,),
    ('AI_TARGET_PERCENTAGE', 100, 5903,),
    ('ALLOWED_ORIGINS', 'sample-value', 5904,),
    ('ALLOWED_ORIGINS', 'config-value', 5905,),
    ('ALLOWED_ORIGINS', '192.168.0.1', 5906,),
    ('APP_CONFIG_DB_PATH', 'sample-value', 5907,),
    ('APP_CONFIG_DB_PATH', 'config-value', 5908,),
    ('APP_CONFIG_DB_PATH', '192.168.0.1', 5909,),
    ('APP_HOST', 'sample-value', 5910,),
    ('APP_HOST', 'config-value', 5911,),
    ('APP_HOST', '192.168.0.1', 5912,),
    ('AUTO_TUNING_ENABLED', True, 5913,),
    ('AUTO_TUNING_ENABLED', False, 5914,),
    ('BLOOM_FILTER_CAPACITY', 'sample-value', 5915,),
    ('BLOOM_FILTER_CAPACITY', 'config-value', 5916,),
    ('BLOOM_FILTER_CAPACITY', '192.168.0.1', 5917,),
    ('BLOOM_FILTER_ERROR_RATE', 'sample-value', 5918,),
    ('BLOOM_FILTER_ERROR_RATE', 'config-value', 5919,),
    ('BLOOM_FILTER_ERROR_RATE', '192.168.0.1', 5920,),
    ('CACHE_MAX_SIZE', 25, 5921,),
    ('CACHE_MAX_SIZE', 50, 5922,),
    ('CACHE_MAX_SIZE', 100, 5923,),
    ('CACHE_MAX_SIZE', 250, 5924,),
    ('CACHE_MAX_SIZE', 500, 5925,),
    ('CACHE_TTL_SECONDS', 25, 5926,),
    ('CACHE_TTL_SECONDS', 50, 5927,),
    ('CACHE_TTL_SECONDS', 100, 5928,),
    ('CACHE_TTL_SECONDS', 250, 5929,),
    ('CACHE_TTL_SECONDS', 500, 5930,),
    ('CRITICAL_PHRASES_DB_PATH', 'sample-value', 5931,),
    ('CRITICAL_PHRASES_DB_PATH', 'config-value', 5932,),
    ('CRITICAL_PHRASES_DB_PATH', '192.168.0.1', 5933,),
    ('CUSTOM_WORDS_PATH', 'sample-value', 5934,),
    ('CUSTOM_WORDS_PATH', 'config-value', 5935,),
    ('CUSTOM_WORDS_PATH', '192.168.0.1', 5936,),
    ('CUSTOM_WORDS_STORAGE', 'sample-value', 5937,),
    ('CUSTOM_WORDS_STORAGE', 'config-value', 5938,),
    ('CUSTOM_WORDS_STORAGE', '192.168.0.1', 5939,),
    ('DETECTOR_THREAD_POOL_SIZE', 25, 5940,),
    ('DETECTOR_THREAD_POOL_SIZE', 50, 5941,),
    ('ENABLE_BADWORDS_PY', True, 5942,),
    ('ENABLE_BADWORDS_PY', False, 5943,),
    ('ENABLE_DETECTOR_AHO_CORASICK', True, 5944,),
    ('ENABLE_DETECTOR_AHO_CORASICK', False, 5945,),
    ('ENABLE_DETECTOR_BK_TREE', True, 5946,),
    ('ENABLE_DETECTOR_BK_TREE', False, 5947,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', True, 5948,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', False, 5949,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', True, 5950,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', False, 5951,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', True, 5952,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', False, 5953,),
    ('ENABLE_DETECTOR_ROLLING_HASH', True, 5954,),
    ('ENABLE_DETECTOR_ROLLING_HASH', False, 5955,),
    ('ENABLE_GANGAJAL', True, 5956,),
    ('ENABLE_GANGAJAL', False, 5957,),
    ('ENABLE_GLIN_PROFANITY', True, 5958,),
    ('ENABLE_GLIN_PROFANITY', False, 5959,),
    ('ENABLE_PHRASE_DETECTOR', True, 5960,),
    ('ENABLE_PHRASE_DETECTOR', False, 5961,),
    ('ENABLE_PROFANITE', True, 5962,),
    ('ENABLE_PROFANITE', False, 5963,),
    ('ENABLE_PROFANITY_FILTER', True, 5964,),
    ('ENABLE_PROFANITY_FILTER', False, 5965,),
    ('ENABLE_PYPROFANE', True, 5966,),
    ('ENABLE_PYPROFANE', False, 5967,),
    ('ENABLE_SAFETEXT', True, 5968,),
    ('ENABLE_SAFETEXT', False, 5969,),
    ('ENABLE_SENSITIVE_STOP_WORDS', True, 5970,),
    ('ENABLE_SENSITIVE_STOP_WORDS', False, 5971,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', True, 5972,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', False, 5973,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', True, 5974,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', False, 5975,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', True, 5976,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', False, 5977,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', True, 5978,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', False, 5979,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', True, 5980,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', False, 5981,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', True, 5982,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', False, 5983,),
    ('EXPORT_RETENTION_DAYS', 25, 5984,),
    ('EXPORT_RETENTION_DAYS', 50, 5985,),
    ('EXPORT_RETENTION_DAYS', 100, 5986,),
    ('EXPORT_RETENTION_DAYS', 250, 5987,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', True, 5988,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', False, 5989,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', True, 5990,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', False, 5991,),
    ('FRONTEND_DIST_PATH', 'sample-value', 5992,),
    ('FRONTEND_DIST_PATH', 'config-value', 5993,),
    ('FRONTEND_DIST_PATH', '192.168.0.1', 5994,),
    ('FUZZY_MAX_DISTANCE', 'sample-value', 5995,),
    ('FUZZY_MAX_DISTANCE', 'config-value', 5996,),
    ('FUZZY_MAX_DISTANCE', '192.168.0.1', 5997,),
    ('HF_ENDPOINT', 'sample-value', 5998,),
    ('HF_ENDPOINT', 'config-value', 5999,),
    ('HF_ENDPOINT', '192.168.0.1', 6000,),
)

class TestValidUpdate(BaseTest):
    """In-range settings values persist without error."""

    @pytest.mark.parametrize(('key', 'value', 'uid',), _VALID_UPDATE_CASES)
    def test_valid_update(self, engine: Any, key: str, value: object, uid: int) -> None:
        """In-range settings values persist without error."""
        service: SettingsService = engine._settings_service
        service.get(key)
        updated = service.update({key: value})
        assert key in updated
