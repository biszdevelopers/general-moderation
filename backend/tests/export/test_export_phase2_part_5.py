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


_RETENTION_CASES: tuple[tuple[int, int, str, int], ...] = (
    (
        1,
        1,
        "stale0.zip",
        8332,
    ),
    (
        1,
        1,
        "stale1.zip",
        8333,
    ),
    (
        1,
        1,
        "stale2.zip",
        8334,
    ),
    (
        1,
        1,
        "stale3.zip",
        8335,
    ),
    (
        1,
        1,
        "stale4.zip",
        8336,
    ),
    (
        1,
        1,
        "stale5.zip",
        8337,
    ),
    (
        1,
        1,
        "stale6.zip",
        8338,
    ),
    (
        1,
        1,
        "stale7.zip",
        8339,
    ),
    (
        1,
        1,
        "stale8.zip",
        8340,
    ),
    (
        1,
        1,
        "stale9.zip",
        8341,
    ),
    (
        90,
        89,
        "stale0.zip",
        8342,
    ),
    (
        90,
        89,
        "stale1.zip",
        8343,
    ),
    (
        90,
        89,
        "stale2.zip",
        8344,
    ),
    (
        90,
        89,
        "stale3.zip",
        8345,
    ),
    (
        90,
        89,
        "stale4.zip",
        8346,
    ),
    (
        90,
        89,
        "stale5.zip",
        8347,
    ),
    (
        90,
        89,
        "stale6.zip",
        8348,
    ),
    (
        90,
        89,
        "stale7.zip",
        8349,
    ),
    (
        90,
        89,
        "stale8.zip",
        8350,
    ),
    (
        90,
        89,
        "stale9.zip",
        8351,
    ),
    (
        90,
        91,
        "stale0.zip",
        8352,
    ),
    (
        90,
        91,
        "stale1.zip",
        8353,
    ),
    (
        90,
        91,
        "stale2.zip",
        8354,
    ),
    (
        90,
        91,
        "stale3.zip",
        8355,
    ),
    (
        90,
        91,
        "stale4.zip",
        8356,
    ),
    (
        90,
        91,
        "stale5.zip",
        8357,
    ),
    (
        90,
        91,
        "stale6.zip",
        8358,
    ),
    (
        90,
        91,
        "stale7.zip",
        8359,
    ),
    (
        90,
        91,
        "stale8.zip",
        8360,
    ),
    (
        90,
        91,
        "stale9.zip",
        8361,
    ),
    (
        365,
        364,
        "stale0.zip",
        8362,
    ),
    (
        365,
        364,
        "stale1.zip",
        8363,
    ),
    (
        365,
        364,
        "stale2.zip",
        8364,
    ),
    (
        365,
        364,
        "stale3.zip",
        8365,
    ),
    (
        365,
        364,
        "stale4.zip",
        8366,
    ),
    (
        365,
        364,
        "stale5.zip",
        8367,
    ),
    (
        365,
        364,
        "stale6.zip",
        8368,
    ),
    (
        365,
        364,
        "stale7.zip",
        8369,
    ),
    (
        365,
        364,
        "stale8.zip",
        8370,
    ),
    (
        365,
        364,
        "stale9.zip",
        8371,
    ),
    (
        365,
        366,
        "stale0.zip",
        8372,
    ),
    (
        365,
        366,
        "stale1.zip",
        8373,
    ),
    (
        365,
        366,
        "stale2.zip",
        8374,
    ),
    (
        365,
        366,
        "stale3.zip",
        8375,
    ),
    (
        365,
        366,
        "stale4.zip",
        8376,
    ),
    (
        365,
        366,
        "stale5.zip",
        8377,
    ),
    (
        365,
        366,
        "stale6.zip",
        8378,
    ),
    (
        365,
        366,
        "stale7.zip",
        8379,
    ),
    (
        365,
        366,
        "stale8.zip",
        8380,
    ),
    (
        365,
        366,
        "stale9.zip",
        8381,
    ),
)


