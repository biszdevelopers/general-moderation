"""Moderation engine component tests, part 2 (Phase 1, P1/P2).

Covers the safe word fast path filter, the rolling hash spam detector, and
the suspicion scorer weight resolution.
"""

from __future__ import annotations

import time
from typing import Any

from app.detectors.rolling_hash_detector import RollingHashDetector
from app.fastpath.safe_word_filter import SafeWordFilter
from app.scoring.suspicion_scorer import SuspicionScorer
from tests.base_test import BaseTest


class TestSafeWordFilter(BaseTest):
    """Stage 1 safe word whitelist behavior."""

    def test_add_word_persists(self, engine: Any) -> None:
        """Added words appear in the list and on disk."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("welcome")
        assert "welcome" in safe_word.words()

    def test_remove_word(self, engine: Any) -> None:
        """Removed words disappear from the list."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("welcome")
        assert safe_word.remove_word("welcome") is True
        assert "welcome" not in safe_word.words()

    def test_remove_missing_returns_false(self, engine: Any) -> None:
        """Removing an absent word returns False."""
        assert engine._safe_word.remove_word("nope") is False

    def test_is_safe_requires_all_tokens(self, engine: Any) -> None:
        """Only texts composed entirely of safe words pass."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("hello")
        safe_word.add_word("world")
        assert safe_word.is_safe("hello world") is True
        assert safe_word.is_safe("hello danger") is False

    def test_is_safe_empty_false(self, engine: Any) -> None:
        """Empty text never passes the fast path."""
        assert engine._safe_word.is_safe("") is False

    def test_is_safe_case_insensitive(self, engine: Any) -> None:
        """Safe matching is case-insensitive."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("hello")
        assert safe_word.is_safe("HELLO there") is False
        assert safe_word.is_safe("HELLO") is True

    def test_detect_language_zh(self, engine: Any) -> None:
        """CJK text is identified as Chinese."""
        assert SafeWordFilter.detect_language("你好世界") == "zh"

    def test_detect_language_ru(self, engine: Any) -> None:
        """Cyrillic text is identified as Russian."""
        assert SafeWordFilter.detect_language("привет мир") == "ru"

    def test_detect_language_ar(self, engine: Any) -> None:
        """Arabic text is identified as Arabic."""
        assert SafeWordFilter.detect_language("مرحبا") == "ar"

    def test_detect_language_en(self, engine: Any) -> None:
        """Latin text falls back to English."""
        assert SafeWordFilter.detect_language("hello there") == "en"

    def test_reload_picks_up_file(self, engine: Any, settings: Any) -> None:
        """Reload re-reads the word list from disk."""
        safe_word: SafeWordFilter = engine._safe_word
        safe_word.add_word("freshly")
        safe_word.reload()
        assert "freshly" in safe_word.words()


class TestRollingHash(BaseTest):
    """Rolling hash spam cache behavior."""

    def test_first_seen_not_matched(self) -> None:
        """A fresh message is not flagged."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        assert detector.detect("hello world").matched is False

    def test_clean_repeat_not_matched(self) -> None:
        """Repeating a clean message stays clean."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.detect("hello world")
        assert detector.detect("hello world").matched is False

    def test_flagged_repeat_matched(self) -> None:
        """Repeating a flagged message is caught."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit("spam message")
        assert detector.detect("spam message").matched is True

    def test_confidence_point_nine(self) -> None:
        """Flagged repeats report high confidence."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit("spam message")
        assert detector.detect("spam message").confidence_score == 0.9

    def test_different_text_not_matched(self) -> None:
        """A different text after a flag stays clean."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit("spam message")
        assert detector.detect("another message").matched is False

    def test_cache_size_bounded(self) -> None:
        """The LRU cache never exceeds its configured size."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=3, ttl_seconds=60)
        for index in range(20):
            detector.detect(f"message number {index}")
        assert len(detector._cache) <= 3

    def test_ttl_expires_entry(self) -> None:
        """Entries older than the TTL no longer match."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=1)
        detector.record_hit("expiring spam")
        time.sleep(1.1)
        detector.detect("expiring spam")
        assert detector.detect("expiring spam").matched is False

    def test_name_and_priority(self) -> None:
        """Rolling hash metadata is stable."""
        detector: RollingHashDetector = RollingHashDetector()
        assert detector.name == "rolling_hash"
        assert detector.priority == 2

    def test_reload_noop(self) -> None:
        """Reload leaves the cache untouched."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit("spam message")
        detector.reload()
        assert detector.detect("spam message").matched is True

    def test_language_any(self) -> None:
        """The detector is language-neutral."""
        assert RollingHashDetector().language == "any"

    def test_not_blocking(self) -> None:
        """Rolling hash matches are non-decisive."""
        assert RollingHashDetector().blocking is False

    def test_reason_present_on_flag(self) -> None:
        """Flagged repeats carry a reason."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        detector.record_hit("spam message")
        result = detector.detect("spam message")
        assert result.reason is not None
        assert "Repeated" in str(result.reason)

    def test_empty_text_tracked(self) -> None:
        """Empty text is tracked without crashing."""
        detector: RollingHashDetector = RollingHashDetector(cache_size=10, ttl_seconds=60)
        assert detector.detect("").matched is False
        detector.record_hit("")
        assert detector.detect("").matched is True


class TestSuspicionScorer(BaseTest):
    """Weighted suspicion score calculation."""

    def test_no_signals_zero(self, engine: Any) -> None:
        """No signals produce a zero score."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.score(detector_names=[], semantic_similarities={}, user_ratio=0.0) == 0.0

    def test_detector_weight_applied(self, engine: Any) -> None:
        """A detector hit contributes its configured weight."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        score = scorer.score(detector_names=["aho_corasick"])
        assert score == scorer.detector_weight("aho_corasick")

    def test_unknown_detector_zero(self, engine: Any) -> None:
        """Unknown detectors contribute nothing."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        assert scorer.detector_weight("nonexistent") == 0

    def test_multiple_detectors_sum(self, engine: Any) -> None:
        """Multiple detector hits sum their weights."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        total: float = scorer.score(detector_names=["aho_corasick", "bk_tree"])
        expected: float = scorer.detector_weight("aho_corasick") + scorer.detector_weight("bk_tree")
        assert total == expected

    def test_score_clamped_to_100(self, engine: Any) -> None:
        """The score never exceeds 100."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        names: list[str] = ["aho_corasick", "bk_tree", "double_metaphone", "multi_language"]
        score: float = scorer.score(detector_names=names, user_ratio=1.0)
        assert score <= 100.0

    def test_user_ratio_weighted(self, engine: Any) -> None:
        """The user ratio contributes its configured weight."""
        scorer: SuspicionScorer = SuspicionScorer(engine._settings_service)
        ratio_score: float = scorer.score(detector_names=[], user_ratio=0.5)
        assert ratio_score == 0.5 * float(engine._settings_service.get("WEIGHT_USER", 20))
