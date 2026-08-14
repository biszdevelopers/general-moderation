"""High-severity phrase detector (Layer 7).

Detects administrator-curated critical phrases (multi-word or otherwise) that
carry an explicit severity. The detector itself is non-blocking; the engine
promotes a match to a hard BLOCK when its severity clears the per-app
``SEVERITY_HARD_BLOCK_THRESHOLD``, otherwise the severity feeds the suspicion
score floor so ambiguous high-severity content escalates to the LLM.
"""

from __future__ import annotations

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.phrases.manager import CriticalPhraseManager
from app.utils.unicode_utils import UnicodeUtils


class PhraseDetector(DetectorInterface):
    """Matches critical phrases and reports their severity."""

    def __init__(self, manager: CriticalPhraseManager) -> None:
        """Bind the detector to the shared phrase manager.

        :param manager: manager whose automaton supplies the phrase matches
        """
        self._manager: CriticalPhraseManager = manager

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "phrase_detector"

    @property
    def priority(self) -> int:
        """Return the pipeline position (after the multi-language packages)."""
        return 7

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    def is_available(self) -> bool:
        """Whether at least one phrase is loaded."""
        return self._manager.is_available()

    def reload(self) -> None:
        """Rebuild the automaton after the phrase store changes."""
        self._manager.reload()

    def detect(self, text: str) -> DetectionResult:
        """Scan the text for critical phrases, including obfuscated variants.

        Runs the exact automaton first, then a deobfuscated pass so leetspeak
        and separator-heavy evasions (``k1ll y0urs3lf``, ``k i l l``) still
        match the stored phrase.

        :param text: normalized input text
        :return: a positive result with the maximum matched severity
        """
        result: DetectionResult = self._manager.detect(text)
        if result.matched:
            return result
        variants: tuple[str, str] = UnicodeUtils.deobfuscate(text)
        plain: str = UnicodeUtils.prepare(text)
        if all(variant == plain for variant in variants):
            return result
        for variant in variants:
            obfuscated: DetectionResult = self._manager.detect(variant)
            if not obfuscated.matched:
                continue
            return DetectionResult(
                matched=True,
                matched_words=obfuscated.matched_words,
                severity=obfuscated.severity,
                category=obfuscated.category,
                reason="Critical phrase matched (obfuscated)",
                confidence_score=obfuscated.confidence_score,
            )
        return result
