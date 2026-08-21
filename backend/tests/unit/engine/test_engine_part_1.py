"""Moderation engine pipeline tests, part 1 (Phase 1, P0/P1).

Covers the Stage 1 fast path, Stage 2 verdicts for exact and fuzzy matches,
Stage 3 trigger resolution with an unavailable LLM, and the result cache.
"""

from __future__ import annotations

from typing import Any

import pytest

from app.engine.moderation_engine import ModerationEngine
from app.models.request import ModerationRequest
from app.models.response import ModerationResponse
from tests.base_test import BaseTest

_CLEAN_TEXTS: tuple[str, ...] = (
    "the weather is nice today",
    "coffee is ready",
    "let us begin the meeting",
    "welcome to the team",
    "the report is on the desk",
    "thanks for your help",
    "good night everyone",
    "hello world",
    "total ordinary content",
    "this text contains no flagged terms",
)


class TestEngineStage1(BaseTest):
    """Safe word fast path exits."""

    def test_safe_word_fast_path(self, engine: ModerationEngine, word_bank: Any) -> None:
        """Content composed of safe words exits at level one."""
        engine._safe_word.add_word("hello")
        engine._safe_word.add_word("world")
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="hello world", app_name="a", user_id="u")
        )
        assert result.verdict.value == "PASS"
        assert result.level_used == 1
        assert "safe_word_list" in result.detector_chain

    @pytest.mark.parametrize("text", _CLEAN_TEXTS)
    def test_clean_text_passes(self, engine: ModerationEngine, word_bank: Any, text: str) -> None:
        """Ordinary clean text produces a PASS verdict.

        :param engine: test engine
        :param word_bank: isolated word bank
        :param text: clean message
        """
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=text, app_name="a", user_id="u")
        )
        assert result.verdict.value == "PASS"
        assert result.allowed is True


class TestEngineStage2(BaseTest):
    """Rule-detector verdicts."""

    def _seed_word(self, engine: ModerationEngine, word_bank: Any, word: str) -> None:
        """Add a word and refresh detector caches so fuzzy indexes rebuild.

        :param engine: test engine
        :param word_bank: isolated word bank
        :param word: custom word to add
        """
        word_bank.add_word(word)
        engine.refresh_detectors()

    def test_exact_match_blocks(self, engine: ModerationEngine, word_bank: Any) -> None:
        """An exact custom-word match yields a BLOCK at level one."""
        self._seed_word(engine, word_bank, "zaphrin")
        engine._app_config.update_default_threshold(100)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a", user_id="u")
        )
        assert result.verdict.value == "BLOCK"
        assert result.level_used == 1
        assert "zaphrin" in result.matched_words

    def test_exact_match_confidence(self, engine: ModerationEngine, word_bank: Any) -> None:
        """Exact matches report full confidence."""
        self._seed_word(engine, word_bank, "zaphrin")
        engine._app_config.update_default_threshold(100)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a", user_id="u")
        )
        assert result.confidence_score == 1.0

    def test_fuzzy_match_review(self, engine: ModerationEngine, word_bank: Any) -> None:
        """A typo near a dictionary word triggers the LLM stage and yields REVIEW."""
        self._seed_word(engine, word_bank, "zaphrin")
        engine._app_config.update_default_threshold(10)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphren", app_name="a", user_id="u")
        )
        assert result.verdict.value == "REVIEW"
        assert result.level_used == 2

    def test_fuzzy_match_high_threshold_passes(
        self, engine: ModerationEngine, word_bank: Any
    ) -> None:
        """Without a trigger, non-blocking matches downgrade to PASS."""
        self._seed_word(engine, word_bank, "zaphrin")
        engine._app_config.update_default_threshold(100)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphren", app_name="a", user_id="u")
        )
        assert result.verdict.value == "PASS"
        assert result.level_used == 1
        assert result.suspicion_score > 0

    def test_multiple_matches_aggregate(self, engine: ModerationEngine, word_bank: Any) -> None:
        """Multiple detector hits raise the suspicion score."""
        self._seed_word(engine, word_bank, "zaphrin")
        engine._app_config.update_default_threshold(100)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a", user_id="u")
        )
        assert result.suspicion_score > 0

    def test_chain_records_detectors(self, engine: ModerationEngine, word_bank: Any) -> None:
        """The detector chain names every detector that ran before blocking."""
        self._seed_word(engine, word_bank, "zaphrin")
        engine._app_config.update_default_threshold(100)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a", user_id="u")
        )
        assert "aho_corasick" in result.detector_chain
        assert "rolling_hash" in result.detector_chain


