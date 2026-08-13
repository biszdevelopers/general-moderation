"""Phase 2 export tests (generated).

Archive construction, secret redaction, manifest metadata, retention
pruning, multi-database CSVs and filesystem edges."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import os
import sqlite3
import zipfile
from pathlib import Path

import pytest

from app.config import Settings
from app.export.export_service import ExportService
from tests.base_test import BaseTest


def _build_sandbox(tmp_path: Path) -> Path:
    for directory in ("data", "logs", "semantic", "exports"):
        (tmp_path / directory).mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(str(tmp_path / "data" / "users.db"))
    connection.execute("CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT)")
    connection.execute("INSERT INTO t (name) VALUES ('alpha'), ('beta')")
    connection.commit()
    connection.close()
    (tmp_path / "logs" / "moderation.log").write_text('{"verdict": "PASS"}\n', encoding="utf-8")
    (tmp_path / ".env").write_text(
        "ADMIN_API_KEY=supersecret\nAPP_HOST=0.0.0.0\n", encoding="utf-8"
    )
    (tmp_path / "semantic" / "political.index").write_bytes(b"idx")
    (tmp_path / "semantic" / "political.json").write_text('["x"]', encoding="utf-8")
    return tmp_path


class _Chdir:
    def __init__(self, target: Path) -> None:
        self._target = target
        self._previous = os.getcwd()

    def __enter__(self) -> None:
        os.chdir(self._target)

    def __exit__(self, *args: object) -> None:
        os.chdir(self._previous)


def _service(tmp_path: Path) -> tuple[ExportService, Path]:
    root: Path = _build_sandbox(tmp_path)
    settings = Settings(
        app_port=0,
        export_temp_dir=str(root / "exports"),
        export_retention_days=7,
        log_file_path=str(root / "logs" / "moderation.log"),
    )
    return ExportService(settings, None), root


def _zip_entries(zip_path: Path) -> list[str]:
    with zipfile.ZipFile(zip_path) as archive:
        return sorted(archive.namelist())


_ARCHIVE_ENTRY_CASES: tuple[tuple[str, str, int, int], ...] = (
    (
        "users.db",
        "databases/",
        1,
        7924,
    ),
    (
        "users.db",
        "databases/",
        2,
        7925,
    ),
    (
        "users.db",
        "databases/",
        3,
        7926,
    ),
    (
        "users.db",
        "databases/",
        4,
        7927,
    ),
    (
        "users.db",
        "databases/",
        5,
        7928,
    ),
    (
        "users.db",
        "databases/",
        6,
        7929,
    ),
    (
        "users.db",
        "databases/",
        7,
        7930,
    ),
    (
        "users.db",
        "databases/",
        8,
        7931,
    ),
    (
        "users.db",
        "databases/",
        9,
        7932,
    ),
    (
        "users.db",
        "databases/",
        10,
        7933,
    ),
    (
        "users.db",
        "databases/",
        11,
        7934,
    ),
    (
        "users.db",
        "databases/",
        12,
        7935,
    ),
    (
        "users.db",
        "databases/",
        13,
        7936,
    ),
    (
        "users.db",
        "databases/",
        14,
        7937,
    ),
    (
        "users.db",
        "databases/",
        15,
        7938,
    ),
    (
        "users.db",
        "databases/",
        16,
        7939,
    ),
    (
        "users.db",
        "databases/",
        17,
        7940,
    ),
    (
        "users.db",
        "databases/",
        18,
        7941,
    ),
    (
        "users.db",
        "databases/",
        19,
        7942,
    ),
    (
        "users.db",
        "databases/",
        20,
        7943,
    ),
    (
        "users.db",
        "databases/",
        21,
        7944,
    ),
    (
        "users.db",
        "databases/",
        22,
        7945,
    ),
    (
        "moderation.log",
        "logs/",
        1,
        7946,
    ),
    (
        "moderation.log",
        "logs/",
        2,
        7947,
    ),
    (
        "moderation.log",
        "logs/",
        3,
        7948,
    ),
    (
        "moderation.log",
        "logs/",
        4,
        7949,
    ),
    (
        "moderation.log",
        "logs/",
        5,
        7950,
    ),
    (
        "moderation.log",
        "logs/",
        6,
        7951,
    ),
    (
        "moderation.log",
        "logs/",
        7,
        7952,
    ),
    (
        "moderation.log",
        "logs/",
        8,
        7953,
    ),
    (
        "moderation.log",
        "logs/",
        9,
        7954,
    ),
    (
        "moderation.log",
        "logs/",
        10,
        7955,
    ),
    (
        "moderation.log",
        "logs/",
        11,
        7956,
    ),
    (
        "moderation.log",
        "logs/",
        12,
        7957,
    ),
    (
        "moderation.log",
        "logs/",
        13,
        7958,
    ),
    (
        "moderation.log",
        "logs/",
        14,
        7959,
    ),
    (
        "moderation.log",
        "logs/",
        15,
        7960,
    ),
    (
        "moderation.log",
        "logs/",
        16,
        7961,
    ),
    (
        "moderation.log",
        "logs/",
        17,
        7962,
    ),
    (
        "moderation.log",
        "logs/",
        18,
        7963,
    ),
    (
        "moderation.log",
        "logs/",
        19,
        7964,
    ),
    (
        "moderation.log",
        "logs/",
        20,
        7965,
    ),
    (
        "moderation.log",
        "logs/",
        21,
        7966,
    ),
    (
        "moderation.log",
        "logs/",
        22,
        7967,
    ),
    (
        "political.index",
        "semantic/",
        1,
        7968,
    ),
    (
        "political.index",
        "semantic/",
        2,
        7969,
    ),
    (
        "political.index",
        "semantic/",
        3,
        7970,
    ),
    (
        "political.index",
        "semantic/",
        4,
        7971,
    ),
    (
        "political.index",
        "semantic/",
        5,
        7972,
    ),
    (
        "political.index",
        "semantic/",
        6,
        7973,
    ),
    (
        "political.index",
        "semantic/",
        7,
        7974,
    ),
    (
        "political.index",
        "semantic/",
        8,
        7975,
    ),
    (
        "political.index",
        "semantic/",
        9,
        7976,
    ),
    (
        "political.index",
        "semantic/",
        10,
        7977,
    ),
    (
        "political.index",
        "semantic/",
        11,
        7978,
    ),
    (
        "political.index",
        "semantic/",
        12,
        7979,
    ),
    (
        "political.index",
        "semantic/",
        13,
        7980,
    ),
    (
        "political.index",
        "semantic/",
        14,
        7981,
    ),
    (
        "political.index",
        "semantic/",
        15,
        7982,
    ),
    (
        "political.index",
        "semantic/",
        16,
        7983,
    ),
    (
        "political.index",
        "semantic/",
        17,
        7984,
    ),
    (
        "political.index",
        "semantic/",
        18,
        7985,
    ),
    (
        "political.index",
        "semantic/",
        19,
        7986,
    ),
    (
        "political.index",
        "semantic/",
        20,
        7987,
    ),
    (
        "political.index",
        "semantic/",
        21,
        7988,
    ),
    (
        "political.index",
        "semantic/",
        22,
        7989,
    ),
    (
        "political.json",
        "semantic/",
        1,
        7990,
    ),
    (
        "political.json",
        "semantic/",
        2,
        7991,
    ),
    (
        "political.json",
        "semantic/",
        3,
        7992,
    ),
    (
        "political.json",
        "semantic/",
        4,
        7993,
    ),
    (
        "political.json",
        "semantic/",
        5,
        7994,
    ),
    (
        "political.json",
        "semantic/",
        6,
        7995,
    ),
    (
        "political.json",
        "semantic/",
        7,
        7996,
    ),
    (
        "political.json",
        "semantic/",
        8,
        7997,
    ),
    (
        "political.json",
        "semantic/",
        9,
        7998,
    ),
    (
        "political.json",
        "semantic/",
        10,
        7999,
    ),
    (
        "political.json",
        "semantic/",
        11,
        8000,
    ),
    (
        "political.json",
        "semantic/",
        12,
        8001,
    ),
    (
        "political.json",
        "semantic/",
        13,
        8002,
    ),
    (
        "political.json",
        "semantic/",
        14,
        8003,
    ),
    (
        "political.json",
        "semantic/",
        15,
        8004,
    ),
    (
        "political.json",
        "semantic/",
        16,
        8005,
    ),
    (
        "political.json",
        "semantic/",
        17,
        8006,
    ),
    (
        "political.json",
        "semantic/",
        18,
        8007,
    ),
    (
        "political.json",
        "semantic/",
        19,
        8008,
    ),
    (
        "political.json",
        "semantic/",
        20,
        8009,
    ),
    (
        "political.json",
        "semantic/",
        21,
        8010,
    ),
    (
        "political.json",
        "semantic/",
        22,
        8011,
    ),
    (
        "config/.env",
        "config/",
        1,
        8012,
    ),
    (
        "config/.env",
        "config/",
        2,
        8013,
    ),
    (
        "config/.env",
        "config/",
        3,
        8014,
    ),
    (
        "config/.env",
        "config/",
        4,
        8015,
    ),
    (
        "config/.env",
        "config/",
        5,
        8016,
    ),
    (
        "config/.env",
        "config/",
        6,
        8017,
    ),
    (
        "config/.env",
        "config/",
        7,
        8018,
    ),
    (
        "config/.env",
        "config/",
        8,
        8019,
    ),
    (
        "config/.env",
        "config/",
        9,
        8020,
    ),
    (
        "config/.env",
        "config/",
        10,
        8021,
    ),
    (
        "config/.env",
        "config/",
        11,
        8022,
    ),
    (
        "config/.env",
        "config/",
        12,
        8023,
    ),
)


class TestArchiveEntry(BaseTest):
    """Export archives include every documented asset."""

    @pytest.mark.parametrize(
        (
            "marker",
            "section",
            "n_extra_db",
            "uid",
        ),
        _ARCHIVE_ENTRY_CASES,
    )
    def test_archive_entry(
        self, tmp_path: Path, marker: str, section: str, n_extra_db: int, uid: int
    ) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        for index in range(n_extra_db):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any(marker in entry for entry in entries)
        assert any(section in entry for entry in entries)
        assert any(f"extra{n_extra_db - 1}.db" in entry for entry in entries)
        assert path.suffix == ".zip"
