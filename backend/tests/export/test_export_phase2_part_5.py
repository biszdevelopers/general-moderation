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
    for directory in ('data', 'logs', 'semantic', 'exports'):
        (tmp_path / directory).mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(str(tmp_path / 'data' / 'users.db'))
    connection.execute('CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT)')
    connection.execute("INSERT INTO t (name) VALUES ('alpha'), ('beta')")
    connection.commit()
    connection.close()
    (tmp_path / 'logs' / 'moderation.log').write_text('{"verdict": "PASS"}\n', encoding='utf-8')
    (tmp_path / '.env').write_text('ADMIN_API_KEY=supersecret\nAPP_HOST=0.0.0.0\n', encoding='utf-8')
    (tmp_path / 'semantic' / 'political.index').write_bytes(b'idx')
    (tmp_path / 'semantic' / 'political.json').write_text('["x"]', encoding='utf-8')
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
        export_temp_dir=str(root / 'exports'),
        export_retention_days=7,
        log_file_path=str(root / 'logs' / 'moderation.log'),
    )
    return ExportService(settings, None), root

def _zip_entries(zip_path: Path) -> list[str]:
    with zipfile.ZipFile(zip_path) as archive:
        return sorted(archive.namelist())

_RETENTION_CASES: tuple[tuple[int, int, str, int], ...] = (
    (1, 1, 'stale0.zip', 8531,),
    (1, 1, 'stale1.zip', 8532,),
    (1, 1, 'stale2.zip', 8533,),
    (1, 1, 'stale3.zip', 8534,),
    (1, 1, 'stale4.zip', 8535,),
    (1, 1, 'stale5.zip', 8536,),
    (1, 1, 'stale6.zip', 8537,),
    (1, 1, 'stale7.zip', 8538,),
    (1, 1, 'stale8.zip', 8539,),
    (1, 1, 'stale9.zip', 8540,),
    (90, 89, 'stale0.zip', 8541,),
    (90, 89, 'stale1.zip', 8542,),
    (90, 89, 'stale2.zip', 8543,),
    (90, 89, 'stale3.zip', 8544,),
    (90, 89, 'stale4.zip', 8545,),
    (90, 89, 'stale5.zip', 8546,),
    (90, 89, 'stale6.zip', 8547,),
    (90, 89, 'stale7.zip', 8548,),
    (90, 89, 'stale8.zip', 8549,),
    (90, 89, 'stale9.zip', 8550,),
    (90, 91, 'stale0.zip', 8551,),
    (90, 91, 'stale1.zip', 8552,),
    (90, 91, 'stale2.zip', 8553,),
    (90, 91, 'stale3.zip', 8554,),
    (90, 91, 'stale4.zip', 8555,),
    (90, 91, 'stale5.zip', 8556,),
    (90, 91, 'stale6.zip', 8557,),
    (90, 91, 'stale7.zip', 8558,),
    (90, 91, 'stale8.zip', 8559,),
    (90, 91, 'stale9.zip', 8560,),
    (365, 364, 'stale0.zip', 8561,),
    (365, 364, 'stale1.zip', 8562,),
    (365, 364, 'stale2.zip', 8563,),
    (365, 364, 'stale3.zip', 8564,),
    (365, 364, 'stale4.zip', 8565,),
    (365, 364, 'stale5.zip', 8566,),
    (365, 364, 'stale6.zip', 8567,),
    (365, 364, 'stale7.zip', 8568,),
    (365, 364, 'stale8.zip', 8569,),
    (365, 364, 'stale9.zip', 8570,),
    (365, 366, 'stale0.zip', 8571,),
    (365, 366, 'stale1.zip', 8572,),
    (365, 366, 'stale2.zip', 8573,),
    (365, 366, 'stale3.zip', 8574,),
    (365, 366, 'stale4.zip', 8575,),
    (365, 366, 'stale5.zip', 8576,),
    (365, 366, 'stale6.zip', 8577,),
    (365, 366, 'stale7.zip', 8578,),
    (365, 366, 'stale8.zip', 8579,),
    (365, 366, 'stale9.zip', 8580,),
)

