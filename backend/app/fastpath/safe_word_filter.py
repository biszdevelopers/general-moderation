"""Stage 1 fast path: safe word list and language detection.

Content that is entirely composed of approved words exits the pipeline
immediately with a PASS verdict, keeping latency under one millisecond for
clean traffic. The word list is editable through the admin UI and reloaded on
demand. Language detection uses a lightweight script heuristic and falls back
to English when no library is installed, per the pipeline contract.
"""

from __future__ import annotations

import re
import threading
from pathlib import Path
from typing import Any

_TOKEN_RE = re.compile(r"[\w'-]+", re.UNICODE)
_CJK_RE = re.compile(r"[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af]")
_CYRILLIC_RE = re.compile(r"[\u0400-\u04ff]")
_ARABIC_RE = re.compile(r"[\u0600-\u06ff]")


class SafeWordFilter:
    """Fast-path safe word whitelist.

    :param settings: application settings
    :param logger: audit logger
    """

    def __init__(self, settings: Any, logger: Any) -> None:
        self._path: str = settings.safe_word_list_path
        self._enabled: bool = bool(settings.safe_word_enabled)
        self._logger: Any = logger
        self._lock: threading.Lock = threading.Lock()
        self._words: set[str] = set()
        self._load()

    def is_available(self) -> bool:
        """Return whether the fast path is enabled."""
        return self._enabled

    def _load(self) -> None:
        """Load the safe word list from disk."""
        path: Path = Path(self._path)
        if path.exists():
            self._words = {
                line.strip().lower()
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.strip().startswith("#")
            }
        else:
            self._words = set()
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("", encoding="utf-8")

    def reload(self) -> None:
        """Reload the word list after an admin edit."""
        with self._lock:
            self._load()

    def add_word(self, word: str) -> None:
        """Append a safe word to the list.

        :param word: the safe term to add
        """
        word = word.strip().lower()
        if not word:
            return
        with self._lock:
            self._words.add(word)
            path: Path = Path(self._path)
            lines: list[str] = (
                path.read_text(encoding="utf-8").splitlines() if path.exists() else []
            )
            if word not in {line.strip().lower() for line in lines}:
                lines.append(word)
                path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def remove_word(self, word: str) -> bool:
        """Remove a safe word from the list.

        :param word: the safe term to remove
        :return: True when the word was present
        """
        word = word.strip().lower()
        if not word:
            return False
        with self._lock:
            if word not in self._words:
                return False
            self._words.discard(word)
            path: Path = Path(self._path)
            if path.exists():
                lines: list[str] = [
                    line for line in path.read_text(encoding="utf-8").splitlines() if line.strip()
                ]
                path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return True

    def words(self) -> list[str]:
        """Return the current safe word list, sorted."""
        return sorted(self._words)

    def is_safe(self, text: str) -> bool:
        """Return True when the text contains only safe tokens.

        :param text: input text
        :return: True for a fast-path PASS, False to continue the pipeline
        """
        if not self._enabled:
            return False
        tokens: list[str] = _TOKEN_RE.findall(text.lower())
        if not tokens:
            return False
        return all(token in self._words for token in tokens)

    @staticmethod
    def detect_language(text: str) -> str:
        """Identify the dominant script of a text.

        Uses the installed ``langdetect`` or ``fasttext`` package when present
        and otherwise falls back to a Unicode script heuristic. English is the
        final fallback.

        :param text: input text
        :return: an ISO 639-1 language code
        """
        try:
            from langdetect import detect

            detected: str = detect(text)
            if detected:
                return detected
        except Exception:
            pass
        try:
            import fasttext

            model = fasttext.load_model("lid.176.bin")
            return model.predict(text)[0][0].replace("__label__", "")
        except Exception:
            pass
        if _CJK_RE.search(text):
            return "zh"
        if _CYRILLIC_RE.search(text):
            return "ru"
        if _ARABIC_RE.search(text):
            return "ar"
        return "en"
