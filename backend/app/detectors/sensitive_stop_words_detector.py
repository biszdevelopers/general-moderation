"""Sensitive-stop-words detector (Layer 0, top priority).

Runs the external ``sensitive-stop-words`` submodule lists (political, porn,
gun, ad, url) before every other detector so decisive Chinese terms are
checked first. Words are loaded through the cached, toggle-aware loader and
compiled into an Aho-Corasick automaton on first use; the lists are
Chinese-only, so the detector only scans text that contains CJK characters.
"""

from __future__ import annotations

import re
from typing import Any

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.sensitive_word_loader import SensitiveWordLoader

_CJK_RE = re.compile(r"[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af]")

# Category name -> runtime setting key for the per-category toggle.
_CATEGORY_KEYS: dict[str, str] = {
    "political": "ENABLE_SENSITIVE_STOP_WORDS_POLITICAL",
    "porn": "ENABLE_SENSITIVE_STOP_WORDS_PORN",
    "gun": "ENABLE_SENSITIVE_STOP_WORDS_GUN",
    "ad": "ENABLE_SENSITIVE_STOP_WORDS_AD",
    "url": "ENABLE_SENSITIVE_STOP_WORDS_URL",
}


class SensitiveStopWordsDetector(DetectorInterface):
    """Matches the external sensitive-stop-words submodule lists first.

    :param settings: application settings holding the submodule directory
    :param settings_service: runtime settings used to resolve category toggles
    :param logger: optional logger for the unavailable warning
    """

    def __init__(self, settings: Any, settings_service: Any, logger: Any | None = None) -> None:
        self._settings: Any = settings
        self._settings_service: Any = settings_service
        self._logger: Any = logger
        self._loader: SensitiveWordLoader = self._build_loader()
        self._automaton: Any | None = None

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "sensitive_stop_words"

    @property
    def priority(self) -> int:
        """Return the pipeline position (runs first)."""
        return 0

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "zh-CN"

    @property
    def blocking(self) -> bool:
        """Sensitive submodule matches are decisive."""
        return True

    def _build_loader(self) -> SensitiveWordLoader:
        """Create the loader with the live per-category toggles applied."""
        loader: SensitiveWordLoader = SensitiveWordLoader(self._settings.sensitive_stop_words_dir)
        for category, key in _CATEGORY_KEYS.items():
            loader.set_category_enabled(category, bool(self._settings_service.get(key, True)))
        return loader

    def is_available(self) -> bool:
        """Whether the submodule is enabled and exposes a loaded category."""
        if not bool(self._settings_service.get("ENABLE_SENSITIVE_STOP_WORDS", True)):
            return False
        return self._loader.available() and bool(self._loader.loaded_categories())

    def reload(self) -> None:
        """Rebuild the loader and drop the compiled automaton."""
        self._loader = self._build_loader()
        self._automaton = None

    def _ensure_automaton(self) -> None:
        """Build the Aho-Corasick automaton from the loaded words once."""
        if self._automaton is not None:
            return
        try:
            import ahocorasick
        except ImportError:
            return
        words: tuple[str, ...] = self._loader.all_words()
        if not words:
            return
        automaton: Any = ahocorasick.Automaton()
        for word in words:
            automaton.add_word(word, word)
        automaton.make_automaton()
        self._automaton = automaton

    def detect(self, text: str) -> DetectionResult:
        """Scan the text for submodule words.

        :param text: normalized input text
        :return: a positive result when a submodule word occurs
        """
        if not _CJK_RE.search(text):
            return DetectionResult(matched=False)
        self._ensure_automaton()
        if self._automaton is None:
            return DetectionResult(matched=False)
        matched: list[str] = []
        for _, stored_word in self._automaton.iter(text):
            matched.append(str(stored_word))
        if not matched:
            return DetectionResult(matched=False)
        return DetectionResult(
            matched=True,
            matched_words=tuple(dict.fromkeys(matched)),
            matched_language="zh-CN",
            reason="Sensitive stop word matched from submodule lists",
            confidence_score=0.85,
        )
