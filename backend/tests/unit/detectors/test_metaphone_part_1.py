"""Double Metaphone detector tests (Phase 1, P1).

Covers phonetic equivalents, code tolerance of one, non-matches, and
detector metadata.
"""

from __future__ import annotations

import pytest

from app.detectors.metaphone_detector import MetaphoneDetector
from app.wordbank.manager import WordBankManager
from tests.base_test import BaseTest

_PHONETIC_CASES: tuple[tuple[str, str, bool], ...] = (
    ("asshole", "ashole", True),
    ("phuk", "fuk", True),
    ("phuk", "phuck", True),
    ("kill", "kil", True),
    ("hate", "hait", True),
    ("jerk", "jirk", True),
    ("fool", "fule", True),
    ("damn", "damm", True),
    ("hell", "hel", True),
    ("crap", "crap", True),
    ("weed", "whede", True),
    ("scam", "skam", True),
)


class TestMetaphonePart1(BaseTest):
    """Phonetic equivalence scenarios."""

    @pytest.mark.parametrize(("word", "text", "expected"), _PHONETIC_CASES)
    def test_phonetic_match(
        self,
        word_bank: WordBankManager,
        word: str,
        text: str,
        expected: bool,
    ) -> None:
        """Tokens sharing a phonetic code are flagged.

        :param word_bank: isolated word bank fixture
        :param word: dictionary term to add
        :param text: message under test
        :param expected: whether a match is expected
        """
        word_bank.add_word(word)
        detector: MetaphoneDetector = MetaphoneDetector(word_bank)
        assert detector.is_available()
        assert detector.detect(text).matched is expected


class TestMetaphoneMetadata(BaseTest):
    """Metaphone metadata and non-match behavior."""

    def test_clean_text_no_match(self, word_bank: WordBankManager) -> None:
        """Clean text produces no phonetic match."""
        word_bank.add_word("phuk")
        result = MetaphoneDetector(word_bank).detect("have a nice day")
        assert result.matched is False

    def test_confidence_point_six(self, word_bank: WordBankManager) -> None:
        """Phonetic matches report moderate confidence."""
        word_bank.add_word("asshole")
        result = MetaphoneDetector(word_bank).detect("ashole")
        assert result.confidence_score == 0.6

    def test_name(self, word_bank: WordBankManager) -> None:
        """The detector name is stable."""
        assert MetaphoneDetector(word_bank).name == "double_metaphone"

    def test_priority_is_five(self, word_bank: WordBankManager) -> None:
        """The detector sits at pipeline position five."""
        assert MetaphoneDetector(word_bank).priority == 5

    def test_language_any(self, word_bank: WordBankManager) -> None:
        """The detector is language-neutral."""
        assert MetaphoneDetector(word_bank).language == "any"

    def test_not_blocking(self, word_bank: WordBankManager) -> None:
        """Phonetic matches are non-decisive."""
        assert MetaphoneDetector(word_bank).blocking is False

    def test_reload_rebuilds(self, word_bank: WordBankManager) -> None:
        """Reload rebuilds the phonetic index."""
        word_bank.add_word("phuk")
        detector: MetaphoneDetector = MetaphoneDetector(word_bank)
        word_bank.add_word("freek")
        detector.reload()
        assert detector.detect("freak").matched is True

    def test_reason_present(self, word_bank: WordBankManager) -> None:
        """Matches carry a human-readable reason."""
        word_bank.add_word("phuk")
        result = MetaphoneDetector(word_bank).detect("fuk")
        assert result.reason is not None
        assert "phonetic" in str(result.reason)
