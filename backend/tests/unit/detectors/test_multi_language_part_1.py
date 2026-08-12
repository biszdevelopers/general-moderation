"""Multi-language detector tests, part 1 (Phase 1, P0/P1).

Covers package availability, positive detection across the wired C/C++/Rust/
WASM packages, clean-text negatives, and detector metadata.
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


class TestMultiLanguagePart1(BaseTest):
    """Multi-language package availability."""

    def test_name(self, engine: Any) -> None:
        """The detector name is stable."""
        assert _detector(engine).name == "multi_language"

    def test_priority_is_six(self, engine: Any) -> None:
        """The detector sits at pipeline position six."""
        assert _detector(engine).priority == 6

    def test_language_multi(self, engine: Any) -> None:
        """The detector reports a multi-language scope."""
        assert _detector(engine).language == "multi"

    def test_blocking(self, engine: Any) -> None:
        """Package positives are decisive."""
        assert _detector(engine).blocking is True

    def test_available_with_packages(self, engine: Any) -> None:
        """At least one wired package is usable."""
        detector: MultiLanguageDetector = _detector(engine)
        assert detector.is_available()
        assert len(detector.available_packages()) >= 1

    @pytest.mark.parametrize(
        "package",
        ("profanite", "glin_profanity", "badwords", "gangajal", "PyProfane"),
    )
    def test_known_package_present(self, engine: Any, package: str) -> None:
        """The five installable packages are registered.

        :param engine: test engine
        :param package: expected package name
        """
        assert package in _detector(engine).available_packages()

    @pytest.mark.parametrize(
        "text",
        ("this is a clean sentence", "hello world welcome"),
    )
    def test_clean_text(self, engine: Any, text: str) -> None:
        """Clean text is not flagged by any package.

        :param engine: test engine
        :param text: clean message
        """
        assert _detector(engine).detect(text).matched is False


class TestMultiLanguagePositive(BaseTest):
    """Positive detection across the wired packages."""

    @pytest.mark.parametrize(
        "text",
        (
            "fuck this noise",
            "asshole behavior",
            "bullshit excuse",
        ),
    )
    def test_profanity_flagged(self, engine: Any, text: str) -> None:
        """Profane input is flagged by at least one package.

        :param engine: test engine
        :param text: profane message
        """
        result = _detector(engine).detect(text)
        assert result.matched is True
        assert result.reason is not None
