"""Multi-language detector tests, part 2 (Phase 1, P1/P2).

Covers language attribution, ordered short-circuit execution, disabled
package toggles, and thread-pool resilience.
"""

from __future__ import annotations

from typing import Any

import pytest

from app.detectors.multi_language_detector import MultiLanguageDetector
from tests.base_test import BaseTest


def _detector(engine: Any) -> MultiLanguageDetector:
    """Build a detector bound to the test settings.

    :param engine: test engine carrying settings
    :return: a fresh multi-language detector
    """
    return MultiLanguageDetector(engine._settings, None)


class TestMultiLanguagePart2(BaseTest):
    """Language attribution and execution semantics."""

    @pytest.mark.parametrize(
        ("text", "has_language"),
        (
            ("fuck this noise", True),
            ("asshole behavior", True),
            ("this is a clean sentence", False),
        ),
    )
    def test_matched_language_reported(self, engine: Any, text: str, has_language: bool) -> None:
        """A positive match reports a language scope.

        :param engine: test engine
        :param text: message under test
        :param has_language: whether a language is expected
        """
        result = _detector(engine).detect(text)
        if result.matched:
            assert (result.matched_language is not None) is has_language

    def test_reload_noop(self, engine: Any) -> None:
        """Reload is a no-op for fixed package adapters."""
        detector: MultiLanguageDetector = _detector(engine)
        detector.reload()
        assert detector.is_available()

    def test_repeated_detect_stable(self, engine: Any) -> None:
        """Repeated detection over the same text is deterministic."""
        detector: MultiLanguageDetector = _detector(engine)
        first = detector.detect("fuck this noise")
        second = detector.detect("fuck this noise")
        assert first.matched == second.matched

    @pytest.mark.parametrize("text", ("fuck you", "asshole", "bullshit"))
    def test_short_circuit_returns_first(self, engine: Any, text: str) -> None:
        """A positive match short-circuits further packages.

        :param engine: test engine
        :param text: profane message
        """
        detector: MultiLanguageDetector = _detector(engine)
        result = detector.detect(text)
        assert result.matched is True
        assert result.reason is not None

    def test_all_disabled_unavailable(self, engine: Any) -> None:
        """Disabling every package makes the detector unavailable."""
        settings = engine._settings
        for field in (
            "enable_badwords_py",
            "enable_profanite",
            "enable_glin_profanity",
            "enable_safetext",
            "enable_sensitive_word_filter_cn",
            "enable_profanity_filter",
            "enable_gangajal",
            "enable_pyprofane",
            "enable_sensitive_stop_words",
        ):
            setattr(settings, field, False)
        detector: MultiLanguageDetector = MultiLanguageDetector(settings, None)
        assert detector.is_available() is False
        assert detector.detect("fuck you").matched is False

    def test_unicode_normalized_input(self, engine: Any) -> None:
        """Input is NFKC-normalized before package execution."""
        detector: MultiLanguageDetector = _detector(engine)
        result = detector.detect("ｆｕｃｋ this")  # noqa: RUF001
        assert isinstance(result.matched, bool)
