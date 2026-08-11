"""Base word list loading from installed pip packages.

The service keeps no local sensitive-word text files. Base dictionaries are
pulled from the C/C++/Rust pip packages at runtime; this loader introspects
those modules for collection attributes and merges everything it finds into a
deduplicated tuple. Missing or unreadable packages are skipped silently so the
service stays operational regardless of which dictionaries are installed.
"""

from __future__ import annotations

import importlib
from collections.abc import Iterable
from typing import Any

# Candidate (module, attribute-path) pairs for each installed package.
_PACKAGE_ATTRIBUTES: list[tuple[str, tuple[str, ...]]] = [
    ("badwords", ("words",)),
    ("badwords", ("WORDS",)),
    ("badwords", ("all_words",)),
    ("profanite", ("words",)),
    ("profanite", ("PROFANITY_WORDS",)),
    ("glin_profanity", ("words",)),
    ("glin_profanity", ("profanities",)),
    ("gangajal", ("words",)),
    ("scheckbl", ("WORDS",)),
    ("valx", ("words",)),
    ("PyProfane", ("words",)),
    ("PyProfane", ("all_profanities",)),
]


class WordListLoader:
    """Collect base dictionaries from installed pip packages."""

    @staticmethod
    def _resolve_attribute(module: Any, path: tuple[str, ...]) -> Any:
        """Walk a dotted attribute path on a module.

        :param module: imported module object
        :param path: sequence of attribute names
        :return: the resolved value, or None when any step is missing
        """
        current: Any = module
        for name in path:
            if not hasattr(current, name):
                return None
            current = getattr(current, name)
        return current

    @classmethod
    def load_from_packages(cls) -> tuple[str, ...]:
        """Merge every extractable word list from the installed packages.

        :return: a deduplicated, lowercased tuple of base words
        """
        collected: set[str] = set()
        for module_name, attr_path in _PACKAGE_ATTRIBUTES:
            try:
                module: Any = importlib.import_module(module_name)
            except ImportError:
                continue
            value: Any = cls._resolve_attribute(module, attr_path)
            if not isinstance(value, Iterable) or isinstance(value, (str, bytes)):
                continue
            for entry in value:
                if isinstance(entry, str) and entry.strip():
                    collected.add(entry.strip().lower())
        return tuple(sorted(collected))
