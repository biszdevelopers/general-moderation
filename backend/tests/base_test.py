"""Base test class with performance helpers.

Shared setup is intentionally minimal: the heavy fixtures (engine, word bank,
settings) live in ``conftest.py`` and are per-test so the suite is isolated.
This class only provides the tiny convenience helpers every test file reuses.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

import pytest


class _FrozenClock:
    """A ``datetime``-like object exposing ``now`` for time-sensitive tests."""

    def __init__(self, start: datetime) -> None:
        """Anchor the clock.

        :param start: the initial frozen instant (UTC)
        """
        self._current: datetime = start.astimezone(UTC)

    def now(self, tz: Any = UTC) -> datetime:
        """Return the frozen instant.

        :param tz: timezone to attach (UTC unless overridden)
        :return: the frozen datetime
        """
        return self._current.astimezone(tz)

    @classmethod
    def fromisoformat(cls, value: str) -> datetime:
        """Parse an ISO datetime, mirroring the real class.

        :param value: ISO 8601 string
        :return: the parsed datetime
        """
        return datetime.fromisoformat(value)

    def advance(self, **delta: int) -> None:
        """Advance the clock.

        :param delta: keyword arguments accepted by :class:`timedelta`
        """
        self._current = self._current + timedelta(**delta)


class BaseTest:
    """Common helpers for all moderation test classes.

    Provides deterministic date control for archive/cycle tests and small
    SQLite/JSON utilities so individual test files stay focused on behavior.
    """

    _window_days: int = 91

    @pytest.fixture(autouse=True)
    def _isolate_time(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Freeze ``datetime.now`` at an anchored UTC date.

        Archive and profiling logic branches on the current date; anchoring
        makes every cycle test deterministic. Individual tests advance the
        clock with :meth:`advance_days` or :meth:`advance_hours`.

        :param monkeypatch: pytest monkeypatch fixture
        """
        self._clock: _FrozenClock = _FrozenClock(datetime(2026, 1, 1, tzinfo=UTC))
        monkeypatch.setattr("app.profiling.user_profiler.datetime", self._clock)
        monkeypatch.setattr("app.feedback.feedback_service.datetime", self._clock)

    def advance_days(self, days: int) -> None:
        """Advance the frozen clock by ``days``.

        :param days: number of days to move forward
        """
        self._clock.advance(days=days)

    def advance_hours(self, hours: int) -> None:
        """Advance the frozen clock by ``hours``.

        :param hours: number of hours to move forward
        """
        self._clock.advance(hours=hours)

    @staticmethod
    def insert_row(
        db_path: Path, table: str, columns: tuple[str, ...], values: tuple[object, ...]
    ) -> None:
        """Insert one row into a SQLite database.

        :param db_path: path to the database file
        :param table: target table name
        :param columns: column names
        :param values: row values matching the columns
        """
        connection: sqlite3.Connection = sqlite3.connect(str(db_path))
        try:
            placeholders: str = ", ".join("?" for _ in values)
            connection.execute(
                f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})", values
            )
            connection.commit()
        finally:
            connection.close()

    @staticmethod
    def read_rows(db_path: Path, query: str, *params: object) -> list[tuple[object, ...]]:
        """Run a SELECT and return every row.

        :param db_path: path to the database file
        :param query: the SQL statement
        :param params: bound parameters
        :return: the result rows
        """
        connection: sqlite3.Connection = sqlite3.connect(str(db_path))
        try:
            return list(connection.execute(query, params).fetchall())
        finally:
            connection.close()

    @staticmethod
    def write_json(path: Path, payload: object) -> None:
        """Write a JSON document.

        :param path: target file
        :param payload: object to serialize
        """
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
