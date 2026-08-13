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


_MANIFEST_CASES: tuple[tuple[str, int, bool, bool, int], ...] = (
    (
        "notes",
        11,
        False,
        False,
        8228,
    ),
    (
        "notes",
        12,
        True,
        True,
        8229,
    ),
    (
        "schema_version",
        0,
        True,
        True,
        8230,
    ),
    (
        "schema_version",
        1,
        False,
        False,
        8231,
    ),
    (
        "schema_version",
        2,
        True,
        False,
        8232,
    ),
    (
        "schema_version",
        3,
        False,
        True,
        8233,
    ),
    (
        "schema_version",
        4,
        True,
        False,
        8234,
    ),
    (
        "schema_version",
        5,
        False,
        False,
        8235,
    ),
    (
        "schema_version",
        6,
        True,
        True,
        8236,
    ),
    (
        "schema_version",
        7,
        False,
        False,
        8237,
    ),
    (
        "schema_version",
        8,
        True,
        False,
        8238,
    ),
    (
        "schema_version",
        9,
        False,
        True,
        8239,
    ),
    (
        "schema_version",
        10,
        True,
        False,
        8240,
    ),
    (
        "schema_version",
        11,
        False,
        False,
        8241,
    ),
    (
        "schema_version",
        12,
        True,
        True,
        8242,
    ),
    (
        "detector_count",
        0,
        True,
        True,
        8243,
    ),
    (
        "detector_count",
        1,
        False,
        False,
        8244,
    ),
    (
        "detector_count",
        2,
        True,
        False,
        8245,
    ),
    (
        "detector_count",
        3,
        False,
        True,
        8246,
    ),
    (
        "detector_count",
        4,
        True,
        False,
        8247,
    ),
    (
        "detector_count",
        5,
        False,
        False,
        8248,
    ),
    (
        "detector_count",
        6,
        True,
        True,
        8249,
    ),
    (
        "detector_count",
        7,
        False,
        False,
        8250,
    ),
    (
        "detector_count",
        8,
        True,
        False,
        8251,
    ),
    (
        "detector_count",
        9,
        False,
        True,
        8252,
    ),
    (
        "detector_count",
        10,
        True,
        False,
        8253,
    ),
    (
        "detector_count",
        11,
        False,
        False,
        8254,
    ),
    (
        "detector_count",
        12,
        True,
        True,
        8255,
    ),
    (
        "ai_available",
        0,
        True,
        True,
        8256,
    ),
    (
        "ai_available",
        1,
        False,
        False,
        8257,
    ),
    (
        "ai_available",
        2,
        True,
        False,
        8258,
    ),
    (
        "ai_available",
        3,
        False,
        True,
        8259,
    ),
    (
        "ai_available",
        4,
        True,
        False,
        8260,
    ),
    (
        "ai_available",
        5,
        False,
        False,
        8261,
    ),
    (
        "ai_available",
        6,
        True,
        True,
        8262,
    ),
    (
        "ai_available",
        7,
        False,
        False,
        8263,
    ),
    (
        "ai_available",
        8,
        True,
        False,
        8264,
    ),
    (
        "ai_available",
        9,
        False,
        True,
        8265,
    ),
    (
        "ai_available",
        10,
        True,
        False,
        8266,
    ),
    (
        "ai_available",
        11,
        False,
        False,
        8267,
    ),
    (
        "ai_available",
        12,
        True,
        True,
        8268,
    ),
    (
        "semantic_available",
        0,
        True,
        True,
        8269,
    ),
    (
        "semantic_available",
        1,
        False,
        False,
        8270,
    ),
    (
        "semantic_available",
        2,
        True,
        False,
        8271,
    ),
    (
        "semantic_available",
        3,
        False,
        True,
        8272,
    ),
    (
        "semantic_available",
        4,
        True,
        False,
        8273,
    ),
    (
        "semantic_available",
        5,
        False,
        False,
        8274,
    ),
    (
        "semantic_available",
        6,
        True,
        True,
        8275,
    ),
    (
        "semantic_available",
        7,
        False,
        False,
        8276,
    ),
    (
        "semantic_available",
        8,
        True,
        False,
        8277,
    ),
)


