"""Per-application trigger policy stored in ``config.db``.

Each app can tune how the suspicion score reaches the LLM stage:

- ``score_threshold``: the suspicion score that alone forces the LLM.
- ``semantic_boost``: force the LLM when a semantic similarity is high.
- ``user_ratio_boost``: force the LLM when the user bad-content ratio is high.
- ``logic_type``: "or" triggers on any condition, "and" requires all.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any

_SCHEMA = """
    CREATE TABLE IF NOT EXISTS app_config (
        app_name TEXT PRIMARY KEY,
        score_threshold INTEGER NOT NULL DEFAULT 50,
        semantic_boost INTEGER NOT NULL DEFAULT 1,
        user_ratio_boost INTEGER NOT NULL DEFAULT 1,
        logic_type TEXT NOT NULL DEFAULT 'or'
    )
"""

_DEFAULTS: dict[str, Any] = {
    "score_threshold": 50,
    "semantic_boost": True,
    "user_ratio_boost": True,
    "logic_type": "or",
}


class AppConfigService:
    """Reads and writes per-application trigger policies.

    :param db_path: path to the ``config.db`` database
    """

    def __init__(self, db_path: str = "./data/config.db") -> None:
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self._connection: sqlite3.Connection = sqlite3.connect(db_path, check_same_thread=False)
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.execute("PRAGMA synchronous=NORMAL")
        self._connection.executescript(_SCHEMA)
        self._connection.commit()

    def get(self, app_name: str | None) -> dict[str, Any]:
        """Return the effective policy for an app.

        Apps without a stored row fall back to the ``_default`` row and then
        to the built-in defaults.

        :param app_name: the application name
        :return: score_threshold, semantic_boost, user_ratio_boost, logic_type
        """
        for candidate in (app_name or "", "_default"):
            row = self._connection.execute(
                "SELECT app_name, score_threshold, semantic_boost, user_ratio_boost, logic_type "
                "FROM app_config WHERE app_name = ?",
                (candidate,),
            ).fetchone()
            if row is not None:
                return {
                    "app_name": row[0],
                    "score_threshold": row[1],
                    "semantic_boost": bool(row[2]),
                    "user_ratio_boost": bool(row[3]),
                    "logic_type": row[4],
                }
        return dict(_DEFAULTS)

    def set(self, app_name: str, **values: Any) -> dict[str, Any]:
        """Create or update an app policy row.

        :param app_name: the application name
        :param values: any of score_threshold, semantic_boost, user_ratio_boost, logic_type
        :return: the stored policy
        :raises ValueError: for invalid values
        """
        allowed: set[str] = {"score_threshold", "semantic_boost", "user_ratio_boost", "logic_type"}
        invalid: set[str] = set(values) - allowed
        if invalid:
            raise ValueError(f"Unknown app config fields: {sorted(invalid)}")
        current: dict[str, Any] = self.get(app_name)
        if "logic_type" in values and values["logic_type"] not in ("and", "or"):
            raise ValueError("logic_type must be 'and' or 'or'")
        if "score_threshold" in values:
            threshold: int = int(values["score_threshold"])
            if not 0 <= threshold <= 100:
                raise ValueError("score_threshold must be between 0 and 100")
            values["score_threshold"] = threshold
        merged: dict[str, Any] = {**current, **values}
        merged.pop("app_name", None)
        self._connection.execute(
            "INSERT INTO app_config (app_name, score_threshold, semantic_boost, "
            "user_ratio_boost, logic_type) VALUES (?, ?, ?, ?, ?) "
            "ON CONFLICT(app_name) DO UPDATE SET "
            "score_threshold = excluded.score_threshold, "
            "semantic_boost = excluded.semantic_boost, "
            "user_ratio_boost = excluded.user_ratio_boost, "
            "logic_type = excluded.logic_type",
            (
                app_name,
                int(merged["score_threshold"]),
                int(bool(merged["semantic_boost"])),
                int(bool(merged["user_ratio_boost"])),
                merged["logic_type"],
            ),
        )
        self._connection.commit()
        return self.get(app_name)

    def list_all(self) -> list[dict[str, Any]]:
        """Return every stored app policy."""
        rows = self._connection.execute(
            "SELECT app_name, score_threshold, semantic_boost, user_ratio_boost, logic_type "
            "FROM app_config ORDER BY app_name ASC"
        ).fetchall()
        return [
            {
                "app_name": row[0],
                "score_threshold": row[1],
                "semantic_boost": bool(row[2]),
                "user_ratio_boost": bool(row[3]),
                "logic_type": row[4],
            }
            for row in rows
        ]

    def update_default_threshold(self, threshold: int) -> None:
        """Tune the fallback threshold used by apps without a policy row.

        :param threshold: the new default suspicion score threshold
        """
        threshold = max(0, min(100, int(threshold)))
        row = self._connection.execute(
            "SELECT score_threshold FROM app_config WHERE app_name = '_default'"
        ).fetchone()
        if row is None:
            self._connection.execute(
                "INSERT INTO app_config (app_name, score_threshold, semantic_boost, "
                "user_ratio_boost, logic_type) VALUES ('_default', ?, 1, 1, 'or')",
                (threshold,),
            )
        else:
            self._connection.execute(
                "UPDATE app_config SET score_threshold = ? WHERE app_name = '_default'",
                (threshold,),
            )
        self._connection.commit()

    def close(self) -> None:
        """Close the underlying database connection."""
        self._connection.close()
