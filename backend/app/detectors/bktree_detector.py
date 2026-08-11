"""BK-tree fuzzy matcher (Layer 4).

A BK-tree indexed with the C ``python-Levenshtein`` edit distance finds every
dictionary word within a bounded edit distance of each token, catching
typos, leetspeak drift, and deliberate misspellings.
"""

from __future__ import annotations

from typing import Any

try:
    from pybktree import BKTree as _BKTree
except ImportError:  # pragma: no cover - requires C pybktree
    _BKTree = None  # type: ignore[assignment]

try:
    from Levenshtein import distance as _distance
except ImportError:  # pragma: no cover - requires C python-Levenshtein
    try:
        import Levenshtein as _Levenshtein

        _distance = _Levenshtein.distance
    except ImportError:  # pragma: no cover
        _distance = None  # type: ignore[assignment]

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.unicode_utils import UnicodeUtils
from app.wordbank.manager import WordBankManager


class BkTreeDetector(DetectorInterface):
    """Fuzzy word matching using a BK-tree and C edit distance."""

    def __init__(self, word_bank: WordBankManager, max_distance: int = 2) -> None:
        """Build the BK-tree from the current word bank.

        :param word_bank: manager supplying the active word set
        :param max_distance: maximum edit distance considered a match
        """
        self._word_bank: WordBankManager = word_bank
        self._max_distance: int = max_distance
        self._tree: Any | None = None
        self.reload()

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "bk_tree"

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 4

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    def is_available(self) -> bool:
        """Whether both C libraries are installed."""
        return _BKTree is not None and _distance is not None and self._tree is not None

    def reload(self) -> None:
        """Rebuild the BK-tree after the word bank changes."""
        if _BKTree is None or _distance is None:
            self._tree = None
            return
        words: tuple[str, ...] = self._word_bank.snapshot.words
        self._tree = _BKTree(_distance, words)

    def detect(self, text: str) -> DetectionResult:
        """Find dictionary words within the edit distance bound.

        :param text: normalized input text
        :return: the closest matches when any token is near a dictionary word
        """
        if self._tree is None:
            return DetectionResult(matched=False)
        matched: set[str] = set()
        for token in UnicodeUtils.tokenize(text):
            for _dist, word in self._tree.find(token, self._max_distance):
                if word != token:
                    matched.add(str(word))
        if not matched:
            return DetectionResult(matched=False)
        return DetectionResult(
            matched=True,
            matched_words=tuple(sorted(matched)),
            reason="Token within edit distance of a dictionary word",
            confidence_score=0.7,
        )
