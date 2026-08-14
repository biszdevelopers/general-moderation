"""Base word list loading from installed pip packages.

The service keeps no local sensitive-word text files. Base dictionaries are
pulled from the C/C++/Rust pip packages at runtime; this loader runs one
small resolver per wired package and merges everything it finds into a
deduplicated tuple. Missing or unreadable packages are skipped silently so the
service stays operational regardless of which dictionaries are installed.

The resolvers use the real, installed package APIs (not guessed attribute
names), so the base word list is actually non-empty on a stock install.
"""

from __future__ import annotations

import importlib
from collections.abc import Callable, Iterable
from typing import Any

_STRING_TYPES: tuple[type, ...] = (str, bytes)


def _badwords_words() -> list[str]:
    """Return the union of every language dictionary bundled by ``badwords``."""
    module: Any = importlib.import_module("badwords")
    instance: Any = module.ProfanityFilter()
    instance.init()
    words: Any = getattr(instance, "bad_words", None)
    return (
        list(words) if isinstance(words, Iterable) and not isinstance(words, _STRING_TYPES) else []
    )


def _glin_words() -> list[str]:
    """Return the active word set exposed by ``glin_profanity``."""
    module: Any = importlib.import_module("glin_profanity")
    instance: Any = module.Filter()
    words: Any = getattr(instance, "words", None)
    return (
        list(words) if isinstance(words, Iterable) and not isinstance(words, _STRING_TYPES) else []
    )


def _pyprofane_words() -> list[str]:
    """Return the profanity dictionary exposed by ``PyProfane``."""
    module: Any = importlib.import_module("PyProfane")
    words: Any = module.getProfaneWords()
    return (
        list(words) if isinstance(words, Iterable) and not isinstance(words, _STRING_TYPES) else []
    )


# One resolver per wired package that exposes a usable dictionary. profanite
# and gangajal expose no word collection on their public APIs and are skipped.
_PACKAGE_RESOLVERS: tuple[Callable[[], list[str]], ...] = (
    _badwords_words,
    _glin_words,
    _pyprofane_words,
)


class WordListLoader:
    """Collect base dictionaries from installed pip packages."""

    _cache: tuple[str, ...] | None = None

    @classmethod
    def _resolve_words(cls, resolver: Callable[[], list[str]]) -> list[str]:
        """Run one resolver, tolerating any import or API failure.

        :param resolver: callable returning a word collection
        :return: the extracted words, or an empty list on failure
        """
        try:
            return resolver()
        except Exception:
            return []

    @classmethod
    def load_from_packages(cls) -> tuple[str, ...]:
        """Merge every extractable word list from the installed packages.

        Results are cached for the process lifetime because the installed
        package dictionaries never change at runtime; the word bank reloads
        stay cheap after the first extraction.

        :return: a deduplicated, lowercased tuple of base words
        """
        if cls._cache is not None:
            return cls._cache
        collected: set[str] = set()
        for resolver in _PACKAGE_RESOLVERS:
            for entry in cls._resolve_words(resolver):
                if isinstance(entry, str) and entry.strip():
                    collected.add(entry.strip().lower())
        cls._cache = tuple(sorted(collected))
        return cls._cache

    @classmethod
    def invalidate_cache(cls) -> None:
        """Drop the cached base words (used by tests)."""
        cls._cache = None
