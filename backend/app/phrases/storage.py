"""Critical phrase persistence.

High-severity multi-word phrases live in their own SQLite table so operators
can manage them independently of the general word bank. Each phrase carries a
category and a severity (0-10) that drives the hard-block policy.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path


@dataclass(frozen=True)
class CriticalPhrase:
    """A single high-severity phrase.

    :param id: storage-assigned identifier
    :param phrase: the phrase, NFKC-normalized and lowercased
    :param language: ISO 639-1 language code, or "any"
    :param category: semantic bucket
    :param severity: severity from 0 to 10, higher is more severe
    :param created_at: ISO 8601 UTC timestamp of creation
    """

    id: int
    phrase: str
    language: str
    category: str
    severity: int
    created_at: str


class SqlitePhraseStorage:
    """SQLite-backed storage for critical phrases."""

    _SCHEMA = """
        CREATE TABLE IF NOT EXISTS critical_phrases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phrase TEXT NOT NULL UNIQUE,
            language TEXT NOT NULL DEFAULT 'any',
            category TEXT NOT NULL DEFAULT 'other',
            severity INTEGER NOT NULL DEFAULT 5,
            created_at TEXT NOT NULL
        )
    """

    _ALLOWED_FIELDS = frozenset({"phrase", "language", "category", "severity"})

    def __init__(self, db_path: str) -> None:
        """Open the database and create the schema if needed.

        :param db_path: filesystem path to the SQLite file
        """
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._connection: sqlite3.Connection = sqlite3.connect(db_path, check_same_thread=False)
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.executescript(SqlitePhraseStorage._SCHEMA)
        self._connection.commit()

    @staticmethod
    def _now() -> str:
        """Return the current UTC time as an ISO 8601 string."""
        return datetime.now(UTC).isoformat()

    def add(self, phrase: str, language: str, category: str, severity: int) -> CriticalPhrase:
        """Insert a phrase using parameterized SQL.

        :param phrase: normalized phrase
        :param language: ISO 639-1 language code
        :param category: semantic bucket
        :param severity: severity score
        :return: the persisted CriticalPhrase
        :raises ValueError: when the phrase already exists
        """
        created_at: str = self._now()
        try:
            cursor = self._connection.execute(
                "INSERT INTO critical_phrases (phrase, language, category, severity, created_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (phrase, language, category, severity, created_at),
            )
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"Phrase already exists: {phrase!r}") from exc
        self._connection.commit()
        return CriticalPhrase(
            id=cursor.lastrowid or 0,
            phrase=phrase,
            language=language,
            category=category,
            severity=severity,
            created_at=created_at,
        )

    def remove(self, phrase_id: int) -> bool:
        """Delete a phrase by id.

        :param phrase_id: identifier of the phrase to delete
        :return: True when a row was deleted, False otherwise
        """
        cursor = self._connection.execute("DELETE FROM critical_phrases WHERE id = ?", (phrase_id,))
        self._connection.commit()
        return cursor.rowcount > 0

    def update(self, phrase_id: int, **fields: object) -> CriticalPhrase:
        """Update mutable fields of a stored phrase.

        :param phrase_id: identifier of the phrase to update
        :param fields: allowed keys are phrase, language, category, severity
        :return: the updated CriticalPhrase
        :raises ValueError: when the phrase id does not exist
        """
        invalid: set[str] = set(fields) - SqlitePhraseStorage._ALLOWED_FIELDS
        if invalid:
            raise ValueError(f"Unknown fields: {sorted(invalid)}")
        if not fields:
            existing: CriticalPhrase | None = self._find(phrase_id)
            if existing is None:
                raise ValueError(f"Phrase not found: {phrase_id}")
            return existing
        assignments: list[str] = []
        parameters: list[object] = []
        for key, value in fields.items():
            assignments.append(f"{key} = ?")
            parameters.append(value)
        parameters.append(phrase_id)
        self._connection.execute(
            f"UPDATE critical_phrases SET {', '.join(assignments)} WHERE id = ?",
            tuple(parameters),
        )
        self._connection.commit()
        updated: CriticalPhrase | None = self._find(phrase_id)
        if updated is None:
            raise ValueError(f"Phrase not found: {phrase_id}")
        return updated

    def list_all(self) -> list[CriticalPhrase]:
        """Return every stored phrase, ordered by id ascending."""
        rows = self._connection.execute(
            "SELECT id, phrase, language, category, severity, created_at "
            "FROM critical_phrases ORDER BY id ASC"
        ).fetchall()
        return [CriticalPhrase(*row) for row in rows]

    def _find(self, phrase_id: int) -> CriticalPhrase | None:
        """Fetch a single phrase by id.

        :param phrase_id: identifier of the phrase
        :return: the phrase or None when absent
        """
        row = self._connection.execute(
            "SELECT id, phrase, language, category, severity, created_at "
            "FROM critical_phrases WHERE id = ?",
            (phrase_id,),
        ).fetchone()
        return CriticalPhrase(*row) if row else None

    def close(self) -> None:
        """Close the underlying connection."""
        self._connection.close()
