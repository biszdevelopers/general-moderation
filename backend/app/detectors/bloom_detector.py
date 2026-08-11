"""Bloom filter detector (Layer 1).

A C-implemented Bloom filter gives an O(1) membership test: words that are
definitely absent are rejected in under a microsecond. Hits are reported as a
weak positive (REVIEW) because Bloom filters permit false positives.
"""

from __future__ import annotations

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.unicode_utils import UnicodeUtils
from app.wordbank.manager import WordBankManager, WordBankSnapshot


class BloomFilterDetector(DetectorInterface):
    """Fast negative pre-filter backed by the C pybloom_live library."""

    def __init__(self, word_bank: WordBankManager) -> None:
        """Bind the detector to the shared word bank.

        :param word_bank: manager whose snapshot supplies the Bloom filter
        """
        self._word_bank: WordBankManager = word_bank

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "bloom_filter"

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 1

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    def is_available(self) -> bool:
        """Whether a Bloom filter exists in the current snapshot."""
        return self._word_bank.snapshot.bloom is not None

    def detect(self, text: str) -> DetectionResult:
        """Test every token against the Bloom filter.

        :param text: normalized input text
        :return: a weak positive when any token may be in the word bank
        """
        snapshot: WordBankSnapshot = self._word_bank.snapshot
        bloom = snapshot.bloom
        if bloom is None:
            return DetectionResult(matched=False)
        for token in UnicodeUtils.tokenize(text):
            if token in bloom:
                return DetectionResult(
                    matched=True,
                    matched_words=(token,),
                    reason="Token possibly present in word bank (Bloom hit)",
                    confidence_score=0.5,
                )
        return DetectionResult(matched=False)
