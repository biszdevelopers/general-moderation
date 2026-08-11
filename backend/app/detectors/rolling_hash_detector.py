"""Rolling hash spam detector (Layer 2).

MurmurHash3 (C) is applied to incoming message text; messages that repeat
within the TTL window reuse the verdict of their first occurrence. The cache
is a plain LRU keyed by 64-bit hash, bounded by ``spam_cache_size``.
"""

from __future__ import annotations

import time
from collections import OrderedDict
from collections.abc import MutableMapping

import mmh3

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.unicode_utils import UnicodeUtils


class RollingHashDetector(DetectorInterface):
    """Repeat-message detector using a hashed LRU spam cache."""

    def __init__(self, cache_size: int = 10_000, ttl_seconds: int = 60) -> None:
        """Configure the spam cache.

        :param cache_size: maximum number of tracked message hashes
        :param ttl_seconds: how long a hash stays relevant
        """
        self._cache_size: int = cache_size
        self._ttl_seconds: int = ttl_seconds
        self._cache: MutableMapping[int, tuple[float, bool]] = OrderedDict()

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "rolling_hash"

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 2

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    def reload(self) -> None:
        """No-op: the spam cache is independent of the word bank."""

    def _hash(self, text: str) -> int:
        """Compute the 64-bit MurmurHash3 of the normalized text.

        :param text: input text
        :return: signed 64-bit hash value
        """
        return mmh3.hash64(UnicodeUtils.prepare(text))[0]

    def detect(self, text: str) -> DetectionResult:
        """Check whether the text repeats a recently-flagged message.

        :param text: normalized input text
        :return: a match when an earlier identical message was flagged
        """
        now: float = time.monotonic()
        message_hash: int = self._hash(text)
        entry: tuple[float, bool] | None = self._cache.get(message_hash)
        if entry is not None and entry[0] > now:
            self._cache.move_to_end(message_hash)
            previously_matched: bool = entry[1]
            if previously_matched:
                return DetectionResult(
                    matched=True,
                    reason="Repeated message previously flagged",
                    confidence_score=0.9,
                )
            return DetectionResult(matched=False)
        self._cache[message_hash] = (now + self._ttl_seconds, False)
        self._evict(now)
        return DetectionResult(matched=False)

    def record_hit(self, text: str) -> None:
        """Mark a message as flagged so repeats are caught quickly.

        :param text: the message that was flagged by a later layer
        """
        now: float = time.monotonic()
        self._cache[self._hash(text)] = (now + self._ttl_seconds, True)
        self._evict(now)

    def _evict(self, now: float) -> None:
        """Drop expired then overflow entries from the LRU cache.

        :param now: current monotonic timestamp
        """
        while self._cache:
            oldest_key: int = next(iter(self._cache))
            oldest_expiry, _ = self._cache[oldest_key]
            if oldest_expiry > now:
                break
            del self._cache[oldest_key]
        while len(self._cache) > self._cache_size:
            self._cache.popitem(last=False)
