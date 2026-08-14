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

_REDACTION_CASES: tuple[tuple[str, str, int], ...] = (
    ('APP_SECRET', 'secret_value_xyz_0', 8287,),
    ('APP_SECRET', 'secret_value_xyz_1', 8288,),
    ('APP_SECRET', 'secret_value_xyz_2', 8289,),
    ('APP_SECRET', 'secret_value_xyz_3', 8290,),
    ('APP_SECRET', 'secret_value_xyz_4', 8291,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_0', 8292,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_1', 8293,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_2', 8294,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_3', 8295,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_4', 8296,),
    ('SESSION_TOKEN', 'secret_value_xyz_0', 8297,),
    ('SESSION_TOKEN', 'secret_value_xyz_1', 8298,),
    ('SESSION_TOKEN', 'secret_value_xyz_2', 8299,),
    ('SESSION_TOKEN', 'secret_value_xyz_3', 8300,),
    ('SESSION_TOKEN', 'secret_value_xyz_4', 8301,),
    ('WALLET_KEY', 'secret_value_xyz_0', 8302,),
    ('WALLET_KEY', 'secret_value_xyz_1', 8303,),
    ('WALLET_KEY', 'secret_value_xyz_2', 8304,),
    ('WALLET_KEY', 'secret_value_xyz_3', 8305,),
    ('WALLET_KEY', 'secret_value_xyz_4', 8306,),
    ('PASS_KEY', 'secret_value_xyz_0', 8307,),
    ('PASS_KEY', 'secret_value_xyz_1', 8308,),
    ('PASS_KEY', 'secret_value_xyz_2', 8309,),
    ('PASS_KEY', 'secret_value_xyz_3', 8310,),
    ('PASS_KEY', 'secret_value_xyz_4', 8311,),
    ('SECRET_SALT', 'secret_value_xyz_0', 8312,),
    ('SECRET_SALT', 'secret_value_xyz_1', 8313,),
    ('SECRET_SALT', 'secret_value_xyz_2', 8314,),
    ('SECRET_SALT', 'secret_value_xyz_3', 8315,),
    ('SECRET_SALT', 'secret_value_xyz_4', 8316,),
    ('TOKEN_SECRET', 'secret_value_xyz_0', 8317,),
    ('TOKEN_SECRET', 'secret_value_xyz_1', 8318,),
    ('TOKEN_SECRET', 'secret_value_xyz_2', 8319,),
    ('TOKEN_SECRET', 'secret_value_xyz_3', 8320,),
    ('TOKEN_SECRET', 'secret_value_xyz_4', 8321,),
    ('PASSWORD_1', 'secret_value_xyz_0', 8322,),
    ('PASSWORD_1', 'secret_value_xyz_1', 8323,),
    ('PASSWORD_1', 'secret_value_xyz_2', 8324,),
    ('PASSWORD_1', 'secret_value_xyz_3', 8325,),
    ('PASSWORD_1', 'secret_value_xyz_4', 8326,),
    ('KEY_PAIR', 'secret_value_xyz_0', 8327,),
    ('KEY_PAIR', 'secret_value_xyz_1', 8328,),
    ('KEY_PAIR', 'secret_value_xyz_2', 8329,),
    ('KEY_PAIR', 'secret_value_xyz_3', 8330,),
    ('KEY_PAIR', 'secret_value_xyz_4', 8331,),
    ('MASTER_KEY', 'secret_value_xyz_0', 8332,),
    ('MASTER_KEY', 'secret_value_xyz_1', 8333,),
    ('MASTER_KEY', 'secret_value_xyz_2', 8334,),
    ('MASTER_KEY', 'secret_value_xyz_3', 8335,),
    ('MASTER_KEY', 'secret_value_xyz_4', 8336,),
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


_MANIFEST_CASES: tuple[tuple[str, int, bool, bool, int], ...] = (
    ('project', 0, True, True, 8337,),
    ('project', 1, False, False, 8338,),
    ('project', 2, True, False, 8339,),
    ('project', 3, False, True, 8340,),
    ('project', 4, True, False, 8341,),
    ('project', 5, False, False, 8342,),
    ('project', 6, True, True, 8343,),
    ('project', 7, False, False, 8344,),
    ('project', 8, True, False, 8345,),
    ('project', 9, False, True, 8346,),
    ('project', 10, True, False, 8347,),
    ('project', 11, False, False, 8348,),
    ('project', 12, True, True, 8349,),
    ('exported_at', 0, True, True, 8350,),
    ('exported_at', 1, False, False, 8351,),
    ('exported_at', 2, True, False, 8352,),
    ('exported_at', 3, False, True, 8353,),
    ('exported_at', 4, True, False, 8354,),
    ('exported_at', 5, False, False, 8355,),
    ('exported_at', 6, True, True, 8356,),
    ('exported_at', 7, False, False, 8357,),
    ('exported_at', 8, True, False, 8358,),
    ('exported_at', 9, False, True, 8359,),
    ('exported_at', 10, True, False, 8360,),
    ('exported_at', 11, False, False, 8361,),
    ('exported_at', 12, True, True, 8362,),
    ('databases', 0, True, True, 8363,),
    ('databases', 1, False, False, 8364,),
    ('databases', 2, True, False, 8365,),
    ('databases', 3, False, True, 8366,),
    ('databases', 4, True, False, 8367,),
    ('databases', 5, False, False, 8368,),
    ('databases', 6, True, True, 8369,),
    ('databases', 7, False, False, 8370,),
    ('databases', 8, True, False, 8371,),
    ('databases', 9, False, True, 8372,),
    ('databases', 10, True, False, 8373,),
    ('databases', 11, False, False, 8374,),
    ('databases', 12, True, True, 8375,),
    ('notes', 0, True, True, 8376,),
    ('notes', 1, False, False, 8377,),
    ('notes', 2, True, False, 8378,),
    ('notes', 3, False, True, 8379,),
    ('notes', 4, True, False, 8380,),
    ('notes', 5, False, False, 8381,),
    ('notes', 6, True, True, 8382,),
    ('notes', 7, False, False, 8383,),
    ('notes', 8, True, False, 8384,),
    ('notes', 9, False, True, 8385,),
    ('notes', 10, True, False, 8386,),
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
