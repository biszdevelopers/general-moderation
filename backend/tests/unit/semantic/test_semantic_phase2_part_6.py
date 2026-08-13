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
    service.query("warmup")
    return service


_SCORER_WEIGHT_MAPPING_CASES: tuple[tuple[str, str, int, int], ...] = (
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        45,
        2401,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        50,
        2402,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        5,
        2403,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        8,
        2404,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        10,
        2405,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        12,
        2406,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        15,
        2407,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        20,
        2408,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        25,
        2409,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        30,
        2410,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        35,
        2411,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        40,
        2412,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        45,
        2413,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        50,
        2414,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        5,
        2415,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        8,
        2416,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        10,
        2417,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        12,
        2418,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        15,
        2419,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        20,
        2420,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        25,
        2421,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        30,
        2422,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        35,
        2423,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        40,
        2424,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        45,
        2425,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        50,
        2426,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        5,
        2427,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        8,
        2428,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        10,
        2429,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        12,
        2430,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        15,
        2431,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        20,
        2432,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        25,
        2433,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        30,
        2434,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        35,
        2435,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        40,
        2436,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        45,
        2437,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        50,
        2438,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        5,
        2439,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        8,
        2440,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        10,
        2441,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        12,
        2442,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        15,
        2443,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        20,
        2444,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        25,
        2445,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        30,
        2446,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        35,
        2447,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        40,
        2448,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        45,
        2449,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        50,
        2450,
    ),
)


class TestScorerWeightMapping(BaseTest):
    """Detector weights resolve from their settings keys."""

    @pytest.mark.parametrize(
        (
            "detector",
            "key",
            "expected_value",
            "uid",
        ),
        _SCORER_WEIGHT_MAPPING_CASES,
    )
    def test_scorer_weight_mapping(
        self, engine: Any, detector: str, key: str, expected_value: int, uid: int
    ) -> None:
        """Detector weights resolve from their settings keys."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        scorer._settings.update({key: expected_value})
        weight = scorer.detector_weight(detector)
        assert weight == expected_value
        assert 0 <= weight <= 50


_CATEGORY_WEIGHT_CASES: tuple[tuple[str, float, int], ...] = (
    (
        "political",
        0.5,
        2451,
    ),
    (
        "political",
        0.84,
        2452,
    ),
    (
        "political",
        0.86,
        2453,
    ),
    (
        "political",
        0.95,
        2454,
    ),
    (
        "violence",
        0.5,
        2455,
    ),
    (
        "violence",
        0.84,
        2456,
    ),
    (
        "violence",
        0.86,
        2457,
    ),
    (
        "violence",
        0.95,
        2458,
    ),
    (
        "sexual",
        0.5,
        2459,
    ),
    (
        "sexual",
        0.84,
        2460,
    ),
    (
        "sexual",
        0.86,
        2461,
    ),
    (
        "sexual",
        0.95,
        2462,
    ),
    (
        "hate",
        0.5,
        2463,
    ),
    (
        "hate",
        0.84,
        2464,
    ),
    (
        "hate",
        0.86,
        2465,
    ),
    (
        "hate",
        0.95,
        2466,
    ),
    (
        "pii",
        0.5,
        2467,
    ),
    (
        "pii",
        0.84,
        2468,
    ),
    (
        "pii",
        0.86,
        2469,
    ),
    (
        "pii",
        0.95,
        2470,
    ),
    (
        "ads",
        0.5,
        2471,
    ),
    (
        "ads",
        0.84,
        2472,
    ),
    (
        "ads",
        0.86,
        2473,
    ),
    (
        "ads",
        0.95,
        2474,
    ),
    (
        "other",
        0.5,
        2475,
    ),
    (
        "other",
        0.84,
        2476,
    ),
    (
        "other",
        0.86,
        2477,
    ),
    (
        "other",
        0.95,
        2478,
    ),
)


class TestCategoryWeight(BaseTest):
    """Above-threshold categories boost the score."""

    @pytest.mark.parametrize(
        (
            "category",
            "similarity",
            "uid",
        ),
        _CATEGORY_WEIGHT_CASES,
    )
    def test_category_weight(self, engine: Any, category: str, similarity: float, uid: int) -> None:
        """Above-threshold categories boost the score."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        threshold = float(scorer._settings.get("SEMANTIC_SIMILARITY_THRESHOLD", 0.85))
        baseline = scorer.score(semantic_similarities={})
        boosted = scorer.score(semantic_similarities={category: similarity})
        if similarity > threshold:
            assert boosted > baseline
        else:
            assert boosted == baseline
        assert boosted <= 100.0


_AVAILABILITY_CASES: tuple[tuple[bool, int, int], ...] = (
    (
        True,
        1,
        2479,
    ),
    (
        False,
        1,
        2480,
    ),
    (
        True,
        2,
        2481,
    ),
    (
        False,
        2,
        2482,
    ),
    (
        True,
        3,
        2483,
    ),
    (
        False,
        3,
        2484,
    ),
    (
        True,
        4,
        2485,
    ),
    (
        False,
        4,
        2486,
    ),
    (
        True,
        5,
        2487,
    ),
    (
        False,
        5,
        2488,
    ),
    (
        True,
        6,
        2489,
    ),
    (
        False,
        6,
        2490,
    ),
    (
        True,
        7,
        2491,
    ),
    (
        False,
        7,
        2492,
    ),
    (
        True,
        8,
        2493,
    ),
    (
        False,
        8,
        2494,
    ),
    (
        True,
        9,
        2495,
    ),
    (
        False,
        9,
        2496,
    ),
    (
        True,
        10,
        2497,
    ),
    (
        False,
        10,
        2498,
    ),
    (
        True,
        11,
        2499,
    ),
    (
        False,
        11,
        2500,
    ),
)


class TestAvailability(BaseTest):
    """The enable toggle drives availability and query results."""

    @pytest.mark.parametrize(
        (
            "enabled",
            "top_k",
            "uid",
        ),
        _AVAILABILITY_CASES,
    )
    def test_availability(
        self, settings: Any, fake_semantic_modules: None, enabled: bool, top_k: int, uid: int
    ) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = enabled
        settings.semantic_top_k = top_k
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is enabled
        result = service.query("anything")
        if enabled:
            assert set(result.keys()) == set(CATEGORIES)
        else:
            assert result == {}
