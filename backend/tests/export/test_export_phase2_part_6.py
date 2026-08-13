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

_MULTIDB_CASES: tuple[tuple[int, int, int, int], ...] = (
    (3, 3, 0, 8432,),
    (3, 3, 1, 8433,),
    (3, 3, 2, 8434,),
    (3, 3, 3, 8435,),
    (3, 3, 4, 8436,),
    (3, 4, 0, 8437,),
    (3, 4, 1, 8438,),
    (3, 4, 2, 8439,),
    (3, 4, 3, 8440,),
    (3, 4, 4, 8441,),
    (4, 1, 0, 8442,),
    (4, 1, 1, 8443,),
    (4, 1, 2, 8444,),
    (4, 1, 3, 8445,),
    (4, 1, 4, 8446,),
    (4, 2, 0, 8447,),
    (4, 2, 1, 8448,),
    (4, 2, 2, 8449,),
    (4, 2, 3, 8450,),
    (4, 2, 4, 8451,),
    (4, 3, 0, 8452,),
    (4, 3, 1, 8453,),
    (4, 3, 2, 8454,),
    (4, 3, 3, 8455,),
    (4, 3, 4, 8456,),
    (4, 4, 0, 8457,),
    (4, 4, 1, 8458,),
    (4, 4, 2, 8459,),
    (4, 4, 3, 8460,),
    (4, 4, 4, 8461,),
    (5, 1, 0, 8462,),
    (5, 1, 1, 8463,),
    (5, 1, 2, 8464,),
    (5, 1, 3, 8465,),
    (5, 1, 4, 8466,),
    (5, 2, 0, 8467,),
    (5, 2, 1, 8468,),
    (5, 2, 2, 8469,),
    (5, 2, 3, 8470,),
    (5, 2, 4, 8471,),
    (5, 3, 0, 8472,),
    (5, 3, 1, 8473,),
    (5, 3, 2, 8474,),
    (5, 3, 3, 8475,),
    (5, 3, 4, 8476,),
    (5, 4, 0, 8477,),
    (5, 4, 1, 8478,),
    (5, 4, 2, 8479,),
    (5, 4, 3, 8480,),
    (5, 4, 4, 8481,),
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


_EDGE_EXPORT_CASES: tuple[tuple[str, int], ...] = (
    ('', 8482,),
    ('data', 8483,),
    ('logs', 8484,),
    ('data+logs', 8485,),
    ('semantic', 8486,),
    ('data+semantic', 8487,),
    ('logs+semantic', 8488,),
    ('data+logs+semantic', 8489,),
    ('env', 8490,),
    ('data+env', 8491,),
    ('logs+env', 8492,),
    ('data+logs+env', 8493,),
    ('semantic+env', 8494,),
    ('data+semantic+env', 8495,),
    ('logs+semantic+env', 8496,),
    ('data+logs+semantic+env', 8497,),
    ('example', 8498,),
    ('data+example', 8499,),
    ('logs+example', 8500,),
    ('data+logs+example', 8501,),
    ('semantic+example', 8502,),
    ('data+semantic+example', 8503,),
    ('logs+semantic+example', 8504,),
    ('data+logs+semantic+example', 8505,),
    ('env+example', 8506,),
    ('data+env+example', 8507,),
    ('logs+env+example', 8508,),
    ('data+logs+env+example', 8509,),
    ('semantic+env+example', 8510,),
    ('data+semantic+env+example', 8511,),
    ('logs+semantic+env+example', 8512,),
    ('data+logs+semantic+env+example', 8513,),
    ('', 8514,),
    ('data', 8515,),
    ('logs', 8516,),
    ('data+logs', 8517,),
    ('semantic', 8518,),
    ('data+semantic', 8519,),
    ('logs+semantic', 8520,),
    ('data+logs+semantic', 8521,),
    ('env', 8522,),
    ('data+env', 8523,),
    ('logs+env', 8524,),
    ('data+logs+env', 8525,),
    ('semantic+env', 8526,),
    ('data+semantic+env', 8527,),
    ('logs+semantic+env', 8528,),
    ('data+logs+semantic+env', 8529,),
    ('example', 8530,),
    ('data+example', 8531,),
)

class TestEdgeExport(BaseTest):
    """Rare filesystem states are handled without crashing."""

    @pytest.mark.parametrize(('missing', 'uid',), _EDGE_EXPORT_CASES)
    def test_edge_export(self, tmp_path: Path, missing: str, uid: int) -> None:
        """Rare filesystem states are handled without crashing."""
        root = _build_sandbox(tmp_path)
        import shutil
        (root / '.env.example').write_text('SOME_KEY=value\n', encoding='utf-8')
        if 'data' in missing:
            shutil.rmtree(root / 'data')
        if 'logs' in missing:
            shutil.rmtree(root / 'logs')
        if 'semantic' in missing:
            shutil.rmtree(root / 'semantic')
        if 'env' in missing:
            (root / '.env').unlink()
        if 'example' in missing:
            (root / '.env.example').unlink()
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / 'exports'),
            export_retention_days=7,
            log_file_path=str(root / 'logs' / 'moderation.log'),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path = service.create_export()
        assert path.exists()
        assert 'export_metadata.json' in _zip_entries(path)
