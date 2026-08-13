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
    ('APP_SECRET', 'secret_value_xyz_0', 8128,),
    ('APP_SECRET', 'secret_value_xyz_1', 8129,),
    ('APP_SECRET', 'secret_value_xyz_2', 8130,),
    ('APP_SECRET', 'secret_value_xyz_3', 8131,),
    ('APP_SECRET', 'secret_value_xyz_4', 8132,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_0', 8133,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_1', 8134,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_2', 8135,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_3', 8136,),
    ('LOGIN_PASSWORD', 'secret_value_xyz_4', 8137,),
    ('SESSION_TOKEN', 'secret_value_xyz_0', 8138,),
    ('SESSION_TOKEN', 'secret_value_xyz_1', 8139,),
    ('SESSION_TOKEN', 'secret_value_xyz_2', 8140,),
    ('SESSION_TOKEN', 'secret_value_xyz_3', 8141,),
    ('SESSION_TOKEN', 'secret_value_xyz_4', 8142,),
    ('WALLET_KEY', 'secret_value_xyz_0', 8143,),
    ('WALLET_KEY', 'secret_value_xyz_1', 8144,),
    ('WALLET_KEY', 'secret_value_xyz_2', 8145,),
    ('WALLET_KEY', 'secret_value_xyz_3', 8146,),
    ('WALLET_KEY', 'secret_value_xyz_4', 8147,),
    ('PASS_KEY', 'secret_value_xyz_0', 8148,),
    ('PASS_KEY', 'secret_value_xyz_1', 8149,),
    ('PASS_KEY', 'secret_value_xyz_2', 8150,),
    ('PASS_KEY', 'secret_value_xyz_3', 8151,),
    ('PASS_KEY', 'secret_value_xyz_4', 8152,),
    ('SECRET_SALT', 'secret_value_xyz_0', 8153,),
    ('SECRET_SALT', 'secret_value_xyz_1', 8154,),
    ('SECRET_SALT', 'secret_value_xyz_2', 8155,),
    ('SECRET_SALT', 'secret_value_xyz_3', 8156,),
    ('SECRET_SALT', 'secret_value_xyz_4', 8157,),
    ('TOKEN_SECRET', 'secret_value_xyz_0', 8158,),
    ('TOKEN_SECRET', 'secret_value_xyz_1', 8159,),
    ('TOKEN_SECRET', 'secret_value_xyz_2', 8160,),
    ('TOKEN_SECRET', 'secret_value_xyz_3', 8161,),
    ('TOKEN_SECRET', 'secret_value_xyz_4', 8162,),
    ('PASSWORD_1', 'secret_value_xyz_0', 8163,),
    ('PASSWORD_1', 'secret_value_xyz_1', 8164,),
    ('PASSWORD_1', 'secret_value_xyz_2', 8165,),
    ('PASSWORD_1', 'secret_value_xyz_3', 8166,),
    ('PASSWORD_1', 'secret_value_xyz_4', 8167,),
    ('KEY_PAIR', 'secret_value_xyz_0', 8168,),
    ('KEY_PAIR', 'secret_value_xyz_1', 8169,),
    ('KEY_PAIR', 'secret_value_xyz_2', 8170,),
    ('KEY_PAIR', 'secret_value_xyz_3', 8171,),
    ('KEY_PAIR', 'secret_value_xyz_4', 8172,),
    ('MASTER_KEY', 'secret_value_xyz_0', 8173,),
    ('MASTER_KEY', 'secret_value_xyz_1', 8174,),
    ('MASTER_KEY', 'secret_value_xyz_2', 8175,),
    ('MASTER_KEY', 'secret_value_xyz_3', 8176,),
    ('MASTER_KEY', 'secret_value_xyz_4', 8177,),
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
    ('project', 0, True, True, 8178,),
    ('project', 1, False, False, 8179,),
    ('project', 2, True, False, 8180,),
    ('project', 3, False, True, 8181,),
    ('project', 4, True, False, 8182,),
    ('project', 5, False, False, 8183,),
    ('project', 6, True, True, 8184,),
    ('project', 7, False, False, 8185,),
    ('project', 8, True, False, 8186,),
    ('project', 9, False, True, 8187,),
    ('project', 10, True, False, 8188,),
    ('project', 11, False, False, 8189,),
    ('project', 12, True, True, 8190,),
    ('exported_at', 0, True, True, 8191,),
    ('exported_at', 1, False, False, 8192,),
    ('exported_at', 2, True, False, 8193,),
    ('exported_at', 3, False, True, 8194,),
    ('exported_at', 4, True, False, 8195,),
    ('exported_at', 5, False, False, 8196,),
    ('exported_at', 6, True, True, 8197,),
    ('exported_at', 7, False, False, 8198,),
    ('exported_at', 8, True, False, 8199,),
    ('exported_at', 9, False, True, 8200,),
    ('exported_at', 10, True, False, 8201,),
    ('exported_at', 11, False, False, 8202,),
    ('exported_at', 12, True, True, 8203,),
    ('databases', 0, True, True, 8204,),
    ('databases', 1, False, False, 8205,),
    ('databases', 2, True, False, 8206,),
    ('databases', 3, False, True, 8207,),
    ('databases', 4, True, False, 8208,),
    ('databases', 5, False, False, 8209,),
    ('databases', 6, True, True, 8210,),
    ('databases', 7, False, False, 8211,),
    ('databases', 8, True, False, 8212,),
    ('databases', 9, False, True, 8213,),
    ('databases', 10, True, False, 8214,),
    ('databases', 11, False, False, 8215,),
    ('databases', 12, True, True, 8216,),
    ('notes', 0, True, True, 8217,),
    ('notes', 1, False, False, 8218,),
    ('notes', 2, True, False, 8219,),
    ('notes', 3, False, True, 8220,),
    ('notes', 4, True, False, 8221,),
    ('notes', 5, False, False, 8222,),
    ('notes', 6, True, True, 8223,),
    ('notes', 7, False, False, 8224,),
    ('notes', 8, True, False, 8225,),
    ('notes', 9, False, True, 8226,),
    ('notes', 10, True, False, 8227,),
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
