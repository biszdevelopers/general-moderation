"""Word bank persistence.

Two backends are supported:
- ``sqlite``: the default, backed by the C-implemented SQLite library with
  parameterized queries to prevent injection.
- ``json``: a single JSON document written atomically via ``atomicwrites``
  and serialized with Rust ``orjson``.
"""

from __future__ import annotations

import sqlite3
from abc import ABC, abstractmethod
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import orjson
from atomicwrites import atomic_write

from app.wordbank.models import CustomWord


class WordStorageInterface(ABC):
    """Contract implemented by every word bank storage backend."""

    @abstractmethod
    def add(self, word: str, language: str, category: str, severity: int) -> CustomWord:
        """Insert a new custom word and return the stored record.

        :param word: normalized term
        :param language: ISO 639-1 language code
        :param category: semantic bucket
        :param severity: severity score
        :return: the persisted CustomWord with its assigned id
        :raises ValueError: when the word already exists
        """

    @abstractmethod
    def remove(self, word_id: int) -> bool:
        """Delete a word by id.

        :param word_id: identifier of the word to delete
        :return: True when a row was deleted, False otherwise
        """

    @abstractmethod
    def update(self, word_id: int, **fields: Any) -> CustomWord:
        """Update mutable fields of a stored word.

        :param word_id: identifier of the word to update
        :param fields: allowed keys are word, language, category, severity
        :return: the updated CustomWord
        :raises ValueError: when the word id does not exist
        """

    @abstractmethod
    def list_all(self) -> list[CustomWord]:
        """Return every stored word, ordered by id ascending."""

    @abstractmethod
    def close(self) -> None:
        """Release any held resources."""


class SqliteWordStorage(WordStorageInterface):
    """SQLite-backed storage using the C sqlite3 module."""

    _SCHEMA = """
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL UNIQUE,
            language TEXT NOT NULL DEFAULT 'any',
            category TEXT NOT NULL DEFAULT 'other',
            severity INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL
        )
    """

    _ALLOWED_FIELDS = frozenset({"word", "language", "category", "severity"})

    def __init__(self, db_path: str) -> None:
        """Open the database and create the schema if needed.

        :param db_path: filesystem path to the SQLite file
        """
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        # Thread-pooled workers reuse one connection; WAL serializes writes.
        self._connection: sqlite3.Connection = sqlite3.connect(db_path, check_same_thread=False)
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.executescript(SqliteWordStorage._SCHEMA)
        self._connection.commit()

    @staticmethod
    def _now() -> str:
        """Return the current UTC time as an ISO 8601 string."""
        return datetime.now(UTC).isoformat()

    def add(self, word: str, language: str, category: str, severity: int) -> CustomWord:
        """Insert a word using parameterized SQL.

        :param word: normalized term
        :param language: ISO 639-1 language code
        :param category: semantic bucket
        :param severity: severity score
        :return: the persisted CustomWord
        :raises ValueError: when the word already exists
        """
        created_at: str = self._now()
        try:
            cursor = self._connection.execute(
                "INSERT INTO words (word, language, category, severity, created_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (word, language, category, severity, created_at),
            )
        except sqlite3.IntegrityError as exc:
            raise ValueError(f"Word already exists: {word!r}") from exc
        self._connection.commit()
        return CustomWord(
            id=cursor.lastrowid or 0,
            word=word,
            language=language,
            category=category,
            severity=severity,
            created_at=created_at,
        )

    def remove(self, word_id: int) -> bool:
        """Delete a word by id.

        :param word_id: identifier of the word to delete
        :return: True when a row was deleted, False otherwise
        """
        cursor = self._connection.execute("DELETE FROM words WHERE id = ?", (word_id,))
        self._connection.commit()
        return cursor.rowcount > 0

    def update(self, word_id: int, **fields: Any) -> CustomWord:
        """Update mutable fields of a stored word.

        :param word_id: identifier of the word to update
        :param fields: allowed keys are word, language, category, severity
        :return: the updated CustomWord
        :raises ValueError: when the word id does not exist
        """
        invalid: set[str] = set(fields) - SqliteWordStorage._ALLOWED_FIELDS
        if invalid:
            raise ValueError(f"Unknown fields: {sorted(invalid)}")
        if not fields:
            existing: CustomWord | None = self._find(word_id)
            if existing is None:
                raise ValueError(f"Word not found: {word_id}")
            return existing
        assignments: list[str] = []
        parameters: list[Any] = []
        for key, value in fields.items():
            assignments.append(f"{key} = ?")
            parameters.append(value)
        parameters.append(word_id)
        self._connection.execute(
            f"UPDATE words SET {', '.join(assignments)} WHERE id = ?", tuple(parameters)
        )
        self._connection.commit()
        updated: CustomWord | None = self._find(word_id)
        if updated is None:
            raise ValueError(f"Word not found: {word_id}")
        return updated

    def list_all(self) -> list[CustomWord]:
        """Return every stored word, ordered by id ascending."""
        rows = self._connection.execute(
            "SELECT id, word, language, category, severity, created_at FROM words ORDER BY id ASC"
        ).fetchall()
        return [CustomWord(*row) for row in rows]

    def _find(self, word_id: int) -> CustomWord | None:
        """Fetch a single word by id.

        :param word_id: identifier of the word
        :return: the word or None when absent
        """
        row = self._connection.execute(
            "SELECT id, word, language, category, severity, created_at FROM words WHERE id = ?",
            (word_id,),
        ).fetchone()
        return CustomWord(*row) if row else None

    def close(self) -> None:
        """Close the underlying connection."""
        self._connection.close()


