"""Shared interface implemented by every detector in the pipeline."""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.models.verdict import DetectionResult


class DetectorInterface(ABC):
    """Contract for a single moderation detector.

    Detectors are ordered by their numeric ``priority``; lower values run
    first. A detector either returns a positive ``DetectionResult`` or a
    non-matching one; the engine aggregates these into the final verdict.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Return the stable detector name used in logs and responses."""

    @property
    @abstractmethod
    def priority(self) -> int:
        """Return the pipeline position of this detector."""

    @property
    @abstractmethod
    def language(self) -> str:
        """Return the ISO language code, or "any" when language-neutral."""

    @property
    def blocking(self) -> bool:
        """Whether a match immediately yields a BLOCK verdict.

        Exact matchers override this to True; probabilistic matchers keep the
        default False, which yields a REVIEW verdict instead.
        """
        return False

    @abstractmethod
    def detect(self, text: str) -> DetectionResult:
        """Analyze ``text`` and return the detection outcome.

        :param text: already-normalized input text
        :return: the detection result
        """

    def is_available(self) -> bool:
        """Whether the underlying library is installed and usable.

        :return: True when the detector can run
        """
        return True

    def reload(self) -> None:
        """Rebuild any cached structures after the word bank changes."""
