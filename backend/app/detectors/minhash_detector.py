"""MinHash near-duplicate detector (Layer 7).

Character n-gram MinHashes computed with ``datasketch`` (NumPy/C) catch
paraphrases and lightly transformed repeats of known sensitive phrases that
string matching misses entirely.
"""

from __future__ import annotations

from typing import Any

try:
    from datasketch import MinHash as _MinHashImpl

    _MINHASH_AVAILABLE = True
except ImportError:  # pragma: no cover - requires datasketch
    _MinHashImpl = None  # type: ignore[assignment]
    _MINHASH_AVAILABLE = False

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.unicode_utils import UnicodeUtils
from app.wordbank.manager import WordBankManager

_SHINGLE_SIZE: int = 5


class MinHashDetector(DetectorInterface):
    """Near-duplicate detection over character n-gram MinHashes."""

    def __init__(
        self, word_bank: WordBankManager, num_perm: int = 128, threshold: float = 0.85
    ) -> None:
        """Precompute a MinHash for every word.

        :param word_bank: manager supplying the active word set
        :param num_perm: number of MinHash permutations
        :param threshold: Jaccard similarity threshold for a match
        """
        self._word_bank: WordBankManager = word_bank
        self._num_perm: int = num_perm
        self._threshold: float = threshold
        self._word_hashes: list[tuple[str, Any]] = []
        self.reload()

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "minhash"

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 7

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    def is_available(self) -> bool:
        """Whether datasketch is installed."""
        return _MINHASH_AVAILABLE

    def reload(self) -> None:
        """Rebuild the word MinHashes after the word bank changes."""
        self._word_hashes = []
        if not _MINHASH_AVAILABLE:
            return
        for word in self._word_bank.snapshot.words:
            minhash: Any = _MinHashImpl(num_perm=self._num_perm)
            for shingle in self._shingles(word):
                minhash.update(shingle.encode("utf-8"))
            self._word_hashes.append((word, minhash))

    @staticmethod
    def _shingles(text: str) -> list[str]:
        """Split text into lowercase character n-grams.

        :param text: input text
        :return: the n-gram shingles
        """
        normalized: str = UnicodeUtils.prepare(text).lower()
        if len(normalized) < _SHINGLE_SIZE:
            return [normalized]
        return [
            normalized[index : index + _SHINGLE_SIZE]
            for index in range(len(normalized) - _SHINGLE_SIZE + 1)
        ]

    def detect(self, text: str) -> DetectionResult:
        """Compare the text MinHash against every word MinHash.

        :param text: normalized input text
        :return: the near-duplicate words when similarity is high enough
        """
        if not self._word_hashes:
            return DetectionResult(matched=False)
        text_minhash: Any = _MinHashImpl(num_perm=self._num_perm)
        for shingle in self._shingles(text):
            text_minhash.update(shingle.encode("utf-8"))
        best_word: str | None = None
        best_similarity: float = 0.0
        # ponytail: linear scan over word hashes; swap for LSH when the word bank grows
        for word, word_minhash in self._word_hashes:
            similarity: float = text_minhash.jaccard(word_minhash)
            if similarity > best_similarity:
                best_word = word
                best_similarity = similarity
        if best_word is None or best_similarity < self._threshold:
            return DetectionResult(matched=False)
        return DetectionResult(
            matched=True,
            matched_words=(best_word,),
            reason="Text is a near-duplicate of a dictionary phrase",
            confidence_score=best_similarity,
        )