class JsonWordStorage(WordStorageInterface):
    """JSON-file-backed storage with atomic writes.

    The document is a JSON array of records. Writes go through
    ``atomicwrites`` so a crash can never corrupt the file.
    """

    def __init__(self, file_path: str) -> None:
        """Load the document or create an empty one.

        :param file_path: path to the JSON document
        """
        self._file_path: str = file_path
        self._records: list[dict[str, Any]] = self._load()

    def _load(self) -> list[dict[str, Any]]:
        """Read the document from disk.

        :return: the stored record list, empty when the file is absent
        """
        path: Path = Path(self._file_path)
        if not path.exists():
            return []
        raw: bytes = path.read_bytes()
        if not raw.strip():
            return []
        return list(orjson.loads(raw))

    def _persist(self) -> None:
        """Atomically write the current record list to disk."""
        path: Path = Path(self._file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        payload: bytes = orjson.dumps(self._records, option=orjson.OPT_INDENT_2)
        with atomic_write(str(path), mode="wb", overwrite=True) as handle:
            handle.write(payload)

    def _next_id(self) -> int:
        """Return the next record identifier.

        :return: one greater than the current maximum id
        """
        return max((record.get("id", 0) for record in self._records), default=0) + 1

    @staticmethod
    def _now() -> str:
        """Return the current UTC time as an ISO 8601 string."""
        return datetime.now(UTC).isoformat()

    def add(self, word: str, language: str, category: str, severity: int) -> CustomWord:
        """Append a new record.

        :param word: normalized term
        :param language: ISO 639-1 language code
        :param category: semantic bucket
        :param severity: severity score
        :return: the persisted CustomWord
        :raises ValueError: when the word already exists
        """
        if any(record.get("word") == word for record in self._records):
            raise ValueError(f"Word already exists: {word!r}")
        record: dict[str, Any] = {
            "id": self._next_id(),
            "word": word,
            "language": language,
            "category": category,
            "severity": severity,
            "created_at": self._now(),
        }
        self._records.append(record)
        self._persist()
        return CustomWord(**record)

    def remove(self, word_id: int) -> bool:
        """Delete a record by id.

        :param word_id: identifier of the word to delete
        :return: True when a record was deleted, False otherwise
        """
        remaining: list[dict[str, Any]] = [
            record for record in self._records if record.get("id") != word_id
        ]
        if len(remaining) == len(self._records):
            return False
        self._records = remaining
        self._persist()
        return True

    def update(self, word_id: int, **fields: Any) -> CustomWord:
        """Update mutable fields of a stored record.

        :param word_id: identifier of the word to update
        :param fields: allowed keys are word, language, category, severity
        :return: the updated CustomWord
        :raises ValueError: when the word id does not exist
        """
        invalid: set[str] = set(fields) - SqliteWordStorage._ALLOWED_FIELDS
        if invalid:
            raise ValueError(f"Unknown fields: {sorted(invalid)}")
        for record in self._records:
            if record.get("id") != word_id:
                continue
            record.update(fields)
            self._persist()
            return CustomWord(**record)
        raise ValueError(f"Word not found: {word_id}")

    def list_all(self) -> list[CustomWord]:
        """Return every stored record, ordered by id ascending."""
        ordered: list[dict[str, Any]] = sorted(self._records, key=lambda r: r.get("id", 0))
        return [CustomWord(**record) for record in ordered]

    def close(self) -> None:
        """Persist any pending changes (no-op; writes are immediate)."""
        self._persist()


def create_storage(storage_type: str, path: str) -> WordStorageInterface:
    """Instantiate the storage backend named by configuration.

    :param storage_type: "sqlite" or "json"
    :param path: database or document file path
    :return: a configured WordStorageInterface
    :raises ValueError: for an unknown storage type
    """
    if storage_type == "sqlite":
        return SqliteWordStorage(path)
    if storage_type == "json":
        return JsonWordStorage(path)
    raise ValueError(f"Unknown custom words storage: {storage_type!r}")
