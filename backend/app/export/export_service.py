"""Complete system data export.

Builds a ZIP archive containing every SQLite database, a CSV dump of every
table, the rotated log files, configuration snapshots (secrets redacted), the
semantic index files, and a metadata document. Exports run on a background
thread so the API never blocks, and old archives are removed after
``EXPORT_RETENTION_DAYS``.
"""

from __future__ import annotations

import csv
import io
import json
import logging
import re
import sqlite3
import threading
import zipfile
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

_LOGGER: logging.Logger = logging.getLogger(__name__)

_SECRET_LINE = re.compile(r"^(?P<key>[A-Za-z0-9_]*(?:KEY|SECRET|PASSWORD|TOKEN)[A-Za-z0-9_]*)=.+$")


class ExportService:
    """Builds and cleans up full data export archives.

    :param settings: application settings
    :param logger: audit logger
    """

    def __init__(self, settings: Any, logger: Any) -> None:
        self._export_dir: Path = Path(settings.export_temp_dir)
        if settings.export_temp_dir.startswith("."):
            self._export_dir = Path.cwd() / self._export_dir
        self._retention_days: int = int(settings.export_retention_days)
        self._logger: Any = logger
        self._lock: threading.Lock = threading.Lock()
        self._export_dir.mkdir(parents=True, exist_ok=True)

    def _timestamp(self) -> str:
        """Return a filesystem-safe export timestamp."""
        return datetime.now(UTC).strftime("%Y%m%d_%H%M%S")

    def _database_files(self) -> list[Path]:
        """Return every SQLite file under the backend data directory."""
        data_dir: Path = Path.cwd() / "data"
        if not data_dir.is_dir():
            return []
        return sorted(data_dir.glob("*.db"))

    def _log_files(self) -> list[Path]:
        """Return the audit log file and every rotated backup."""
        log_dir: Path = Path.cwd() / "logs"
        if not log_dir.is_dir():
            return []
        return sorted(log_dir.glob("moderation.log*"))

    def _semantic_files(self) -> list[Path]:
        """Return every semantic index artifact."""
        semantic_dir: Path = Path.cwd() / "semantic"
        if not semantic_dir.is_dir():
            return []
        return sorted(file for file in semantic_dir.iterdir() if file.suffix in (".index", ".json"))

    def _redact_env(self) -> str:
        """Return the ``.env`` contents with every secret replaced."""
        env_path: Path = Path.cwd() / ".env"
        if not env_path.exists():
            return ""
        lines: list[str] = []
        for line in env_path.read_text(encoding="utf-8").splitlines():
            if _SECRET_LINE.match(line) and "=" in line:
                key: str = line.split("=", 1)[0]
                lines.append(f"{key}=[REDACTED]")
            else:
                lines.append(line)
        return "\n".join(lines) + "\n"

    def _dump_table_csv(self, db_path: Path, table: str) -> str:
        """Serialize one table as a CSV string.

        :param db_path: path to the SQLite database
        :param table: table name
        :return: the CSV payload
        """
        connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        try:
            rows = connection.execute(f"SELECT * FROM {table}").fetchall()
            columns = [column[0] for column in connection.execute(f"PRAGMA table_info({table})")]
            buffer = io.StringIO()
            writer = csv.writer(buffer)
            writer.writerow(columns)
            writer.writerows(rows)
            return buffer.getvalue()
        finally:
            connection.close()

    def create_export(self, metadata: dict[str, Any] | None = None) -> Path:
        """Build the export archive and return its path.

        :param metadata: extra metadata merged into the manifest
        :return: the path of the created ZIP file
        """
        with self._lock:
            return self._build(metadata or {})

    def _build(self, metadata: dict[str, Any]) -> Path:
        """Assemble every data source into a ZIP file.

        :param metadata: extra metadata to merge into the manifest
        :return: the path of the created ZIP file
        """
        export_dir: Path = self._export_dir / f"export_{self._timestamp()}"
        export_dir.mkdir(parents=True, exist_ok=True)
        zip_path: Path = self._export_dir / f"general_moderation_export_{self._timestamp()}.zip"
        manifest: dict[str, Any] = {
            "project": "General Moderation",
            "exported_at": datetime.now(UTC).isoformat(),
            "schema_version": 1,
            "detector_count": metadata.get("detector_count", 0),
            "ai_available": metadata.get("ai_available", False),
            "semantic_available": metadata.get("semantic_available", False),
            "semantic_categories": metadata.get("semantic_categories", {}),
            "databases": {},
            "notes": "Secrets in .env are redacted in this archive.",
        }

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
            for db_path in self._database_files():
                manifest["databases"][db_path.name] = db_path.stat().st_size
                archive.write(db_path, arcname=f"databases/{db_path.name}")
                self._archive_table_csvs(archive, db_path)
            for log_path in self._log_files():
                archive.write(log_path, arcname=f"logs/{log_path.name}")
            for semantic_path in self._semantic_files():
                archive.write(semantic_path, arcname=f"semantic/{semantic_path.name}")
            archive.writestr("config/.env", self._redact_env())
            example_path: Path = Path.cwd() / ".env.example"
            if example_path.exists():
                archive.write(example_path, arcname="config/.env.example")
            archive.writestr(
                "config/settings_snapshot.json", metadata.get("settings_snapshot", "{}")
            )
            archive.writestr("export_metadata.json", json.dumps(manifest, indent=2))
        self._prune_old()
        _LOGGER.info("Export archive created at %s", zip_path)
        return zip_path

    def _archive_table_csvs(self, archive: zipfile.ZipFile, db_path: Path) -> None:
        """Dump every table of one database into the archive as CSV.

        :param archive: the open ZIP file
        :param db_path: path to the SQLite database
        """
        connection = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        try:
            tables = [
                row[0]
                for row in connection.execute(
                    "SELECT name FROM sqlite_master WHERE type = 'table' "
                    "AND name NOT LIKE 'sqlite_%'"
                )
            ]
        finally:
            connection.close()
        for table in tables:
            archive.writestr(
                f"csv/{db_path.stem}_{table}.csv", self._dump_table_csv(db_path, table)
            )

    def _prune_old(self) -> None:
        """Delete export archives older than the retention period."""
        cutoff: datetime = datetime.now(UTC).timestamp() - self._retention_days * 86400
        for path in self._export_dir.iterdir():
            if not path.is_file() or path.suffix != ".zip":
                continue
            if path.stat().st_mtime < cutoff:
                path.unlink(missing_ok=True)
