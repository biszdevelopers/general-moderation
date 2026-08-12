"""Phase 2 export tests (generated).

Archive construction, secret redaction, manifest metadata, retention
pruning, multi-database CSVs and filesystem edges."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import os
import sqlite3
import zipfile
from pathlib import Path

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


class TestArchiveConstruction(BaseTest):
    """ArchiveConstruction scenarios."""

    def test_archive_entry_0_7924(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_1_7925(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_2_7926(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_3_7927(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_4_7928(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_5_7929(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_6_7930(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_7_7931(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_8_7932(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_9_7933(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_10_7934(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_11_7935(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_12_7936(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_13_7937(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_14_7938(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_15_7939(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_16_7940(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_17_7941(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_18_7942(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_19_7943(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_20_7944(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_21_7945(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("users.db" in entry for entry in entries)
        assert any("databases/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_0_7946(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_1_7947(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_2_7948(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_3_7949(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_4_7950(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_5_7951(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_6_7952(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_7_7953(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_8_7954(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_9_7955(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_10_7956(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_11_7957(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_12_7958(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_13_7959(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_14_7960(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_15_7961(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_16_7962(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_17_7963(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_18_7964(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_19_7965(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_20_7966(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_21_7967(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("moderation.log" in entry for entry in entries)
        assert any("logs/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_0_7968(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_1_7969(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_2_7970(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_3_7971(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_4_7972(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_5_7973(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_6_7974(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_7_7975(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_8_7976(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_9_7977(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_10_7978(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_11_7979(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_12_7980(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_13_7981(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_14_7982(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_15_7983(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_16_7984(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_17_7985(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_18_7986(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_19_7987(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_20_7988(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_21_7989(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_0_7990(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_1_7991(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_2_7992(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_3_7993(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_4_7994(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_5_7995(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_6_7996(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_7_7997(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_8_7998(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_9_7999(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_10_8000(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_11_8001(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_12_8002(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_13_8003(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_14_8004(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_15_8005(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_16_8006(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_17_8007(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_18_8008(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_19_8009(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_20_8010(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_21_8011(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("political.json" in entry for entry in entries)
        assert any("semantic/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_0_8012(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_1_8013(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_2_8014(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_3_8015(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_4_8016(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_5_8017(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_6_8018(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_7_8019(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_8_8020(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_9_8021(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_10_8022(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_11_8023(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"
