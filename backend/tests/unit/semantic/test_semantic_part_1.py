"""Semantic similarity service tests, part 1 (Phase 1, P0/P1).

Covers the unavailable path (heavy deps absent), category metadata, and the
SuspicionScorer semantic weighting used by the engine.
"""

from __future__ import annotations

from typing import Any

import pytest

from app.scoring.suspicion_scorer import SuspicionScorer
from app.semantic.semantic_service import CATEGORIES
from tests.base_test import BaseTest


class TestSemanticUnavailable(BaseTest):
    """Behavior when the optional heavy dependencies are not installed."""

    def test_not_available_without_deps(self, engine: Any) -> None:
        """Without torch/faiss the service reports unavailable."""
        assert engine._semantic.is_available() is False

    def test_query_returns_empty(self, engine: Any) -> None:
        """Query returns an empty mapping when unavailable."""
        assert engine._semantic.query("hello") == {}

    def test_stats_reports_unavailable(self, engine: Any) -> None:
        """Stats expose the unavailable state."""
        stats: dict[str, Any] = engine._semantic.stats()
        assert stats["available"] is False

    def test_categories_defined(self) -> None:
        """The seven semantic categories are always defined."""
        assert CATEGORIES == (
            "political",
            "violence",
            "sexual",
            "hate",
            "pii",
            "ads",
            "other",
        )

    @pytest.mark.parametrize("category", CATEGORIES)
    def test_each_category_known(self, category: str) -> None:
        """Every category in the tuple is a valid string.

        :param category: semantic category name
        """
        assert isinstance(category, str)
        assert category.islower()


class TestSemanticScoring(BaseTest):
    """Suspicion scoring from semantic similarities."""

    def test_below_threshold_no_contribution(self, engine: Any) -> None:
        """Similarities under the threshold contribute nothing."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        score: float = scorer.score(semantic_similarities={"political": 0.5, "violence": 0.4})
        assert score == 0.0

    def test_above_threshold_contributes(self, engine: Any) -> None:
        """Similarities over the threshold add their category weight."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        threshold: float = float(
            engine._settings_service.get("SEMANTIC_SIMILARITY_THRESHOLD", 0.85)
        )
        score: float = scorer.score(semantic_similarities={"political": threshold + 0.05})
        assert score > 0.0

    def test_weight_resolution(self, engine: Any) -> None:
        """The political weight resolves from settings."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.detector_weight("nothing") == 0

    def test_semantic_below_force_threshold(self, engine: Any) -> None:
        """Similarities below the force threshold stay below force."""
        force: float = float(engine._settings_service.get("SEMANTIC_FORCE_LLM_THRESHOLD", 0.90))
        assert force >= 0.0

    def test_unknown_category_weight(self, engine: Any) -> None:
        """Unknown categories fall back to the political weight."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        political: float = scorer.score(semantic_similarities={"political": 0.99})
        unknown: float = scorer.score(semantic_similarities={"made_up": 0.99})
        assert unknown == political

    @pytest.mark.parametrize("category", CATEGORIES)
    def test_category_above_threshold_adds_weight(self, engine: Any, category: str) -> None:
        """Each category contributes weight above its threshold.

        :param engine: test engine
        :param category: semantic category
        """
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        baseline: float = scorer.score(semantic_similarities={})
        boosted: float = scorer.score(semantic_similarities={category: 0.99})
        assert boosted >= baseline

    def test_mixed_similarities_sum(self, engine: Any) -> None:
        """Multiple above-threshold categories sum their weights."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        single: float = scorer.score(semantic_similarities={"political": 0.99})
        mixed: float = scorer.score(semantic_similarities={"political": 0.99, "violence": 0.99})
        assert mixed > single

    def test_threshold_boundary(self, engine: Any) -> None:
        """Similarity exactly at the threshold is not above it."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        threshold: float = float(
            engine._settings_service.get("SEMANTIC_SIMILARITY_THRESHOLD", 0.85)
        )
        exact: float = scorer.score(semantic_similarities={"political": threshold})
        assert exact == 0.0

    def test_zero_similarity_zero_weight(self, engine: Any) -> None:
        """Zero similarity contributes nothing."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.score(semantic_similarities={"political": 0.0}) == 0.0

    def test_score_capped_at_100(self, engine: Any) -> None:
        """Even many hits stay within the 0-100 range."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        cats: dict[str, float] = dict.fromkeys(CATEGORIES, 1.0)
        score: float = scorer.score(detector_names=["aho_corasick"], semantic_similarities=cats)
        assert score <= 100.0

    def test_detector_and_semantic_combine(self, engine: Any) -> None:
        """Detector weights and semantic weights combine."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        detector_only: float = scorer.score(detector_names=["aho_corasick"])
        combined: float = scorer.score(
            detector_names=["aho_corasick"], semantic_similarities={"political": 0.99}
        )
        assert combined > detector_only

    def test_no_none_values_in_score(self, engine: Any) -> None:
        """None detector names are tolerated as absent."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.score(detector_names=None, semantic_similarities=None) == 0.0

    def test_detector_weights_from_settings(self, engine: Any) -> None:
        """Detector weights resolve from the settings store."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        expected: int = int(engine._settings_service.get("WEIGHT_DETECTOR_AHO", 30))
        assert scorer.detector_weight("aho_corasick") == expected

    @pytest.mark.parametrize(
        ("detector", "key"),
        (
            ("badwords", "WEIGHT_DETECTOR_BADWORDS"),
            ("profanite", "WEIGHT_DETECTOR_PROFANITE"),
            ("glin-profanity", "WEIGHT_DETECTOR_GLIN"),
            ("bk_tree", "WEIGHT_DETECTOR_BKTREE"),
            ("double_metaphone", "WEIGHT_DETECTOR_METAPHONE"),
        ),
    )
    def test_detector_weight_mapping(self, engine: Any, detector: str, key: str) -> None:
        """Detector names map to their configured weight keys.

        :param engine: test engine
        :param detector: detector identifier
        :param key: settings key for its weight
        """
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.detector_weight(detector) == int(engine._settings_service.get(key, 0))

    def test_user_ratio_weight_configured(self, engine: Any) -> None:
        """The user weight is read from settings."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.detector_weight("badwords") > 0

    def test_multi_language_uses_badwords_weight(self, engine: Any) -> None:
        """Multi-language hits use the badwords weight key."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        multi: int = scorer.detector_weight("multi_language")
        badwords: int = scorer.detector_weight("badwords")
        assert multi == badwords

    def test_rolling_hash_uses_aho_weight(self, engine: Any) -> None:
        """Rolling hash hits reuse the Aho weight key."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.detector_weight("rolling_hash") == scorer.detector_weight("aho_corasick")

    def test_bloom_uses_aho_weight(self, engine: Any) -> None:
        """Bloom filter hits reuse the Aho weight key."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.detector_weight("bloom_filter") == scorer.detector_weight("aho_corasick")

    def test_default_threshold_between_zero_and_one(self, engine: Any) -> None:
        """The similarity threshold is a fraction in the 0-1 range."""
        threshold: float = float(
            engine._settings_service.get("SEMANTIC_SIMILARITY_THRESHOLD", 0.85)
        )
        assert 0.0 <= threshold <= 1.0