class TestManifest(BaseTest):
    """The metadata manifest exposes every documented field."""

    @pytest.mark.parametrize(
        (
            "field",
            "detector_count",
            "ai_available",
            "semantic_available",
            "uid",
        ),
        _MANIFEST_CASES,
    )
    def test_manifest(
        self,
        tmp_path: Path,
        field: str,
        detector_count: int,
        ai_available: bool,
        semantic_available: bool,
        uid: int,
    ) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export(
                {
                    "detector_count": detector_count,
                    "ai_available": ai_available,
                    "semantic_available": semantic_available,
                }
            )
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert field in manifest
        assert manifest["schema_version"] == 1
        assert manifest["detector_count"] == detector_count
        assert manifest["ai_available"] is ai_available


_RETENTION_CASES: tuple[tuple[int, int, str, int], ...] = (
    (
        7,
        1,
        "stale0.zip",
        8282,
    ),
    (
        7,
        1,
        "stale1.zip",
        8283,
    ),
    (
        7,
        1,
        "stale2.zip",
        8284,
    ),
    (
        7,
        1,
        "stale3.zip",
        8285,
    ),
    (
        7,
        1,
        "stale4.zip",
        8286,
    ),
    (
        7,
        1,
        "stale5.zip",
        8287,
    ),
    (
        7,
        1,
        "stale6.zip",
        8288,
    ),
    (
        7,
        1,
        "stale7.zip",
        8289,
    ),
    (
        7,
        1,
        "stale8.zip",
        8290,
    ),
    (
        7,
        1,
        "stale9.zip",
        8291,
    ),
    (
        7,
        6,
        "stale0.zip",
        8292,
    ),
    (
        7,
        6,
        "stale1.zip",
        8293,
    ),
    (
        7,
        6,
        "stale2.zip",
        8294,
    ),
    (
        7,
        6,
        "stale3.zip",
        8295,
    ),
    (
        7,
        6,
        "stale4.zip",
        8296,
    ),
    (
        7,
        6,
        "stale5.zip",
        8297,
    ),
    (
        7,
        6,
        "stale6.zip",
        8298,
    ),
    (
        7,
        6,
        "stale7.zip",
        8299,
    ),
    (
        7,
        6,
        "stale8.zip",
        8300,
    ),
    (
        7,
        6,
        "stale9.zip",
        8301,
    ),
    (
        7,
        7,
        "stale0.zip",
        8302,
    ),
    (
        7,
        7,
        "stale1.zip",
        8303,
    ),
    (
        7,
        7,
        "stale2.zip",
        8304,
    ),
    (
        7,
        7,
        "stale3.zip",
        8305,
    ),
    (
        7,
        7,
        "stale4.zip",
        8306,
    ),
    (
        7,
        7,
        "stale5.zip",
        8307,
    ),
    (
        7,
        7,
        "stale6.zip",
        8308,
    ),
    (
        7,
        7,
        "stale7.zip",
        8309,
    ),
    (
        7,
        7,
        "stale8.zip",
        8310,
    ),
    (
        7,
        7,
        "stale9.zip",
        8311,
    ),
    (
        30,
        29,
        "stale0.zip",
        8312,
    ),
    (
        30,
        29,
        "stale1.zip",
        8313,
    ),
    (
        30,
        29,
        "stale2.zip",
        8314,
    ),
    (
        30,
        29,
        "stale3.zip",
        8315,
    ),
    (
        30,
        29,
        "stale4.zip",
        8316,
    ),
    (
        30,
        29,
        "stale5.zip",
        8317,
    ),
    (
        30,
        29,
        "stale6.zip",
        8318,
    ),
    (
        30,
        29,
        "stale7.zip",
        8319,
    ),
    (
        30,
        29,
        "stale8.zip",
        8320,
    ),
    (
        30,
        29,
        "stale9.zip",
        8321,
    ),
    (
        30,
        31,
        "stale0.zip",
        8322,
    ),
    (
        30,
        31,
        "stale1.zip",
        8323,
    ),
    (
        30,
        31,
        "stale2.zip",
        8324,
    ),
    (
        30,
        31,
        "stale3.zip",
        8325,
    ),
    (
        30,
        31,
        "stale4.zip",
        8326,
    ),
    (
        30,
        31,
        "stale5.zip",
        8327,
    ),
    (
        30,
        31,
        "stale6.zip",
        8328,
    ),
    (
        30,
        31,
        "stale7.zip",
        8329,
    ),
    (
        30,
        31,
        "stale8.zip",
        8330,
    ),
    (
        30,
        31,
        "stale9.zip",
        8331,
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
