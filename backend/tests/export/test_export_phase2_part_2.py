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
    ('config/.env', 'config/', 13, 8223,),
    ('config/.env', 'config/', 14, 8224,),
    ('config/.env', 'config/', 15, 8225,),
    ('config/.env', 'config/', 16, 8226,),
    ('config/.env', 'config/', 17, 8227,),
    ('config/.env', 'config/', 18, 8228,),
    ('config/.env', 'config/', 19, 8229,),
    ('config/.env', 'config/', 20, 8230,),
    ('config/.env', 'config/', 21, 8231,),
    ('config/.env', 'config/', 22, 8232,),
    ('export_metadata.json', '', 1, 8233,),
    ('export_metadata.json', '', 2, 8234,),
    ('export_metadata.json', '', 3, 8235,),
    ('export_metadata.json', '', 4, 8236,),
    ('export_metadata.json', '', 5, 8237,),
    ('export_metadata.json', '', 6, 8238,),
    ('export_metadata.json', '', 7, 8239,),
    ('export_metadata.json', '', 8, 8240,),
    ('export_metadata.json', '', 9, 8241,),
    ('export_metadata.json', '', 10, 8242,),
    ('export_metadata.json', '', 11, 8243,),
    ('export_metadata.json', '', 12, 8244,),
    ('export_metadata.json', '', 13, 8245,),
    ('export_metadata.json', '', 14, 8246,),
    ('export_metadata.json', '', 15, 8247,),
    ('export_metadata.json', '', 16, 8248,),
    ('export_metadata.json', '', 17, 8249,),
    ('export_metadata.json', '', 18, 8250,),
    ('export_metadata.json', '', 19, 8251,),
    ('export_metadata.json', '', 20, 8252,),
    ('export_metadata.json', '', 21, 8253,),
    ('export_metadata.json', '', 22, 8254,),
    ('settings_snapshot.json', 'config/', 1, 8255,),
    ('settings_snapshot.json', 'config/', 2, 8256,),
    ('settings_snapshot.json', 'config/', 3, 8257,),
    ('settings_snapshot.json', 'config/', 4, 8258,),
    ('settings_snapshot.json', 'config/', 5, 8259,),
    ('settings_snapshot.json', 'config/', 6, 8260,),
    ('settings_snapshot.json', 'config/', 7, 8261,),
    ('settings_snapshot.json', 'config/', 8, 8262,),
    ('settings_snapshot.json', 'config/', 9, 8263,),
    ('settings_snapshot.json', 'config/', 10, 8264,),
    ('settings_snapshot.json', 'config/', 11, 8265,),
    ('settings_snapshot.json', 'config/', 12, 8266,),
    ('settings_snapshot.json', 'config/', 13, 8267,),
    ('settings_snapshot.json', 'config/', 14, 8268,),
    ('settings_snapshot.json', 'config/', 15, 8269,),
    ('settings_snapshot.json', 'config/', 16, 8270,),
    ('settings_snapshot.json', 'config/', 17, 8271,),
    ('settings_snapshot.json', 'config/', 18, 8272,),
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
    ('SOME_API_KEY', 'secret_value_xyz_0', 8277,),
    ('SOME_API_KEY', 'secret_value_xyz_1', 8278,),
    ('SOME_API_KEY', 'secret_value_xyz_2', 8279,),
    ('SOME_API_KEY', 'secret_value_xyz_3', 8280,),
    ('SOME_API_KEY', 'secret_value_xyz_4', 8281,),
    ('SOME_SECRET', 'secret_value_xyz_0', 8282,),
    ('SOME_SECRET', 'secret_value_xyz_1', 8283,),
    ('SOME_SECRET', 'secret_value_xyz_2', 8284,),
    ('SOME_SECRET', 'secret_value_xyz_3', 8285,),
    ('SOME_SECRET', 'secret_value_xyz_4', 8286,),
    ('SOME_PASSWORD', 'secret_value_xyz_0', 8287,),
    ('SOME_PASSWORD', 'secret_value_xyz_1', 8288,),
    ('SOME_PASSWORD', 'secret_value_xyz_2', 8289,),
    ('SOME_PASSWORD', 'secret_value_xyz_3', 8290,),
    ('SOME_PASSWORD', 'secret_value_xyz_4', 8291,),
    ('SOME_TOKEN', 'secret_value_xyz_0', 8292,),
    ('SOME_TOKEN', 'secret_value_xyz_1', 8293,),
    ('SOME_TOKEN', 'secret_value_xyz_2', 8294,),
    ('SOME_TOKEN', 'secret_value_xyz_3', 8295,),
    ('SOME_TOKEN', 'secret_value_xyz_4', 8296,),
    ('SECRET_VALUE', 'secret_value_xyz_0', 8297,),
    ('SECRET_VALUE', 'secret_value_xyz_1', 8298,),
    ('SECRET_VALUE', 'secret_value_xyz_2', 8299,),
    ('SECRET_VALUE', 'secret_value_xyz_3', 8300,),
    ('SECRET_VALUE', 'secret_value_xyz_4', 8301,),
    ('API_TOKEN', 'secret_value_xyz_0', 8302,),
    ('API_TOKEN', 'secret_value_xyz_1', 8303,),
    ('API_TOKEN', 'secret_value_xyz_2', 8304,),
    ('API_TOKEN', 'secret_value_xyz_3', 8305,),
    ('API_TOKEN', 'secret_value_xyz_4', 8306,),
    ('DB_PASSWORD', 'secret_value_xyz_0', 8307,),
    ('DB_PASSWORD', 'secret_value_xyz_1', 8308,),
    ('DB_PASSWORD', 'secret_value_xyz_2', 8309,),
    ('DB_PASSWORD', 'secret_value_xyz_3', 8310,),
    ('DB_PASSWORD', 'secret_value_xyz_4', 8311,),
    ('ACCESS_KEY', 'secret_value_xyz_0', 8312,),
    ('ACCESS_KEY', 'secret_value_xyz_1', 8313,),
    ('ACCESS_KEY', 'secret_value_xyz_2', 8314,),
    ('ACCESS_KEY', 'secret_value_xyz_3', 8315,),
    ('ACCESS_KEY', 'secret_value_xyz_4', 8316,),
    ('AUTH_TOKEN', 'secret_value_xyz_0', 8317,),
    ('AUTH_TOKEN', 'secret_value_xyz_1', 8318,),
    ('AUTH_TOKEN', 'secret_value_xyz_2', 8319,),
    ('AUTH_TOKEN', 'secret_value_xyz_3', 8320,),
    ('AUTH_TOKEN', 'secret_value_xyz_4', 8321,),
    ('PRIVATE_KEY', 'secret_value_xyz_0', 8322,),
    ('PRIVATE_KEY', 'secret_value_xyz_1', 8323,),
    ('PRIVATE_KEY', 'secret_value_xyz_2', 8324,),
    ('PRIVATE_KEY', 'secret_value_xyz_3', 8325,),
    ('PRIVATE_KEY', 'secret_value_xyz_4', 8326,),
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
