"""Phase 2 semantic similarity tests (generated).

Threshold sweeps, category query matrices, add/delete roundtrips and
weight mappings; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from typing import Any

import pytest

from app.scoring.suspicion_scorer import SuspicionScorer
from app.semantic.semantic_service import CATEGORIES, SemanticService
from tests.base_test import BaseTest


def _service(settings: Any) -> SemanticService:
    """Build a semantic service against the test settings."""
    service: SemanticService = SemanticService(settings, None)
    service.query('warmup')
    return service

_DELETE_ROUNDTRIP_CASES: tuple[tuple[str, int, int], ...] = (
    ('other', 2, 2301,),
    ('other', 3, 2303,),
    ('other', 5, 2305,),
    ('other', 10, 2307,),
    ('other', 15, 2309,),
    ('other', 20, 2311,),
    ('other', 25, 2313,),
)

class TestDeleteRoundtrip(BaseTest):
    """Deleting added examples restores the baseline count."""

    @pytest.mark.parametrize(('category', 'count', 'uid',), _DELETE_ROUNDTRIP_CASES)
    def test_delete_roundtrip(self, settings: Any, fake_semantic_modules: None, category: str, count: int, uid: int) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()['categories'][category]
        example = f'unique example phrase {category}_{count}'
        for _offset in range(count):
            service.add(category, example)
        for _offset in range(count):
            assert service.delete(category, example) is True
        assert service.stats()['categories'][category] == baseline


_ADD_COUNT_CASES: tuple[tuple[str, int, int], ...] = (
    ('other', 3, 2302,),
    ('other', 5, 2304,),
    ('other', 10, 2306,),
    ('other', 15, 2308,),
    ('other', 20, 2310,),
    ('other', 25, 2312,),
)

class TestAddCount(BaseTest):
    """Adding examples increments the category count."""

    @pytest.mark.parametrize(('category', 'count', 'uid',), _ADD_COUNT_CASES)
    def test_add_count(self, settings: Any, fake_semantic_modules: None, category: str, count: int, uid: int) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()['categories'][category]
        example = f'unique example phrase {category}_{count}'
        for _offset in range(count):
            service.add(category, example)
        after = service.stats()['categories'][category]
        assert after == before + count


_STATS_FIELD_CASES: tuple[tuple[str, str, int], ...] = (
    ('political', 'categories', 2314,),
    ('political', 'model', 2315,),
    ('political', 'available', 2316,),
    ('political', 'top_k', 2317,),
    ('violence', 'categories', 2318,),
    ('violence', 'model', 2319,),
    ('violence', 'available', 2320,),
    ('violence', 'top_k', 2321,),
    ('sexual', 'categories', 2322,),
    ('sexual', 'model', 2323,),
    ('sexual', 'available', 2324,),
    ('sexual', 'top_k', 2325,),
    ('hate', 'categories', 2326,),
    ('hate', 'model', 2327,),
    ('hate', 'available', 2328,),
    ('hate', 'top_k', 2329,),
    ('pii', 'categories', 2330,),
    ('pii', 'model', 2331,),
    ('pii', 'available', 2332,),
    ('pii', 'top_k', 2333,),
    ('ads', 'categories', 2334,),
    ('ads', 'model', 2335,),
    ('ads', 'available', 2336,),
    ('ads', 'top_k', 2337,),
    ('other', 'categories', 2338,),
    ('other', 'model', 2339,),
    ('other', 'available', 2340,),
    ('other', 'top_k', 2341,),
)

class TestStatsField(BaseTest):
    """Stats expose every category with a non-negative count."""

    @pytest.mark.parametrize(('category', 'stat_key', 'uid',), _STATS_FIELD_CASES)
    def test_stats_field(self, settings: Any, fake_semantic_modules: None, category: str, stat_key: str, uid: int) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats['available'] is True
        if stat_key == 'categories':
            assert stats['categories'][category] >= 0
        elif stat_key == 'model':
            assert stats['model'] == settings.semantic_model
        elif stat_key == 'available':
            assert stats['available'] is True
        else:
            assert settings.semantic_top_k >= 1


_TOP_K_CASES: tuple[tuple[int, int], ...] = (
    (1, 2342,),
    (2, 2343,),
    (3, 2344,),
    (5, 2345,),
    (8, 2346,),
    (10, 2347,),
    (16, 2348,),
    (25, 2349,),
    (32, 2350,),
    (50, 2351,),
    (64, 2352,),
    (100, 2353,),
    (128, 2354,),
)

class TestTopK(BaseTest):
    """Every supported top-k initializes the service cleanly."""

    @pytest.mark.parametrize(('top_k', 'uid',), _TOP_K_CASES)
    def test_top_k(self, settings: Any, fake_semantic_modules: None, top_k: int, uid: int) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = top_k
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query('sample query text')
        assert set(result.keys()) == set(CATEGORIES)


_SCORER_WEIGHT_MAPPING_CASES: tuple[tuple[str, str, int, int], ...] = (
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 5, 2355,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 8, 2356,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 10, 2357,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 12, 2358,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 15, 2359,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 20, 2360,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 25, 2361,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 30, 2362,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 35, 2363,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 40, 2364,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 45, 2365,),
    ('badwords', 'WEIGHT_DETECTOR_BADWORDS', 50, 2366,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 5, 2367,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 8, 2368,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 10, 2369,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 12, 2370,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 15, 2371,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 20, 2372,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 25, 2373,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 30, 2374,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 35, 2375,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 40, 2376,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 45, 2377,),
    ('profanite', 'WEIGHT_DETECTOR_PROFANITE', 50, 2378,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 5, 2379,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 8, 2380,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 10, 2381,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 12, 2382,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 15, 2383,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 20, 2384,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 25, 2385,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 30, 2386,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 35, 2387,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 40, 2388,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 45, 2389,),
    ('glin-profanity', 'WEIGHT_DETECTOR_GLIN', 50, 2390,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 5, 2391,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 8, 2392,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 10, 2393,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 12, 2394,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 15, 2395,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 20, 2396,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 25, 2397,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 30, 2398,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 35, 2399,),
    ('bk_tree', 'WEIGHT_DETECTOR_BKTREE', 40, 2400,),
)

class TestScorerWeightMapping(BaseTest):
    """Detector weights resolve from their settings keys."""

    @pytest.mark.parametrize(('detector', 'key', 'expected_value', 'uid',), _SCORER_WEIGHT_MAPPING_CASES)
    def test_scorer_weight_mapping(self, engine: Any, detector: str, key: str, expected_value: int, uid: int) -> None:
        """Detector weights resolve from their settings keys."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        scorer._settings.update({key: expected_value})
        weight = scorer.detector_weight(detector)
        assert weight == expected_value
        assert 0 <= weight <= 50
