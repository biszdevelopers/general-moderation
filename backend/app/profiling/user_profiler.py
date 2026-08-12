"""91-day rolling window user profiling with cycle summaries.

Each (app_name, user_id) pair keeps at most ``USER_WINDOW_DAYS`` daily rows in
the live ``users.db``. On day 91 of a cycle the day-91 row is written, all
rows from the cycle are aggregated into a summary record in ``archive.db``,
the live rows are removed, and the summary is linked to the previous cycle's
summary through ``next_cycle_id`` (a linked-list of periods). Long-term
history is therefore always available from the summaries, while the live
table stays bounded at one window of raw data per user.
"""

from __future__ import annotations

import sqlite3
import threading
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any

_LIVE_SCHEMA = """
    CREATE TABLE IF NOT EXISTS user_daily_stats (
        id INTEGER PRIMARY KEY,
        app_name TEXT NOT NULL,
        user_id TEXT NOT NULL,
        day_offset INTEGER NOT NULL,
        total_msgs INTEGER NOT NULL DEFAULT 0,
        flagged_msgs INTEGER NOT NULL DEFAULT 0,
        blocked_msgs INTEGER NOT NULL DEFAULT 0,
        reviewed_msgs INTEGER NOT NULL DEFAULT 0,
        date TEXT NOT NULL
    )
"""
_LIVE_INDEX = (
    "CREATE INDEX IF NOT EXISTS idx_daily_user ON user_daily_stats (app_name, user_id, date)"
)

_ARCHIVE_SCHEMA = """
    CREATE TABLE IF NOT EXISTS user_summaries (
        id INTEGER PRIMARY KEY,
        app_name TEXT NOT NULL,
        user_id TEXT NOT NULL,
        cycle_id INTEGER NOT NULL,
        start_day TEXT NOT NULL,
        end_day TEXT NOT NULL,
        total_msgs INTEGER NOT NULL DEFAULT 0,
        flagged_msgs INTEGER NOT NULL DEFAULT 0,
        blocked_msgs INTEGER NOT NULL DEFAULT 0,
        reviewed_msgs INTEGER NOT NULL DEFAULT 0,
        next_cycle_id INTEGER,
        created_at TEXT NOT NULL
    )
"""
_ARCHIVE_INDEX = (
    "CREATE INDEX IF NOT EXISTS idx_summaries_user ON user_summaries (app_name, user_id, cycle_id)"
)

_ARCHIVED_DAILY_SCHEMA = """
    CREATE TABLE IF NOT EXISTS user_daily_archive (
        id INTEGER PRIMARY KEY,
        app_name TEXT NOT NULL,
        user_id TEXT NOT NULL,
        cycle_id INTEGER NOT NULL,
        day_offset INTEGER NOT NULL,
        total_msgs INTEGER NOT NULL DEFAULT 0,
        flagged_msgs INTEGER NOT NULL DEFAULT 0,
        blocked_msgs INTEGER NOT NULL DEFAULT 0,
        reviewed_msgs INTEGER NOT NULL DEFAULT 0,
        date TEXT NOT NULL
    )
"""


