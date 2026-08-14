"""Phase 2 runtime settings tests (generated).

Catalog metadata, read-only protection, probed valid/invalid matrices
and typed coercion; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from tests.base_test import BaseTest

_DESCRIBE_FIELD_CASES: tuple[tuple[str, str, int], ...] = (
    ('ADMIN_API_KEY', 'key', 5363,),
    ('ADMIN_API_KEY', 'value', 5364,),
    ('ADMIN_API_KEY', 'type', 5365,),
    ('ADMIN_API_KEY', 'editable', 5366,),
    ('AI_TARGET_PERCENTAGE', 'key', 5367,),
    ('AI_TARGET_PERCENTAGE', 'value', 5368,),
    ('AI_TARGET_PERCENTAGE', 'type', 5369,),
    ('AI_TARGET_PERCENTAGE', 'editable', 5370,),
    ('ALLOWED_ORIGINS', 'key', 5371,),
    ('ALLOWED_ORIGINS', 'value', 5372,),
    ('ALLOWED_ORIGINS', 'type', 5373,),
    ('ALLOWED_ORIGINS', 'editable', 5374,),
    ('APP_CONFIG_DB_PATH', 'key', 5375,),
    ('APP_CONFIG_DB_PATH', 'value', 5376,),
    ('APP_CONFIG_DB_PATH', 'type', 5377,),
    ('APP_CONFIG_DB_PATH', 'editable', 5378,),
    ('APP_HOST', 'key', 5379,),
    ('APP_HOST', 'value', 5380,),
    ('APP_HOST', 'type', 5381,),
    ('APP_HOST', 'editable', 5382,),
    ('APP_PORT', 'key', 5383,),
    ('APP_PORT', 'value', 5384,),
    ('APP_PORT', 'type', 5385,),
    ('APP_PORT', 'editable', 5386,),
    ('AUTO_TUNING_BATCH_HOUR', 'key', 5387,),
    ('AUTO_TUNING_BATCH_HOUR', 'value', 5388,),
    ('AUTO_TUNING_BATCH_HOUR', 'type', 5389,),
    ('AUTO_TUNING_BATCH_HOUR', 'editable', 5390,),
    ('AUTO_TUNING_ENABLED', 'key', 5391,),
    ('AUTO_TUNING_ENABLED', 'value', 5392,),
    ('AUTO_TUNING_ENABLED', 'type', 5393,),
    ('AUTO_TUNING_ENABLED', 'editable', 5394,),
    ('BLOOM_FILTER_CAPACITY', 'key', 5395,),
    ('BLOOM_FILTER_CAPACITY', 'value', 5396,),
    ('BLOOM_FILTER_CAPACITY', 'type', 5397,),
    ('BLOOM_FILTER_CAPACITY', 'editable', 5398,),
    ('BLOOM_FILTER_ERROR_RATE', 'key', 5399,),
    ('BLOOM_FILTER_ERROR_RATE', 'value', 5400,),
    ('BLOOM_FILTER_ERROR_RATE', 'type', 5401,),
    ('BLOOM_FILTER_ERROR_RATE', 'editable', 5402,),
    ('CACHE_MAX_SIZE', 'key', 5403,),
    ('CACHE_MAX_SIZE', 'value', 5404,),
    ('CACHE_MAX_SIZE', 'type', 5405,),
    ('CACHE_MAX_SIZE', 'editable', 5406,),
    ('CACHE_TTL_SECONDS', 'key', 5407,),
    ('CACHE_TTL_SECONDS', 'value', 5408,),
    ('CACHE_TTL_SECONDS', 'type', 5409,),
    ('CACHE_TTL_SECONDS', 'editable', 5410,),
    ('CRITICAL_PHRASES_DB_PATH', 'key', 5411,),
    ('CRITICAL_PHRASES_DB_PATH', 'value', 5412,),
    ('CRITICAL_PHRASES_DB_PATH', 'type', 5413,),
    ('CRITICAL_PHRASES_DB_PATH', 'editable', 5414,),
    ('CUSTOM_WORDS_PATH', 'key', 5415,),
    ('CUSTOM_WORDS_PATH', 'value', 5416,),
    ('CUSTOM_WORDS_PATH', 'type', 5417,),
    ('CUSTOM_WORDS_PATH', 'editable', 5418,),
    ('CUSTOM_WORDS_STORAGE', 'key', 5419,),
    ('CUSTOM_WORDS_STORAGE', 'value', 5420,),
    ('CUSTOM_WORDS_STORAGE', 'type', 5421,),
    ('CUSTOM_WORDS_STORAGE', 'editable', 5422,),
    ('DETECTOR_THREAD_POOL_SIZE', 'key', 5423,),
    ('DETECTOR_THREAD_POOL_SIZE', 'value', 5424,),
    ('DETECTOR_THREAD_POOL_SIZE', 'type', 5425,),
    ('DETECTOR_THREAD_POOL_SIZE', 'editable', 5426,),
    ('ENABLE_BADWORDS_PY', 'key', 5427,),
    ('ENABLE_BADWORDS_PY', 'value', 5428,),
    ('ENABLE_BADWORDS_PY', 'type', 5429,),
    ('ENABLE_BADWORDS_PY', 'editable', 5430,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'key', 5431,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'value', 5432,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'type', 5433,),
    ('ENABLE_DETECTOR_AHO_CORASICK', 'editable', 5434,),
    ('ENABLE_DETECTOR_BK_TREE', 'key', 5435,),
    ('ENABLE_DETECTOR_BK_TREE', 'value', 5436,),
    ('ENABLE_DETECTOR_BK_TREE', 'type', 5437,),
    ('ENABLE_DETECTOR_BK_TREE', 'editable', 5438,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'key', 5439,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'value', 5440,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'type', 5441,),
    ('ENABLE_DETECTOR_BLOOM_FILTER', 'editable', 5442,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'key', 5443,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'value', 5444,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'type', 5445,),
    ('ENABLE_DETECTOR_DOUBLE_METAPHONE', 'editable', 5446,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'key', 5447,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'value', 5448,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'type', 5449,),
    ('ENABLE_DETECTOR_MULTI_LANGUAGE', 'editable', 5450,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'key', 5451,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'value', 5452,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'type', 5453,),
    ('ENABLE_DETECTOR_ROLLING_HASH', 'editable', 5454,),
    ('ENABLE_GANGAJAL', 'key', 5455,),
    ('ENABLE_GANGAJAL', 'value', 5456,),
    ('ENABLE_GANGAJAL', 'type', 5457,),
    ('ENABLE_GANGAJAL', 'editable', 5458,),
    ('ENABLE_GLIN_PROFANITY', 'key', 5459,),
    ('ENABLE_GLIN_PROFANITY', 'value', 5460,),
    ('ENABLE_GLIN_PROFANITY', 'type', 5461,),
    ('ENABLE_GLIN_PROFANITY', 'editable', 5462,),
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