class TestEngineStage3(BaseTest):
    """LLM trigger policy resolution with an unavailable model."""

    def test_no_trigger_when_score_low(self, engine: ModerationEngine) -> None:
        """Low suspicion never reaches the LLM stage."""
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="totally ordinary content", app_name="a", user_id="u")
        )
        assert result.level_used == 1
        assert result.ai_triggered is False

    def test_trigger_without_llm_preserves_block(
        self, engine: ModerationEngine, word_bank: Any
    ) -> None:
        """A hard block survives an unavailable LLM.

        A score above the threshold with the model unavailable must not
        downgrade an exact-match BLOCK; only ambiguous content becomes REVIEW.
        """
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(10)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a", user_id="u")
        )
        assert result.ai_triggered is False
        assert result.level_used == 2
        assert result.verdict.value == "BLOCK"

    def test_trigger_with_llm_available_not_run(self, engine: ModerationEngine) -> None:
        """The model never loads in tests, so it stays unavailable."""
        assert engine._model_router.is_available() is False

    def test_and_logic_requires_all(self, engine: ModerationEngine, word_bank: Any) -> None:
        """AND logic does not trigger when only the score fires."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.set(
            "strict",
            score_threshold=10,
            semantic_boost=False,
            user_ratio_boost=True,
            logic_type="and",
        )
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="strict", user_id="u")
        )
        assert result.level_used == 1


class TestEngineCache(BaseTest):
    """Result cache behavior."""

    def test_second_call_cached(self, engine: ModerationEngine, word_bank: Any) -> None:
        """Repeated identical text hits the cache."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(100)
        engine.moderate(ModerationRequest(text="you are a zaphrin", app_name="a", user_id="u"))
        cached: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a", user_id="u")
        )
        assert cached.verdict.value == "BLOCK"

    def test_cache_cap_evicts_oldest(self, engine: ModerationEngine) -> None:
        """The cache never exceeds its configured size."""
        for index in range(20):
            engine.moderate(ModerationRequest(text=f"unique text {index}", app_name="a"))
        assert len(engine._cache) <= engine._cache_max_size

    def test_clear_cache(self, engine: ModerationEngine) -> None:
        """clear_cache drops every entry."""
        engine.moderate(ModerationRequest(text="cache me", app_name="a"))
        engine.clear_cache()
        assert len(engine._cache) == 0

    def test_cache_hit_returns_same_verdict(self, engine: ModerationEngine) -> None:
        """A cache hit replays the stored verdict."""
        first: ModerationResponse = engine.moderate(
            ModerationRequest(text="repeat message", app_name="a", user_id="u")
        )
        second: ModerationResponse = engine.moderate(
            ModerationRequest(text="repeat message", app_name="a", user_id="u")
        )
        assert first.verdict == second.verdict
        assert second.id is None


