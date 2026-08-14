"""Aho-Corasick exact matcher (Layer 3).

The C ``pyahocorasick`` automaton scans the whole text in a single pass and
reports every dictionary word that occurs, in linear time regardless of the
dictionary size. This is the primary exact-match engine for both base and
custom words.

Base dictionary words are only honored at ASCII word boundaries so noisy
package dictionaries (e.g. ``ass``) do not fire inside innocent words such as
``class`` or ``grass``. Administrator-curated custom words keep full substring
semantics, and their configured severity/category ride along on a match.
"""

from __future__ import annotations

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.unicode_utils import UnicodeUtils
from app.wordbank.manager import WordBankManager, WordBankSnapshot

_ASCII_WORD_CHARS = set("abcdefghijklmnopqrstuvwxyz0123456789_")


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

    @staticmethod
    def _at_word_boundary(text: str, start: int, end: int) -> bool:
        """Return True when the span has no ASCII word char on either side.

        Only ASCII context is guarded: CJK and other non-ASCII neighbors are
        treated as boundaries so the match is kept, preserving substring
        behaviour for non-Latin dictionaries.

        :param text: the scanned text
        :param start: inclusive start index of the match
        :param end: inclusive end index of the match
        :return: True when the match is not glued to ASCII word characters
        """
        before: str = text[start - 1] if start > 0 else ""
        after: str = text[end + 1] if end + 1 < len(text) else ""
        return not (before in _ASCII_WORD_CHARS or after in _ASCII_WORD_CHARS)

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
        for end_index, stored_word in automaton.iter(normalized):
            word: str = str(stored_word)
            start: int = end_index - len(word) + 1
            if word in snapshot.base_words and not self._at_word_boundary(
                normalized, start, end_index
            ):
                continue
            matched.append(word)
        if not matched:
            return DetectionResult(matched=False)
        matched = list(dict.fromkeys(matched))
        severity: int | None = None
        category: str | None = None
        for word in matched:
            word_severity: int = snapshot.severity_by_word.get(word, 0)
            if severity is None or word_severity > severity:
                severity = word_severity
            word_category: str | None = snapshot.category_by_word.get(word)
            if word_category is not None:
                category = word_category
        return DetectionResult(
            matched=True,
            matched_words=tuple(matched),
            reason="Exact sensitive word matched in Aho-Corasick automaton",
            confidence_score=1.0,
            severity=severity or None,
            category=category,
        )
