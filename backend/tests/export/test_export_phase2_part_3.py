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


class TestRedactionCases(BaseTest):
    """RedactionCases scenarios."""

    def test_redaction_0_8128(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "APP_SECRET=secret_value_xyz_0\n"
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

    def test_redaction_1_8129(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "APP_SECRET=secret_value_xyz_1\n"
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

    def test_redaction_2_8130(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "APP_SECRET=secret_value_xyz_2\n"
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

    def test_redaction_3_8131(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "APP_SECRET=secret_value_xyz_3\n"
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

    def test_redaction_4_8132(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "APP_SECRET=secret_value_xyz_4\n"
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

    def test_redaction_0_8133(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "LOGIN_PASSWORD=secret_value_xyz_0\n"
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

    def test_redaction_1_8134(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "LOGIN_PASSWORD=secret_value_xyz_1\n"
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

    def test_redaction_2_8135(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "LOGIN_PASSWORD=secret_value_xyz_2\n"
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

    def test_redaction_3_8136(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "LOGIN_PASSWORD=secret_value_xyz_3\n"
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

    def test_redaction_4_8137(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "LOGIN_PASSWORD=secret_value_xyz_4\n"
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

    def test_redaction_0_8138(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SESSION_TOKEN=secret_value_xyz_0\n"
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

    def test_redaction_1_8139(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SESSION_TOKEN=secret_value_xyz_1\n"
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

    def test_redaction_2_8140(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SESSION_TOKEN=secret_value_xyz_2\n"
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

    def test_redaction_3_8141(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SESSION_TOKEN=secret_value_xyz_3\n"
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

    def test_redaction_4_8142(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SESSION_TOKEN=secret_value_xyz_4\n"
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

    def test_redaction_0_8143(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "WALLET_KEY=secret_value_xyz_0\n"
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

    def test_redaction_1_8144(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "WALLET_KEY=secret_value_xyz_1\n"
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

    def test_redaction_2_8145(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "WALLET_KEY=secret_value_xyz_2\n"
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

    def test_redaction_3_8146(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "WALLET_KEY=secret_value_xyz_3\n"
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

    def test_redaction_4_8147(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "WALLET_KEY=secret_value_xyz_4\n"
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

    def test_redaction_0_8148(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASS_KEY=secret_value_xyz_0\n"
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

    def test_redaction_1_8149(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASS_KEY=secret_value_xyz_1\n"
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

    def test_redaction_2_8150(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASS_KEY=secret_value_xyz_2\n"
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

    def test_redaction_3_8151(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASS_KEY=secret_value_xyz_3\n"
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

    def test_redaction_4_8152(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASS_KEY=secret_value_xyz_4\n"
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

    def test_redaction_0_8153(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_SALT=secret_value_xyz_0\n"
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

    def test_redaction_1_8154(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_SALT=secret_value_xyz_1\n"
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

    def test_redaction_2_8155(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_SALT=secret_value_xyz_2\n"
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

    def test_redaction_3_8156(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_SALT=secret_value_xyz_3\n"
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

    def test_redaction_4_8157(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "SECRET_SALT=secret_value_xyz_4\n"
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

    def test_redaction_0_8158(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "TOKEN_SECRET=secret_value_xyz_0\n"
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

    def test_redaction_1_8159(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "TOKEN_SECRET=secret_value_xyz_1\n"
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

    def test_redaction_2_8160(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "TOKEN_SECRET=secret_value_xyz_2\n"
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

    def test_redaction_3_8161(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "TOKEN_SECRET=secret_value_xyz_3\n"
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

    def test_redaction_4_8162(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "TOKEN_SECRET=secret_value_xyz_4\n"
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

    def test_redaction_0_8163(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASSWORD_1=secret_value_xyz_0\n"
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

    def test_redaction_1_8164(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASSWORD_1=secret_value_xyz_1\n"
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

    def test_redaction_2_8165(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASSWORD_1=secret_value_xyz_2\n"
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

    def test_redaction_3_8166(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASSWORD_1=secret_value_xyz_3\n"
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

    def test_redaction_4_8167(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "PASSWORD_1=secret_value_xyz_4\n"
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

    def test_redaction_0_8168(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "KEY_PAIR=secret_value_xyz_0\n"
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

    def test_redaction_1_8169(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "KEY_PAIR=secret_value_xyz_1\n"
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

    def test_redaction_2_8170(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "KEY_PAIR=secret_value_xyz_2\n"
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

    def test_redaction_3_8171(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "KEY_PAIR=secret_value_xyz_3\n"
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

    def test_redaction_4_8172(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "KEY_PAIR=secret_value_xyz_4\n"
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

    def test_redaction_0_8173(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "MASTER_KEY=secret_value_xyz_0\n"
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

    def test_redaction_1_8174(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "MASTER_KEY=secret_value_xyz_1\n"
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

    def test_redaction_2_8175(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "MASTER_KEY=secret_value_xyz_2\n"
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

    def test_redaction_3_8176(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "MASTER_KEY=secret_value_xyz_3\n"
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

    def test_redaction_4_8177(self, tmp_path: Path) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        secret_line = "MASTER_KEY=secret_value_xyz_4\n"
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


class TestManifestCases(BaseTest):
    """ManifestCases scenarios."""

    def test_manifest_0_8178(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_1_8179(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_2_8180(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_3_8181(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_4_8182(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_5_8183(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_6_8184(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_7_8185(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_8_8186(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_9_8187(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_10_8188(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_11_8189(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_12_8190(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "project" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_0_8191(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_1_8192(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_2_8193(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_3_8194(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_4_8195(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_5_8196(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_6_8197(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_7_8198(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_8_8199(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_9_8200(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_10_8201(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_11_8202(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_12_8203(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "exported_at" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_0_8204(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_1_8205(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_2_8206(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_3_8207(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_4_8208(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_5_8209(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_6_8210(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_7_8211(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_8_8212(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_9_8213(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_10_8214(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_11_8215(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_12_8216(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "databases" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_0_8217(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_1_8218(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_2_8219(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_3_8220(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_4_8221(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_5_8222(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_6_8223(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_7_8224(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_8_8225(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_9_8226(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_10_8227(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1
