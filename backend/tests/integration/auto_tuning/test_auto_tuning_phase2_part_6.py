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

_WEIGHT_CLAMP_CASES: tuple[tuple[str, int, int], ...] = (
    ('WEIGHT_DETECTOR_BKTREE', 5, 4759,),
    ('WEIGHT_DETECTOR_BKTREE', 15, 4760,),
    ('WEIGHT_DETECTOR_BKTREE', 25, 4761,),
    ('WEIGHT_DETECTOR_BKTREE', 35, 4762,),
    ('WEIGHT_DETECTOR_BKTREE', 45, 4763,),
    ('WEIGHT_DETECTOR_BKTREE', 50, 4764,),
    ('WEIGHT_DETECTOR_METAPHONE', 5, 4765,),
    ('WEIGHT_DETECTOR_METAPHONE', 15, 4766,),
    ('WEIGHT_DETECTOR_METAPHONE', 25, 4767,),
    ('WEIGHT_DETECTOR_METAPHONE', 35, 4768,),
    ('WEIGHT_DETECTOR_METAPHONE', 45, 4769,),
    ('WEIGHT_DETECTOR_METAPHONE', 50, 4770,),
    ('WEIGHT_SEMANTIC_POLITICAL', 5, 4771,),
    ('WEIGHT_SEMANTIC_POLITICAL', 15, 4772,),
    ('WEIGHT_SEMANTIC_POLITICAL', 25, 4773,),
    ('WEIGHT_SEMANTIC_POLITICAL', 35, 4774,),
    ('WEIGHT_SEMANTIC_POLITICAL', 45, 4775,),
    ('WEIGHT_SEMANTIC_POLITICAL', 50, 4776,),
    ('WEIGHT_SEMANTIC_VIOLENCE', 5, 4777,),
    ('WEIGHT_SEMANTIC_VIOLENCE', 15, 4778,),
    ('WEIGHT_SEMANTIC_VIOLENCE', 25, 4779,),
    ('WEIGHT_SEMANTIC_VIOLENCE', 35, 4780,),
    ('WEIGHT_SEMANTIC_VIOLENCE', 45, 4781,),
    ('WEIGHT_SEMANTIC_VIOLENCE', 50, 4782,),
    ('WEIGHT_SEMANTIC_SEXUAL', 5, 4783,),
    ('WEIGHT_SEMANTIC_SEXUAL', 15, 4784,),
    ('WEIGHT_SEMANTIC_SEXUAL', 25, 4785,),
    ('WEIGHT_SEMANTIC_SEXUAL', 35, 4786,),
    ('WEIGHT_SEMANTIC_SEXUAL', 45, 4787,),
    ('WEIGHT_SEMANTIC_SEXUAL', 50, 4788,),
    ('WEIGHT_SEMANTIC_HATE', 5, 4789,),
    ('WEIGHT_SEMANTIC_HATE', 15, 4790,),
    ('WEIGHT_SEMANTIC_HATE', 25, 4791,),
    ('WEIGHT_SEMANTIC_HATE', 35, 4792,),
    ('WEIGHT_SEMANTIC_HATE', 45, 4793,),
    ('WEIGHT_SEMANTIC_HATE', 50, 4794,),
    ('WEIGHT_SEMANTIC_PII', 5, 4795,),
    ('WEIGHT_SEMANTIC_PII', 15, 4796,),
    ('WEIGHT_SEMANTIC_PII', 25, 4797,),
    ('WEIGHT_SEMANTIC_PII', 35, 4798,),
    ('WEIGHT_SEMANTIC_PII', 45, 4799,),
    ('WEIGHT_SEMANTIC_PII', 50, 4800,),
    ('WEIGHT_SEMANTIC_ADS', 5, 4801,),
    ('WEIGHT_SEMANTIC_ADS', 15, 4802,),
    ('WEIGHT_SEMANTIC_ADS', 25, 4803,),
    ('WEIGHT_SEMANTIC_ADS', 35, 4804,),
    ('WEIGHT_SEMANTIC_ADS', 45, 4805,),
    ('WEIGHT_SEMANTIC_ADS', 50, 4806,),
    ('WEIGHT_USER', 5, 4807,),
    ('WEIGHT_USER', 15, 4808,),
)

class TestWeightClamp(BaseTest):
    """Tuned weights stay clamped between 5 and 50."""

    @pytest.mark.parametrize(('key', 'value', 'uid',), _WEIGHT_CLAMP_CASES)
    def test_weight_clamp(self, key: str, value: int, uid: int) -> None:
        """Tuned weights stay clamped between 5 and 50."""
        feedback: FeedbackService = _feedback_service()
        service: SettingsService = feedback._settings_service
        service.get(key)
        service.update({key: value})
        feedback.run_batch()
        stored = int(service.get(key, 0))
        assert 5 <= stored <= 50
        feedback.close()
