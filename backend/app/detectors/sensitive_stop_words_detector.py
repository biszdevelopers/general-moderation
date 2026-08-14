"""Sensitive-stop-words detector (Layer 0, top priority).

Runs the Chinese sensitive-word lists before every other detector so decisive
terms are checked first. Sources:

- the ``sensitive-stop-words`` submodule category files (political, porn, gun,
  ad, url), each with an admin toggle;
- raw newline-delimited txt lists from ``sensitive-word-data``,
  ``sensitive-lexicon``, and ``sensitive``, matched by this service's own
  Aho-Corasick automaton.

Words are loaded through the cached, toggle-aware loader and compiled into an
Aho-Corasick automaton on first use; the lists are Chinese-only, so the
detector only scans text that contains CJK characters.
"""

from __future__ import annotations

import re
from typing import Any

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.sensitive_word_loader import SensitiveWordLoader

_CJK_RE = re.compile(r"[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af]")


class _RustMatcher:
    """Thin wrapper over the Rust ``ahocorasick_rs`` automaton.

    :param automaton: a prebuilt ``ahocorasick_rs.AhoCorasick``
    """

    __slots__ = ("_automaton",)

    def __init__(self, automaton: Any) -> None:
        self._automaton: Any = automaton

    def match(self, text: str) -> tuple[str, ...]:
        """Return the deduplicated matched words in one native call."""
        return tuple(set(self._automaton.find_matches_as_strings(text)))


class _CydMatcher:
    """Thin wrapper over the C ``ahocorasick`` automaton.

    :param automaton: a prebuilt ``ahocorasick.Automaton``
    """

    __slots__ = ("_automaton",)

    def __init__(self, automaton: Any) -> None:
        self._automaton: Any = automaton

    def match(self, text: str) -> tuple[str, ...]:
        """Return the deduplicated matched words."""
        return tuple(dict.fromkeys(str(word) for _, word in self._automaton.iter(text)))


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
        """Create the loader with the live per-category toggles applied.

        Merges the sensitive-stop-words category files with the raw extra
        lists (sensitive-word-data, sensitive-lexicon, sensitive), which are
        newline-delimited txt and are matched by this service's own
        Aho-Corasick automaton.
        """
        loader: SensitiveWordLoader = SensitiveWordLoader(
            self._settings.sensitive_stop_words_dir,
            extra_files=(
                self._settings.sensitive_word_data_dict,
                self._settings.sensitive_dict_path,
            ),
            extra_dirs=(self._settings.sensitive_lexicon_dir,),
        )
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
        """Build the native matcher from the loaded words once.

        Prefers the Rust ``ahocorasick_rs`` backend (fastest scan path) and
        falls back to the C ``ahocorasick`` automaton when Rust is missing.
        """
        if self._automaton is not None:
            return
        words: tuple[str, ...] = self._loader.all_words()
        if not words:
            return
        try:
            import ahocorasick_rs

            self._automaton = _RustMatcher(ahocorasick_rs.AhoCorasick(list(words)))
            return
        except ImportError:
            pass
        try:
            import ahocorasick

            automaton: Any = ahocorasick.Automaton()
            for word in words:
                automaton.add_word(word, word)
            automaton.make_automaton()
            self._automaton = _CydMatcher(automaton)
        except ImportError:
            return

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
        matched: tuple[str, ...] = self._automaton.match(text)
        if not matched:
            return DetectionResult(matched=False)
        return DetectionResult(
            matched=True,
            matched_words=matched,
            matched_language="zh-CN",
            reason="Sensitive stop word matched from submodule lists",
            confidence_score=0.85,
        )