class TestRetention(BaseTest):
    """Exports older than retention are pruned."""

    @pytest.mark.parametrize(
        (
            "retention",
            "age",
            "stale_name",
            "uid",
        ),
        _RETENTION_CASES,
    )
    def test_retention(
        self, tmp_path: Path, retention: int, age: int, stale_name: str, uid: int
    ) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=retention,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / stale_name
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (age * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (age < retention)


_MULTIDB_CASES: tuple[tuple[int, int, int, int], ...] = (
    (
        1,
        1,
        0,
        8382,
    ),
    (
        1,
        1,
        1,
        8383,
    ),
    (
        1,
        1,
        2,
        8384,
    ),
    (
        1,
        1,
        3,
        8385,
    ),
    (
        1,
        1,
        4,
        8386,
    ),
    (
        1,
        2,
        0,
        8387,
    ),
    (
        1,
        2,
        1,
        8388,
    ),
    (
        1,
        2,
        2,
        8389,
    ),
    (
        1,
        2,
        3,
        8390,
    ),
    (
        1,
        2,
        4,
        8391,
    ),
    (
        1,
        3,
        0,
        8392,
    ),
    (
        1,
        3,
        1,
        8393,
    ),
    (
        1,
        3,
        2,
        8394,
    ),
    (
        1,
        3,
        3,
        8395,
    ),
    (
        1,
        3,
        4,
        8396,
    ),
    (
        1,
        4,
        0,
        8397,
    ),
    (
        1,
        4,
        1,
        8398,
    ),
    (
        1,
        4,
        2,
        8399,
    ),
    (
        1,
        4,
        3,
        8400,
    ),
    (
        1,
        4,
        4,
        8401,
    ),
    (
        2,
        1,
        0,
        8402,
    ),
    (
        2,
        1,
        1,
        8403,
    ),
    (
        2,
        1,
        2,
        8404,
    ),
    (
        2,
        1,
        3,
        8405,
    ),
    (
        2,
        1,
        4,
        8406,
    ),
    (
        2,
        2,
        0,
        8407,
    ),
    (
        2,
        2,
        1,
        8408,
    ),
    (
        2,
        2,
        2,
        8409,
    ),
    (
        2,
        2,
        3,
        8410,
    ),
    (
        2,
        2,
        4,
        8411,
    ),
    (
        2,
        3,
        0,
        8412,
    ),
    (
        2,
        3,
        1,
        8413,
    ),
    (
        2,
        3,
        2,
        8414,
    ),
    (
        2,
        3,
        3,
        8415,
    ),
    (
        2,
        3,
        4,
        8416,
    ),
    (
        2,
        4,
        0,
        8417,
    ),
    (
        2,
        4,
        1,
        8418,
    ),
    (
        2,
        4,
        2,
        8419,
    ),
    (
        2,
        4,
        3,
        8420,
    ),
    (
        2,
        4,
        4,
        8421,
    ),
    (
        3,
        1,
        0,
        8422,
    ),
    (
        3,
        1,
        1,
        8423,
    ),
    (
        3,
        1,
        2,
        8424,
    ),
    (
        3,
        1,
        3,
        8425,
    ),
    (
        3,
        1,
        4,
        8426,
    ),
    (
        3,
        2,
        0,
        8427,
    ),
    (
        3,
        2,
        1,
        8428,
    ),
    (
        3,
        2,
        2,
        8429,
    ),
    (
        3,
        2,
        3,
        8430,
    ),
    (
        3,
        2,
        4,
        8431,
    ),
)


class TestMultidb(BaseTest):
    """Every database and table is archived with CSVs."""

    @pytest.mark.parametrize(
        (
            "db_count",
            "table_count",
            "scenario",
            "uid",
        ),
        _MULTIDB_CASES,
    )
    def test_multidb(
        self, tmp_path: Path, db_count: int, table_count: int, scenario: int, uid: int
    ) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, db_count):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(table_count):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{scenario}_{index} (id INTEGER)")
            connection.commit()
            connection.close()
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        db_entries = [entry for entry in entries if "databases/" in entry]
        assert len(db_entries) == db_count + 1
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == table_count
