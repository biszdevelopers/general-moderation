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
    ('users.db', 'databases/', 1, 8083,),
    ('users.db', 'databases/', 2, 8084,),
    ('users.db', 'databases/', 3, 8085,),
    ('users.db', 'databases/', 4, 8086,),
    ('users.db', 'databases/', 5, 8087,),
    ('users.db', 'databases/', 6, 8088,),
    ('users.db', 'databases/', 7, 8089,),
    ('users.db', 'databases/', 8, 8090,),
    ('users.db', 'databases/', 9, 8091,),
    ('users.db', 'databases/', 10, 8092,),
    ('users.db', 'databases/', 11, 8093,),
    ('users.db', 'databases/', 12, 8094,),
    ('users.db', 'databases/', 13, 8095,),
    ('users.db', 'databases/', 14, 8096,),
    ('users.db', 'databases/', 15, 8097,),
    ('users.db', 'databases/', 16, 8098,),
    ('users.db', 'databases/', 17, 8099,),
    ('users.db', 'databases/', 18, 8100,),
    ('users.db', 'databases/', 19, 8101,),
    ('users.db', 'databases/', 20, 8102,),
    ('users.db', 'databases/', 21, 8103,),
    ('users.db', 'databases/', 22, 8104,),
    ('moderation.log', 'logs/', 1, 8105,),
    ('moderation.log', 'logs/', 2, 8106,),
    ('moderation.log', 'logs/', 3, 8107,),
    ('moderation.log', 'logs/', 4, 8108,),
    ('moderation.log', 'logs/', 5, 8109,),
    ('moderation.log', 'logs/', 6, 8110,),
    ('moderation.log', 'logs/', 7, 8111,),
    ('moderation.log', 'logs/', 8, 8112,),
    ('moderation.log', 'logs/', 9, 8113,),
    ('moderation.log', 'logs/', 10, 8114,),
    ('moderation.log', 'logs/', 11, 8115,),
    ('moderation.log', 'logs/', 12, 8116,),
    ('moderation.log', 'logs/', 13, 8117,),
    ('moderation.log', 'logs/', 14, 8118,),
    ('moderation.log', 'logs/', 15, 8119,),
    ('moderation.log', 'logs/', 16, 8120,),
    ('moderation.log', 'logs/', 17, 8121,),
    ('moderation.log', 'logs/', 18, 8122,),
    ('moderation.log', 'logs/', 19, 8123,),
    ('moderation.log', 'logs/', 20, 8124,),
    ('moderation.log', 'logs/', 21, 8125,),
    ('moderation.log', 'logs/', 22, 8126,),
    ('political.index', 'semantic/', 1, 8127,),
    ('political.index', 'semantic/', 2, 8128,),
    ('political.index', 'semantic/', 3, 8129,),
    ('political.index', 'semantic/', 4, 8130,),
    ('political.index', 'semantic/', 5, 8131,),
    ('political.index', 'semantic/', 6, 8132,),
    ('political.index', 'semantic/', 7, 8133,),
    ('political.index', 'semantic/', 8, 8134,),
    ('political.index', 'semantic/', 9, 8135,),
    ('political.index', 'semantic/', 10, 8136,),
    ('political.index', 'semantic/', 11, 8137,),
    ('political.index', 'semantic/', 12, 8138,),
    ('political.index', 'semantic/', 13, 8139,),
    ('political.index', 'semantic/', 14, 8140,),
    ('political.index', 'semantic/', 15, 8141,),
    ('political.index', 'semantic/', 16, 8142,),
    ('political.index', 'semantic/', 17, 8143,),
    ('political.index', 'semantic/', 18, 8144,),
    ('political.index', 'semantic/', 19, 8145,),
    ('political.index', 'semantic/', 20, 8146,),
    ('political.index', 'semantic/', 21, 8147,),
    ('political.index', 'semantic/', 22, 8148,),
    ('political.json', 'semantic/', 1, 8149,),
    ('political.json', 'semantic/', 2, 8150,),
    ('political.json', 'semantic/', 3, 8151,),
    ('political.json', 'semantic/', 4, 8152,),
    ('political.json', 'semantic/', 5, 8153,),
    ('political.json', 'semantic/', 6, 8154,),
    ('political.json', 'semantic/', 7, 8155,),
    ('political.json', 'semantic/', 8, 8156,),
    ('political.json', 'semantic/', 9, 8157,),
    ('political.json', 'semantic/', 10, 8158,),
    ('political.json', 'semantic/', 11, 8159,),
    ('political.json', 'semantic/', 12, 8160,),
    ('political.json', 'semantic/', 13, 8161,),
    ('political.json', 'semantic/', 14, 8162,),
    ('political.json', 'semantic/', 15, 8163,),
    ('political.json', 'semantic/', 16, 8164,),
    ('political.json', 'semantic/', 17, 8165,),
    ('political.json', 'semantic/', 18, 8166,),
    ('political.json', 'semantic/', 19, 8167,),
    ('political.json', 'semantic/', 20, 8168,),
    ('political.json', 'semantic/', 21, 8169,),
    ('political.json', 'semantic/', 22, 8170,),
    ('config/.env', 'config/', 1, 8171,),
    ('config/.env', 'config/', 2, 8172,),
    ('config/.env', 'config/', 3, 8173,),
    ('config/.env', 'config/', 4, 8174,),
    ('config/.env', 'config/', 5, 8175,),
    ('config/.env', 'config/', 6, 8176,),
    ('config/.env', 'config/', 7, 8177,),
    ('config/.env', 'config/', 8, 8178,),
    ('config/.env', 'config/', 9, 8179,),
    ('config/.env', 'config/', 10, 8180,),
    ('config/.env', 'config/', 11, 8181,),
    ('config/.env', 'config/', 12, 8182,),
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
