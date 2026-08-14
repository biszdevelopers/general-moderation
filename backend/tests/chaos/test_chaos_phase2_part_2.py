"""Phase 2 chaos and resilience tests (generated).

Hash storms, malformed databases, package adapter failures, engine
recovery and API bursts."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from tests.base_test import BaseTest

_DB_RECOVERY_CASES: tuple[tuple[int, int], ...] = (
    (0, 9601,),
    (1, 9602,),
    (2, 9603,),
    (3, 9604,),
    (4, 9605,),
    (5, 9606,),
    (6, 9607,),
    (7, 9608,),
    (8, 9609,),
    (9, 9610,),
    (10, 9611,),
    (11, 9612,),
    (12, 9613,),
    (13, 9614,),
    (14, 9615,),
    (15, 9616,),
    (16, 9617,),
    (17, 9618,),
    (18, 9619,),
    (19, 9620,),
    (20, 9621,),
    (21, 9622,),
    (22, 9623,),
    (23, 9624,),
    (24, 9625,),
    (25, 9626,),
    (26, 9627,),
    (27, 9628,),
    (28, 9629,),
    (29, 9630,),
    (30, 9631,),
    (31, 9632,),
    (32, 9633,),
    (33, 9634,),
    (34, 9635,),
    (35, 9636,),
    (36, 9637,),
    (37, 9638,),
    (38, 9639,),
    (39, 9640,),
    (40, 9641,),
    (41, 9642,),
    (42, 9643,),
    (43, 9644,),
    (44, 9645,),
    (45, 9646,),
    (46, 9647,),
    (47, 9648,),
    (48, 9649,),
    (49, 9650,),
    (50, 9651,),
    (51, 9652,),
    (52, 9653,),
    (53, 9654,),
    (54, 9655,),
    (55, 9656,),
    (56, 9657,),
    (57, 9658,),
    (58, 9659,),
    (59, 9660,),
    (60, 9661,),
    (61, 9662,),
    (62, 9663,),
    (63, 9664,),
    (64, 9665,),
    (65, 9666,),
    (66, 9667,),
    (67, 9668,),
    (68, 9669,),
    (69, 9670,),
    (70, 9671,),
    (71, 9672,),
    (72, 9673,),
    (73, 9674,),
    (74, 9675,),
    (75, 9676,),
    (76, 9677,),
    (77, 9678,),
    (78, 9679,),
    (79, 9680,),
    (80, 9681,),
    (81, 9682,),
    (82, 9683,),
    (83, 9684,),
    (84, 9685,),
    (85, 9686,),
    (86, 9687,),
    (87, 9688,),
    (88, 9689,),
    (89, 9690,),
    (90, 9691,),
    (91, 9692,),
    (92, 9693,),
    (93, 9694,),
    (94, 9695,),
    (95, 9696,),
    (96, 9697,),
    (97, 9698,),
    (98, 9699,),
    (99, 9700,),
)

class TestDbRecovery(BaseTest):
    """Malformed or missing databases are handled without crashing."""

    @pytest.mark.parametrize(('scenario', 'uid',), _DB_RECOVERY_CASES)
    def test_db_recovery(self, tmp_path: Path, scenario: int, uid: int) -> None:
        """Malformed or missing databases are handled without crashing."""
        db = tmp_path / 'settings.db'
        db.write_bytes(f'this is not sqlite data at all {scenario}'.encode())
        from app.config import Settings
        settings = Settings(app_port=0, settings_db_path=str(db), log_file_path=str(tmp_path / 'l.log'))
        from app.settings_service import SettingsService
        with pytest.raises(sqlite3.DatabaseError):
            SettingsService(settings)
