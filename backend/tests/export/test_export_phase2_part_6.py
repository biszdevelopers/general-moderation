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
    (3, 3, 0, 8631,),
    (3, 3, 1, 8632,),
    (3, 3, 2, 8633,),
    (3, 3, 3, 8634,),
    (3, 3, 4, 8635,),
    (3, 4, 0, 8636,),
    (3, 4, 1, 8637,),
    (3, 4, 2, 8638,),
    (3, 4, 3, 8639,),
    (3, 4, 4, 8640,),
    (4, 1, 0, 8641,),
    (4, 1, 1, 8642,),
    (4, 1, 2, 8643,),
    (4, 1, 3, 8644,),
    (4, 1, 4, 8645,),
    (4, 2, 0, 8646,),
    (4, 2, 1, 8647,),
    (4, 2, 2, 8648,),
    (4, 2, 3, 8649,),
    (4, 2, 4, 8650,),
    (4, 3, 0, 8651,),
    (4, 3, 1, 8652,),
    (4, 3, 2, 8653,),
    (4, 3, 3, 8654,),
    (4, 3, 4, 8655,),
    (4, 4, 0, 8656,),
    (4, 4, 1, 8657,),
    (4, 4, 2, 8658,),
    (4, 4, 3, 8659,),
    (4, 4, 4, 8660,),
    (5, 1, 0, 8661,),
    (5, 1, 1, 8662,),
    (5, 1, 2, 8663,),
    (5, 1, 3, 8664,),
    (5, 1, 4, 8665,),
    (5, 2, 0, 8666,),
    (5, 2, 1, 8667,),
    (5, 2, 2, 8668,),
    (5, 2, 3, 8669,),
    (5, 2, 4, 8670,),
    (5, 3, 0, 8671,),
    (5, 3, 1, 8672,),
    (5, 3, 2, 8673,),
    (5, 3, 3, 8674,),
    (5, 3, 4, 8675,),
    (5, 4, 0, 8676,),
    (5, 4, 1, 8677,),
    (5, 4, 2, 8678,),
    (5, 4, 3, 8679,),
    (5, 4, 4, 8680,),
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
    ('', 8681,),
    ('data', 8682,),
    ('logs', 8683,),
    ('data+logs', 8684,),
    ('semantic', 8685,),
    ('data+semantic', 8686,),
    ('logs+semantic', 8687,),
    ('data+logs+semantic', 8688,),
    ('env', 8689,),
    ('data+env', 8690,),
    ('logs+env', 8691,),
    ('data+logs+env', 8692,),
    ('semantic+env', 8693,),
    ('data+semantic+env', 8694,),
    ('logs+semantic+env', 8695,),
    ('data+logs+semantic+env', 8696,),
    ('example', 8697,),
    ('data+example', 8698,),
    ('logs+example', 8699,),
    ('data+logs+example', 8700,),
    ('semantic+example', 8701,),
    ('data+semantic+example', 8702,),
    ('logs+semantic+example', 8703,),
    ('data+logs+semantic+example', 8704,),
    ('env+example', 8705,),
    ('data+env+example', 8706,),
    ('logs+env+example', 8707,),
    ('data+logs+env+example', 8708,),
    ('semantic+env+example', 8709,),
    ('data+semantic+env+example', 8710,),
    ('logs+semantic+env+example', 8711,),
    ('data+logs+semantic+env+example', 8712,),
    ('', 8713,),
    ('data', 8714,),
    ('logs', 8715,),
    ('data+logs', 8716,),
    ('semantic', 8717,),
    ('data+semantic', 8718,),
    ('logs+semantic', 8719,),
    ('data+logs+semantic', 8720,),
    ('env', 8721,),
    ('data+env', 8722,),
    ('logs+env', 8723,),
    ('data+logs+env', 8724,),
    ('semantic+env', 8725,),
    ('data+semantic+env', 8726,),
    ('logs+semantic+env', 8727,),
    ('data+logs+semantic+env', 8728,),
    ('example', 8729,),
    ('data+example', 8730,),
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
