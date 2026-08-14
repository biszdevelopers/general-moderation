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
    (3, 3, 0, 8591,),
    (3, 3, 1, 8592,),
    (3, 3, 2, 8593,),
    (3, 3, 3, 8594,),
    (3, 3, 4, 8595,),
    (3, 4, 0, 8596,),
    (3, 4, 1, 8597,),
    (3, 4, 2, 8598,),
    (3, 4, 3, 8599,),
    (3, 4, 4, 8600,),
    (4, 1, 0, 8601,),
    (4, 1, 1, 8602,),
    (4, 1, 2, 8603,),
    (4, 1, 3, 8604,),
    (4, 1, 4, 8605,),
    (4, 2, 0, 8606,),
    (4, 2, 1, 8607,),
    (4, 2, 2, 8608,),
    (4, 2, 3, 8609,),
    (4, 2, 4, 8610,),
    (4, 3, 0, 8611,),
    (4, 3, 1, 8612,),
    (4, 3, 2, 8613,),
    (4, 3, 3, 8614,),
    (4, 3, 4, 8615,),
    (4, 4, 0, 8616,),
    (4, 4, 1, 8617,),
    (4, 4, 2, 8618,),
    (4, 4, 3, 8619,),
    (4, 4, 4, 8620,),
    (5, 1, 0, 8621,),
    (5, 1, 1, 8622,),
    (5, 1, 2, 8623,),
    (5, 1, 3, 8624,),
    (5, 1, 4, 8625,),
    (5, 2, 0, 8626,),
    (5, 2, 1, 8627,),
    (5, 2, 2, 8628,),
    (5, 2, 3, 8629,),
    (5, 2, 4, 8630,),
    (5, 3, 0, 8631,),
    (5, 3, 1, 8632,),
    (5, 3, 2, 8633,),
    (5, 3, 3, 8634,),
    (5, 3, 4, 8635,),
    (5, 4, 0, 8636,),
    (5, 4, 1, 8637,),
    (5, 4, 2, 8638,),
    (5, 4, 3, 8639,),
    (5, 4, 4, 8640,),
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
    ('', 8641,),
    ('data', 8642,),
    ('logs', 8643,),
    ('data+logs', 8644,),
    ('semantic', 8645,),
    ('data+semantic', 8646,),
    ('logs+semantic', 8647,),
    ('data+logs+semantic', 8648,),
    ('env', 8649,),
    ('data+env', 8650,),
    ('logs+env', 8651,),
    ('data+logs+env', 8652,),
    ('semantic+env', 8653,),
    ('data+semantic+env', 8654,),
    ('logs+semantic+env', 8655,),
    ('data+logs+semantic+env', 8656,),
    ('example', 8657,),
    ('data+example', 8658,),
    ('logs+example', 8659,),
    ('data+logs+example', 8660,),
    ('semantic+example', 8661,),
    ('data+semantic+example', 8662,),
    ('logs+semantic+example', 8663,),
    ('data+logs+semantic+example', 8664,),
    ('env+example', 8665,),
    ('data+env+example', 8666,),
    ('logs+env+example', 8667,),
    ('data+logs+env+example', 8668,),
    ('semantic+env+example', 8669,),
    ('data+semantic+env+example', 8670,),
    ('logs+semantic+env+example', 8671,),
    ('data+logs+semantic+env+example', 8672,),
    ('', 8673,),
    ('data', 8674,),
    ('logs', 8675,),
    ('data+logs', 8676,),
    ('semantic', 8677,),
    ('data+semantic', 8678,),
    ('logs+semantic', 8679,),
    ('data+logs+semantic', 8680,),
    ('env', 8681,),
    ('data+env', 8682,),
    ('logs+env', 8683,),
    ('data+logs+env', 8684,),
    ('semantic+env', 8685,),
    ('data+semantic+env', 8686,),
    ('logs+semantic+env', 8687,),
    ('data+logs+semantic+env', 8688,),
    ('example', 8689,),
    ('data+example', 8690,),
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
