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
        "config/.env",
        "config/",
        13,
        8024,
    ),
    (
        "config/.env",
        "config/",
        14,
        8025,
    ),
    (
        "config/.env",
        "config/",
        15,
        8026,
    ),
    (
        "config/.env",
        "config/",
        16,
        8027,
    ),
    (
        "config/.env",
        "config/",
        17,
        8028,
    ),
    (
        "config/.env",
        "config/",
        18,
        8029,
    ),
    (
        "config/.env",
        "config/",
        19,
        8030,
    ),
    (
        "config/.env",
        "config/",
        20,
        8031,
    ),
    (
        "config/.env",
        "config/",
        21,
        8032,
    ),
    (
        "config/.env",
        "config/",
        22,
        8033,
    ),
    (
        "export_metadata.json",
        "",
        1,
        8034,
    ),
    (
        "export_metadata.json",
        "",
        2,
        8035,
    ),
    (
        "export_metadata.json",
        "",
        3,
        8036,
    ),
    (
        "export_metadata.json",
        "",
        4,
        8037,
    ),
    (
        "export_metadata.json",
        "",
        5,
        8038,
    ),
    (
        "export_metadata.json",
        "",
        6,
        8039,
    ),
    (
        "export_metadata.json",
        "",
        7,
        8040,
    ),
    (
        "export_metadata.json",
        "",
        8,
        8041,
    ),
    (
        "export_metadata.json",
        "",
        9,
        8042,
    ),
    (
        "export_metadata.json",
        "",
        10,
        8043,
    ),
    (
        "export_metadata.json",
        "",
        11,
        8044,
    ),
    (
        "export_metadata.json",
        "",
        12,
        8045,
    ),
    (
        "export_metadata.json",
        "",
        13,
        8046,
    ),
    (
        "export_metadata.json",
        "",
        14,
        8047,
    ),
    (
        "export_metadata.json",
        "",
        15,
        8048,
    ),
    (
        "export_metadata.json",
        "",
        16,
        8049,
    ),
    (
        "export_metadata.json",
        "",
        17,
        8050,
    ),
    (
        "export_metadata.json",
        "",
        18,
        8051,
    ),
    (
        "export_metadata.json",
        "",
        19,
        8052,
    ),
    (
        "export_metadata.json",
        "",
        20,
        8053,
    ),
    (
        "export_metadata.json",
        "",
        21,
        8054,
    ),
    (
        "export_metadata.json",
        "",
        22,
        8055,
    ),
    (
        "settings_snapshot.json",
        "config/",
        1,
        8056,
    ),
    (
        "settings_snapshot.json",
        "config/",
        2,
        8057,
    ),
    (
        "settings_snapshot.json",
        "config/",
        3,
        8058,
    ),
    (
        "settings_snapshot.json",
        "config/",
        4,
        8059,
    ),
    (
        "settings_snapshot.json",
        "config/",
        5,
        8060,
    ),
    (
        "settings_snapshot.json",
        "config/",
        6,
        8061,
    ),
    (
        "settings_snapshot.json",
        "config/",
        7,
        8062,
    ),
    (
        "settings_snapshot.json",
        "config/",
        8,
        8063,
    ),
    (
        "settings_snapshot.json",
        "config/",
        9,
        8064,
    ),
    (
        "settings_snapshot.json",
        "config/",
        10,
        8065,
    ),
    (
        "settings_snapshot.json",
        "config/",
        11,
        8066,
    ),
    (
        "settings_snapshot.json",
        "config/",
        12,
        8067,
    ),
    (
        "settings_snapshot.json",
        "config/",
        13,
        8068,
    ),
    (
        "settings_snapshot.json",
        "config/",
        14,
        8069,
    ),
    (
        "settings_snapshot.json",
        "config/",
        15,
        8070,
    ),
    (
        "settings_snapshot.json",
        "config/",
        16,
        8071,
    ),
    (
        "settings_snapshot.json",
        "config/",
        17,
        8072,
    ),
    (
        "settings_snapshot.json",
        "config/",
        18,
        8073,
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


_REDACTION_CASES: tuple[tuple[str, str, int], ...] = (
    (
        "SOME_API_KEY",
        "secret_value_xyz_0",
        8078,
    ),
    (
        "SOME_API_KEY",
        "secret_value_xyz_1",
        8079,
    ),
    (
        "SOME_API_KEY",
        "secret_value_xyz_2",
        8080,
    ),
    (
        "SOME_API_KEY",
        "secret_value_xyz_3",
        8081,
    ),
    (
        "SOME_API_KEY",
        "secret_value_xyz_4",
        8082,
    ),
    (
        "SOME_SECRET",
        "secret_value_xyz_0",
        8083,
    ),
    (
        "SOME_SECRET",
        "secret_value_xyz_1",
        8084,
    ),
    (
        "SOME_SECRET",
        "secret_value_xyz_2",
        8085,
    ),
    (
        "SOME_SECRET",
        "secret_value_xyz_3",
        8086,
    ),
    (
        "SOME_SECRET",
        "secret_value_xyz_4",
        8087,
    ),
    (
        "SOME_PASSWORD",
        "secret_value_xyz_0",
        8088,
    ),
    (
        "SOME_PASSWORD",
        "secret_value_xyz_1",
        8089,
    ),
    (
        "SOME_PASSWORD",
        "secret_value_xyz_2",
        8090,
    ),
    (
        "SOME_PASSWORD",
        "secret_value_xyz_3",
        8091,
    ),
    (
        "SOME_PASSWORD",
        "secret_value_xyz_4",
        8092,
    ),
    (
        "SOME_TOKEN",
        "secret_value_xyz_0",
        8093,
    ),
    (
        "SOME_TOKEN",
        "secret_value_xyz_1",
        8094,
    ),
    (
        "SOME_TOKEN",
        "secret_value_xyz_2",
        8095,
    ),
    (
        "SOME_TOKEN",
        "secret_value_xyz_3",
        8096,
    ),
    (
        "SOME_TOKEN",
        "secret_value_xyz_4",
        8097,
    ),
    (
        "SECRET_VALUE",
        "secret_value_xyz_0",
        8098,
    ),
    (
        "SECRET_VALUE",
        "secret_value_xyz_1",
        8099,
    ),
    (
        "SECRET_VALUE",
        "secret_value_xyz_2",
        8100,
    ),
    (
        "SECRET_VALUE",
        "secret_value_xyz_3",
        8101,
    ),
    (
        "SECRET_VALUE",
        "secret_value_xyz_4",
        8102,
    ),
    (
        "API_TOKEN",
        "secret_value_xyz_0",
        8103,
    ),
    (
        "API_TOKEN",
        "secret_value_xyz_1",
        8104,
    ),
    (
        "API_TOKEN",
        "secret_value_xyz_2",
        8105,
    ),
    (
        "API_TOKEN",
        "secret_value_xyz_3",
        8106,
    ),
    (
        "API_TOKEN",
        "secret_value_xyz_4",
        8107,
    ),
    (
        "DB_PASSWORD",
        "secret_value_xyz_0",
        8108,
    ),
    (
        "DB_PASSWORD",
        "secret_value_xyz_1",
        8109,
    ),
    (
        "DB_PASSWORD",
        "secret_value_xyz_2",
        8110,
    ),
    (
        "DB_PASSWORD",
        "secret_value_xyz_3",
        8111,
    ),
    (
        "DB_PASSWORD",
        "secret_value_xyz_4",
        8112,
    ),
    (
        "ACCESS_KEY",
        "secret_value_xyz_0",
        8113,
    ),
    (
        "ACCESS_KEY",
        "secret_value_xyz_1",
        8114,
    ),
    (
        "ACCESS_KEY",
        "secret_value_xyz_2",
        8115,
    ),
    (
        "ACCESS_KEY",
        "secret_value_xyz_3",
        8116,
    ),
    (
        "ACCESS_KEY",
        "secret_value_xyz_4",
        8117,
    ),
    (
        "AUTH_TOKEN",
        "secret_value_xyz_0",
        8118,
    ),
    (
        "AUTH_TOKEN",
        "secret_value_xyz_1",
        8119,
    ),
    (
        "AUTH_TOKEN",
        "secret_value_xyz_2",
        8120,
    ),
    (
        "AUTH_TOKEN",
        "secret_value_xyz_3",
        8121,
    ),
    (
        "AUTH_TOKEN",
        "secret_value_xyz_4",
        8122,
    ),
    (
        "PRIVATE_KEY",
        "secret_value_xyz_0",
        8123,
    ),
    (
        "PRIVATE_KEY",
        "secret_value_xyz_1",
        8124,
    ),
    (
        "PRIVATE_KEY",
        "secret_value_xyz_2",
        8125,
    ),
    (
        "PRIVATE_KEY",
        "secret_value_xyz_3",
        8126,
    ),
    (
        "PRIVATE_KEY",
        "secret_value_xyz_4",
        8127,
    ),
)


class TestRedaction(BaseTest):
    """Secret values never leak into the exported environment."""

    @pytest.mark.parametrize(
        (
            "key",
            "secret_value",
            "uid",
        ),
        _REDACTION_CASES,
    )
    def test_redaction(self, tmp_path: Path, key: str, secret_value: str, uid: int) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        (root / ".env").write_text(f"{key}={secret_value}\n", encoding="utf-8")
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            content = archive.read("config/.env").decode()
        assert secret_value not in content
        assert "[REDACTED]" in content
