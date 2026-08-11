"""Aho-Corasick exact matcher (Layer 3).

The C ``pyahocorasick`` automaton scans the whole text in a single pass and
reports every dictionary word that occurs, in linear time regardless of the
dictionary size. This is the primary exact-match engine for both base and
custom words.
"""

from __future__ import annotations

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.unicode_utils import UnicodeUtils
from app.wordbank.manager import WordBankManager, WordBankSnapshot


class AhoCorasickDetector(DetectorInterface):
    """Single-pass exact match against the compiled word bank automaton."""

    def __init__(self, word_bank: WordBankManager) -> None:
        """Bind the detector to the shared word bank.

        :param word_bank: manager whose snapshot supplies the automaton
        """
        self._word_bank: WordBankManager = word_bank

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "aho_corasick"

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 3

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    @property
    def blocking(self) -> bool:
        """Exact matches are decisive."""
        return True

    def is_available(self) -> bool:
        """Whether an automaton exists in the current snapshot."""
        return self._word_bank.snapshot.automaton is not None

    def reload(self) -> None:
        """No-op: the automaton is read live from the snapshot."""

    def detect(self, text: str) -> DetectionResult:
        """Scan the text with the Aho-Corasick automaton.

        :param text: normalized input text
        :return: every exact dictionary word found in the text
        """
        snapshot: WordBankSnapshot = self._word_bank.snapshot
        automaton = snapshot.automaton
        if automaton is None:
            return DetectionResult(matched=False)
        normalized: str = UnicodeUtils.prepare(text)
        matched: list[str] = []
        for _, stored_word in automaton.iter(normalized):
            matched.append(str(stored_word))
        if not matched:
            return DetectionResult(matched=False)
        return DetectionResult(
            matched=True,
            matched_words=tuple(dict.fromkeys(matched)),
            reason="Exact sensitive word matched in Aho-Corasick automaton",
            confidence_score=1.0,
        )
