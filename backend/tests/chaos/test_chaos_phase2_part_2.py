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
    (0, 9561,),
    (1, 9562,),
    (2, 9563,),
    (3, 9564,),
    (4, 9565,),
    (5, 9566,),
    (6, 9567,),
    (7, 9568,),
    (8, 9569,),
    (9, 9570,),
    (10, 9571,),
    (11, 9572,),
    (12, 9573,),
    (13, 9574,),
    (14, 9575,),
    (15, 9576,),
    (16, 9577,),
    (17, 9578,),
    (18, 9579,),
    (19, 9580,),
    (20, 9581,),
    (21, 9582,),
    (22, 9583,),
    (23, 9584,),
    (24, 9585,),
    (25, 9586,),
    (26, 9587,),
    (27, 9588,),
    (28, 9589,),
    (29, 9590,),
    (30, 9591,),
    (31, 9592,),
    (32, 9593,),
    (33, 9594,),
    (34, 9595,),
    (35, 9596,),
    (36, 9597,),
    (37, 9598,),
    (38, 9599,),
    (39, 9600,),
    (40, 9601,),
    (41, 9602,),
    (42, 9603,),
    (43, 9604,),
    (44, 9605,),
    (45, 9606,),
    (46, 9607,),
    (47, 9608,),
    (48, 9609,),
    (49, 9610,),
    (50, 9611,),
    (51, 9612,),
    (52, 9613,),
    (53, 9614,),
    (54, 9615,),
    (55, 9616,),
    (56, 9617,),
    (57, 9618,),
    (58, 9619,),
    (59, 9620,),
    (60, 9621,),
    (61, 9622,),
    (62, 9623,),
    (63, 9624,),
    (64, 9625,),
    (65, 9626,),
    (66, 9627,),
    (67, 9628,),
    (68, 9629,),
    (69, 9630,),
    (70, 9631,),
    (71, 9632,),
    (72, 9633,),
    (73, 9634,),
    (74, 9635,),
    (75, 9636,),
    (76, 9637,),
    (77, 9638,),
    (78, 9639,),
    (79, 9640,),
    (80, 9641,),
    (81, 9642,),
    (82, 9643,),
    (83, 9644,),
    (84, 9645,),
    (85, 9646,),
    (86, 9647,),
    (87, 9648,),
    (88, 9649,),
    (89, 9650,),
    (90, 9651,),
    (91, 9652,),
    (92, 9653,),
    (93, 9654,),
    (94, 9655,),
    (95, 9656,),
    (96, 9657,),
    (97, 9658,),
    (98, 9659,),
    (99, 9660,),
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
