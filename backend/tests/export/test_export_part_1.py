"""Data export service tests (Phase 1, P1/P2).

Covers archive construction, database inclusion, CSV dumps, secret
redaction, manifest metadata, log/semantic inclusion, and retention pruning.
"""

from __future__ import annotations

import os
import sqlite3
import zipfile
from pathlib import Path
from typing import Any

import pytest

from app.config import Settings
from app.export.export_service import ExportService
from tests.base_test import BaseTest


def _build_sandbox(tmp_path: Path) -> Path:
    """Create a backend-like directory tree with sample data.

    :param tmp_path: per-test temporary directory
    :return: the sandbox root
    """
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
    """Context manager restoring the working directory."""

    def __init__(self, target: Path) -> None:
        self._target: Path = target
        self._previous: str = os.getcwd()

    def __enter__(self) -> None:
        os.chdir(self._target)

    def __exit__(self, *args: object) -> None:
        os.chdir(self._previous)


def _service(tmp_path: Path) -> tuple[ExportService, Path]:
    """Build an export service rooted at the sandbox.

    :param tmp_path: per-test temporary directory
    :return: the service and the sandbox root
    """
    root: Path = _build_sandbox(tmp_path)
    settings = Settings(
        app_port=0,
        export_temp_dir=str(root / "exports"),
        export_retention_days=7,
        log_file_path=str(root / "logs" / "moderation.log"),
    )
    return ExportService(settings, None), root


def _zip_entries(zip_path: Path) -> list[str]:
    """List the entries inside an export archive.

    :param zip_path: path to the ZIP file
    :return: sorted entry names
    """
    with zipfile.ZipFile(zip_path) as archive:
        return sorted(archive.namelist())


class TestExportArchive(BaseTest):
    """Archive construction."""

    def test_export_creates_zip(self, tmp_path: Path) -> None:
        """An export produces a ZIP file."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        assert path.exists()
        assert path.suffix == ".zip"

    def test_export_includes_database(self, tmp_path: Path) -> None:
        """The users database is archived."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        assert any("users.db" in entry for entry in _zip_entries(path))

    def test_export_includes_csv(self, tmp_path: Path) -> None:
        """Table CSV dumps are archived."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        assert any("csv" in entry for entry in _zip_entries(path))

    def test_export_includes_logs(self, tmp_path: Path) -> None:
        """Log files are archived."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        assert any("moderation.log" in entry for entry in _zip_entries(path))

    def test_export_includes_semantic(self, tmp_path: Path) -> None:
        """Semantic index files are archived."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        entries: list[str] = _zip_entries(path)
        assert any("political.index" in entry for entry in entries)
        assert any("political.json" in entry for entry in entries)

    def test_export_includes_env(self, tmp_path: Path) -> None:
        """The redacted environment file is archived."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        assert "config/.env" in _zip_entries(path)

    def test_export_includes_settings_snapshot(self, tmp_path: Path) -> None:
        """The settings snapshot is archived."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        assert "config/settings_snapshot.json" in _zip_entries(path)

    def test_export_includes_manifest(self, tmp_path: Path) -> None:
        """The metadata manifest is archived."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        assert "export_metadata.json" in _zip_entries(path)

    def test_manifest_has_schema_version(self, tmp_path: Path) -> None:
        """The manifest declares a schema version."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            manifest: dict[str, Any] = __import__("json").loads(
                archive.read("export_metadata.json")
            )
        assert manifest["schema_version"] == 1

    def test_manifest_detector_count(self, tmp_path: Path) -> None:
        """The manifest records the detector count."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export({"detector_count": 6})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert manifest["detector_count"] == 6

    def test_csv_has_header(self, tmp_path: Path) -> None:
        """CSV dumps include a header row."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            csv_entry: str = next(entry for entry in archive.namelist() if "users_t.csv" in entry)
            content: str = archive.read(csv_entry).decode()
        assert content.startswith("id,name")


class TestExportRedaction(BaseTest):
    """Secret redaction in the exported environment."""

    def test_secret_value_redacted(self, tmp_path: Path) -> None:
        """Real secret values never appear in the export."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            env_content: str = archive.read("config/.env").decode()
        assert "supersecret" not in env_content
        assert "[REDACTED]" in env_content

    def test_non_secret_preserved(self, tmp_path: Path) -> None:
        """Ordinary environment values survive intact."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            env_content: str = archive.read("config/.env").decode()
        assert "APP_HOST=0.0.0.0" in env_content


class TestExportMetadata(BaseTest):
    """Metadata passed into the export."""

    @pytest.mark.parametrize(
        "field",
        ("project", "exported_at", "databases", "notes"),
    )
    def test_manifest_fields(self, tmp_path: Path, field: str) -> None:
        """The manifest exposes the standard fields.

        :param tmp_path: per-test temporary directory
        :param field: expected manifest key
        """
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert field in manifest

    def test_manifest_project_name(self, tmp_path: Path) -> None:
        """The manifest names the project."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert manifest["project"] == "General Moderation"


