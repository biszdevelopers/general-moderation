"""Multi-language detector (Layer 6).

Initializes the installed C/C++/Rust/WebAssembly profanity packages in the
specified priority order and runs each one over the text. Every package is
optional: a missing module, a disabled toggle, or a package whose API is not
usable simply skips that package, so the service stays operational regardless
of which dictionaries are installed.

Only packages that actually work on the supported platforms are wired here.
Packages such as ``badwords-py``, ``safetext``, ``profanity-filter2``,
``sensitive-word-filter``, ``sensitive-word-filter-cn``, ``valx``, and
``scheckbl`` are either absent from PyPI or carry broken dependencies or
broken Python 3.14 runtimes, so they are not registered.
"""

from __future__ import annotations

import importlib
import inspect
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
    "isProfane",
    "validate",
    "detect",
    "score",
    "is_clean",
    "filter",
    "censor",
    "test",
)

# (module name, language scope, match mode)
# Match modes:
# - "truthy": a truthy callable result is a positive.
# - "censored": the callable returns censored text; a result that differs
#   from the input is a positive (e.g. gangajal).
_PACKAGES: tuple[tuple[str, str, str], ...] = (
    ("profanite", "any", "truthy"),
    ("glin_profanity", "multi", "truthy"),
    ("gangajal", "any", "censored"),
    ("PyProfane", "any", "truthy"),
)


class _PackageAdapter:
    """Runs one profanity package defensively.

    :param package_name: importable module name
    :param language: ISO code reported on a match
    :param mode: match strategy, "truthy" or "censored"
    """

    def __init__(self, package_name: str, language: str, mode: str) -> None:
        self.package_name: str = package_name
        self.language: str = language
        self._mode: str = mode
        self._module: Any | None = self._import()
        self._callable: Any | None = self._resolve_callable()

    def _import(self) -> Any | None:
        """Import the module.

        :return: the module object, or None when not installed
        """
        try:
            return importlib.import_module(self.package_name)
        except ImportError:
            return None

    def _resolve_callable(self) -> Any | None:
        """Find a callable on the module or on an instantiated checker class.

        Async functions are skipped because the detection pipeline is
        synchronous.

        :return: a bound callable accepting one text argument, or None
        """
        if self._module is None:
            return None
        for method in _PROFANITY_METHODS:
            candidate: Any = getattr(self._module, method, None)
            if callable(candidate) and not inspect.iscoroutinefunction(candidate):
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
                if callable(bound) and not inspect.iscoroutinefunction(bound):
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
        positive: bool = self._is_positive(text, result)
        if positive:
            return DetectionResult(
                matched=True,
                matched_language=self.language,
                reason=f"{self.package_name} flagged the text",
                confidence_score=0.8,
            )
        return DetectionResult(matched=False)

    def _is_positive(self, text: str, result: Any) -> bool:
        """Evaluate the callable result against the match mode.

        :param text: the input that was passed to the callable
        :param result: the callable output
        :return: True when the result indicates a match
        """
        if self._mode == "censored":
            return isinstance(result, str) and result != text
        return bool(result)


class MultiLanguageDetector(DetectorInterface):
    """Runs the verified multi-language packages in priority order.

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
            "profanite": self._settings.enable_profanite,
            "glin_profanity": self._settings.enable_glin_profanity,
            "gangajal": self._settings.enable_gangajal,
            "PyProfane": self._settings.enable_pyprofane,
        }
        adapters: list[_PackageAdapter] = []
        for package_name, language, mode in _PACKAGES:
            if not toggles.get(package_name, True):
                continue
            adapter: _PackageAdapter = _PackageAdapter(package_name, language, mode)
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

    def reload(self) -> None:
        """No-op: package adapters are fixed for the process lifetime."""

    def available_packages(self) -> list[str]:
        """List the names of the usable packages.

        :return: names of installed and callable packages
        """
        return [adapter.package_name for adapter in self._adapters if adapter.available]

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
