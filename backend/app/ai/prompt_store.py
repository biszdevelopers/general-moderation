"""Versioned storage for the editable system prompt.

Administrators edit a single system prompt template through the admin
API; every save creates a new version and any version can be reactivated.
When no version is active the built-in default prompt applies.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

from app.ai.prompt import SYSTEM_PROMPT


class PromptStore:
    """Persists prompt template versions in a small SQLite database.

    :param db_path: path to the prompts database file
    """

    _SCHEMA = """
        CREATE TABLE IF NOT EXISTS prompt_versions (
            id INTEGER PRIMARY KEY,
            template TEXT NOT NULL,
            is_active INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """

    def __init__(self, db_path: str) -> None:
        self._db_path: str = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._connection: sqlite3.Connection = sqlite3.connect(db_path, check_same_thread=False)
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.executescript(PromptStore._SCHEMA)
        self._connection.commit()

    def get_active(self) -> str:
        """Return the active template or the built-in default.

        :return: the system prompt text
        """
        row = self._connection.execute(
            "SELECT template FROM prompt_versions WHERE is_active = 1 ORDER BY id DESC LIMIT 1"
        ).fetchone()
        return str(row[0]) if row is not None else SYSTEM_PROMPT

    def save(self, template: str) -> int:
        """Store a new version and make it active.

        :param template: the prompt text to store
        :return: the new version id
        :raises ValueError: when the template is empty
        """
        if not template.strip():
            raise ValueError("Prompt template must not be empty")
        with self._connection:
            self._connection.execute("UPDATE prompt_versions SET is_active = 0")
            cursor = self._connection.execute(
                "INSERT INTO prompt_versions (template, is_active) VALUES (?, 1)",
                (template,),
            )
        return int(cursor.lastrowid)

    def list_versions(self) -> list[dict[str, object]]:
        """Return every stored version, newest first.

        :return: id, preview, active flag, and creation timestamp per version
        """
        rows = self._connection.execute(
            "SELECT id, template, is_active, created_at FROM prompt_versions ORDER BY id DESC"
        ).fetchall()
        return [
            {
                "id": row[0],
                "preview": str(row[1])[:120],
                "active": bool(row[2]),
                "created_at": row[3],
            }
            for row in rows
        ]

    def get_version(self, version_id: int) -> str | None:
        """Return one version's full template text.

        :param version_id: the version to fetch
        :return: the template, or None when the id is unknown
        """
        row = self._connection.execute(
            "SELECT template FROM prompt_versions WHERE id = ?", (version_id,)
        ).fetchone()
        return str(row[0]) if row is not None else None

    def activate(self, version_id: int) -> None:
        """Make one stored version the single active version.

        :param version_id: the version to activate
        :raises ValueError: when the id is unknown
        """
        exists = self._connection.execute(
            "SELECT id FROM prompt_versions WHERE id = ?", (version_id,)
        ).fetchone()
        if exists is None:
            raise ValueError(f"Unknown prompt version: {version_id}")
        with self._connection:
            self._connection.execute("UPDATE prompt_versions SET is_active = 0")
            self._connection.execute(
                "UPDATE prompt_versions SET is_active = 1 WHERE id = ?", (version_id,)
            )

    def close(self) -> None:
        """Close the underlying database connection."""
        self._connection.close()
