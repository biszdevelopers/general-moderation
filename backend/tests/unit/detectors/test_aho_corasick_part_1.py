"""Aho-Corasick detector tests (Phase 1, P0/P1).

Covers exact-match blocking, case folding, Unicode normalization (NFKC),
multi-word phrases, deduplication, punctuation boundaries, and non-matches.
"""

from __future__ import annotations

import pytest

from app.detectors.aho_detector import AhoCorasickDetector
from app.wordbank.manager import WordBankManager
from tests.base_test import BaseTest

_EXACT_CASES: tuple[tuple[str, str, bool], ...] = (
    ("blocked", "you are blocked", True),
    ("blocked", "you are fine here", False),
    ("asshole", "what an asshole", True),
    ("bomb", "there is a bomb", True),
    ("bomb", "bombardment is normal", True),
    ("fuck", "fck that noise", False),
    ("kill", "I will kill you", True),
    ("kill", "skill and drill", True),
    ("murder", "murder mystery novel", True),
    ("hate", "I hate this place", True),
    ("scam", "free scam alert", True),
    ("weed", "weed the garden", True),
    ("darn", "darn it all", True),
    ("jerk", "what a jerk", True),
    ("crap", "total crap", True),
    ("idiot", "you idiot", True),
    ("stupid", "stupid idea", True),
    ("fool", "you fool", True),
    ("damn", "damn weather", True),
    ("hell", "what the hell", True),
    ("bitch", "bitch please", True),
    ("terror", "terror attack", True),
    ("gun", "hand me the gun", True),
    ("knife", "a sharp knife", True),
    ("poison", "poison control", True),
    ("rape", "rape culture", True),
    ("drink", "drink water", True),
    ("dumb", "dumb question", True),
    ("weak", "weak excuse", True),
    ("liar", "you liar", True),
    ("thief", "caught a thief", True),
    ("smuggle", "smuggle goods", True),
    ("fraud", "insurance fraud", True),
    ("gamble", "gamble online", True),
    ("lottery", "lottery winner", True),
    ("porn", "porn site", True),
    ("nude", "nude beach", True),
)


class TestAhoCorasickPart1(BaseTest):
    """Exact-match Aho-Corasick scenarios."""

    @pytest.mark.parametrize(("word", "text", "expected"), _EXACT_CASES)
    def test_exact_match(
        self,
        word_bank: WordBankManager,
        word: str,
        text: str,
        expected: bool,
    ) -> None:
        """Exact dictionary words must be detected in arbitrary text.

        :param word_bank: isolated word bank fixture
        :param word: dictionary term to add
        :param text: message under test
        :param expected: whether a match is expected
        """
        word_bank.add_word(word)
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.is_available()
        result = detector.detect(text)
        assert result.matched is expected


class TestAhoCorasickBlocking(BaseTest):
    """Blocking semantics, normalization, and metadata."""

    def test_blocking_flag(self, word_bank: WordBankManager) -> None:
        """Exact matches are decisive."""
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.blocking is True

    def test_priority_is_three(self, word_bank: WordBankManager) -> None:
        """The Aho detector sits at pipeline position three."""
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.priority == 3

    def test_name(self, word_bank: WordBankManager) -> None:
        """The detector name is stable."""
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.name == "aho_corasick"

    def test_language_any(self, word_bank: WordBankManager) -> None:
        """The detector is language-neutral."""
        detector: AhoCorasickDetector = AhoCorasickDetector(word_bank)
        assert detector.language == "any"

    def test_confidence_one(self, word_bank: WordBankManager) -> None:
        """Exact matches report full confidence."""
        word_bank.add_word("blocked")
        result = AhoCorasickDetector(word_bank).detect("you are blocked")
        assert result.confidence_score == 1.0

    def test_reason_present(self, word_bank: WordBankManager) -> None:
        """Matches carry a human-readable reason."""
        word_bank.add_word("blocked")
        result = AhoCorasickDetector(word_bank).detect("you are blocked")
        assert result.reason is not None
        assert "Aho" in str(result.reason)

    def test_matched_words_reported(self, word_bank: WordBankManager) -> None:
        """The matched term is returned to the caller."""
        word_bank.add_word("blocked")
        result = AhoCorasickDetector(word_bank).detect("you are blocked")
        assert result.matched_words == ("blocked",)

    def test_case_sensitive(self, word_bank: WordBankManager) -> None:
        """Uppercase input does not match lowercase dictionary words.

        Normalization folds Unicode but does not lowercase; the admin word
        path lowercases on write, so dictionary entries are already lower.
        """
        word_bank.add_word("blocked")
        result = AhoCorasickDetector(word_bank).detect("YOU ARE BLOCKED")
        assert result.matched is False

    def test_fullwidth_unicode(self, word_bank: WordBankManager) -> None:
        """NFKC folding catches full-width obfuscation."""
        word_bank.add_word("blocked")
        result = AhoCorasickDetector(word_bank).detect("you are ｂｌｏｃｋｅｄ")  # noqa: RUF001
        assert result.matched is True

    def test_duplicate_words_deduplicated(self, word_bank: WordBankManager) -> None:
        """Repeated dictionary words appear only once."""
        word_bank.add_word("blocked")
        result = AhoCorasickDetector(word_bank).detect("blocked blocked blocked")
        assert result.matched_words == ("blocked",)

    def test_multiple_distinct_matches(self, word_bank: WordBankManager) -> None:
        """Every distinct dictionary word in the text is reported."""
        word_bank.add_word("blocked")
        word_bank.add_word("bomb")
        result = AhoCorasickDetector(word_bank).detect("blocked bomb")
        assert set(result.matched_words) == {"blocked", "bomb"}

    def test_empty_text_no_match(self, word_bank: WordBankManager) -> None:
        """Empty text never matches."""
        word_bank.add_word("blocked")
        result = AhoCorasickDetector(word_bank).detect("")
        assert result.matched is False

    def test_whitespace_only_no_match(self, word_bank: WordBankManager) -> None:
        """Whitespace-only text never matches."""
        word_bank.add_word("blocked")
        result = AhoCorasickDetector(word_bank).detect("   \t\n  ")
        assert result.matched is False
