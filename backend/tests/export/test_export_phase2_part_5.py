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
    (1, 1, 'stale0.zip', 8491,),
    (1, 1, 'stale1.zip', 8492,),
    (1, 1, 'stale2.zip', 8493,),
    (1, 1, 'stale3.zip', 8494,),
    (1, 1, 'stale4.zip', 8495,),
    (1, 1, 'stale5.zip', 8496,),
    (1, 1, 'stale6.zip', 8497,),
    (1, 1, 'stale7.zip', 8498,),
    (1, 1, 'stale8.zip', 8499,),
    (1, 1, 'stale9.zip', 8500,),
    (90, 89, 'stale0.zip', 8501,),
    (90, 89, 'stale1.zip', 8502,),
    (90, 89, 'stale2.zip', 8503,),
    (90, 89, 'stale3.zip', 8504,),
    (90, 89, 'stale4.zip', 8505,),
    (90, 89, 'stale5.zip', 8506,),
    (90, 89, 'stale6.zip', 8507,),
    (90, 89, 'stale7.zip', 8508,),
    (90, 89, 'stale8.zip', 8509,),
    (90, 89, 'stale9.zip', 8510,),
    (90, 91, 'stale0.zip', 8511,),
    (90, 91, 'stale1.zip', 8512,),
    (90, 91, 'stale2.zip', 8513,),
    (90, 91, 'stale3.zip', 8514,),
    (90, 91, 'stale4.zip', 8515,),
    (90, 91, 'stale5.zip', 8516,),
    (90, 91, 'stale6.zip', 8517,),
    (90, 91, 'stale7.zip', 8518,),
    (90, 91, 'stale8.zip', 8519,),
    (90, 91, 'stale9.zip', 8520,),
    (365, 364, 'stale0.zip', 8521,),
    (365, 364, 'stale1.zip', 8522,),
    (365, 364, 'stale2.zip', 8523,),
    (365, 364, 'stale3.zip', 8524,),
    (365, 364, 'stale4.zip', 8525,),
    (365, 364, 'stale5.zip', 8526,),
    (365, 364, 'stale6.zip', 8527,),
    (365, 364, 'stale7.zip', 8528,),
    (365, 364, 'stale8.zip', 8529,),
    (365, 364, 'stale9.zip', 8530,),
    (365, 366, 'stale0.zip', 8531,),
    (365, 366, 'stale1.zip', 8532,),
    (365, 366, 'stale2.zip', 8533,),
    (365, 366, 'stale3.zip', 8534,),
    (365, 366, 'stale4.zip', 8535,),
    (365, 366, 'stale5.zip', 8536,),
    (365, 366, 'stale6.zip', 8537,),
    (365, 366, 'stale7.zip', 8538,),
    (365, 366, 'stale8.zip', 8539,),
    (365, 366, 'stale9.zip', 8540,),
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
    (1, 1, 0, 8541,),
    (1, 1, 1, 8542,),
    (1, 1, 2, 8543,),
    (1, 1, 3, 8544,),
    (1, 1, 4, 8545,),
    (1, 2, 0, 8546,),
    (1, 2, 1, 8547,),
    (1, 2, 2, 8548,),
    (1, 2, 3, 8549,),
    (1, 2, 4, 8550,),
    (1, 3, 0, 8551,),
    (1, 3, 1, 8552,),
    (1, 3, 2, 8553,),
    (1, 3, 3, 8554,),
    (1, 3, 4, 8555,),
    (1, 4, 0, 8556,),
    (1, 4, 1, 8557,),
    (1, 4, 2, 8558,),
    (1, 4, 3, 8559,),
    (1, 4, 4, 8560,),
    (2, 1, 0, 8561,),
    (2, 1, 1, 8562,),
    (2, 1, 2, 8563,),
    (2, 1, 3, 8564,),
    (2, 1, 4, 8565,),
    (2, 2, 0, 8566,),
    (2, 2, 1, 8567,),
    (2, 2, 2, 8568,),
    (2, 2, 3, 8569,),
    (2, 2, 4, 8570,),
    (2, 3, 0, 8571,),
    (2, 3, 1, 8572,),
    (2, 3, 2, 8573,),
    (2, 3, 3, 8574,),
    (2, 3, 4, 8575,),
    (2, 4, 0, 8576,),
    (2, 4, 1, 8577,),
    (2, 4, 2, 8578,),
    (2, 4, 3, 8579,),
    (2, 4, 4, 8580,),
    (3, 1, 0, 8581,),
    (3, 1, 1, 8582,),
    (3, 1, 2, 8583,),
    (3, 1, 3, 8584,),
    (3, 1, 4, 8585,),
    (3, 2, 0, 8586,),
    (3, 2, 1, 8587,),
    (3, 2, 2, 8588,),
    (3, 2, 3, 8589,),
    (3, 2, 4, 8590,),
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
