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
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2355,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2356,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2357,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2358,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2359,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2360,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2361,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2362,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2363,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2364,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2365,
    ),
    (
        "badwords",
        "WEIGHT_DETECTOR_BADWORDS",
        2366,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2367,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2368,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2369,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2370,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2371,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2372,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2373,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2374,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2375,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2376,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2377,
    ),
    (
        "profanite",
        "WEIGHT_DETECTOR_PROFANITE",
        2378,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2379,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2380,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2381,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2382,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2383,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2384,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2385,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2386,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2387,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2388,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2389,
    ),
    (
        "glin-profanity",
        "WEIGHT_DETECTOR_GLIN",
        2390,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2391,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2392,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2393,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2394,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2395,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2396,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2397,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2398,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2399,
    ),
    (
        "bk_tree",
        "WEIGHT_DETECTOR_BKTREE",
        2400,
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


class TestDeleteRoundtrips(BaseTest):
    """DeleteRoundtrips scenarios."""

    def test_delete_roundtrip_other_2_2301(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["other"]
        for _offset in range(2):
            service.add("other", "unique example phrase 6_2")
        for _offset in range(2):
            assert service.delete("other", "unique example phrase 6_2") is True
        assert service.stats()["categories"]["other"] == baseline

    def test_delete_roundtrip_other_3_2303(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["other"]
        for _offset in range(3):
            service.add("other", "unique example phrase 6_3")
        for _offset in range(3):
            assert service.delete("other", "unique example phrase 6_3") is True
        assert service.stats()["categories"]["other"] == baseline

    def test_delete_roundtrip_other_5_2305(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["other"]
        for _offset in range(5):
            service.add("other", "unique example phrase 6_5")
        for _offset in range(5):
            assert service.delete("other", "unique example phrase 6_5") is True
        assert service.stats()["categories"]["other"] == baseline

    def test_delete_roundtrip_other_10_2307(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["other"]
        for _offset in range(10):
            service.add("other", "unique example phrase 6_10")
        for _offset in range(10):
            assert service.delete("other", "unique example phrase 6_10") is True
        assert service.stats()["categories"]["other"] == baseline

    def test_delete_roundtrip_other_15_2309(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["other"]
        for _offset in range(15):
            service.add("other", "unique example phrase 6_15")
        for _offset in range(15):
            assert service.delete("other", "unique example phrase 6_15") is True
        assert service.stats()["categories"]["other"] == baseline

    def test_delete_roundtrip_other_20_2311(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["other"]
        for _offset in range(20):
            service.add("other", "unique example phrase 6_20")
        for _offset in range(20):
            assert service.delete("other", "unique example phrase 6_20") is True
        assert service.stats()["categories"]["other"] == baseline

    def test_delete_roundtrip_other_25_2313(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Deleting added examples restores the baseline count."""
        service: SemanticService = _service(settings)
        baseline = service.stats()["categories"]["other"]
        for _offset in range(25):
            service.add("other", "unique example phrase 6_25")
        for _offset in range(25):
            assert service.delete("other", "unique example phrase 6_25") is True
        assert service.stats()["categories"]["other"] == baseline


class TestAddCounts(BaseTest):
    """AddCounts scenarios."""

    def test_add_count_other_3_2302(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["other"]
        for _offset in range(3):
            service.add("other", "unique example phrase 6_3")
        after = service.stats()["categories"]["other"]
        assert after == before + 3

    def test_add_count_other_5_2304(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["other"]
        for _offset in range(5):
            service.add("other", "unique example phrase 6_5")
        after = service.stats()["categories"]["other"]
        assert after == before + 5

    def test_add_count_other_10_2306(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["other"]
        for _offset in range(10):
            service.add("other", "unique example phrase 6_10")
        after = service.stats()["categories"]["other"]
        assert after == before + 10

    def test_add_count_other_15_2308(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["other"]
        for _offset in range(15):
            service.add("other", "unique example phrase 6_15")
        after = service.stats()["categories"]["other"]
        assert after == before + 15

    def test_add_count_other_20_2310(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["other"]
        for _offset in range(20):
            service.add("other", "unique example phrase 6_20")
        after = service.stats()["categories"]["other"]
        assert after == before + 20

    def test_add_count_other_25_2312(self, settings: Any, fake_semantic_modules: None) -> None:
        """Adding examples increments the category count."""
        service: SemanticService = _service(settings)
        before = service.stats()["categories"]["other"]
        for _offset in range(25):
            service.add("other", "unique example phrase 6_25")
        after = service.stats()["categories"]["other"]
        assert after == before + 25


class TestStatsFields(BaseTest):
    """StatsFields scenarios."""

    def test_stats_field_political_verify_2314(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["political"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_political_sample_2315(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["political"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_political_count_2316(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["political"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_political_shape_2317(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["political"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_violence_verify_2318(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["violence"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_violence_sample_2319(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["violence"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_violence_count_2320(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["violence"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_violence_shape_2321(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["violence"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_sexual_verify_2322(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["sexual"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_sexual_sample_2323(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["sexual"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_sexual_count_2324(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["sexual"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_sexual_shape_2325(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["sexual"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_hate_verify_2326(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["hate"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_hate_sample_2327(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["hate"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_hate_count_2328(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["hate"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_hate_shape_2329(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["hate"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_pii_verify_2330(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["pii"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_pii_sample_2331(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["pii"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_pii_count_2332(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["pii"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_pii_shape_2333(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["pii"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_ads_verify_2334(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["ads"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_ads_sample_2335(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["ads"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_ads_count_2336(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["ads"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_ads_shape_2337(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["ads"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_other_verify_2338(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["other"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_other_sample_2339(
        self, settings: Any, fake_semantic_modules: None
    ) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["other"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_other_count_2340(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["other"] >= 0
        assert settings.semantic_top_k >= 1

    def test_stats_field_other_shape_2341(self, settings: Any, fake_semantic_modules: None) -> None:
        """Stats expose every category with a non-negative count."""
        stats = _service(settings).stats()
        assert stats["available"] is True
        assert stats["model"] == settings.semantic_model
        assert stats["categories"]["other"] >= 0
        assert settings.semantic_top_k >= 1


class TestTopK(BaseTest):
    """TopK scenarios."""

    def test_top_k_1_2342(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 1
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_2_2343(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 2
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_3_2344(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 3
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_5_2345(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 5
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_8_2346(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 8
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_10_2347(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 10
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_16_2348(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 16
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_25_2349(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 25
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_32_2350(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 32
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_50_2351(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 50
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_64_2352(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 64
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_100_2353(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 100
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)

    def test_top_k_128_2354(self, settings: Any, fake_semantic_modules: None) -> None:
        """Every supported top-k initializes the service cleanly."""
        settings.semantic_top_k = 128
        service: SemanticService = _service(settings)
        assert service.is_available() is True
        result = service.query("sample query text")
        assert set(result.keys()) == set(CATEGORIES)
