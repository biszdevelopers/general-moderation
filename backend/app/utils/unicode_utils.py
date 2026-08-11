"""Unicode normalization helpers.

Normalization is delegated to the C-implemented ``unicodedata`` module from
the Python standard library.
"""

from __future__ import annotations

import re
import unicodedata


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
