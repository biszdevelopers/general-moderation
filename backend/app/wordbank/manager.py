"""Word bank manager with lock-free atomic reload.

The manager combines the base dictionaries pulled from pip packages with the
custom words persisted in storage, then compiles both into an Aho-Corasick
automaton (C) and a Bloom filter (C). ``reload()`` builds a fresh snapshot and
swaps a single reference, so concurrent readers never observe a half-built
structure and no locks are required.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

from app.utils.wordlist_loader import WordListLoader
from app.wordbank.models import CustomWord
from app.wordbank.storage import WordStorageInterface


@dataclass(frozen=True)
class WordBankSnapshot:
    """An immutable, ready-to-use view of the word bank.

    :param words: every active word (base plus custom), lowercased
    :param automaton: compiled Aho-Corasick automaton, or None when unavailable
    :param bloom: seeded Bloom filter, or None when unavailable
    """

    words: tuple[str, ...]
    automaton: Any | None
    bloom: Any | None


class WordBankManager:
    """Coordinates storage, base dictionaries, and compiled structures.

    :param storage: persistence backend for custom words
    :param bloom_capacity: Bloom filter capacity
    :param bloom_error_rate: Bloom filter false-positive rate
    :param logger: audit logger for change tracking
    """

    def __init__(
        self,
        storage: WordStorageInterface,
        bloom_capacity: int = 1_000_000,
        bloom_error_rate: float = 0.001,
        logger: Any | None = None,
    ) -> None:
        self._storage: WordStorageInterface = storage
        self._bloom_capacity: int = bloom_capacity
        self._bloom_error_rate: float = bloom_error_rate
        self._logger: Any = logger
        self._snapshot: WordBankSnapshot = WordBankSnapshot(
            words=(), automaton=None, bloom=None
        )
        self.reload()

    def add_word(
        self, word: str, language: str = "any", category: str = "other", severity: int = 1
    ) -> CustomWord:
        """Add a custom word and rebuild the snapshot.

        :param word: the term to add, normalized by the caller
        :param language: ISO 639-1 language code
        :param category: semantic bucket
        :param severity: severity score
        :return: the persisted CustomWord
        :raises ValueError: when the word already exists
        """
        created: CustomWord = self._storage.add(word, language, category, severity)
        self.reload()
        self._audit("word_added", word=word, language=language, category=category)
        return created

    def remove_word(self, word_id: int) -> bool:
        """Remove a custom word and rebuild the snapshot.

        :param word_id: identifier of the word to remove
        :return: True when a word was removed, False otherwise
        """
        removed: bool = self._storage.remove(word_id)
        if removed:
            self.reload()
            self._audit("word_removed", word_id=word_id)
        return removed

    def update_word(self, word_id: int, **fields: Any) -> CustomWord:
        """Update a custom word and rebuild the snapshot.

        :param word_id: identifier of the word to update
        :param fields: allowed keys are word, language, category, severity
        :return: the updated CustomWord
        :raises ValueError: when the word id does not exist
        """
        updated: CustomWord = self._storage.update(word_id, **fields)
        self.reload()
        self._audit("word_updated", word_id=word_id, **fields)
        return updated

    def get_all_words(self) -> list[CustomWord]:
        """Return every stored custom word.

        :return: the custom words ordered by id ascending
        """
        return self._storage.list_all()

    def import_words(self, words: list[dict[str, Any]]) -> int:
        """Bulk-import custom words.

        :param words: list of dicts with word, language, category, severity
        :return: the number of successfully imported words
        """
        imported: int = 0
        for entry in words:
            try:
                self.add_word(
                    word=str(entry["word"]),
                    language=str(entry.get("language", "any")),
                    category=str(entry.get("category", "other")),
                    severity=int(entry.get("severity", 1)),
                )
                imported += 1
            except (ValueError, KeyError):
                continue
        return imported

    def export_words(self) -> list[CustomWord]:
        """Return every custom word for export.

        :return: the custom words ordered by id ascending
        """
        return self._storage.list_all()

    def get_languages(self) -> list[str]:
        """List the distinct languages present in the word bank.

        :return: sorted language codes
        """
        return sorted({word.language for word in self._storage.list_all()})

    def get_categories(self) -> list[str]:
        """List the distinct categories present in the word bank.

        :return: sorted category names
        """
        return sorted({word.category for word in self._storage.list_all()})

    def get_stats(self) -> dict[str, Any]:
        """Return summary statistics for the word bank.

        :return: dict with total, custom, base, and language counts
        """
        custom: list[CustomWord] = self._storage.list_all()
        return {
            "total_words": len(self._snapshot.words),
            "custom_words": len(custom),
            "base_words": len(self._snapshot.words) - len(custom),
            "languages": len(self.get_languages()),
            "categories": len(self.get_categories()),
        }

    def reload(self) -> None:
        """Rebuild the automaton and Bloom filter, then swap the snapshot.

        The new snapshot is fully built before the single reference swap,
        making the reload atomic with respect to concurrent readers.
        """
        custom_words: list[CustomWord] = self._storage.list_all()
        base_words: tuple[str, ...] = WordListLoader.load_from_packages()
        all_words: tuple[str, ...] = tuple(
            dict.fromkeys((*base_words, *(word.word for word in custom_words)))
        )
        self._snapshot = WordBankSnapshot(
            words=all_words,
            automaton=self._build_automaton(all_words),
            bloom=self._build_bloom(all_words),
        )
        self._audit("wordbank_reloaded", total_words=len(all_words))

    @property
    def snapshot(self) -> WordBankSnapshot:
        """Return the current snapshot.

        :return: the active immutable snapshot
        """
        return self._snapshot

    def close(self) -> None:
        """Release storage resources."""
        self._storage.close()

    def _build_automaton(self, words: tuple[str, ...]) -> Any | None:
        """Compile the words into an Aho-Corasick automaton.

        :param words: the words to index
        :return: a pyahocorasick Automaton, or None when unavailable
        """
        try:
            from pyahocorasick import Automaton
        except ImportError:
            return None
        if not words:
            return None
        automaton: Automaton = Automaton()
        for word in words:
            automaton.add_word(word, len(word))
        automaton.make_automaton()
        return automaton

    def _build_bloom(self, words: tuple[str, ...]) -> Any | None:
        """Seed a Bloom filter with the words.

        :param words: the words to index
        :return: a pybloom_live BloomFilter, or None when unavailable
        """
        try:
            from pybloom_live import BloomFilter
        except ImportError:
            return None
        if not words:
            return None
        bloom: Any = BloomFilter(capacity=self._bloom_capacity, error_rate=self._bloom_error_rate)
        for word in words:
            bloom.add(word)
        return bloom

    def _audit(self, event: str, **fields: Any) -> None:
        """Emit a structured audit record when a logger is configured.

        :param event: short event name
        :param fields: structured event fields
        """
        if self._logger is not None:
            self._logger.log(logging.INFO, f"wordbank:{event}", **fields)
