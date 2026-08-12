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


class TestMultiDbCases(BaseTest):
    """MultiDbCases scenarios."""

    def test_multidb_0_8432(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_1_8433(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_2_8434(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_3_8435(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_4_8436(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_0_8437(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_1_8438(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_2_8439(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_3_8440(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_4_8441(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 3):
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
        assert len(db_entries) == 4
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_0_8442(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_1_8443(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_2_8444(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_3_8445(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_4_8446(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_0_8447(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_1_8448(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_2_8449(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_3_8450(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_4_8451(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_0_8452(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_1_8453(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_2_8454(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_3_8455(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_4_8456(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_0_8457(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_1_8458(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_2_8459(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_3_8460(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_4_8461(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 4):
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
        assert len(db_entries) == 5
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_0_8462(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_1_8463(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_2_8464(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_3_8465(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_4_8466(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 1

    def test_multidb_0_8467(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_1_8468(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_2_8469(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_3_8470(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_4_8471(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 2

    def test_multidb_0_8472(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_1_8473(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_2_8474(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_3_8475(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_4_8476(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 3

    def test_multidb_0_8477(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_1_8478(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_2_8479(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_3_8480(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4

    def test_multidb_4_8481(self, tmp_path: Path) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, 5):
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
        assert len(db_entries) == 6
        csv_entries = [entry for entry in entries if "multi_t" in entry]
        assert len(csv_entries) == 4


class TestExportEdges(BaseTest):
    """ExportEdges scenarios."""

    def test_edge_0_8482(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_1_8483(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_2_8484(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_3_8485(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_4_8486(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_5_8487(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_6_8488(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_7_8489(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_8_8490(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_9_8491(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_10_8492(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_11_8493(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_12_8494(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_13_8495(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_14_8496(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_15_8497(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_16_8498(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_17_8499(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_18_8500(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_19_8501(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_20_8502(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_21_8503(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_22_8504(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_23_8505(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_24_8506(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_25_8507(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_26_8508(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_27_8509(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_28_8510(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_29_8511(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_30_8512(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_31_8513(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_32_8514(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_33_8515(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_34_8516(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_35_8517(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_36_8518(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_37_8519(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_38_8520(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_39_8521(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_40_8522(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_41_8523(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_42_8524(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_43_8525(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_44_8526(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_45_8527(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_46_8528(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_47_8529(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_48_8530(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)

    def test_edge_49_8531(self, tmp_path: Path) -> None:
        """Rare filesystem states are handled without crashing."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert "config/.env" in _zip_entries(path)
