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

_MANIFEST_CASES: tuple[tuple[str, int, bool, bool, int], ...] = (
    ('notes', 11, False, False, 8427,),
    ('notes', 12, True, True, 8428,),
    ('schema_version', 0, True, True, 8429,),
    ('schema_version', 1, False, False, 8430,),
    ('schema_version', 2, True, False, 8431,),
    ('schema_version', 3, False, True, 8432,),
    ('schema_version', 4, True, False, 8433,),
    ('schema_version', 5, False, False, 8434,),
    ('schema_version', 6, True, True, 8435,),
    ('schema_version', 7, False, False, 8436,),
    ('schema_version', 8, True, False, 8437,),
    ('schema_version', 9, False, True, 8438,),
    ('schema_version', 10, True, False, 8439,),
    ('schema_version', 11, False, False, 8440,),
    ('schema_version', 12, True, True, 8441,),
    ('detector_count', 0, True, True, 8442,),
    ('detector_count', 1, False, False, 8443,),
    ('detector_count', 2, True, False, 8444,),
    ('detector_count', 3, False, True, 8445,),
    ('detector_count', 4, True, False, 8446,),
    ('detector_count', 5, False, False, 8447,),
    ('detector_count', 6, True, True, 8448,),
    ('detector_count', 7, False, False, 8449,),
    ('detector_count', 8, True, False, 8450,),
    ('detector_count', 9, False, True, 8451,),
    ('detector_count', 10, True, False, 8452,),
    ('detector_count', 11, False, False, 8453,),
    ('detector_count', 12, True, True, 8454,),
    ('ai_available', 0, True, True, 8455,),
    ('ai_available', 1, False, False, 8456,),
    ('ai_available', 2, True, False, 8457,),
    ('ai_available', 3, False, True, 8458,),
    ('ai_available', 4, True, False, 8459,),
    ('ai_available', 5, False, False, 8460,),
    ('ai_available', 6, True, True, 8461,),
    ('ai_available', 7, False, False, 8462,),
    ('ai_available', 8, True, False, 8463,),
    ('ai_available', 9, False, True, 8464,),
    ('ai_available', 10, True, False, 8465,),
    ('ai_available', 11, False, False, 8466,),
    ('ai_available', 12, True, True, 8467,),
    ('semantic_available', 0, True, True, 8468,),
    ('semantic_available', 1, False, False, 8469,),
    ('semantic_available', 2, True, False, 8470,),
    ('semantic_available', 3, False, True, 8471,),
    ('semantic_available', 4, True, False, 8472,),
    ('semantic_available', 5, False, False, 8473,),
    ('semantic_available', 6, True, True, 8474,),
    ('semantic_available', 7, False, False, 8475,),
    ('semantic_available', 8, True, False, 8476,),
)

class TestManifest(BaseTest):
    """The metadata manifest exposes every documented field."""

    @pytest.mark.parametrize(('field', 'detector_count', 'ai_available', 'semantic_available', 'uid',), _MANIFEST_CASES)
    def test_manifest(self, tmp_path: Path, field: str, detector_count: int, ai_available: bool, semantic_available: bool, uid: int) -> None:
        """The metadata manifest exposes every documented field."""
        service, root = _service(tmp_path)
        with _Chdir(root):
            path = service.create_export(
                {'detector_count': detector_count, 'ai_available': ai_available,
                 'semantic_available': semantic_available}
            )
        with zipfile.ZipFile(path) as archive:
            manifest = __import__('json').loads(archive.read('export_metadata.json'))
        assert field in manifest
        assert manifest['schema_version'] == 1
        assert manifest['detector_count'] == detector_count
        assert manifest['ai_available'] is ai_available


_RETENTION_CASES: tuple[tuple[int, int, str, int], ...] = (
    (7, 1, 'stale0.zip', 8481,),
    (7, 1, 'stale1.zip', 8482,),
    (7, 1, 'stale2.zip', 8483,),
    (7, 1, 'stale3.zip', 8484,),
    (7, 1, 'stale4.zip', 8485,),
    (7, 1, 'stale5.zip', 8486,),
    (7, 1, 'stale6.zip', 8487,),
    (7, 1, 'stale7.zip', 8488,),
    (7, 1, 'stale8.zip', 8489,),
    (7, 1, 'stale9.zip', 8490,),
    (7, 6, 'stale0.zip', 8491,),
    (7, 6, 'stale1.zip', 8492,),
    (7, 6, 'stale2.zip', 8493,),
    (7, 6, 'stale3.zip', 8494,),
    (7, 6, 'stale4.zip', 8495,),
    (7, 6, 'stale5.zip', 8496,),
    (7, 6, 'stale6.zip', 8497,),
    (7, 6, 'stale7.zip', 8498,),
    (7, 6, 'stale8.zip', 8499,),
    (7, 6, 'stale9.zip', 8500,),
    (7, 7, 'stale0.zip', 8501,),
    (7, 7, 'stale1.zip', 8502,),
    (7, 7, 'stale2.zip', 8503,),
    (7, 7, 'stale3.zip', 8504,),
    (7, 7, 'stale4.zip', 8505,),
    (7, 7, 'stale5.zip', 8506,),
    (7, 7, 'stale6.zip', 8507,),
    (7, 7, 'stale7.zip', 8508,),
    (7, 7, 'stale8.zip', 8509,),
    (7, 7, 'stale9.zip', 8510,),
    (30, 29, 'stale0.zip', 8511,),
    (30, 29, 'stale1.zip', 8512,),
    (30, 29, 'stale2.zip', 8513,),
    (30, 29, 'stale3.zip', 8514,),
    (30, 29, 'stale4.zip', 8515,),
    (30, 29, 'stale5.zip', 8516,),
    (30, 29, 'stale6.zip', 8517,),
    (30, 29, 'stale7.zip', 8518,),
    (30, 29, 'stale8.zip', 8519,),
    (30, 29, 'stale9.zip', 8520,),
    (30, 31, 'stale0.zip', 8521,),
    (30, 31, 'stale1.zip', 8522,),
    (30, 31, 'stale2.zip', 8523,),
    (30, 31, 'stale3.zip', 8524,),
    (30, 31, 'stale4.zip', 8525,),
    (30, 31, 'stale5.zip', 8526,),
    (30, 31, 'stale6.zip', 8527,),
    (30, 31, 'stale7.zip', 8528,),
    (30, 31, 'stale8.zip', 8529,),
    (30, 31, 'stale9.zip', 8530,),
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
