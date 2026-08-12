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


_SCORER_WEIGHT_MAPPING_CASES: tuple[tuple[str, str, int], ...] = (
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2401,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2402,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2403,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2404,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2405,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2406,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2407,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2408,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2409,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2410,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2411,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2412,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2413,
    ),
    (
        "double_metaphone",
        "WEIGHT_DETECTOR_METAPHONE",
        2414,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2415,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2416,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2417,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2418,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2419,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2420,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2421,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2422,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2423,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2424,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2425,
    ),
    (
        "multi_language",
        "WEIGHT_DETECTOR_BADWORDS",
        2426,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2427,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2428,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2429,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2430,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2431,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2432,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2433,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2434,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2435,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2436,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2437,
    ),
    (
        "rolling_hash",
        "WEIGHT_DETECTOR_AHO",
        2438,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2439,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2440,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2441,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2442,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2443,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2444,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2445,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2446,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2447,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2448,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2449,
    ),
    (
        "bloom_filter",
        "WEIGHT_DETECTOR_AHO",
        2450,
    ),
)


class TestScorerWeightMapping(BaseTest):
    """Detector weights resolve from their settings keys."""

    @pytest.mark.parametrize(
        (
            "detector",
            "key",
            "uid",
        ),
        _SCORER_WEIGHT_MAPPING_CASES,
    )
    def test_scorer_weight_mapping(self, engine: Any, detector: str, key: str, uid: int) -> None:
        """Detector weights resolve from their settings keys."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        weight = scorer.detector_weight(detector)
        expected = int(engine._settings_service.get(key, 0))
        assert weight == expected
        assert 0 <= weight <= 50


_CATEGORY_WEIGHT_CASES: tuple[tuple[str, int], ...] = (
    (
        "political",
        2451,
    ),
    (
        "political",
        2452,
    ),
    (
        "political",
        2453,
    ),
    (
        "political",
        2454,
    ),
    (
        "violence",
        2455,
    ),
    (
        "violence",
        2456,
    ),
    (
        "violence",
        2457,
    ),
    (
        "violence",
        2458,
    ),
    (
        "sexual",
        2459,
    ),
    (
        "sexual",
        2460,
    ),
    (
        "sexual",
        2461,
    ),
    (
        "sexual",
        2462,
    ),
    (
        "hate",
        2463,
    ),
    (
        "hate",
        2464,
    ),
    (
        "hate",
        2465,
    ),
    (
        "hate",
        2466,
    ),
    (
        "pii",
        2467,
    ),
    (
        "pii",
        2468,
    ),
    (
        "pii",
        2469,
    ),
    (
        "pii",
        2470,
    ),
    (
        "ads",
        2471,
    ),
    (
        "ads",
        2472,
    ),
    (
        "ads",
        2473,
    ),
    (
        "ads",
        2474,
    ),
    (
        "other",
        2475,
    ),
    (
        "other",
        2476,
    ),
    (
        "other",
        2477,
    ),
    (
        "other",
        2478,
    ),
)


class TestCategoryWeight(BaseTest):
    """Above-threshold categories boost the score."""

    @pytest.mark.parametrize(
        (
            "category",
            "uid",
        ),
        _CATEGORY_WEIGHT_CASES,
    )
    def test_category_weight(self, engine: Any, category: str, uid: int) -> None:
        """Above-threshold categories boost the score."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        baseline = scorer.score(semantic_similarities={})
        boosted = scorer.score(semantic_similarities={category: 0.99})
        assert boosted >= baseline
        assert boosted <= 100.0


class TestAvailabilityToggles(BaseTest):
    """AvailabilityToggles scenarios."""

    def test_availability_0_2479(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_1_2480(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_2_2481(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_3_2482(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_4_2483(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_5_2484(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_6_2485(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_7_2486(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_8_2487(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_9_2488(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_10_2489(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_11_2490(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_12_2491(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_13_2492(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_14_2493(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_15_2494(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_16_2495(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_17_2496(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_18_2497(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_19_2498(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_20_2499(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = True
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is True
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)

    def test_availability_21_2500(self, settings: Any, fake_semantic_modules: None) -> None:
        """The enable toggle drives availability and query results."""
        settings.semantic_enabled = False
        service: SemanticService = SemanticService(settings, None)
        assert service.is_available() is False
        result = service.query("anything")
        assert result == {} or set(result.keys()) == set(CATEGORIES)