class TestRetention(BaseTest):
    """Exports older than retention are pruned."""

    @pytest.mark.parametrize(('retention', 'age', 'stale_name', 'uid',), _RETENTION_CASES)
    def test_retention(self, tmp_path: Path, retention: int, age: int, stale_name: str, uid: int) -> None:
        """Exports older than retention are pruned."""
        root = _build_sandbox(tmp_path)
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / 'exports'),
            export_retention_days=retention,
            log_file_path=str(root / 'logs' / 'moderation.log'),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            stale = root / 'exports' / stale_name
            stale.write_bytes(b'old')
            stamp = stale.stat().st_mtime - (age * 86400)
            os.utime(stale, (stamp, stamp))
            service.create_export()
            assert stale.exists() is (age < retention)


_MULTIDB_CASES: tuple[tuple[int, int, int, int], ...] = (
    (1, 1, 0, 8581,),
    (1, 1, 1, 8582,),
    (1, 1, 2, 8583,),
    (1, 1, 3, 8584,),
    (1, 1, 4, 8585,),
    (1, 2, 0, 8586,),
    (1, 2, 1, 8587,),
    (1, 2, 2, 8588,),
    (1, 2, 3, 8589,),
    (1, 2, 4, 8590,),
    (1, 3, 0, 8591,),
    (1, 3, 1, 8592,),
    (1, 3, 2, 8593,),
    (1, 3, 3, 8594,),
    (1, 3, 4, 8595,),
    (1, 4, 0, 8596,),
    (1, 4, 1, 8597,),
    (1, 4, 2, 8598,),
    (1, 4, 3, 8599,),
    (1, 4, 4, 8600,),
    (2, 1, 0, 8601,),
    (2, 1, 1, 8602,),
    (2, 1, 2, 8603,),
    (2, 1, 3, 8604,),
    (2, 1, 4, 8605,),
    (2, 2, 0, 8606,),
    (2, 2, 1, 8607,),
    (2, 2, 2, 8608,),
    (2, 2, 3, 8609,),
    (2, 2, 4, 8610,),
    (2, 3, 0, 8611,),
    (2, 3, 1, 8612,),
    (2, 3, 2, 8613,),
    (2, 3, 3, 8614,),
    (2, 3, 4, 8615,),
    (2, 4, 0, 8616,),
    (2, 4, 1, 8617,),
    (2, 4, 2, 8618,),
    (2, 4, 3, 8619,),
    (2, 4, 4, 8620,),
    (3, 1, 0, 8621,),
    (3, 1, 1, 8622,),
    (3, 1, 2, 8623,),
    (3, 1, 3, 8624,),
    (3, 1, 4, 8625,),
    (3, 2, 0, 8626,),
    (3, 2, 1, 8627,),
    (3, 2, 2, 8628,),
    (3, 2, 3, 8629,),
    (3, 2, 4, 8630,),
)

class TestMultidb(BaseTest):
    """Every database and table is archived with CSVs."""

    @pytest.mark.parametrize(('db_count', 'table_count', 'scenario', 'uid',), _MULTIDB_CASES)
    def test_multidb(self, tmp_path: Path, db_count: int, table_count: int, scenario: int, uid: int) -> None:
        """Every database and table is archived with CSVs."""
        root = _build_sandbox(tmp_path)
        for index in range(1, db_count):
            connection = sqlite3.connect(str(root / 'data' / f'extra{index}.db'))
            connection.execute('CREATE TABLE t (id INTEGER)')
            connection.commit()
            connection.close()
        for index in range(table_count):
            connection = sqlite3.connect(str(root / 'data' / 'multi.db'))
            connection.execute(f'CREATE TABLE t{scenario}_{index} (id INTEGER)')
            connection.commit()
            connection.close()
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / 'exports'),
            export_retention_days=7,
            log_file_path=str(root / 'logs' / 'moderation.log'),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        db_entries = [entry for entry in entries if 'databases/' in entry]
        assert len(db_entries) == db_count + 1
        csv_entries = [entry for entry in entries if 'multi_t' in entry]
        assert len(csv_entries) == table_count
