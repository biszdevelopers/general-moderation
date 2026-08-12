"""BK-tree fuzzy detector tests (Phase 1, P0/P1).

Covers edit-distance-1 and -2 typos, leetspeak drift, boundary distances,
exact-token non-matches, and detector metadata.
"""

from __future__ import annotations

import pytest

from app.detectors.bktree_detector import BkTreeDetector
from app.wordbank.manager import WordBankManager
from tests.base_test import BaseTest

_FUZZY_CASES: tuple[tuple[str, str, bool], ...] = (
    ("asshole", "ashole", True),
    ("asshole", "aszzole", True),
    ("blocked", "bloced", True),
    ("blocked", "blockedd", True),
    ("bomb", "bom", True),
    ("bomb", "bombz", True),
    ("kill", "kil", True),
    ("kill", "killi", True),
    ("hate", "hatee", True),
    ("scam", "sCam", True),
    ("jerk", "jer", True),
    ("fool", "foool", True),
    ("fool", "foolish", False),
    ("crap", "crab", True),
    ("damn", "damm", True),
    ("hell", "hel", True),
    ("gun", "gunn", True),
    ("knife", "knif", True),
    ("knife", "knive", True),
    ("poison", "poizn", True),
)


class TestBkTreePart1(BaseTest):
    """Edit-distance fuzzy matching scenarios."""

    @pytest.mark.parametrize(("word", "text", "expected"), _FUZZY_CASES)
    def test_fuzzy_match(
        self,
        word_bank: WordBankManager,
        word: str,
        text: str,
        expected: bool,
    ) -> None:
        """Tokens near a dictionary word are flagged.

        :param word_bank: isolated word bank fixture
        :param word: dictionary term to add
        :param text: message under test
        :param expected: whether a match is expected
        """
        word_bank.add_word(word)
        detector: BkTreeDetector = BkTreeDetector(word_bank, 2)
        assert detector.is_available()
        assert detector.detect(text).matched is expected


class TestBkTreeMetadata(BaseTest):
    """BK-tree metadata and distance boundaries."""

    def test_name(self, word_bank: WordBankManager) -> None:
        """The detector name is stable."""
        assert BkTreeDetector(word_bank, 2).name == "bk_tree"

    def test_priority_is_four(self, word_bank: WordBankManager) -> None:
        """The BK-tree detector sits at pipeline position four."""
        assert BkTreeDetector(word_bank, 2).priority == 4

    def test_language_any(self, word_bank: WordBankManager) -> None:
        """The detector is language-neutral."""
        assert BkTreeDetector(word_bank, 2).language == "any"

    def test_not_blocking(self, word_bank: WordBankManager) -> None:
        """Fuzzy matches are non-decisive (REVIEW)."""
        assert BkTreeDetector(word_bank, 2).blocking is False

    def test_confidence_point_seven(self, word_bank: WordBankManager) -> None:
        """Fuzzy matches report moderate confidence."""
        word_bank.add_word("asshole")
        result = BkTreeDetector(word_bank, 2).detect("ashole")
        assert result.confidence_score == 0.7

    def test_reason_present(self, word_bank: WordBankManager) -> None:
        """Matches carry a human-readable reason."""
        word_bank.add_word("asshole")
        result = BkTreeDetector(word_bank, 2).detect("ashole")
        assert result.reason is not None
        assert "edit distance" in str(result.reason)

    def test_distance_zero_is_exact(self, word_bank: WordBankManager) -> None:
        """A zero-distance BK-tree rejects mutated tokens and skips exacts."""
        word_bank.add_word("asshole")
        detector: BkTreeDetector = BkTreeDetector(word_bank, 0)
        assert detector.detect("ashole").matched is False
        assert detector.detect("asshole").matched is False

    def test_distance_three_tighten(self, word_bank: WordBankManager) -> None:
        """A wider distance admits more mutations."""
        word_bank.add_word("asshole")
        detector: BkTreeDetector = BkTreeDetector(word_bank, 3)
        assert detector.detect("ashol").matched is True

    def test_reload_rebuilds(self, word_bank: WordBankManager) -> None:
        """Reload rebuilds the tree from the current word bank."""
        word_bank.add_word("alpha")
        detector: BkTreeDetector = BkTreeDetector(word_bank, 2)
        word_bank.add_word("beta")
        detector.reload()
        assert detector.detect("b3ta").matched is True

    def test_empty_text_no_match(self, word_bank: WordBankManager) -> None:
        """Empty text never matches."""
        word_bank.add_word("asshole")
        assert BkTreeDetector(word_bank, 2).detect("").matched is False
