"""Double Metaphone phonetic matcher (Layer 5).

Words that survive normalization but are phonetically equivalent to a
dictionary word are caught by comparing Double Metaphone codes computed with
the ``metaphone`` package, with C edit distance used to tolerate code drift.
"""

from __future__ import annotations

from typing import Any

try:
    import metaphone as _metaphone_module

    _metaphone_function = getattr(_metaphone_module, "dm", None) or getattr(
        _metaphone_module, "metaphone", None
    )
except ImportError:  # pragma: no cover - requires metaphone package
    _metaphone_module = None  # type: ignore[assignment]
    _metaphone_function = None

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


class MetaphoneDetector(DetectorInterface):
    """Phonetic equivalence matcher based on Double Metaphone codes."""

    _CODE_TOLERANCE: int = 1

    def __init__(self, word_bank: WordBankManager) -> None:
        """Precompute phonetic codes for the current word bank.

        :param word_bank: manager supplying the active word set
        """
        self._word_bank: WordBankManager = word_bank
        self._code_to_words: dict[str, set[str]] = {}
        self.reload()

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "double_metaphone"

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 5

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    def is_available(self) -> bool:
        """Whether the phonetic and distance libraries are installed."""
        return _metaphone_function is not None and _distance is not None

    def reload(self) -> None:
        """Rebuild the phonetic code index after the word bank changes."""
        self._code_to_words = {}
        if _metaphone_function is None:
            return
        for word in self._word_bank.snapshot.words:
            code: str = self._encode(word)
            if code:
                self._code_to_words.setdefault(code, set()).add(word)

    def _encode(self, word: str) -> str:
        """Return the primary phonetic code for a word.

        :param word: input word
        :return: the primary Double Metaphone code, or an empty string
        """
        if _metaphone_function is None:
            return ""
        raw: Any = _metaphone_function(word)
        if isinstance(raw, tuple):
            return str(raw[0]) if raw else ""
        return str(raw)

    def detect(self, text: str) -> DetectionResult:
        """Match tokens whose phonetic code resembles a dictionary word.

        :param text: normalized input text
        :return: the phonetic matches when any are found
        """
        matched: set[str] = set()
        for token in UnicodeUtils.tokenize(text):
            token_code: str = self._encode(token)
            if not token_code:
                continue
            for code, words in self._code_to_words.items():
                if code == token_code or (
                    _distance is not None
                    and _distance(code, token_code) <= MetaphoneDetector._CODE_TOLERANCE
                ):
                    matched.update(words)
        if not matched:
            return DetectionResult(matched=False)
        return DetectionResult(
            matched=True,
            matched_words=tuple(sorted(matched)),
            reason="Token phonetically equivalent to a dictionary word",
            confidence_score=0.6,
        )
