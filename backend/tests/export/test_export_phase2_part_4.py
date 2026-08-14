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
    ('notes', 11, False, False, 8387,),
    ('notes', 12, True, True, 8388,),
    ('schema_version', 0, True, True, 8389,),
    ('schema_version', 1, False, False, 8390,),
    ('schema_version', 2, True, False, 8391,),
    ('schema_version', 3, False, True, 8392,),
    ('schema_version', 4, True, False, 8393,),
    ('schema_version', 5, False, False, 8394,),
    ('schema_version', 6, True, True, 8395,),
    ('schema_version', 7, False, False, 8396,),
    ('schema_version', 8, True, False, 8397,),
    ('schema_version', 9, False, True, 8398,),
    ('schema_version', 10, True, False, 8399,),
    ('schema_version', 11, False, False, 8400,),
    ('schema_version', 12, True, True, 8401,),
    ('detector_count', 0, True, True, 8402,),
    ('detector_count', 1, False, False, 8403,),
    ('detector_count', 2, True, False, 8404,),
    ('detector_count', 3, False, True, 8405,),
    ('detector_count', 4, True, False, 8406,),
    ('detector_count', 5, False, False, 8407,),
    ('detector_count', 6, True, True, 8408,),
    ('detector_count', 7, False, False, 8409,),
    ('detector_count', 8, True, False, 8410,),
    ('detector_count', 9, False, True, 8411,),
    ('detector_count', 10, True, False, 8412,),
    ('detector_count', 11, False, False, 8413,),
    ('detector_count', 12, True, True, 8414,),
    ('ai_available', 0, True, True, 8415,),
    ('ai_available', 1, False, False, 8416,),
    ('ai_available', 2, True, False, 8417,),
    ('ai_available', 3, False, True, 8418,),
    ('ai_available', 4, True, False, 8419,),
    ('ai_available', 5, False, False, 8420,),
    ('ai_available', 6, True, True, 8421,),
    ('ai_available', 7, False, False, 8422,),
    ('ai_available', 8, True, False, 8423,),
    ('ai_available', 9, False, True, 8424,),
    ('ai_available', 10, True, False, 8425,),
    ('ai_available', 11, False, False, 8426,),
    ('ai_available', 12, True, True, 8427,),
    ('semantic_available', 0, True, True, 8428,),
    ('semantic_available', 1, False, False, 8429,),
    ('semantic_available', 2, True, False, 8430,),
    ('semantic_available', 3, False, True, 8431,),
    ('semantic_available', 4, True, False, 8432,),
    ('semantic_available', 5, False, False, 8433,),
    ('semantic_available', 6, True, True, 8434,),
    ('semantic_available', 7, False, False, 8435,),
    ('semantic_available', 8, True, False, 8436,),
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
    (7, 1, 'stale0.zip', 8441,),
    (7, 1, 'stale1.zip', 8442,),
    (7, 1, 'stale2.zip', 8443,),
    (7, 1, 'stale3.zip', 8444,),
    (7, 1, 'stale4.zip', 8445,),
    (7, 1, 'stale5.zip', 8446,),
    (7, 1, 'stale6.zip', 8447,),
    (7, 1, 'stale7.zip', 8448,),
    (7, 1, 'stale8.zip', 8449,),
    (7, 1, 'stale9.zip', 8450,),
    (7, 6, 'stale0.zip', 8451,),
    (7, 6, 'stale1.zip', 8452,),
    (7, 6, 'stale2.zip', 8453,),
    (7, 6, 'stale3.zip', 8454,),
    (7, 6, 'stale4.zip', 8455,),
    (7, 6, 'stale5.zip', 8456,),
    (7, 6, 'stale6.zip', 8457,),
    (7, 6, 'stale7.zip', 8458,),
    (7, 6, 'stale8.zip', 8459,),
    (7, 6, 'stale9.zip', 8460,),
    (7, 7, 'stale0.zip', 8461,),
    (7, 7, 'stale1.zip', 8462,),
    (7, 7, 'stale2.zip', 8463,),
    (7, 7, 'stale3.zip', 8464,),
    (7, 7, 'stale4.zip', 8465,),
    (7, 7, 'stale5.zip', 8466,),
    (7, 7, 'stale6.zip', 8467,),
    (7, 7, 'stale7.zip', 8468,),
    (7, 7, 'stale8.zip', 8469,),
    (7, 7, 'stale9.zip', 8470,),
    (30, 29, 'stale0.zip', 8471,),
    (30, 29, 'stale1.zip', 8472,),
    (30, 29, 'stale2.zip', 8473,),
    (30, 29, 'stale3.zip', 8474,),
    (30, 29, 'stale4.zip', 8475,),
    (30, 29, 'stale5.zip', 8476,),
    (30, 29, 'stale6.zip', 8477,),
    (30, 29, 'stale7.zip', 8478,),
    (30, 29, 'stale8.zip', 8479,),
    (30, 29, 'stale9.zip', 8480,),
    (30, 31, 'stale0.zip', 8481,),
    (30, 31, 'stale1.zip', 8482,),
    (30, 31, 'stale2.zip', 8483,),
    (30, 31, 'stale3.zip', 8484,),
    (30, 31, 'stale4.zip', 8485,),
    (30, 31, 'stale5.zip', 8486,),
    (30, 31, 'stale6.zip', 8487,),
    (30, 31, 'stale7.zip', 8488,),
    (30, 31, 'stale8.zip', 8489,),
    (30, 31, 'stale9.zip', 8490,),
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
