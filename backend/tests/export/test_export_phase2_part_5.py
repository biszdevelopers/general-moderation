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


class TestRetentionCases(BaseTest):
    """RetentionCases scenarios."""

    def test_retention_0_8332(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_1_8333(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_2_8334(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_3_8335(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_4_8336(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_5_8337(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_6_8338(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_7_8339(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_8_8340(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_9_8341(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 1)

    def test_retention_0_8342(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_1_8343(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_2_8344(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_3_8345(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_4_8346(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_5_8347(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_6_8348(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_7_8349(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_8_8350(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_9_8351(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (89 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (89 < 90)

    def test_retention_0_8352(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_1_8353(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_2_8354(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_3_8355(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_4_8356(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_5_8357(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_6_8358(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_7_8359(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_8_8360(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_9_8361(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=90,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (91 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (91 < 90)

    def test_retention_0_8362(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_1_8363(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_2_8364(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_3_8365(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_4_8366(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_5_8367(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_6_8368(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_7_8369(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_8_8370(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_9_8371(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (364 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (364 < 365)

    def test_retention_0_8372(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_1_8373(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_2_8374(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_3_8375(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_4_8376(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_5_8377(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_6_8378(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_7_8379(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_8_8380(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)

    def test_retention_9_8381(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=365,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (366 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (366 < 365)


class TestMultiDbCases(BaseTest):
    """MultiDbCases scenarios."""

    def test_multidb_0_8382(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_1_8383(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_2_8384(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_3_8385(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_4_8386(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_0_8387(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_1_8388(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_2_8389(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_3_8390(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_4_8391(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_0_8392(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_1_8393(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_2_8394(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_3_8395(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_4_8396(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_0_8397(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_1_8398(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_2_8399(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_3_8400(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_4_8401(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 1):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 2
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_0_8402(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_1_8403(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_2_8404(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_3_8405(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_4_8406(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_0_8407(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_1_8408(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_2_8409(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_3_8410(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_4_8411(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_0_8412(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_1_8413(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_2_8414(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_3_8415(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_4_8416(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(3):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_0_8417(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_1_8418(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_2_8419(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_3_8420(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_4_8421(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 2):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(4):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 3
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_0_8422(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_1_8423(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_2_8424(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_3_8425(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_4_8426(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(1):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_0_8427(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_1_8428(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_2_8429(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_3_8430(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_4_8431(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
            connection.commit()
            connection.close()
        for index in range(2):
            connection = sqlite3.connect(str(root / "data" / "multi.db"))
            connection.execute(f"CREATE TABLE t{index} (id INTEGER)")
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2
