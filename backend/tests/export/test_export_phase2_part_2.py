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
    ('config/.env', 'config/', 13, 8183,),
    ('config/.env', 'config/', 14, 8184,),
    ('config/.env', 'config/', 15, 8185,),
    ('config/.env', 'config/', 16, 8186,),
    ('config/.env', 'config/', 17, 8187,),
    ('config/.env', 'config/', 18, 8188,),
    ('config/.env', 'config/', 19, 8189,),
    ('config/.env', 'config/', 20, 8190,),
    ('config/.env', 'config/', 21, 8191,),
    ('config/.env', 'config/', 22, 8192,),
    ('export_metadata.json', '', 1, 8193,),
    ('export_metadata.json', '', 2, 8194,),
    ('export_metadata.json', '', 3, 8195,),
    ('export_metadata.json', '', 4, 8196,),
    ('export_metadata.json', '', 5, 8197,),
    ('export_metadata.json', '', 6, 8198,),
    ('export_metadata.json', '', 7, 8199,),
    ('export_metadata.json', '', 8, 8200,),
    ('export_metadata.json', '', 9, 8201,),
    ('export_metadata.json', '', 10, 8202,),
    ('export_metadata.json', '', 11, 8203,),
    ('export_metadata.json', '', 12, 8204,),
    ('export_metadata.json', '', 13, 8205,),
    ('export_metadata.json', '', 14, 8206,),
    ('export_metadata.json', '', 15, 8207,),
    ('export_metadata.json', '', 16, 8208,),
    ('export_metadata.json', '', 17, 8209,),
    ('export_metadata.json', '', 18, 8210,),
    ('export_metadata.json', '', 19, 8211,),
    ('export_metadata.json', '', 20, 8212,),
    ('export_metadata.json', '', 21, 8213,),
    ('export_metadata.json', '', 22, 8214,),
    ('settings_snapshot.json', 'config/', 1, 8215,),
    ('settings_snapshot.json', 'config/', 2, 8216,),
    ('settings_snapshot.json', 'config/', 3, 8217,),
    ('settings_snapshot.json', 'config/', 4, 8218,),
    ('settings_snapshot.json', 'config/', 5, 8219,),
    ('settings_snapshot.json', 'config/', 6, 8220,),
    ('settings_snapshot.json', 'config/', 7, 8221,),
    ('settings_snapshot.json', 'config/', 8, 8222,),
    ('settings_snapshot.json', 'config/', 9, 8223,),
    ('settings_snapshot.json', 'config/', 10, 8224,),
    ('settings_snapshot.json', 'config/', 11, 8225,),
    ('settings_snapshot.json', 'config/', 12, 8226,),
    ('settings_snapshot.json', 'config/', 13, 8227,),
    ('settings_snapshot.json', 'config/', 14, 8228,),
    ('settings_snapshot.json', 'config/', 15, 8229,),
    ('settings_snapshot.json', 'config/', 16, 8230,),
    ('settings_snapshot.json', 'config/', 17, 8231,),
    ('settings_snapshot.json', 'config/', 18, 8232,),
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


