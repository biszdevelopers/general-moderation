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
    ('APP_SECRET', 'secret_value_xyz_0', 8327,),
    ('APP_SECRET', 'secret_value_xyz_1', 8328,),
    ('APP_SECRET', 'secret_value_xyz_2', 8329,),
    ('APP_SECRET', 'secret_value_xyz_3', 8330,),
    ('APP_SECRET', 'secret_value_xyz_4', 8331,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_0', 8332,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_1', 8333,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_2', 8334,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_3', 8335,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_4', 8336,),
    ('SESSION_TOKEN', 'secret_value_xyz_0', 8337,),
    ('SESSION_TOKEN', 'secret_value_xyz_1', 8338,),
    ('SESSION_TOKEN', 'secret_value_xyz_2', 8339,),
    ('SESSION_TOKEN', 'secret_value_xyz_3', 8340,),
    ('SESSION_TOKEN', 'secret_value_xyz_4', 8341,),
    ('WALLET_KEY', 'secret_value_xyz_0', 8342,),
    ('WALLET_KEY', 'secret_value_xyz_1', 8343,),
    ('WALLET_KEY', 'secret_value_xyz_2', 8344,),
    ('WALLET_KEY', 'secret_value_xyz_3', 8345,),
    ('WALLET_KEY', 'secret_value_xyz_4', 8346,),
    ('PASS_KEY', 'secret_value_xyz_0', 8347,),
    ('PASS_KEY', 'secret_value_xyz_1', 8348,),
    ('PASS_KEY', 'secret_value_xyz_2', 8349,),
    ('PASS_KEY', 'secret_value_xyz_3', 8350,),
    ('PASS_KEY', 'secret_value_xyz_4', 8351,),
    ('SECRET_SALT', 'secret_value_xyz_0', 8352,),
    ('SECRET_SALT', 'secret_value_xyz_1', 8353,),
    ('SECRET_SALT', 'secret_value_xyz_2', 8354,),
    ('SECRET_SALT', 'secret_value_xyz_3', 8355,),
    ('SECRET_SALT', 'secret_value_xyz_4', 8356,),
    ('TOKEN_SECRET', 'secret_value_xyz_0', 8357,),
    ('TOKEN_SECRET', 'secret_value_xyz_1', 8358,),
    ('TOKEN_SECRET', 'secret_value_xyz_2', 8359,),
    ('TOKEN_SECRET', 'secret_value_xyz_3', 8360,),
    ('TOKEN_SECRET', 'secret_value_xyz_4', 8361,),
    ('PASSWORD_1', 'secret_value_xyz_0', 8362,),
    ('PASSWORD_1', 'secret_value_xyz_1', 8363,),
    ('PASSWORD_1', 'secret_value_xyz_2', 8364,),
    ('PASSWORD_1', 'secret_value_xyz_3', 8365,),
    ('PASSWORD_1', 'secret_value_xyz_4', 8366,),
    ('KEY_PAIR', 'secret_value_xyz_0', 8367,),
    ('KEY_PAIR', 'secret_value_xyz_1', 8368,),
    ('KEY_PAIR', 'secret_value_xyz_2', 8369,),
    ('KEY_PAIR', 'secret_value_xyz_3', 8370,),
    ('KEY_PAIR', 'secret_value_xyz_4', 8371,),
    ('MASTER_KEY', 'secret_value_xyz_0', 8372,),
    ('MASTER_KEY', 'secret_value_xyz_1', 8373,),
    ('MASTER_KEY', 'secret_value_xyz_2', 8374,),
    ('MASTER_KEY', 'secret_value_xyz_3', 8375,),
    ('MASTER_KEY', 'secret_value_xyz_4', 8376,),
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
    ('project', 0, True, True, 8377,),
    ('project', 1, False, False, 8378,),
    ('project', 2, True, False, 8379,),
    ('project', 3, False, True, 8380,),
    ('project', 4, True, False, 8381,),
    ('project', 5, False, False, 8382,),
    ('project', 6, True, True, 8383,),
    ('project', 7, False, False, 8384,),
    ('project', 8, True, False, 8385,),
    ('project', 9, False, True, 8386,),
    ('project', 10, True, False, 8387,),
    ('project', 11, False, False, 8388,),
    ('project', 12, True, True, 8389,),
    ('exported_at', 0, True, True, 8390,),
    ('exported_at', 1, False, False, 8391,),
    ('exported_at', 2, True, False, 8392,),
    ('exported_at', 3, False, True, 8393,),
    ('exported_at', 4, True, False, 8394,),
    ('exported_at', 5, False, False, 8395,),
    ('exported_at', 6, True, True, 8396,),
    ('exported_at', 7, False, False, 8397,),
    ('exported_at', 8, True, False, 8398,),
    ('exported_at', 9, False, True, 8399,),
    ('exported_at', 10, True, False, 8400,),
    ('exported_at', 11, False, False, 8401,),
    ('exported_at', 12, True, True, 8402,),
    ('databases', 0, True, True, 8403,),
    ('databases', 1, False, False, 8404,),
    ('databases', 2, True, False, 8405,),
    ('databases', 3, False, True, 8406,),
    ('databases', 4, True, False, 8407,),
    ('databases', 5, False, False, 8408,),
    ('databases', 6, True, True, 8409,),
    ('databases', 7, False, False, 8410,),
    ('databases', 8, True, False, 8411,),
    ('databases', 9, False, True, 8412,),
    ('databases', 10, True, False, 8413,),
    ('databases', 11, False, False, 8414,),
    ('databases', 12, True, True, 8415,),
    ('notes', 0, True, True, 8416,),
    ('notes', 1, False, False, 8417,),
    ('notes', 2, True, False, 8418,),
    ('notes', 3, False, True, 8419,),
    ('notes', 4, True, False, 8420,),
    ('notes', 5, False, False, 8421,),
    ('notes', 6, True, True, 8422,),
    ('notes', 7, False, False, 8423,),
    ('notes', 8, True, False, 8424,),
    ('notes', 9, False, True, 8425,),
    ('notes', 10, True, False, 8426,),
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
