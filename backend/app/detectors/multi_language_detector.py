"""Multi-language detector (Layer 6).

Initializes every installed C/C++/Rust/WebAssembly profanity package in the
specified priority order and runs each one over the text. Every package is
optional: a missing module or a disabled toggle simply skips that package, so
the service remains operational no matter which dictionaries are installed.
"""

from __future__ import annotations

import importlib
import logging
from typing import Any

from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult
from app.utils.unicode_utils import UnicodeUtils

# Candidate method names tried on each package, in order.
_PROFANITY_METHODS: tuple[str, ...] = (
    "check",
    "is_profane",
    "is_bad",
    "contains_profanity",
    "contains_bad_words",
    "has_profanity",
    "check_profanity",
    "detect",
    "score",
    "is_clean",
    "filter",
    "censor",
    "test",
)

# (module name, language scope, alternate module name)
_PACKAGES: tuple[tuple[str, str, str | None], ...] = (
    ("badwords_py", "multi", None),
    ("profanite", "any", None),
    ("glin_profanity", "multi", None),
    ("safetext", "multi", None),
    ("sensitive_word_filter_cn", "zh-CN", None),
    ("profanity_filter2", "any", "profanity_filter"),
    ("gangajal", "any", None),
    ("scheckbl", "any", None),
    ("valx", "any", None),
    ("sensitive_word_filter", "zh-CN", None),
    ("pyprofane", "any", None),
)


class _PackageAdapter:
    """Runs one profanity package defensively.

    :param package_name: importable module name
    :param language: ISO code reported on a match
    :param alternate_name: fallback module name, if any
    """

    def __init__(
        self, package_name: str, language: str, alternate_name: str | None
    ) -> None:
        self.package_name: str = package_name
        self.language: str = language
        self._module: Any | None = self._import(alternate_name)
        self._callable: Any | None = self._resolve_callable()

    def _import(self, alternate_name: str | None) -> Any | None:
        """Import the module, trying the alternate name on failure.

        :param alternate_name: fallback module name
        :return: the module object, or None when not installed
        """
        for name in (self.package_name, alternate_name):
            if not name:
                continue
            try:
                return importlib.import_module(name)
            except ImportError:
                continue
        return None

    def _resolve_callable(self) -> Any | None:
        """Find a callable on the module or on an instantiated checker class.

        :return: a bound callable accepting one text argument, or None
        """
        if self._module is None:
            return None
        for method in _PROFANITY_METHODS:
            candidate: Any = getattr(self._module, method, None)
            if callable(candidate):
                return candidate
        for attribute_name in dir(self._module):
            candidate = getattr(self._module, attribute_name, None)
            if not isinstance(candidate, type):
                continue
            try:
                instance: Any = candidate()
            except Exception:
                continue
            for method in _PROFANITY_METHODS:
                bound: Any = getattr(instance, method, None)
                if callable(bound):
                    return bound
        return None

    @property
    def available(self) -> bool:
        """Whether the module is installed and exposes a usable callable."""
        return self._callable is not None

    def detect(self, text: str) -> DetectionResult:
        """Run the package over the text.

        :param text: normalized input text
        :return: a positive result when the package flags the text
        """
        if self._callable is None:
            return DetectionResult(matched=False)
        try:
            result: Any = self._callable(text)
        except Exception:
            return DetectionResult(matched=False)
        if result:
            return DetectionResult(
                matched=True,
                matched_language=self.language,
                reason=f"{self.package_name} flagged the text",
                confidence_score=0.8,
            )
        return DetectionResult(matched=False)


class MultiLanguageDetector(DetectorInterface):
    """Runs all 11 multi-language packages in priority order.

    :param settings: application settings holding the package toggles
    :param logger: optional logger for skipped packages
    """

    def __init__(self, settings: Any, logger: Any | None = None) -> None:
        self._settings: Any = settings
        self._logger: Any = logger
        self._adapters: list[_PackageAdapter] = self._build_adapters()

    def _build_adapters(self) -> list[_PackageAdapter]:
        """Instantiate the adapters, honoring the enable toggles.

        :return: the list of enabled package adapters
        """
        toggles: dict[str, bool] = {
            "badwords_py": self._settings.enable_badwords_py,
            "profanite": self._settings.enable_profanite,
            "glin_profanity": self._settings.enable_glin_profanity,
            "safetext": self._settings.enable_safetext,
            "sensitive_word_filter_cn": self._settings.enable_sensitive_word_filter_cn,
            "profanity_filter2": self._settings.enable_profanity_filter,
            "gangajal": self._settings.enable_gangajal,
            "scheckbl": self._settings.enable_scheckbl,
            "valx": self._settings.enable_valx,
            "sensitive_word_filter": self._settings.enable_sensitive_word_filter,
            "pyprofane": self._settings.enable_pyprofane,
        }
        adapters: list[_PackageAdapter] = []
        for package_name, language, alternate_name in _PACKAGES:
            if not toggles.get(package_name, True):
                continue
            adapter: _PackageAdapter = _PackageAdapter(package_name, language, alternate_name)
            if not adapter.available and self._logger is not None:
                self._logger.log(
                    logging.WARNING,
                    f"multi_language:{package_name}_unavailable",
                    package=package_name,
                )
            adapters.append(adapter)
        return adapters

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "multi_language"

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 6

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "multi"

    @property
    def blocking(self) -> bool:
        """Package positives are decisive."""
        return True

    def is_available(self) -> bool:
        """Whether at least one package is usable."""
        return any(adapter.available for adapter in self._adapters)

    def available_packages(self) -> list[str]:
        """List the names of the usable packages.

        :return: names of installed and callable packages
        """
        return [
            adapter.package_name for adapter in self._adapters if adapter.available
        ]

    def detect(self, text: str) -> DetectionResult:
        """Run every enabled package over the text.

        :param text: normalized input text
        :return: aggregated positive results from all packages
        """
        normalized: str = UnicodeUtils.prepare(text)
        reasons: list[str] = []
        languages: set[str] = set()
        for adapter in self._adapters:
            if not adapter.available:
                continue
            result: DetectionResult = adapter.detect(normalized)
            if result.matched:
                reasons.append(str(result.reason))
                if result.matched_language:
                    languages.add(result.matched_language)
        if not reasons:
            return DetectionResult(matched=False)
        return DetectionResult(
            matched=True,
            matched_language=",".join(sorted(languages)) if languages else "multi",
            reason="; ".join(reasons),
            confidence_score=0.8,
        )
