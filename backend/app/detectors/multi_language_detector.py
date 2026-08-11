"""Multi-language detector (Layer 6).

Initializes the installed C/C++/Rust/WebAssembly profanity packages in the
specified priority order and runs each one over the text. Every package is
optional: a missing module, a disabled toggle, or a package whose API is not
usable simply skips that package, so the service stays operational regardless
of which dictionaries are installed.

Eight packages are guard-wired with their real-world APIs. Five activate on a
standard PyPI install:

- ``profanite`` (Rust) via ``contains_profanity``
- ``glin_profanity`` (C) via ``Filter.is_profane``
- ``badwords`` (Rust) via ``ProfanityFilter.init()`` + ``filter_text``
- ``gangajal`` (WebAssembly) via ``validate`` (returns censored text)
- ``PyProfane`` (C) via ``isProfane``

Three more are wired behind import guards and stay dormant because no
installable release exists on the reachable indexes; they activate only when
a working index or mirror provides them (add via ``uv add``):

- ``safetext`` via ``SafeText(language).check_profanity``
- ``sensitive_word_filter_cn`` via ``SensitiveWordFilter.contains``
- ``profanity_filter`` (profanity-filter2) via ``ProfanityFilter.is_profane``

The remaining packages are intentionally not registered:

- ``scheckbl``: exposes only async functions and has no ``has_bad_word`` API
- ``valx``: has no ``get_hate_score`` API and its model is non-functional on
  the supported runtimes
- ``datasketch``: MinHash semantic similarity is not a direct profanity
  detector and would need a pre-built toxic signature database
"""

from __future__ import annotations

import importlib
import inspect
import logging
from collections.abc import Callable
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
    ("badwords", "multi", "truthy"),
    ("safetext", "multi", "truthy"),
    ("sensitive_word_filter_cn", "zh-CN", "truthy"),
    ("profanity_filter", "any", "truthy"),
    ("gangajal", "any", "censored"),
    ("PyProfane", "any", "truthy"),
)


def _prepare_badwords(module: Any) -> Any:
    """Return a ready-to-use badwords check callable.

    badwords bundles its dictionaries under non-standard language codes, so it
    is initialized without arguments to load every bundled language.

    :param module: the imported badwords module
    :return: a bound ``filter_text`` callable, or None on failure
    """
    instance: Any = module.ProfanityFilter()
    instance.init()
    return instance.filter_text


def _prepare_safetext(module: Any) -> Any:
    """Return a ready-to-use safetext check callable.

    safetext requires a language at construction time; try each supported
    language and use the first one that constructs.

    :param module: the imported safetext module
    :return: a bound ``check_profanity`` callable, or None on failure
    """
    for language in ("en", "es", "zh", "tr", "ja", "ru", "fr", "de", "it", "pt", "nl", "ko", "ar"):
        try:
            instance: Any = module.SafeText(language=language)
            return instance.check_profanity
        except Exception:
            continue
    return None


# Per-package preparation functions for packages whose check callable requires
# explicit initialization before use.
_PREPARE_FUNCTIONS: dict[str, Callable[[Any], Any]] = {
    "badwords": _prepare_badwords,
    "safetext": _prepare_safetext,
}


class _PackageAdapter:
    """Runs one profanity package defensively.

    :param package_name: importable module name
    :param language: ISO code reported on a match
    :param mode: match strategy, "truthy" or "censored"
    :param prepare: optional factory that returns the check callable
    """

    def __init__(
        self,
        package_name: str,
        language: str,
        mode: str,
        prepare: Callable[[Any], Any] | None = None,
    ) -> None:
        self.package_name: str = package_name
        self.language: str = language
        self._mode: str = mode
        self._module: Any | None = self._import()
        self._callable: Any | None = self._resolve_callable(prepare)

    def _import(self) -> Any | None:
        """Import the module.

        :return: the module object, or None when not installed
        """
        try:
            return importlib.import_module(self.package_name)
        except ImportError:
            return None

    def _resolve_callable(self, prepare: Callable[[Any], Any] | None) -> Any | None:
        """Find a callable on the module or on an instantiated checker class.

        When a ``prepare`` factory is supplied it wins, because some packages
        require explicit initialization before their check method works.
        Async functions are skipped because the detection pipeline is
        synchronous.

        :param prepare: optional callable returning the check callable
        :return: a bound callable accepting one text argument, or None
        """
        if self._module is None:
            return None
        if prepare is not None:
            try:
                prepared: Any = prepare(self._module)
            except Exception:
                return None
            return prepared if callable(prepared) else None
        return self._resolve_generic_callable()

    def _resolve_generic_callable(self) -> Any | None:
        """Find a check callable on the module or an instantiated class.

        :return: a bound callable accepting one text argument, or None
        """
        assert self._module is not None
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
    """Runs the wired multi-language packages in priority order.

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
            "badwords": self._settings.enable_badwords_py,
            "profanite": self._settings.enable_profanite,
            "glin_profanity": self._settings.enable_glin_profanity,
            "safetext": self._settings.enable_safetext,
            "sensitive_word_filter_cn": self._settings.enable_sensitive_word_filter_cn,
            "profanity_filter": self._settings.enable_profanity_filter,
            "gangajal": self._settings.enable_gangajal,
            "PyProfane": self._settings.enable_pyprofane,
        }
        adapters: list[_PackageAdapter] = []
        for package_name, language, mode in _PACKAGES:
            if not toggles.get(package_name, True):
                continue
            prepare: Callable[[Any], Any] | None = _PREPARE_FUNCTIONS.get(package_name)
            adapter: _PackageAdapter = _PackageAdapter(package_name, language, mode, prepare)
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
