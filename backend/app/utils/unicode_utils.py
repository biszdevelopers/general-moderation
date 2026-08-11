"""Unicode normalization helpers.

Normalization is delegated to the C-implemented ``unicodedata`` module from
the Python standard library.
"""

from __future__ import annotations

import re
import unicodedata

try:
    import regex as _compiled_regex
except ImportError:  # pragma: no cover - regex is the C-backed primary
    _compiled_regex = None

_TOKEN_PATTERN = re.compile(r"\w+", re.UNICODE)


class UnicodeUtils:
    """Static helpers for normalizing and cleaning input text."""

    _WHITESPACE_PATTERN = re.compile(r"\s+")

    @staticmethod
    def normalize(text: str) -> str:
        """Return the NFKC-normalized form of ``text``.

        NFKC folding converts full-width characters, ligatures, and
        compatibility variants into their canonical C-shaped equivalents,
        defeating common Unicode obfuscation tricks.

        :param text: raw input text
        :return: normalized text
        """
        return unicodedata.normalize("NFKC", text)

    @staticmethod
    def collapse_whitespace(text: str) -> str:
        """Replace every run of whitespace with a single space.

        :param text: input text
        :return: text with collapsed whitespace
        """
        return UnicodeUtils._WHITESPACE_PATTERN.sub(" ", text)

    @staticmethod
    def prepare(text: str) -> str:
        """Normalize then collapse whitespace, the canonical detector input.

        :param text: raw input text
        :return: cleaned text ready for the detection pipeline
        """
        return UnicodeUtils.collapse_whitespace(UnicodeUtils.normalize(text))

    @staticmethod
    def tokenize(text: str) -> list[str]:
        """Split text into lowercased word tokens.

        Uses the C-backed ``regex`` module when available, falling back to the
        standard library ``re`` module.

        :param text: input text
        :return: lowercased tokens in document order
        """
        if _compiled_regex is not None:
            return _compiled_regex.findall(r"\w+", UnicodeUtils.prepare(text), _compiled_regex.UNICODE)
        return _TOKEN_PATTERN.findall(UnicodeUtils.prepare(text))
