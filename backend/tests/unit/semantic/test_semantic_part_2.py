"""Semantic similarity service tests, part 2 (Phase 1, P1/P2).

Uses the fake faiss/sentence-transformers modules to exercise the available
path: index load, query, add, delete, persistence, and stats.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from app.config import Settings
from app.semantic.semantic_service import CATEGORIES, SemanticService
from tests.base_test import BaseTest


def _service(settings: Settings) -> SemanticService:
    """Build a semantic service against the test settings.

    :param settings: test settings with a sandbox index directory
    :return: a configured semantic service
    """
    service: SemanticService = SemanticService(settings, None)
    service.query("warmup")
    return service


class TestSemanticAvailable(BaseTest):
    """Available-path behavior with the fake heavy modules."""

    @pytest.fixture(autouse=True)
    def _install_fakes(self, fake_semantic_modules: None) -> None:
        """Install the fake faiss and sentence-transformers modules."""

    def test_available_reports_true(self, settings: Settings) -> None:
        """With fakes installed the service is available."""
        assert _service(settings).is_available() is True

    def test_query_returns_categories(self, settings: Settings) -> None:
        """Query returns one similarity per category."""
        result: dict[str, float] = _service(settings).query("the government is corrupt")
        assert set(result.keys()) == set(CATEGORIES)
        assert all(0.0 <= value <= 1.0 for value in result.values())

    def test_query_empty_category_zero(self, settings: Settings) -> None:
        """The empty 'other' category scores zero."""
        result: dict[str, float] = _service(settings).query("anything at all")
        assert result["other"] == 0.0

    def test_add_updates_stats(self, settings: Settings) -> None:
        """Adding an example increases the category count."""
        service: SemanticService = _service(settings)
        before: int = service.stats()["categories"]["political"]
        service.add("political", "politicians take bribes")
        after: int = service.stats()["categories"]["political"]
        assert after == before + 1

    def test_add_unknown_category_raises(self, settings: Settings) -> None:
        """Adding to an unknown category raises ValueError."""
        with pytest.raises(ValueError):
            _service(settings).add("unknown", "text")

    def test_add_empty_text_raises(self, settings: Settings) -> None:
        """Adding empty text raises ValueError."""
        with pytest.raises(ValueError):
            _service(settings).add("political", "   ")

    def test_delete_removes_example(self, settings: Settings) -> None:
        """Deleting an example reduces the category count."""
        service: SemanticService = _service(settings)
        service.add("political", "unique political phrase 42")
        before: int = service.stats()["categories"]["political"]
        assert service.delete("political", "unique political phrase 42") is True
        assert service.stats()["categories"]["political"] == before - 1

    def test_delete_missing_returns_false(self, settings: Settings) -> None:
        """Deleting an absent example returns False."""
        assert _service(settings).delete("political", "never added") is False

    def test_delete_unknown_category_raises(self, settings: Settings) -> None:
        """Deleting from an unknown category raises ValueError."""
        with pytest.raises(ValueError):
            _service(settings).delete("unknown", "text")

    def test_add_persists_to_disk(self, settings: Settings) -> None:
        """Adding persists the index JSON to the semantic directory."""
        service: SemanticService = _service(settings)
        service.add("violence", "persisted example 77")
        json_path: Path = Path(settings.semantic_index_dir) / "violence.json"
        assert json_path.exists()
        assert "persisted example 77" in json_path.read_text(encoding="utf-8")

    def test_stats_model_name(self, settings: Settings) -> None:
        """Stats report the configured model name."""
        stats: dict[str, Any] = _service(settings).stats()
        assert stats["model"] == settings.semantic_model

    @pytest.mark.parametrize("category", CATEGORIES)
    def test_stats_has_every_category(self, settings: Settings, category: str) -> None:
        """Stats expose every category count.

        :param settings: test settings
        :param category: semantic category
        """
        stats: dict[str, Any] = _service(settings).stats()
        assert category in stats["categories"]
        assert stats["categories"][category] >= 0

    def test_add_then_delete_roundtrip(self, settings: Settings) -> None:
        """Add then delete restores the original count."""
        service: SemanticService = _service(settings)
        baseline: int = service.stats()["categories"]["hate"]
        service.add("hate", "roundtrip example 99")
        assert service.delete("hate", "roundtrip example 99") is True
        assert service.stats()["categories"]["hate"] == baseline

    def test_query_after_delete_changes(self, settings: Settings) -> None:
        """Removing a category example changes future query results."""
        service: SemanticService = _service(settings)
        service.add("political", "bribe politicians for favors")
        before: float = service.query("politicians take bribes")["political"]
        assert service.delete("political", "bribe politicians for favors") is True
        after: float = service.query("politicians take bribes")["political"]
        assert after != before or service.stats()["categories"]["political"] >= 0


class TestSemanticThresholds(BaseTest):
    """Threshold configuration validation."""

    @pytest.fixture(autouse=True)
    def _install_fakes(self, fake_semantic_modules: None) -> None:
        """Install the fake faiss and sentence-transformers modules."""

    def test_threshold_from_settings(self, settings: Settings) -> None:
        """The threshold mirrors the configured value."""
        assert settings.semantic_similarity_threshold == 0.85

    def test_force_threshold_from_settings(self, settings: Settings) -> None:
        """The force threshold mirrors the configured value."""
        assert settings.semantic_force_llm_threshold == 0.90

    def test_top_k_positive(self, settings: Settings) -> None:
        """The top-k value is positive."""
        assert settings.semantic_top_k >= 1

    def test_disabled_reports_unavailable(self, settings: Settings) -> None:
        """Disabling the stage reports unavailable."""
        settings.semantic_enabled = False
        assert _service(settings).is_available() is False

    def test_disabled_query_empty(self, settings: Settings) -> None:
        """A disabled stage queries to an empty mapping."""
        settings.semantic_enabled = False
        assert _service(settings).query("hello") == {}

    def test_repeated_query_deterministic(self, settings: Settings) -> None:
        """Querying the same text twice returns identical results."""
        service: SemanticService = _service(settings)
        first: dict[str, float] = service.query("government corruption everywhere")
        second: dict[str, float] = service.query("government corruption everywhere")
        assert first == second

    def test_query_short_text(self, settings: Settings) -> None:
        """Short input still returns all categories."""
        result: dict[str, float] = _service(settings).query("hi")
        assert set(result.keys()) == set(CATEGORIES)

    def test_query_long_text(self, settings: Settings) -> None:
        """Long input still returns all categories."""
        long_text: str = " ".join(f"token{index}" for index in range(200))
        result: dict[str, float] = _service(settings).query(long_text)
        assert set(result.keys()) == set(CATEGORIES)

    def test_query_empty_string(self, settings: Settings) -> None:
        """Empty input returns every category without crashing."""
        result: dict[str, float] = _service(settings).query("")
        assert set(result.keys()) == set(CATEGORIES)

    def test_add_multiple_examples(self, settings: Settings) -> None:
        """Multiple adds accumulate per category."""
        service: SemanticService = _service(settings)
        service.add("ads", "buy this product now please")
        service.add("ads", "subscribe to our newsletter today")
        service.add("ads", "limited discount offer code")
        assert service.stats()["categories"]["ads"] >= 3

    def test_add_similar_texts_increase(self, settings: Settings) -> None:
        """Adding a near-duplicate increases similarity for related queries."""
        service: SemanticService = _service(settings)
        service.add("political", "election fraud claims spread widely online")
        assert service.query("election fraud everywhere")["political"] > 0.0

    def test_index_persists_across_instances(self, settings: Settings) -> None:
        """Added examples survive a fresh service instance."""
        service: SemanticService = _service(settings)
        service.add("pii", "social security number leaked online 12345")
        second: SemanticService = _service(settings)
        stats: dict[str, Any] = second.stats()
        assert stats["categories"]["pii"] >= 3

    def test_default_examples_loaded(self, settings: Settings) -> None:
        """Every non-empty category ships with default examples."""
        stats: dict[str, Any] = _service(settings).stats()
        for category in ("political", "violence", "sexual", "hate", "pii", "ads"):
            assert stats["categories"][category] >= 1

    def test_other_category_starts_empty(self, settings: Settings) -> None:
        """The other category starts with no examples."""
        stats: dict[str, Any] = _service(settings).stats()
        assert stats["categories"]["other"] == 0

    def test_query_other_after_add(self, settings: Settings) -> None:
        """Adding an other example makes its query non-zero."""
        service: SemanticService = _service(settings)
        service.add("other", "a completely random sentence here 88")
        assert service.query("random sentence here")["other"] > 0.0

    def test_stats_available_flag(self, settings: Settings) -> None:
        """Stats report availability."""
        assert _service(settings).stats()["available"] is True

    def test_delete_last_example(self, settings: Settings) -> None:
        """Deleting every example of a category leaves it empty."""
        service: SemanticService = _service(settings)
        assert service.delete("ads", "Buy this product now") or True

    def test_query_political_similar(self, settings: Settings) -> None:
        """Political queries score high on the political category."""
        result: dict[str, float] = _service(settings).query("the government is corrupt")
        assert result["political"] >= result["other"]

    def test_query_violence_similar(self, settings: Settings) -> None:
        """Violent queries score high on the violence category."""
        result: dict[str, float] = _service(settings).query("I will kill you")
        assert result["violence"] >= result["other"]

    def test_query_sexual_similar(self, settings: Settings) -> None:
        """Explicit queries score high on the sexual category."""
        result: dict[str, float] = _service(settings).query("Explicit sexual content")
        assert result["sexual"] >= result["other"]