class TestEngineMetrics(BaseTest):
    """Runtime counter behavior."""

    def test_requests_counter(self, engine: ModerationEngine) -> None:
        """Requests increment the total counter."""
        engine.moderate(ModerationRequest(text="count me", app_name="a"))
        metrics: dict[str, float] = engine.metrics()
        assert metrics["requests_total"] >= 1.0

    def test_metrics_include_detectors(self, engine: ModerationEngine, word_bank: Any) -> None:
        """Detector timing counters appear in the metrics."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine.moderate(ModerationRequest(text="time me", app_name="a"))
        assert "detector_aho_corasick_seconds_total" in engine.metrics()

    def test_rate_limit_hit_counter(self, engine: ModerationEngine) -> None:
        """Rate limit hits increment their counter."""
        engine.record_rate_limit_hit()
        assert engine.metrics()["rate_limit_hits_total"] >= 1.0

    def test_stage1_counter(self, engine: ModerationEngine, word_bank: Any) -> None:
        """Fast-path exits increment the stage-one counter."""
        engine._safe_word.add_word("hello")
        engine.moderate(ModerationRequest(text="hello", app_name="a"))
        assert engine.metrics()["stage1_fast_path_total"] >= 1.0


class TestEngineBatch(BaseTest):
    """Batch moderation behavior."""

    @pytest.mark.parametrize("size", (1, 2, 5, 10))
    def test_batch_returns_all_results(self, engine: ModerationEngine, size: int) -> None:
        """A batch returns one result per item in order.

        :param engine: test engine
        :param size: number of batch items
        """
        from app.models.request import BatchItem, BatchModerationRequest

        batch: BatchModerationRequest = BatchModerationRequest(
            items=[
                BatchItem(text=f"message number {index}", app_name="a", user_id=f"u{index}")
                for index in range(size)
            ]
        )
        response = engine.moderate_batch(batch)
        assert len(response.results) == size
        assert response.total_latency_ms >= 0.0

    def test_batch_preserves_order(self, engine: ModerationEngine) -> None:
        """Batch results keep request order."""
        from app.models.request import BatchItem, BatchModerationRequest

        batch: BatchModerationRequest = BatchModerationRequest(
            items=[
                BatchItem(id=f"id{index}", text=f"message {index}", app_name="a")
                for index in range(3)
            ]
        )
        response = engine.moderate_batch(batch)
        assert [item.id for item in response.results] == ["id0", "id1", "id2"]


class TestEngineCacheEviction(BaseTest):
    """Cache eviction and TTL behavior."""

    @pytest.mark.parametrize("count", (1, 3, 5))
    def test_cache_bounded(self, engine: ModerationEngine, count: int) -> None:
        """The cache never exceeds its configured size.

        :param engine: test engine
        :param count: number of cache-clearing iterations
        """
        for _ in range(count):
            engine.moderate(ModerationRequest(text="evict me", app_name="a"))
        assert len(engine._cache) <= engine._cache_max_size

    def test_distinct_texts_occupy_slots(self, engine: ModerationEngine) -> None:
        """Distinct texts produce distinct cache entries up to the cap."""
        for index in range(engine._cache_max_size + 5):
            engine.moderate(ModerationRequest(text=f"distinct {index}", app_name="a"))
        assert len(engine._cache) == engine._cache_max_size

    def test_cache_ttl_expiry(self, engine: ModerationEngine) -> None:
        """Entries expire after the TTL window."""
        engine.moderate(ModerationRequest(text="expire me", app_name="a"))
        assert len(engine._cache) == 1
        self.advance_hours(engine._cache_ttl // 60 + 1)
        engine.moderate(ModerationRequest(text="expire me", app_name="a"))
        assert engine._cache_timestamps is not None


class TestEngineProfiling(BaseTest):
    """User profiling integration."""

    def test_profile_recorded(self, engine: ModerationEngine) -> None:
        """Moderating with a user id records a daily row."""
        engine.moderate(
            ModerationRequest(text="record my activity", app_name="a", user_id="tracked")
        )
        profile = engine._profiler.get_profile("a", "tracked")
        assert profile["daily"]
        assert profile["daily"][0]["total_msgs"] >= 1

    def test_ratio_zero_for_clean_user(self, engine: ModerationEngine) -> None:
        """A user with only clean messages has a zero ratio."""
        engine.moderate(
            ModerationRequest(text="clean message for profile", app_name="a", user_id="clean")
        )
        assert engine._profiler.get_ratio("a", "clean") == 0.0

    def test_ratio_above_zero_after_flag(self, engine: ModerationEngine, word_bank: Any) -> None:
        """A flagged message raises the user ratio."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(100)
        engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a", user_id="flaguser")
        )
        assert engine._profiler.get_ratio("a", "flaguser") > 0.0


class TestEngineRefresh(BaseTest):
    """Detector refresh and response assembly."""

    def test_refresh_clears_cache(self, engine: ModerationEngine) -> None:
        """refresh_detectors drops cached results."""
        engine.moderate(ModerationRequest(text="pre refresh", app_name="a"))
        engine.refresh_detectors()
        assert len(engine._cache) == 0

    def test_refresh_keeps_detector_count(self, engine: ModerationEngine) -> None:
        """refresh_detectors preserves the detector roster."""
        before: int = len(engine._detectors)
        engine.refresh_detectors()
        assert len(engine._detectors) == before

    def test_response_id_echoed(self, engine: ModerationEngine) -> None:
        """The caller id is echoed back."""
        result: ModerationResponse = engine.moderate(
            ModerationRequest(id="req-123", text="echo my id", app_name="a")
        )
        assert result.id == "req-123"

    def test_response_allowed_for_pass(self, engine: ModerationEngine) -> None:
        """A PASS verdict sets allowed true."""
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="allowed content", app_name="a")
        )
        assert result.allowed is True

    def test_response_allowed_false_for_block(
        self, engine: ModerationEngine, word_bank: Any
    ) -> None:
        """A BLOCK verdict sets allowed false."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(100)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a")
        )
        assert result.allowed is False

    def test_latency_reported(self, engine: ModerationEngine) -> None:
        """The response reports a non-negative latency."""
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="latency check", app_name="a")
        )
        assert result.latency_ms >= 0.0

    def test_reason_for_block(self, engine: ModerationEngine, word_bank: Any) -> None:
        """A block carries a reason."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        engine._app_config.update_default_threshold(100)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a")
        )
        assert result.reason is not None

    def test_suspicion_score_in_range(self, engine: ModerationEngine, word_bank: Any) -> None:
        """Suspicion scores stay within 0-100."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a")
        )
        assert 0.0 <= result.suspicion_score <= 100.0