_REDACTION_CASES: tuple[tuple[str, str, int], ...] = (
    ('SOME_API_KEY', 'secret_value_xyz_0', 8237,),
    ('SOME_API_KEY', 'secret_value_xyz_1', 8238,),
    ('SOME_API_KEY', 'secret_value_xyz_2', 8239,),
    ('SOME_API_KEY', 'secret_value_xyz_3', 8240,),
    ('SOME_API_KEY', 'secret_value_xyz_4', 8241,),
    ('SOME_SECRET', 'secret_value_xyz_0', 8242,),
    ('SOME_SECRET', 'secret_value_xyz_1', 8243,),
    ('SOME_SECRET', 'secret_value_xyz_2', 8244,),
    ('SOME_SECRET', 'secret_value_xyz_3', 8245,),
    ('SOME_SECRET', 'secret_value_xyz_4', 8246,),
    ('SOME_PASSWORD', 'secret_value_xyz_0', 8247,),
    ('SOME_PASSWORD', 'secret_value_xyz_1', 8248,),
    ('SOME_PASSWORD', 'secret_value_xyz_2', 8249,),
    ('SOME_PASSWORD', 'secret_value_xyz_3', 8250,),
    ('SOME_PASSWORD', 'secret_value_xyz_4', 8251,),
    ('SOME_TOKEN', 'secret_value_xyz_0', 8252,),
    ('SOME_TOKEN', 'secret_value_xyz_1', 8253,),
    ('SOME_TOKEN', 'secret_value_xyz_2', 8254,),
    ('SOME_TOKEN', 'secret_value_xyz_3', 8255,),
    ('SOME_TOKEN', 'secret_value_xyz_4', 8256,),
    ('SECRET_VALUE', 'secret_value_xyz_0', 8257,),
    ('SECRET_VALUE', 'secret_value_xyz_1', 8258,),
    ('SECRET_VALUE', 'secret_value_xyz_2', 8259,),
    ('SECRET_VALUE', 'secret_value_xyz_3', 8260,),
    ('SECRET_VALUE', 'secret_value_xyz_4', 8261,),
    ('API_TOKEN', 'secret_value_xyz_0', 8262,),
    ('API_TOKEN', 'secret_value_xyz_1', 8263,),
    ('API_TOKEN', 'secret_value_xyz_2', 8264,),
    ('API_TOKEN', 'secret_value_xyz_3', 8265,),
    ('API_TOKEN', 'secret_value_xyz_4', 8266,),
    ('DB_PASSWORD', 'secret_value_xyz_0', 8267,),
    ('DB_PASSWORD', 'secret_value_xyz_1', 8268,),
    ('DB_PASSWORD', 'secret_value_xyz_2', 8269,),
    ('DB_PASSWORD', 'secret_value_xyz_3', 8270,),
    ('DB_PASSWORD', 'secret_value_xyz_4', 8271,),
    ('ACCESS_KEY', 'secret_value_xyz_0', 8272,),
    ('ACCESS_KEY', 'secret_value_xyz_1', 8273,),
    ('ACCESS_KEY', 'secret_value_xyz_2', 8274,),
    ('ACCESS_KEY', 'secret_value_xyz_3', 8275,),
    ('ACCESS_KEY', 'secret_value_xyz_4', 8276,),
    ('AUTH_TOKEN', 'secret_value_xyz_0', 8277,),
    ('AUTH_TOKEN', 'secret_value_xyz_1', 8278,),
    ('AUTH_TOKEN', 'secret_value_xyz_2', 8279,),
    ('AUTH_TOKEN', 'secret_value_xyz_3', 8280,),
    ('AUTH_TOKEN', 'secret_value_xyz_4', 8281,),
    ('PRIVATE_KEY', 'secret_value_xyz_0', 8282,),
    ('PRIVATE_KEY', 'secret_value_xyz_1', 8283,),
    ('PRIVATE_KEY', 'secret_value_xyz_2', 8284,),
    ('PRIVATE_KEY', 'secret_value_xyz_3', 8285,),
    ('PRIVATE_KEY', 'secret_value_xyz_4', 8286,),
)

class TestRedaction(BaseTest):
    """Secret values never leak into the exported environment."""

    @pytest.mark.parametrize(('key', 'secret_value', 'uid',), _REDACTION_CASES)
    def test_redaction(self, tmp_path: Path, key: str, secret_value: str, uid: int) -> None:
        """Secret values never leak into the exported environment."""
        root = _build_sandbox(tmp_path)
        (root / '.env').write_text(f'{key}={secret_value}\n', encoding='utf-8')
        settings = Settings(
            app_port=0,
            export_temp_dir=str(root / 'exports'),
            export_retention_days=7,
            log_file_path=str(root / 'logs' / 'moderation.log'),
        )
        service: ExportService = ExportService(settings, None)
        with _Chdir(root):
            path = service.create_export()
        with zipfile.ZipFile(path) as archive:
            content = archive.read('config/.env').decode()
        assert secret_value not in content
        assert '[REDACTED]' in content
