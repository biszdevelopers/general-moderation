"""Critical phrase manager.

Owns the critical-phrase store and a compiled Aho-Corasick automaton over the
phrases. ``detect`` returns the matched phrases with the highest severity and
its category, which the engine promotes to a hard block or a suspicion-score
floor according to the per-app policy.
"""

from __future__ import annotations

from typing import Any

from app.models.verdict import DetectionResult
from app.phrases.models import CriticalPhrase
from app.phrases.storage import SqlitePhraseStorage
from app.utils.unicode_utils import UnicodeUtils


class CriticalPhraseManager:
    """Coordinates the phrase store and the compiled automaton.

    :param db_path: path to the critical-phrases SQLite database
    """

    def __init__(self, db_path: str) -> None:
        self._storage: SqlitePhraseStorage = SqlitePhraseStorage(db_path)
        self._automaton: Any | None = None
        self._severity: dict[str, int] = {}
        self._category: dict[str, str] = {}
        self._language: dict[str, str] = {}
        self.reload()

    @staticmethod
    def _automaton_module() -> Any | None:
        """Resolve the Aho-Corasick module regardless of its import name.

        :return: the Automaton class, or None when unavailable
        """
        for module_name in ("ahocorasick", "pyahocorasick"):
            try:
                module: Any = __import__(module_name)
                return module.Automaton
            except (ImportError, AttributeError):
                continue
        return None

    @property
    def storage(self) -> SqlitePhraseStorage:
        """Return the underlying phrase store."""
        return self._storage

    def is_available(self) -> bool:
        """Whether the automaton holds at least one phrase."""
        return self._automaton is not None and bool(self._severity)

    def add(self, phrase: str, category: str, severity: int, language: str) -> CriticalPhrase:
        """Add a phrase and rebuild the automaton.

        :param phrase: the phrase to add, normalized by the caller
        :param category: semantic bucket
        :param severity: severity score
        :param language: ISO 639-1 language code
        :return: the persisted CriticalPhrase
        :raises ValueError: when the phrase already exists
        """
        created: CriticalPhrase = self._storage.add(phrase, language, category, severity)
        self.reload()
        return created

    def remove(self, phrase_id: int) -> bool:
        """Remove a phrase and rebuild the automaton.

        :param phrase_id: identifier of the phrase to remove
        :return: True when a phrase was removed
        """
        removed: bool = self._storage.remove(phrase_id)
        if removed:
            self.reload()
        return removed

    def update(self, phrase_id: int, **fields: object) -> CriticalPhrase:
        """Update a phrase and rebuild the automaton.

        :param phrase_id: identifier of the phrase to update
        :param fields: allowed keys are phrase, language, category, severity
        :return: the updated CriticalPhrase
        :raises ValueError: when the phrase id does not exist
        """
        updated: CriticalPhrase = self._storage.update(phrase_id, **fields)
        self.reload()
        return updated

    def list_all(self) -> list[CriticalPhrase]:
        """Return every stored phrase.

        :return: the phrases ordered by id ascending
        """
        return self._storage.list_all()

    def reload(self) -> None:
        """Rebuild the automaton and severity/category maps."""
        phrases: list[CriticalPhrase] = self._storage.list_all()
        self._severity = {item.phrase: item.severity for item in phrases}
        self._category = {item.phrase: item.category for item in phrases}
        self._language = {item.phrase: item.language for item in phrases}
        automaton_class: Any | None = self._automaton_module()
        if automaton_class is None or not phrases:
            self._automaton = None
            return
        automaton: Any = automaton_class()
        for item in phrases:
            automaton.add_word(item.phrase, item.phrase)
        automaton.make_automaton()
        self._automaton = automaton

    def detect(self, text: str) -> DetectionResult:
        """Scan the text for stored phrases.

        :param text: normalized input text
        :return: a positive result with the max severity when any phrase occurs
        """
        if not self.is_available():
            return DetectionResult(matched=False)
        normalized: str = UnicodeUtils.prepare(text)
        matched: list[str] = []
        for _, stored_phrase in self._automaton.iter(normalized):
            matched.append(str(stored_phrase))
        if not matched:
            return DetectionResult(matched=False)
        matched = list(dict.fromkeys(matched))
        best: str = max(matched, key=lambda phrase: self._severity.get(phrase, 0))
        return DetectionResult(
            matched=True,
            matched_words=tuple(matched),
            severity=self._severity.get(best) or None,
            category=self._category.get(best),
            reason="Critical phrase matched",
            confidence_score=0.95,
        )

    def close(self) -> None:
        """Release storage resources."""
        self._storage.close()