class UserProfiler:
    """Tracks per-user behavior with a rolling window and cycle summaries.

    :param live_db_path: path to the ``users.db`` database
    :param archive_db_path: path to the ``archive.db`` database
    :param window_days: length of one rolling cycle (91 by default)
    """

    def __init__(self, live_db_path: str, archive_db_path: str, window_days: int) -> None:
        self._window_days: int = window_days
        self._lock: threading.Lock = threading.Lock()
        for raw_path in (live_db_path, archive_db_path):
            Path(raw_path).parent.mkdir(parents=True, exist_ok=True)
        self._live: sqlite3.Connection = sqlite3.connect(live_db_path, check_same_thread=False)
        self._archive: sqlite3.Connection = sqlite3.connect(
            archive_db_path, check_same_thread=False
        )
        self._live.execute("PRAGMA journal_mode=WAL")
        self._live.execute("PRAGMA synchronous=NORMAL")
        self._archive.execute("PRAGMA journal_mode=WAL")
        self._archive.execute("PRAGMA synchronous=NORMAL")
        self._live.executescript(_LIVE_SCHEMA)
        self._live.execute(_LIVE_INDEX)
        self._archive.executescript(_ARCHIVE_SCHEMA)
        self._archive.execute(_ARCHIVE_INDEX)
        self._archive.executescript(_ARCHIVED_DAILY_SCHEMA)
        self._live.commit()
        self._archive.commit()

    @staticmethod
    def _today() -> date:
        """Return the current UTC calendar day."""
        return datetime.now(UTC).date()

    @staticmethod
    def _iso(day: date) -> str:
        """Format a date as ISO 8601 for storage."""
        return day.isoformat()

    def _cycle_start(self, app_name: str, user_id: str) -> date:
        """Derive the start day of the user's current cycle.

        The new cycle begins the day after the newest summary's end day. When
        no summary exists, the earliest live daily row defines the start.
        Without any data at all the cycle starts today.

        :param app_name: application name
        :param user_id: user identifier
        :return: the current cycle start date
        """
        row = self._archive.execute(
            "SELECT end_day FROM user_summaries "
            "WHERE app_name = ? AND user_id = ? ORDER BY cycle_id DESC LIMIT 1",
            (app_name, user_id),
        ).fetchone()
        if row is not None:
            return date.fromisoformat(row[0]) + timedelta(days=1)
        row = self._live.execute(
            "SELECT MIN(date) FROM user_daily_stats WHERE app_name = ? AND user_id = ?",
            (app_name, user_id),
        ).fetchone()
        if row is not None and row[0]:
            return date.fromisoformat(row[0])
        return self._today()

    def record(
        self,
        app_name: str,
        user_id: str,
        total_msgs: int = 1,
        flagged_msgs: int = 0,
        blocked_msgs: int = 0,
        reviewed_msgs: int = 0,
    ) -> None:
        """Record one message for a user, archiving the cycle on day 91.

        :param app_name: application name
        :param user_id: user identifier
        :param total_msgs: messages sent (normally 1 per call)
        :param flagged_msgs: messages flagged as suspicious
        :param blocked_msgs: messages blocked by the LLM
        :param reviewed_msgs: messages reviewed by an administrator
        """
        if not user_id:
            return
        today: date = self._today()
        with self._lock:
            cycle_start: date = self._cycle_start(app_name, user_id)
            day_offset: int = (today - cycle_start).days + 1
            if day_offset > self._window_days:
                # The cycle expired while the user was inactive. Write today's
                # row as the final day so it is included in the summary, close
                # the cycle, and let the next write start a fresh one.
                self._upsert_daily(
                    app_name,
                    user_id,
                    self._window_days,
                    today,
                    total_msgs,
                    flagged_msgs,
                    blocked_msgs,
                    reviewed_msgs,
                )
                self._archive_cycle(app_name, user_id, today)
                return
            if day_offset < 1:
                cycle_start = today
                day_offset = 1
            self._upsert_daily(
                app_name,
                user_id,
                day_offset,
                today,
                total_msgs,
                flagged_msgs,
                blocked_msgs,
                reviewed_msgs,
            )
            if day_offset == self._window_days:
                self._archive_cycle(app_name, user_id, today)

    def _upsert_daily(
        self,
        app_name: str,
        user_id: str,
        day_offset: int,
        day: date,
        total_msgs: int,
        flagged_msgs: int,
        blocked_msgs: int,
        reviewed_msgs: int,
    ) -> None:
        """Increment the daily row for the given calendar day."""
        iso_day: str = self._iso(day)
        row = self._live.execute(
            "SELECT id FROM user_daily_stats WHERE app_name = ? AND user_id = ? AND date = ?",
            (app_name, user_id, iso_day),
        ).fetchone()
        if row is None:
            self._live.execute(
                "INSERT INTO user_daily_stats "
                "(app_name, user_id, day_offset, total_msgs, flagged_msgs, "
                "blocked_msgs, reviewed_msgs, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    app_name,
                    user_id,
                    day_offset,
                    total_msgs,
                    flagged_msgs,
                    blocked_msgs,
                    reviewed_msgs,
                    iso_day,
                ),
            )
        else:
            self._live.execute(
                "UPDATE user_daily_stats SET "
                "total_msgs = total_msgs + ?, flagged_msgs = flagged_msgs + ?, "
                "blocked_msgs = blocked_msgs + ?, reviewed_msgs = reviewed_msgs + ? "
                "WHERE id = ?",
                (total_msgs, flagged_msgs, blocked_msgs, reviewed_msgs, row[0]),
            )
        self._live.commit()

    def _archive_cycle(self, app_name: str, user_id: str, today: date) -> None:
        """Close the current cycle into a summary and reset the live table.

        The day-91 row has already been written. Every row in the cycle is
        aggregated, stored as a summary in ``archive.db`` (also copied to the
        daily archive table), linked to the previous summary, and deleted from
        the live table.

        :param app_name: application name
        :param user_id: user identifier
        :param today: the day the cycle ends
        """
        rows = self._live.execute(
            "SELECT day_offset, total_msgs, flagged_msgs, blocked_msgs, reviewed_msgs, date "
            "FROM user_daily_stats WHERE app_name = ? AND user_id = ? "
            "ORDER BY day_offset ASC",
            (app_name, user_id),
        ).fetchall()
        if not rows:
            return
        total: int = sum(row[1] for row in rows)
        flagged: int = sum(row[2] for row in rows)
        blocked: int = sum(row[3] for row in rows)
        reviewed: int = sum(row[4] for row in rows)
        start_day: str = rows[0][5]
        end_day: str = self._iso(today)
        cycle_id: int = self._next_cycle_id(app_name, user_id)
        now: str = datetime.now(UTC).isoformat()
        cursor = self._archive.execute(
            "INSERT INTO user_summaries "
            "(app_name, user_id, cycle_id, start_day, end_day, total_msgs, "
            "flagged_msgs, blocked_msgs, reviewed_msgs, next_cycle_id, created_at) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, ?)",
            (
                app_name,
                user_id,
                cycle_id,
                start_day,
                end_day,
                total,
                flagged,
                blocked,
                reviewed,
                now,
            ),
        )
        new_id: int = cursor.lastrowid or 0
        previous = self._archive.execute(
            "SELECT id FROM user_summaries WHERE app_name = ? AND user_id = ? "
            "AND id != ? ORDER BY cycle_id DESC LIMIT 1",
            (app_name, user_id, new_id),
        ).fetchone()
        if previous is not None:
            self._archive.execute(
                "UPDATE user_summaries SET next_cycle_id = ? WHERE id = ?",
                (new_id, previous[0]),
            )
        for row in rows:
            self._archive.execute(
                "INSERT INTO user_daily_archive "
                "(app_name, user_id, cycle_id, day_offset, total_msgs, flagged_msgs, "
                "blocked_msgs, reviewed_msgs, date) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (app_name, user_id, cycle_id, row[0], row[1], row[2], row[3], row[4], row[5]),
            )
        self._live.execute(
            "DELETE FROM user_daily_stats WHERE app_name = ? AND user_id = ?",
            (app_name, user_id),
        )
        self._live.commit()
        self._archive.commit()

    def _next_cycle_id(self, app_name: str, user_id: str) -> int:
        """Return the next cycle number for a user."""
        row = self._archive.execute(
            "SELECT MAX(cycle_id) FROM user_summaries WHERE app_name = ? AND user_id = ?",
            (app_name, user_id),
        ).fetchone()
        return (row[0] if row and row[0] is not None else 0) + 1

    def get_ratio(self, app_name: str, user_id: str) -> float:
        """Return the bad-content ratio for a user.

        Combines the live window with every summary so long-term history is
        included.

        :param app_name: application name
        :param user_id: user identifier
        :return: ``(flagged + blocked) / total``, clamped to 0.0 when empty
        """
        daily = self._live.execute(
            "SELECT COALESCE(SUM(total_msgs), 0), "
            "COALESCE(SUM(flagged_msgs + blocked_msgs), 0) "
            "FROM user_daily_stats WHERE app_name = ? AND user_id = ?",
            (app_name, user_id),
        ).fetchone()
        history = self._archive.execute(
            "SELECT COALESCE(SUM(total_msgs), 0), "
            "COALESCE(SUM(flagged_msgs + blocked_msgs), 0) "
            "FROM user_summaries WHERE app_name = ? AND user_id = ?",
            (app_name, user_id),
        ).fetchone()
        total: int = (daily[0] if daily else 0) + (history[0] if history else 0)
        bad: int = (daily[1] if daily else 0) + (history[1] if history else 0)
        if total <= 0:
            return 0.0
        return bad / total

    def get_profile(self, app_name: str, user_id: str) -> dict[str, Any]:
        """Return the daily rows and summaries for one user.

        :param app_name: application name
        :param user_id: user identifier
        :return: live daily rows and historical summaries
        """
        daily_rows = self._live.execute(
            "SELECT day_offset, total_msgs, flagged_msgs, blocked_msgs, reviewed_msgs, date "
            "FROM user_daily_stats WHERE app_name = ? AND user_id = ? "
            "ORDER BY day_offset ASC",
            (app_name, user_id),
        ).fetchall()
        summary_rows = self._archive.execute(
            "SELECT cycle_id, start_day, end_day, total_msgs, flagged_msgs, "
            "blocked_msgs, reviewed_msgs, next_cycle_id "
            "FROM user_summaries WHERE app_name = ? AND user_id = ? "
            "ORDER BY cycle_id ASC",
            (app_name, user_id),
        ).fetchall()
        return {
            "app_name": app_name,
            "user_id": user_id,
            "daily": [
                {
                    "day_offset": row[0],
                    "total_msgs": row[1],
                    "flagged_msgs": row[2],
                    "blocked_msgs": row[3],
                    "reviewed_msgs": row[4],
                    "date": row[5],
                }
                for row in daily_rows
            ],
            "summaries": [
                {
                    "cycle_id": row[0],
                    "start_day": row[1],
                    "end_day": row[2],
                    "total_msgs": row[3],
                    "flagged_msgs": row[4],
                    "blocked_msgs": row[5],
                    "reviewed_msgs": row[6],
                    "next_cycle_id": row[7],
                }
                for row in summary_rows
            ],
            "ratio": self.get_ratio(app_name, user_id),
        }

    def stats(self) -> dict[str, Any]:
        """Return aggregate profiling statistics.

        :return: tracked users, live daily rows, and summary counts
        """
        users = self._live.execute(
            "SELECT COUNT(DISTINCT app_name || ':' || user_id) FROM user_daily_stats"
        ).fetchone()
        summaries = self._archive.execute(
            "SELECT COUNT(*), COUNT(DISTINCT app_name || ':' || user_id) FROM user_summaries"
        ).fetchone()
        daily_rows = self._live.execute("SELECT COUNT(*) FROM user_daily_stats").fetchone()
        return {
            "active_users": users[0] if users else 0,
            "daily_rows": daily_rows[0] if daily_rows else 0,
            "summary_count": summaries[0] if summaries else 0,
            "summary_users": summaries[1] if summaries else 0,
        }

    def close(self) -> None:
        """Close both database connections."""
        self._live.close()
        self._archive.close()
