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
    ('AI_TARGET_PERCENTAGE', 25, 5881,),
    ('AI_TARGET_PERCENTAGE', 50, 5882,),
    ('AI_TARGET_PERCENTAGE', 100, 5883,),
    ('ALLOWED_ORIGINS', 'sample-value', 5884,),
    ('ALLOWED_ORIGINS', 'config-value', 5885,),
    ('ALLOWED_ORIGINS', '192.168.0.1', 5886,),
    ('APP_CONFIG_DB_PATH', 'sample-value', 5887,),
    ('APP_CONFIG_DB_PATH', 'config-value', 5888,),
    ('APP_CONFIG_DB_PATH', '192.168.0.1', 5889,),
    ('APP_HOST', 'sample-value', 5890,),
    ('APP_HOST', 'config-value', 5891,),
    ('APP_HOST', '192.168.0.1', 5892,),
    ('AUTO_TUNING_ENABLED', True, 5893,),
    ('AUTO_TUNING_ENABLED', False, 5894,),
    ('BLOOM_FILTER_CAPACITY', 'sample-value', 5895,),
    ('BLOOM_FILTER_CAPACITY', 'config-value', 5896,),
    ('BLOOM_FILTER_CAPACITY', '192.168.0.1', 5897,),
    ('BLOOM_FILTER_ERROR_RATE', 'sample-value', 5898,),
    ('BLOOM_FILTER_ERROR_RATE', 'config-value', 5899,),
    ('BLOOM_FILTER_ERROR_RATE', '192.168.0.1', 5900,),
    ('CACHE_MAX_SIZE', 25, 5901,),
    ('CACHE_MAX_SIZE', 50, 5902,),
    ('CACHE_MAX_SIZE', 100, 5903,),
    ('CACHE_MAX_SIZE', 250, 5904,),
    ('CACHE_MAX_SIZE', 500, 5905,),
    ('CACHE_TTL_SECONDS', 25, 5906,),
    ('CACHE_TTL_SECONDS', 50, 5907,),
    ('CACHE_TTL_SECONDS', 100, 5908,),
    ('CACHE_TTL_SECONDS', 250, 5909,),
    ('CACHE_TTL_SECONDS', 500, 5910,),
    ('CRITICAL_PHRASES_DB_PATH', 'sample-value', 5911,),
    ('CRITICAL_PHRASES_DB_PATH', 'config-value', 5912,),
    ('CRITICAL_PHRASES_DB_PATH', '192.168.0.1', 5913,),
    ('CUSTOM_WORDS_PATH', 'sample-value', 5914,),
    ('CUSTOM_WORDS_PATH', 'config-value', 5915,),
    ('CUSTOM_WORDS_PATH', '192.168.0.1', 5916,),
    ('CUSTOM_WORDS_STORAGE', 'sample-value', 5917,),
    ('CUSTOM_WORDS_STORAGE', 'config-value', 5918,),
    ('CUSTOM_WORDS_STORAGE', '192.168.0.1', 5919,),
    ('DETECTOR_THREAD_POOL_SIZE', 25, 5920,),
    ('DETECTOR_THREAD_POOL_SIZE', 50, 5921,),
    ('ENABLE_BADWORDS_PY', True, 5922,),
    ('ENABLE_BADWORDS_PY', False, 5923,),
    ('ENABLE_DETECTOR_AHO_CORASICK', True, 5924,),
    ('ENABLE_DETECTOR_AHO_CORASICK', False, 5925,),
    ('ENABLE_DETECTOR_BK_TREE', True, 5926,),
    ('ENABLE_DETECTOR_BK_TREE', False, 5927,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', True, 5928,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', False, 5929,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', True, 5930,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', False, 5931,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', True, 5932,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', False, 5933,),
    ('ENABLE_DETECTOR_ROLLING_HASH', True, 5934,),
    ('ENABLE_DETECTOR_ROLLING_HASH', False, 5935,),
    ('ENABLE_GANGAJAL', True, 5936,),
    ('ENABLE_GANGAJAL', False, 5937,),
    ('ENABLE_GLIN_PROFANITY', True, 5938,),
    ('ENABLE_GLIN_PROFANITY', False, 5939,),
    ('ENABLE_PHRASE_DETECTOR', True, 5940,),
    ('ENABLE_PHRASE_DETECTOR', False, 5941,),
    ('ENABLE_PROFANITE', True, 5942,),
    ('ENABLE_PROFANITE', False, 5943,),
    ('ENABLE_PROFANITY_FILTER', True, 5944,),
    ('ENABLE_PROFANITY_FILTER', False, 5945,),
    ('ENABLE_PYPROFANE', True, 5946,),
    ('ENABLE_PYPROFANE', False, 5947,),
    ('ENABLE_SAFETEXT', True, 5948,),
    ('ENABLE_SAFETEXT', False, 5949,),
    ('ENABLE_SENSITIVE_STOP_WORDS', True, 5950,),
    ('ENABLE_SENSITIVE_STOP_WORDS', False, 5951,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', True, 5952,),
    ('ENABLE_SENSITIVE_STOP_WORDS_AD', False, 5953,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', True, 5954,),
    ('ENABLE_SENSITIVE_STOP_WORDS_GUN', False, 5955,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', True, 5956,),
    ('ENABLE_SENSITIVE_STOP_WORDS_POLITICAL', False, 5957,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', True, 5958,),
    ('ENABLE_SENSITIVE_STOP_WORDS_PORN', False, 5959,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', True, 5960,),
    ('ENABLE_SENSITIVE_STOP_WORDS_URL', False, 5961,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', True, 5962,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', False, 5963,),
    ('EXPORT_RETENTION_DAYS', 25, 5964,),
    ('EXPORT_RETENTION_DAYS', 50, 5965,),
    ('EXPORT_RETENTION_DAYS', 100, 5966,),
    ('EXPORT_RETENTION_DAYS', 250, 5967,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', True, 5968,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', False, 5969,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', True, 5970,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', False, 5971,),
    ('FRONTEND_DIST_PATH', 'sample-value', 5972,),
    ('FRONTEND_DIST_PATH', 'config-value', 5973,),
    ('FRONTEND_DIST_PATH', '192.168.0.1', 5974,),
    ('FUZZY_MAX_DISTANCE', 'sample-value', 5975,),
    ('FUZZY_MAX_DISTANCE', 'config-value', 5976,),
    ('FUZZY_MAX_DISTANCE', '192.168.0.1', 5977,),
    ('HF_ENDPOINT', 'sample-value', 5978,),
    ('HF_ENDPOINT', 'config-value', 5979,),
    ('HF_ENDPOINT', '192.168.0.1', 5980,),
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
