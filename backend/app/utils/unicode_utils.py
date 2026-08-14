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

# Leetspeak substitutions applied by ``deobfuscate``. Lowercase keys only;
# uppercase letters are folded first by NFKC/lowercasing in the caller.
# ``1`` is ambiguous (``i`` in "k1ll", ``l`` in "1337"), so the digit-1 key is
# handled by the caller running both variants; it is mapped to ``i`` here.
_LEET = str.maketrans(
    {
        "0": "o",
        "1": "i",
        "2": "z",
        "3": "e",
        "4": "a",
        "5": "s",
        "6": "g",
        "7": "t",
        "8": "b",
        "9": "g",
        "$": "s",
        "@": "a",
        "!": "i",
    }
)
# Separators stripped between letters (e.g. "k.1.l.l"). Whitespace is kept as
# a word boundary so multi-word phrases still match their stored form.
_OBSF_PUNCT = re.compile(r"[^a-z0-9\s]+")
_OBSF_SPACES = re.compile(r"\s+")
# Variant with ``1`` mapped to ``l`` instead of ``i``.
_LEET_ONE_IS_L = str.maketrans({"1": "l", "0": "o"})


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
    def deobfuscate(text: str) -> tuple[str, str]:
        """Fold common obfuscation: leetspeak digits and letter separators.

        Converts ``k1ll y0urs3lf`` → ``kill yourself`` and ``k i l l
        yourself`` → ``kill yourself`` by substituting leetspeak digits and
        stripping punctuation between letters while preserving word
        boundaries. The digit ``1`` is ambiguous (``i`` in ``k1ll``, ``l`` in
        ``1337``), so both variants are returned.

        :param text: normalized, lowercased input
        :return: the ``1=i`` and ``1=l`` deobfuscated variants
        """
        lowered: str = text.lower()
        substituted: str = lowered.translate(_LEET)
        base: str = UnicodeUtils._join_single_chars(
            _OBSF_SPACES.sub(" ", _OBSF_PUNCT.sub("", substituted)).strip()
        )
        one_is_l: str = UnicodeUtils._join_single_chars(
            _OBSF_SPACES.sub(" ", _OBSF_PUNCT.sub("", lowered.translate(_LEET_ONE_IS_L))).strip()
        )
        return base, one_is_l

    @staticmethod
    def _join_single_chars(text: str) -> str:
        """Join consecutive single-character tokens into one word.

        ``k i l l yourself`` → ``kill yourself``, catching the spaced-letter
        evasion pattern while preserving real word boundaries.
        """
        tokens: list[str] = text.split()
        if len(tokens) < 2:
            return text
        merged: list[str] = []
        index: int = 0
        while index < len(tokens):
            if len(tokens[index]) == 1:
                buffer: list[str] = []
                while index < len(tokens) and len(tokens[index]) == 1:
                    buffer.append(tokens[index])
                    index += 1
                merged.append("".join(buffer))
            else:
                merged.append(tokens[index])
                index += 1
        return " ".join(merged)

    @staticmethod
    def tokenize(text: str) -> list[str]:
        """Split text into lowercased word tokens.

        Uses the C-backed ``regex`` module when available, falling back to the
        standard library ``re`` module.

        :param text: input text
        :return: lowercased tokens in document order
        """
        if _compiled_regex is not None:
            return _compiled_regex.findall(
                r"\w+", UnicodeUtils.prepare(text), _compiled_regex.UNICODE
            )
        return _TOKEN_PATTERN.findall(UnicodeUtils.prepare(text))
