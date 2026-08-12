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


class TestManifestCases(BaseTest):
    """ManifestCases scenarios."""

    def test_manifest_11_8228(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_12_8229(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "notes" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_0_8230(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_1_8231(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_2_8232(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_3_8233(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_4_8234(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_5_8235(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_6_8236(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_7_8237(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_8_8238(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_9_8239(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_10_8240(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_11_8241(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_12_8242(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "schema_version" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_0_8243(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_1_8244(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_2_8245(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_3_8246(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_4_8247(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_5_8248(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_6_8249(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_7_8250(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_8_8251(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_9_8252(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_10_8253(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_11_8254(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_12_8255(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "detector_count" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_0_8256(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_1_8257(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_2_8258(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_3_8259(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_4_8260(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_5_8261(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_6_8262(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_7_8263(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_8_8264(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_9_8265(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_10_8266(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_11_8267(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_12_8268(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "ai_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_0_8269(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_1_8270(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_2_8271(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_3_8272(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_4_8273(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_5_8274(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_6_8275(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_7_8276(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1

    def test_manifest_8_8277(self, tmp_path: Path) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export({"detector_count": 11})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "semantic_available" in manifest
        assert manifest["schema_version"] == 1


class TestRetentionCases(BaseTest):
    """RetentionCases scenarios."""

    def test_retention_0_8282(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_1_8283(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_2_8284(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_3_8285(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_4_8286(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_5_8287(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_6_8288(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_7_8289(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_8_8290(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_9_8291(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (1 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (1 < 7)

    def test_retention_0_8292(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_1_8293(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_2_8294(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_3_8295(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_4_8296(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_5_8297(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_6_8298(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_7_8299(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_8_8300(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_9_8301(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (6 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (6 < 7)

    def test_retention_0_8302(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_1_8303(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_2_8304(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_3_8305(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_4_8306(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_5_8307(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_6_8308(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_7_8309(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_8_8310(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_9_8311(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (7 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (7 < 7)

    def test_retention_0_8312(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_1_8313(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_2_8314(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_3_8315(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_4_8316(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_5_8317(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_6_8318(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_7_8319(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_8_8320(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_9_8321(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (29 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (29 < 30)

    def test_retention_0_8322(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_1_8323(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_2_8324(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_3_8325(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_4_8326(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_5_8327(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_6_8328(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_7_8329(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_8_8330(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)

    def test_retention_9_8331(self, tmp_path: Path) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=30,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp = stale.stat().st_mtime - (31 * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (31 < 30)
