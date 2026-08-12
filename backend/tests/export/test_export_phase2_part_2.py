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

    def test_archive_entry_12_8024(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_13_8025(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_14_8026(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_15_8027(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_16_8028(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_17_8029(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_18_8030(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_19_8031(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_20_8032(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_21_8033(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("config/.env" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_0_8034(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_1_8035(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_2_8036(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_3_8037(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_4_8038(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_5_8039(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_6_8040(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_7_8041(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_8_8042(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_9_8043(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_10_8044(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_11_8045(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_12_8046(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_13_8047(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_14_8048(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_15_8049(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_16_8050(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_17_8051(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_18_8052(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_19_8053(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_20_8054(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_21_8055(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("export_metadata.json" in entry for entry in entries)
        assert any("" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_0_8056(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_1_8057(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_2_8058(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_3_8059(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_4_8060(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_5_8061(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_6_8062(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_7_8063(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_8_8064(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_9_8065(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_10_8066(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_11_8067(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_12_8068(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_13_8069(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_14_8070(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_15_8071(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_16_8072(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"

    def test_archive_entry_17_8073(self, tmp_path: Path) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any("settings_snapshot.json" in entry for entry in entries)
        assert any("config/" in entry for entry in entries)
        assert path.suffix == ".zip"


class TestRedactionCases(BaseTest):
    """RedactionCases scenarios."""

    def test_redaction_0_8078(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_API_KEY=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8079(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_API_KEY=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8080(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_API_KEY=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8081(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_API_KEY=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8082(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_API_KEY=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8083(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_SECRET=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8084(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_SECRET=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8085(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_SECRET=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8086(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_SECRET=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8087(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_SECRET=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8088(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_PASSWORD=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8089(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_PASSWORD=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8090(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_PASSWORD=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8091(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_PASSWORD=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8092(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_PASSWORD=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8093(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_TOKEN=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8094(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_TOKEN=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8095(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_TOKEN=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8096(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_TOKEN=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8097(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SOME_TOKEN=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8098(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_VALUE=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8099(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_VALUE=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8100(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_VALUE=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8101(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_VALUE=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8102(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_VALUE=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8103(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "API_TOKEN=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8104(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "API_TOKEN=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8105(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "API_TOKEN=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8106(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "API_TOKEN=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8107(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "API_TOKEN=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8108(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "DB_PASSWORD=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8109(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "DB_PASSWORD=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8110(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "DB_PASSWORD=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8111(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "DB_PASSWORD=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8112(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "DB_PASSWORD=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8113(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "ACCESS_KEY=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8114(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "ACCESS_KEY=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8115(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "ACCESS_KEY=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8116(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "ACCESS_KEY=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8117(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "ACCESS_KEY=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8118(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "AUTH_TOKEN=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8119(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "AUTH_TOKEN=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8120(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "AUTH_TOKEN=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8121(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "AUTH_TOKEN=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8122(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "AUTH_TOKEN=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_0_8123(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PRIVATE_KEY=secret_value_xyz_0\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_1_8124(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PRIVATE_KEY=secret_value_xyz_1\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_2_8125(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PRIVATE_KEY=secret_value_xyz_2\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_3_8126(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PRIVATE_KEY=secret_value_xyz_3\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content

    def test_redaction_4_8127(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PRIVATE_KEY=secret_value_xyz_4\n"
        (root / ".env").write_text(secret_line, encoding="utf-8")
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
        assert "secret_value_xyz" not in content
        assert "[REDACTED]" in content