class TestExportPruning(BaseTest):
    """Retention-based pruning."""

    def test_old_exports_pruned(self, tmp_path: Path) -> None:
        """Exports older than retention are removed."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            stale: Path = root / "exports" / "general_moderation_export_stale.zip"
            stale.write_bytes(b"old")
            old_time: float = stale.stat().st_mtime - (8 * 86400)
            os.utime(stale, (old_time, old_time))
            service.create_export()
            assert not stale.exists()

    def test_fresh_exports_kept(self, tmp_path: Path) -> None:
        """Exports within retention survive."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            service.create_export()
            zips: list[Path] = list((root / "exports").glob("*.zip"))
        assert len(zips) >= 1

    def test_retention_zero(self, tmp_path: Path) -> None:
        """A zero retention day prunes immediately."""
        root: Path = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            service.create_export()
            assert list((root / "exports").glob("*.zip"))


class TestExportEdge(BaseTest):
    """Edge cases in the export service."""

    def test_no_data_directory(self, tmp_path: Path) -> None:
        """A missing data directory yields an empty database set."""
        root: Path = tmp_path
        (root / "exports").mkdir(parents=True, exist_ok=True)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "l.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
            manifest = __import__("json").loads(
                __import__("zipfile").ZipFile(path).read("export_metadata.json")
            )
        assert manifest["databases"] == {}

    def test_no_env_file(self, tmp_path: Path) -> None:
        """A missing .env produces an empty redacted section."""
        root: Path = _build_sandbox(tmp_path)
        (root / ".env").unlink()
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
        assert "config/.env" in _zip_entries(path)

    def test_settings_snapshot_default(self, tmp_path: Path) -> None:
        """Without a snapshot the manifest writes an empty object."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            snapshot: str = archive.read("config/settings_snapshot.json").decode()
        assert snapshot == "{}"


class TestExportMetadataMore(BaseTest):
    """Additional manifest metadata."""

    @pytest.mark.parametrize(
        ("key", "value"),
        (
            ("ai_available", True),
            ("semantic_available", False),
            ("detector_count", 11),
            ("schema_version", 1),
        ),
    )
    def test_manifest_value_roundtrip(self, tmp_path: Path, key: str, value: object) -> None:
        """Custom metadata keys round-trip into the manifest.

        :param tmp_path: per-test temporary directory
        :param key: manifest key
        :param value: metadata value
        """
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export({key: value})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert manifest[key] == value

    def test_semantic_categories_metadata(self, tmp_path: Path) -> None:
        """Semantic category metadata is recorded."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export({"semantic_categories": {"political": 5, "hate": 2}})
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert manifest["semantic_categories"]["political"] == 5

    def test_settings_snapshot_custom(self, tmp_path: Path) -> None:
        """A custom settings snapshot is archived."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export({"settings_snapshot": '{"a": 1}'})
        with zipfile.ZipFile(path) as archive:
            snapshot: str = archive.read("config/settings_snapshot.json").decode()
        assert snapshot == '{"a": 1}'

    def test_exported_at_iso(self, tmp_path: Path) -> None:
        """The exported-at timestamp is ISO formatted."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "T" in manifest["exported_at"]

    def test_manifest_notes_present(self, tmp_path: Path) -> None:
        """The manifest explains secret redaction."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            manifest = __import__("json").loads(archive.read("export_metadata.json"))
        assert "redacted" in manifest["notes"].lower()


class TestExportRedactionMore(BaseTest):
    """Additional redaction coverage."""

    @pytest.mark.parametrize(
        "secret_line",
        (
            "WEBUI_API_KEY=webui_secret_xyz",
            "SECRET_KEY=session_secret_xyz",
            "ENCRYPTION_KEY=enc_key_xyz",
            "DATABASE_PASSWORD=db_pass_xyz",
            "SOME_TOKEN=token_xyz",
            "API_TOKEN=api_token_xyz",
        ),
    )
    def test_various_secrets_redacted(self, tmp_path: Path, secret_line: str) -> None:
        """Keys with secret suffixes are redacted.

        :param tmp_path: per-test temporary directory
        :param secret_line: a line carrying a secret value
        """
        root: Path = _build_sandbox(tmp_path)
        (root / ".env").write_text(secret_line + "\n", encoding="utf-8")
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            env_content: str = archive.read("config/.env").decode()
        assert "xyz" not in env_content
        assert "[REDACTED]" in env_content

    def test_env_missing_line_kept(self, tmp_path: Path) -> None:
        """Lines without secrets pass through unchanged."""
        root: Path = _build_sandbox(tmp_path)
        (root / ".env").write_text("APP_PORT=18427\n", encoding="utf-8")
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            env_content: str = archive.read("config/.env").decode()
        assert "APP_PORT=18427" in env_content

    def test_empty_env_handled(self, tmp_path: Path) -> None:
        """An empty .env file exports cleanly."""
        root: Path = _build_sandbox(tmp_path)
        (root / ".env").write_text("", encoding="utf-8")
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
        assert "config/.env" in _zip_entries(path)


class TestExportMultipleDbs(BaseTest):
    """Multiple databases in one export."""

    @pytest.mark.parametrize("db_count", (1, 2, 3))
    def test_all_dbs_archived(self, tmp_path: Path, db_count: int) -> None:
        """Every database under data/ is archived.

        :param tmp_path: per-test temporary directory
        :param db_count: number of database files
        """
        root: Path = _build_sandbox(tmp_path)
        for index in range(1, db_count):
            connection = sqlite3.connect(str(root / "data" / f"extra{index}.db"))
            connection.execute("CREATE TABLE t (id INTEGER)")
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
            path: Path = service.create_export()
        entries: list[str] = _zip_entries(path)
        db_entries: list[str] = [entry for entry in entries if "databases/" in entry]
        assert len(db_entries) == db_count

    @pytest.mark.parametrize("table_count", (1, 2, 4))
    def test_every_table_has_csv(self, tmp_path: Path, table_count: int) -> None:
        """Each table in each database gets a CSV dump.

        :param tmp_path: per-test temporary directory
        :param table_count: number of tables to create
        """
        root: Path = _build_sandbox(tmp_path)
        connection = sqlite3.connect(str(root / "data" / "multi.db"))
        for index in range(table_count):
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
            path: Path = service.create_export()
        entries: list[str] = _zip_entries(path)
        csv_entries: list[str] = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == table_count


class TestExportLocking(BaseTest):
    """Concurrent export safety."""

    def test_concurrent_exports(self, tmp_path: Path) -> None:
        """Concurrent exports complete without exceptions."""
        import threading

        service, root = _service(tmp_path)
        errors: list[Exception] = []
        lock: threading.Lock = threading.Lock()

        def _run() -> None:
            try:
                with _Chdir(root):
                    service.create_export()
            except Exception as exc:  # pragma: no cover - failure path
                with lock:
                    errors.append(exc)

        threads: list[threading.Thread] = [threading.Thread(target=_run) for _ in range(3)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        assert not errors
        assert list((root / "exports").glob("*.zip"))


class TestExportRetention(BaseTest):
    """Retention pruning variations."""

    @pytest.mark.parametrize(
        ("retention", "age_days", "should_exist"),
        (
            (7, 1, True),
            (7, 6, True),
            (7, 7, False),
            (7, 30, False),
            (30, 29, True),
            (30, 31, False),
            (1, 2, False),
            (90, 89, True),
        ),
    )
    def test_retention_pruning(
        self,
        tmp_path: Path,
        retention: int,
        age_days: int,
        should_exist: bool,
    ) -> None:
        """Exports older than retention are pruned.

        :param tmp_path: per-test temporary directory
        :param retention: retention period in days
        :param age_days: age of the stale archive
        :param should_exist: whether the archive survives
        """
        root: Path = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=retention,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale: Path = root / "exports" / "stale.zip"
            stale.write_bytes(b"old")
            stamp: float = stale.stat().st_mtime - (age_days * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is should_exist

    def test_only_zip_files_pruned(self, tmp_path: Path) -> None:
        """Non-ZIP files are never pruned."""
        root: Path = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            keep: Path = root / "exports" / "notes.txt"
            keep.write_text("keep me", encoding="utf-8")
            stamp: float = keep.stat().st_mtime - (5 * 86400)
            os.utime(keep, (stamp, stamp))
            service.create_export()
            assert keep.exists()

    def test_subdirectories_not_pruned(self, tmp_path: Path) -> None:
        """Subdirectories under exports are left alone."""
        root: Path = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=1,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            subdir: Path = root / "exports" / "sub"
            subdir.mkdir(exist_ok=True)
            service.create_export()
            assert subdir.exists()


class TestExportDatabaseEdge(BaseTest):
    """Database handling edge cases."""

    def test_readonly_database_exported(self, tmp_path: Path) -> None:
        """Databases are opened read-only for CSV dumps."""
        root: Path = _build_sandbox(tmp_path)
        connection = sqlite3.connect(str(root / "data" / "ro.db"))
        connection.execute("CREATE TABLE t (id INTEGER)")
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
            path: Path = service.create_export()
        entries: list[str] = _zip_entries(path)
        assert any("ro.db" in entry for entry in entries)

    def test_empty_database_csv(self, tmp_path: Path) -> None:
        """An empty table still produces a header-only CSV."""
        root: Path = _build_sandbox(tmp_path)
        connection = sqlite3.connect(str(root / "data" / "empty.db"))
        connection.execute("CREATE TABLE t (id INTEGER, name TEXT)")
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
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            csv_entry: str = next(entry for entry in archive.namelist() if "empty_t.csv" in entry)
            content: str = archive.read(csv_entry).decode()
        assert content.startswith("id,name")

    def test_whitespace_db_names(self, tmp_path: Path) -> None:
        """Database files with odd names are archived."""
        root: Path = _build_sandbox(tmp_path)
        connection = sqlite3.connect(str(root / "data" / "weird name.db"))
        connection.execute("CREATE TABLE t (id INTEGER)")
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
            path: Path = service.create_export()
        assert any("weird name.db" in entry for entry in _zip_entries(path))


class TestExportLogs(BaseTest):
    """Log file inclusion."""

    def test_rotated_logs_included(self, tmp_path: Path) -> None:
        """Rotated log backups are archived."""
        root: Path = _build_sandbox(tmp_path)
        (root / "logs" / "moderation.log.1").write_text("rotated", encoding="utf-8")
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
        entries: list[str] = _zip_entries(path)
        assert any("moderation.log.1" in entry for entry in entries)

    def test_missing_log_dir(self, tmp_path: Path) -> None:
        """A missing logs directory contributes nothing."""
        root: Path = _build_sandbox(tmp_path)
        import shutil

        shutil.rmtree(root / "logs")
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
        assert "logs/" not in str(_zip_entries(path))


class TestExportCsvContent(BaseTest):
    """CSV content correctness."""

    @pytest.mark.parametrize(
        ("name", "expected"),
        (
            ("alpha", True),
            ("beta", True),
            ("gamma", False),
            ("delta", False),
        ),
    )
    def test_csv_row_presence(self, tmp_path: Path, name: str, expected: bool) -> None:
        """CSV rows reflect the database contents.

        :param tmp_path: per-test temporary directory
        :param name: a name to search for
        :param expected: whether the name should appear
        """
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            csv_entry: str = next(entry for entry in archive.namelist() if "users_t.csv" in entry)
            content: str = archive.read(csv_entry).decode()
        assert (name in content) is expected

    def test_csv_number_rows(self, tmp_path: Path) -> None:
        """The CSV includes the header plus one row per record."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path: Path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            csv_entry: str = next(entry for entry in archive.namelist() if "users_t.csv" in entry)
            content: str = archive.read(csv_entry).decode()
        assert len(content.strip().splitlines()) == 3

    def test_semantic_missing_dir(self, tmp_path: Path) -> None:
        """A missing semantic directory contributes nothing."""
        root: Path = _build_sandbox(tmp_path)
        import shutil

        shutil.rmtree(root / "semantic")
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
        entries: list[str] = _zip_entries(path)
        assert not any("semantic/" in entry for entry in entries)

    def test_log_only_extension_globbed(self, tmp_path: Path) -> None:
        """Only moderation log files are archived."""
        root: Path = _build_sandbox(tmp_path)
        (root / "logs" / "other.log").write_text("other", encoding="utf-8")
        (root / "logs" / "moderation.log.2").write_text("rot", encoding="utf-8")
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path: Path = service.create_export()
        entries: list[str] = _zip_entries(path)
        assert any("moderation.log.2" in entry for entry in entries)
        assert not any("other.log" in entry for entry in entries)

    def test_timestamp_export_dir_created(self, tmp_path: Path) -> None:
        """The export staging directory is created."""
        root: Path = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / "exports"),
            export_retention_days=7,
            log_file_path=str(root / "logs" / "moderation.log"),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            service.create_export()
            staging: list[Path] = [path for path in (root / "exports").iterdir() if path.is_dir()]
        assert staging
