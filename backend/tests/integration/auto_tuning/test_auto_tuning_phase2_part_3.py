"""Phase 2 auto-tuning tests (generated).

Precision deltas, threshold pass-rate sweeps, decay half-lives and
report structure under the frozen clock."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

import pytest

from app.appconfig.app_config_service import AppConfigService
from app.config import Settings
from app.feedback.feedback_service import FeedbackService
from app.settings_service import SettingsService
from app.utils.logger import ModerationLogger
from tests.base_test import BaseTest


def _feedback_service(enabled: bool = True) -> FeedbackService:
    import tempfile
    from pathlib import Path
    root: Path = Path(tempfile.mkdtemp())
    (root / 'logs').mkdir(parents=True, exist_ok=True)
    settings = Settings(
        app_port=0,
        log_file_path=str(root / 'logs' / 'l.log'),
        feedback_db_path=str(root / 'f.db'),
        settings_db_path=str(root / 's.db'),
        app_config_db_path=str(root / 'c.db'),
        auto_tuning_enabled=enabled,
    )
    logger: ModerationLogger = ModerationLogger(settings.log_file_path, max_bytes=100_000)
    settings_service: SettingsService = SettingsService(settings)
    app_config: AppConfigService = AppConfigService(settings.app_config_db_path)
    return FeedbackService(settings, settings_service, app_config, logger)

_THRESHOLD_PASS_RATE_CASES: tuple[tuple[int, int, int, int], ...] = (
    (15, 15, 1, 4459,),
    (0, 20, -1, 4460,),
    (1, 20, -1, 4461,),
    (2, 20, -1, 4462,),
    (3, 20, -1, 4463,),
    (4, 20, -1, 4464,),
    (5, 20, -1, 4465,),
    (6, 20, -1, 4466,),
    (7, 20, -1, 4467,),
    (8, 20, -1, 4468,),
    (9, 20, -1, 4469,),
    (10, 20, -1, 4470,),
    (11, 20, -1, 4471,),
    (12, 20, -1, 4472,),
    (13, 20, -1, 4473,),
    (14, 20, -1, 4474,),
    (15, 20, 0, 4475,),
    (16, 20, 0, 4476,),
    (17, 20, 0, 4477,),
    (18, 20, 0, 4478,),
    (19, 20, 1, 4479,),
    (20, 20, 1, 4480,),
    (0, 30, -1, 4481,),
    (1, 30, -1, 4482,),
    (2, 30, -1, 4483,),
    (3, 30, -1, 4484,),
    (4, 30, -1, 4485,),
    (5, 30, -1, 4486,),
    (6, 30, -1, 4487,),
    (7, 30, -1, 4488,),
    (8, 30, -1, 4489,),
    (9, 30, -1, 4490,),
    (10, 30, -1, 4491,),
    (11, 30, -1, 4492,),
    (12, 30, -1, 4493,),
    (13, 30, -1, 4494,),
    (14, 30, -1, 4495,),
    (15, 30, -1, 4496,),
    (16, 30, -1, 4497,),
    (17, 30, -1, 4498,),
    (18, 30, -1, 4499,),
    (19, 30, -1, 4500,),
    (20, 30, -1, 4501,),
    (21, 30, -1, 4502,),
    (22, 30, 0, 4503,),
    (23, 30, 0, 4504,),
    (24, 30, 0, 4505,),
    (25, 30, 0, 4506,),
    (26, 30, 0, 4507,),
    (27, 30, 0, 4508,),
    (28, 30, 1, 4509,),
    (29, 30, 1, 4510,),
    (30, 30, 1, 4511,),
    (0, 40, -1, 4512,),
    (1, 40, -1, 4513,),
    (2, 40, -1, 4514,),
    (3, 40, -1, 4515,),
    (4, 40, -1, 4516,),
    (5, 40, -1, 4517,),
    (6, 40, -1, 4518,),
    (7, 40, -1, 4519,),
    (8, 40, -1, 4520,),
    (9, 40, -1, 4521,),
    (10, 40, -1, 4522,),
    (11, 40, -1, 4523,),
    (12, 40, -1, 4524,),
    (13, 40, -1, 4525,),
    (14, 40, -1, 4526,),
    (15, 40, -1, 4527,),
    (16, 40, -1, 4528,),
    (17, 40, -1, 4529,),
    (18, 40, -1, 4530,),
    (19, 40, -1, 4531,),
    (20, 40, -1, 4532,),
    (21, 40, -1, 4533,),
    (22, 40, -1, 4534,),
    (23, 40, -1, 4535,),
    (24, 40, -1, 4536,),
    (25, 40, -1, 4537,),
    (26, 40, -1, 4538,),
    (27, 40, -1, 4539,),
    (28, 40, -1, 4540,),
    (29, 40, 0, 4541,),
    (30, 40, 0, 4542,),
    (31, 40, 0, 4543,),
    (32, 40, 0, 4544,),
    (33, 40, 0, 4545,),
    (34, 40, 0, 4546,),
    (35, 40, 0, 4547,),
    (36, 40, 0, 4548,),
    (37, 40, 1, 4549,),
    (38, 40, 1, 4550,),
    (39, 40, 1, 4551,),
    (40, 40, 1, 4552,),
    (0, 50, -1, 4553,),
    (1, 50, -1, 4554,),
    (2, 50, -1, 4555,),
    (3, 50, -1, 4556,),
    (4, 50, -1, 4557,),
    (5, 50, -1, 4558,),
)

class TestThresholdPassRate(BaseTest):
    """The threshold rises on high pass rate and falls on high block rate."""

    @pytest.mark.parametrize(('passes', 'total', 'expected', 'uid',), _THRESHOLD_PASS_RATE_CASES)
    def test_threshold_pass_rate(self, passes: int, total: int, expected: int, uid: int) -> None:
        """The threshold rises on high pass rate and falls on high block rate."""
        feedback: FeedbackService = _feedback_service()
        app_config: AppConfigService = feedback._app_config
        before = int(app_config.get(None)['score_threshold'])
        for index in range(total):
            feedback.record_decision('PASS' if index < passes else 'BLOCK', True)
        feedback.run_batch()
        after = int(app_config.get(None)['score_threshold'])
        delta = (after > before) - (after < before)
        assert delta == expected
        feedback.close()
