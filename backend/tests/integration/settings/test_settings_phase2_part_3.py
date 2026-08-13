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
    ('AI_TARGET_PERCENTAGE', 25, 5817,),
    ('AI_TARGET_PERCENTAGE', 50, 5818,),
    ('AI_TARGET_PERCENTAGE', 100, 5819,),
    ('ALLOWED_ORIGINS', 'sample-value', 5820,),
    ('ALLOWED_ORIGINS', 'config-value', 5821,),
    ('ALLOWED_ORIGINS', '192.168.0.1', 5822,),
    ('APP_CONFIG_DB_PATH', 'sample-value', 5823,),
    ('APP_CONFIG_DB_PATH', 'config-value', 5824,),
    ('APP_CONFIG_DB_PATH', '192.168.0.1', 5825,),
    ('APP_HOST', 'sample-value', 5826,),
    ('APP_HOST', 'config-value', 5827,),
    ('APP_HOST', '192.168.0.1', 5828,),
    ('AUTO_TUNING_ENABLED', True, 5829,),
    ('AUTO_TUNING_ENABLED', False, 5830,),
    ('BLOOM_FILTER_CAPACITY', 'sample-value', 5831,),
    ('BLOOM_FILTER_CAPACITY', 'config-value', 5832,),
    ('BLOOM_FILTER_CAPACITY', '192.168.0.1', 5833,),
    ('BLOOM_FILTER_ERROR_RATE', 'sample-value', 5834,),
    ('BLOOM_FILTER_ERROR_RATE', 'config-value', 5835,),
    ('BLOOM_FILTER_ERROR_RATE', '192.168.0.1', 5836,),
    ('CACHE_MAX_SIZE', 25, 5837,),
    ('CACHE_MAX_SIZE', 50, 5838,),
    ('CACHE_MAX_SIZE', 100, 5839,),
    ('CACHE_MAX_SIZE', 250, 5840,),
    ('CACHE_MAX_SIZE', 500, 5841,),
    ('CACHE_TTL_SECONDS', 25, 5842,),
    ('CACHE_TTL_SECONDS', 50, 5843,),
    ('CACHE_TTL_SECONDS', 100, 5844,),
    ('CACHE_TTL_SECONDS', 250, 5845,),
    ('CACHE_TTL_SECONDS', 500, 5846,),
    ('CUSTOM_WORDS_PATH', 'sample-value', 5847,),
    ('CUSTOM_WORDS_PATH', 'config-value', 5848,),
    ('CUSTOM_WORDS_PATH', '192.168.0.1', 5849,),
    ('CUSTOM_WORDS_STORAGE', 'sample-value', 5850,),
    ('CUSTOM_WORDS_STORAGE', 'config-value', 5851,),
    ('CUSTOM_WORDS_STORAGE', '192.168.0.1', 5852,),
    ('DETECTOR_THREAD_POOL_SIZE', 25, 5853,),
    ('DETECTOR_THREAD_POOL_SIZE', 50, 5854,),
    ('ENABLE_BADWORDS_PY', True, 5855,),
    ('ENABLE_BADWORDS_PY', False, 5856,),
    ('ENABLE_GANGAJAL', True, 5857,),
    ('ENABLE_GANGAJAL', False, 5858,),
    ('ENABLE_GLIN_PROFANITY', True, 5859,),
    ('ENABLE_GLIN_PROFANITY', False, 5860,),
    ('ENABLE_PROFANITE', True, 5861,),
    ('ENABLE_PROFANITE', False, 5862,),
    ('ENABLE_PROFANITY_FILTER', True, 5863,),
    ('ENABLE_PROFANITY_FILTER', False, 5864,),
    ('ENABLE_PYPROFANE', True, 5865,),
    ('ENABLE_PYPROFANE', False, 5866,),
    ('ENABLE_SAFETEXT', True, 5867,),
    ('ENABLE_SAFETEXT', False, 5868,),
    ('ENABLE_SENSITIVE_STOP_WORDS', True, 5869,),
    ('ENABLE_SENSITIVE_STOP_WORDS', False, 5870,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', True, 5871,),
    ('ENABLE_SENSITIVE_WORD_FILTER_CN', False, 5872,),
    ('EXPORT_RETENTION_DAYS', 25, 5873,),
    ('EXPORT_RETENTION_DAYS', 50, 5874,),
    ('EXPORT_RETENTION_DAYS', 100, 5875,),
    ('EXPORT_RETENTION_DAYS', 250, 5876,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', True, 5877,),
    ('FORCE_LLM_ON_SEMANTIC_HIGH', False, 5878,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', True, 5879,),
    ('FORCE_LLM_ON_USER_RATIO_HIGH', False, 5880,),
    ('FRONTEND_DIST_PATH', 'sample-value', 5881,),
    ('FRONTEND_DIST_PATH', 'config-value', 5882,),
    ('FRONTEND_DIST_PATH', '192.168.0.1', 5883,),
    ('FUZZY_MAX_DISTANCE', 'sample-value', 5884,),
    ('FUZZY_MAX_DISTANCE', 'config-value', 5885,),
    ('FUZZY_MAX_DISTANCE', '192.168.0.1', 5886,),
    ('HF_ENDPOINT', 'sample-value', 5887,),
    ('HF_ENDPOINT', 'config-value', 5888,),
    ('HF_ENDPOINT', '192.168.0.1', 5889,),
    ('HF_MIRROR', 'sample-value', 5890,),
    ('HF_MIRROR', 'config-value', 5891,),
    ('HF_MIRROR', '192.168.0.1', 5892,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 25, 5893,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 50, 5894,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 100, 5895,),
    ('LLM_RESPONSE_TIMEOUT_SECONDS', 250, 5896,),
    ('LOG_BACKUP_COUNT', 25, 5897,),
    ('LOG_BACKUP_COUNT', 50, 5898,),
    ('LOG_BACKUP_COUNT', 100, 5899,),
    ('LOG_FILE_PATH', 'sample-value', 5900,),
    ('LOG_FILE_PATH', 'config-value', 5901,),
    ('LOG_FILE_PATH', '192.168.0.1', 5902,),
    ('LOG_LEVEL', 'sample-value', 5903,),
    ('LOG_LEVEL', 'config-value', 5904,),
    ('LOG_LEVEL', '192.168.0.1', 5905,),
    ('LOG_RETENTION_DAYS', 25, 5906,),
    ('LOG_RETENTION_DAYS', 50, 5907,),
    ('LOG_RETENTION_DAYS', 100, 5908,),
    ('LOG_RETENTION_DAYS', 250, 5909,),
    ('MAX_BATCH_SIZE', 25, 5910,),
    ('MAX_BATCH_SIZE', 50, 5911,),
    ('MAX_BATCH_SIZE', 100, 5912,),
    ('MAX_BATCH_SIZE', 250, 5913,),
    ('MAX_BATCH_SIZE', 500, 5914,),
    ('METRICS_ENABLED', 'sample-value', 5915,),
    ('METRICS_ENABLED', 'config-value', 5916,),
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
