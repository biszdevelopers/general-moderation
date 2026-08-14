"""Severe-content detection tests (Phase 1, P0).

Covers the severity-aware phrase pipeline: phrase detection with severity
tagging, the hard-block threshold, the suspicion-score floor, review
escalation, the benign false-positive fix (glin resolver), and result-cache
invalidation when configuration changes.
"""

from __future__ import annotations

from typing import Any

from app.engine.moderation_engine import ModerationEngine
from app.models.request import ModerationRequest
from app.models.response import ModerationResponse
from app.phrases.manager import CriticalPhraseManager
from tests.base_test import BaseTest


class TestCriticalPhraseManager(BaseTest):
    """Phrase store and automaton behavior."""

    def test_add_reload_and_detect(self, settings: Any) -> None:
        """Adding a phrase makes it detectable with its severity."""
        manager: CriticalPhraseManager = CriticalPhraseManager(settings.critical_phrases_db_path)
        try:
            assert manager.is_available() is False
            manager.add("kill yourself", category="violence", severity=7, language="en")
            result = manager.detect("please kill yourself tonight")
            assert result.matched is True
            assert result.severity == 7
            assert result.category == "violence"
            assert "kill yourself" in result.matched_words
        finally:
            manager.close()

    def test_remove_phrase(self, settings: Any) -> None:
        """Removing a phrase stops its detection."""
        manager: CriticalPhraseManager = CriticalPhraseManager(settings.critical_phrases_db_path)
        try:
            phrase = manager.add("kill yourself", category="violence", severity=7, language="en")
            assert manager.remove(phrase.id) is True
            assert manager.detect("kill yourself").matched is False
        finally:
            manager.close()

    def test_duplicate_phrase_rejected(self, settings: Any) -> None:
        """Adding the same phrase twice raises ValueError."""
        manager: CriticalPhraseManager = CriticalPhraseManager(settings.critical_phrases_db_path)
        try:
            manager.add("kill yourself", category="violence", severity=7, language="en")
            try:
                manager.add("kill yourself", category="violence", severity=7, language="en")
                raise AssertionError("expected ValueError")
            except ValueError:
                pass
        finally:
            manager.close()


class TestSeverityHardBlock(BaseTest):
    """Severity-aware hard blocking in the engine."""

    def _seed_phrase(self, engine: ModerationEngine, phrase: str, severity: int) -> None:
        """Add a critical phrase and refresh the detector cache."""
        engine._phrases.add(phrase, category="violence", severity=severity, language="en")
        engine.refresh_detectors()

    def test_high_severity_hard_blocks(self, engine: ModerationEngine) -> None:
        """A phrase at or above the threshold hard-blocks without the LLM."""
        self._seed_phrase(engine, "kill yourself", severity=7)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="kill yourself now", app_name="a", user_id="u")
        )
        assert result.verdict.value == "BLOCK"
        assert result.severity == 7
        assert result.category == "violence"
        assert result.ai_triggered is False

    def test_low_severity_not_hard_blocked(self, engine: ModerationEngine) -> None:
        """A phrase below the threshold is not hard-blocked."""
        self._seed_phrase(engine, "zaphrin army", severity=2)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="the zaphrin army is coming", app_name="a", user_id="u")
        )
        assert result.verdict.value != "BLOCK"

    def test_per_app_severity_threshold(self, engine: ModerationEngine) -> None:
        """An app can raise its hard-block threshold."""
        self._seed_phrase(engine, "kill yourself", severity=7)
        engine._app_config.set("lenient", severity_hard_block_threshold=10)
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="kill yourself now", app_name="lenient", user_id="u")
        )
        assert result.verdict.value != "BLOCK"
        assert result.suspicion_score >= 50


class TestSeverityScoring(BaseTest):
    """Severity feeds the suspicion-score floor."""

    def test_severity_floor_raises_score(self, engine: ModerationEngine) -> None:
        """A moderate-severity match lifts the score toward the LLM."""
        engine._phrases.add("stab you", category="violence", severity=4, language="en")
        engine.refresh_detectors()
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="i will stab you", app_name="a", user_id="u")
        )
        assert result.suspicion_score >= 20

    def test_ordinary_words_unaffected(self, engine: ModerationEngine, word_bank: Any) -> None:
        """Default custom words (severity 1) report their severity unchanged."""
        word_bank.add_word("zaphrin")
        engine.refresh_detectors()
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text="you are a zaphrin", app_name="a", user_id="u")
        )
        assert result.severity == 1
        assert result.suspicion_score == 60


class TestFalsePositiveFix(BaseTest):
    """The multi-language resolver no longer false-positives on benign text."""

    def test_benign_text_passes(self, engine: ModerationEngine) -> None:
        """Clean everyday sentences are not blocked."""
        for text in (
            "class president, pass the glass",
            "the weather is pleasant today",
            "hello world, how are you today",
        ):
            result: ModerationResponse = engine.moderate(
                ModerationRequest(text=text, app_name="a", user_id="u")
            )
            assert result.verdict.value == "PASS", text


class TestCacheInvalidation(BaseTest):
    """Config changes invalidate cached verdicts."""

    def test_settings_change_invalidates_cache(self, engine: ModerationEngine) -> None:
        """Tuning a threshold drops stale cached responses."""
        text: str = "cache invalidation check"
        engine.moderate(ModerationRequest(text=text, app_name="a"))
        key: int = engine._get_cache_key(text)
        assert engine._get_cached(key) is not None
        old_fingerprint: int = engine._cache_fingerprints[key]
        engine._settings_service.update({"WEIGHT_DETECTOR_AHO": 45})
        engine.moderate(ModerationRequest(text=text, app_name="a"))
        assert engine._cache_fingerprints[key] != old_fingerprint
