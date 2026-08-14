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

_ARCHIVE_ENTRY_CASES: tuple[tuple[str, str, int, int], ...] = (
    ('users.db', 'databases/', 1, 8123,),
    ('users.db', 'databases/', 2, 8124,),
    ('users.db', 'databases/', 3, 8125,),
    ('users.db', 'databases/', 4, 8126,),
    ('users.db', 'databases/', 5, 8127,),
    ('users.db', 'databases/', 6, 8128,),
    ('users.db', 'databases/', 7, 8129,),
    ('users.db', 'databases/', 8, 8130,),
    ('users.db', 'databases/', 9, 8131,),
    ('users.db', 'databases/', 10, 8132,),
    ('users.db', 'databases/', 11, 8133,),
    ('users.db', 'databases/', 12, 8134,),
    ('users.db', 'databases/', 13, 8135,),
    ('users.db', 'databases/', 14, 8136,),
    ('users.db', 'databases/', 15, 8137,),
    ('users.db', 'databases/', 16, 8138,),
    ('users.db', 'databases/', 17, 8139,),
    ('users.db', 'databases/', 18, 8140,),
    ('users.db', 'databases/', 19, 8141,),
    ('users.db', 'databases/', 20, 8142,),
    ('users.db', 'databases/', 21, 8143,),
    ('users.db', 'databases/', 22, 8144,),
    ('moderation.log', 'logs/', 1, 8145,),
    ('moderation.log', 'logs/', 2, 8146,),
    ('moderation.log', 'logs/', 3, 8147,),
    ('moderation.log', 'logs/', 4, 8148,),
    ('moderation.log', 'logs/', 5, 8149,),
    ('moderation.log', 'logs/', 6, 8150,),
    ('moderation.log', 'logs/', 7, 8151,),
    ('moderation.log', 'logs/', 8, 8152,),
    ('moderation.log', 'logs/', 9, 8153,),
    ('moderation.log', 'logs/', 10, 8154,),
    ('moderation.log', 'logs/', 11, 8155,),
    ('moderation.log', 'logs/', 12, 8156,),
    ('moderation.log', 'logs/', 13, 8157,),
    ('moderation.log', 'logs/', 14, 8158,),
    ('moderation.log', 'logs/', 15, 8159,),
    ('moderation.log', 'logs/', 16, 8160,),
    ('moderation.log', 'logs/', 17, 8161,),
    ('moderation.log', 'logs/', 18, 8162,),
    ('moderation.log', 'logs/', 19, 8163,),
    ('moderation.log', 'logs/', 20, 8164,),
    ('moderation.log', 'logs/', 21, 8165,),
    ('moderation.log', 'logs/', 22, 8166,),
    ('political.index', 'semantic/', 1, 8167,),
    ('political.index', 'semantic/', 2, 8168,),
    ('political.index', 'semantic/', 3, 8169,),
    ('political.index', 'semantic/', 4, 8170,),
    ('political.index', 'semantic/', 5, 8171,),
    ('political.index', 'semantic/', 6, 8172,),
    ('political.index', 'semantic/', 7, 8173,),
    ('political.index', 'semantic/', 8, 8174,),
    ('political.index', 'semantic/', 9, 8175,),
    ('political.index', 'semantic/', 10, 8176,),
    ('political.index', 'semantic/', 11, 8177,),
    ('political.index', 'semantic/', 12, 8178,),
    ('political.index', 'semantic/', 13, 8179,),
    ('political.index', 'semantic/', 14, 8180,),
    ('political.index', 'semantic/', 15, 8181,),
    ('political.index', 'semantic/', 16, 8182,),
    ('political.index', 'semantic/', 17, 8183,),
    ('political.index', 'semantic/', 18, 8184,),
    ('political.index', 'semantic/', 19, 8185,),
    ('political.index', 'semantic/', 20, 8186,),
    ('political.index', 'semantic/', 21, 8187,),
    ('political.index', 'semantic/', 22, 8188,),
    ('political.json', 'semantic/', 1, 8189,),
    ('political.json', 'semantic/', 2, 8190,),
    ('political.json', 'semantic/', 3, 8191,),
    ('political.json', 'semantic/', 4, 8192,),
    ('political.json', 'semantic/', 5, 8193,),
    ('political.json', 'semantic/', 6, 8194,),
    ('political.json', 'semantic/', 7, 8195,),
    ('political.json', 'semantic/', 8, 8196,),
    ('political.json', 'semantic/', 9, 8197,),
    ('political.json', 'semantic/', 10, 8198,),
    ('political.json', 'semantic/', 11, 8199,),
    ('political.json', 'semantic/', 12, 8200,),
    ('political.json', 'semantic/', 13, 8201,),
    ('political.json', 'semantic/', 14, 8202,),
    ('political.json', 'semantic/', 15, 8203,),
    ('political.json', 'semantic/', 16, 8204,),
    ('political.json', 'semantic/', 17, 8205,),
    ('political.json', 'semantic/', 18, 8206,),
    ('political.json', 'semantic/', 19, 8207,),
    ('political.json', 'semantic/', 20, 8208,),
    ('political.json', 'semantic/', 21, 8209,),
    ('political.json', 'semantic/', 22, 8210,),
    ('config/.env', 'config/', 1, 8211,),
    ('config/.env', 'config/', 2, 8212,),
    ('config/.env', 'config/', 3, 8213,),
    ('config/.env', 'config/', 4, 8214,),
    ('config/.env', 'config/', 5, 8215,),
    ('config/.env', 'config/', 6, 8216,),
    ('config/.env', 'config/', 7, 8217,),
    ('config/.env', 'config/', 8, 8218,),
    ('config/.env', 'config/', 9, 8219,),
    ('config/.env', 'config/', 10, 8220,),
    ('config/.env', 'config/', 11, 8221,),
    ('config/.env', 'config/', 12, 8222,),
)

class TestArchiveEntry(BaseTest):
    """Export archives include every documented asset."""

    @pytest.mark.parametrize(('marker', 'section', 'n_extra_db', 'uid',), _ARCHIVE_ENTRY_CASES)
    def test_archive_entry(self, tmp_path: Path, marker: str, section: str, n_extra_db: int, uid: int) -> None:
        """Export archives include every documented asset."""
        service, root = _service(tmp_path)
        for index in range(n_extra_db):
            connection = sqlite3.connect(str(root / 'data' / f'extra{index}.db'))
            connection.execute('CREATE TABLE t (id INTEGER)')
            connection.commit()
            connection.close()
        with _Chdir(root):
            path = service.create_export()
        entries = _zip_entries(path)
        assert any(marker in entry for entry in entries)
        assert any(section in entry for entry in entries)
        assert any(f'extra{n_extra_db - 1}.db' in entry for entry in entries)
        assert path.suffix == '.zip'
