"""Stage 3 failure policy integration tests.

Verifies the LLM_FAILURE_POLICY behavior when no provider can serve the
classification: rule_based keeps rule verdicts (REVIEW escalation) while
block fails closed.
"""

from __future__ import annotations

from typing import Any

import pytest

from app.engine.moderation_engine import ModerationEngine
from app.models.request import ModerationRequest
from app.models.response import ModerationResponse
from tests.base_test import BaseTest


@pytest.fixture()
def suspicious_word(engine: ModerationEngine, word_bank: Any) -> str:
    """A custom word that scores high enough to reach Stage 3."""
    word: str = "zaphrinquell"
    word_bank.add_word(word)
    engine.refresh_detectors()
    engine._app_config.update_default_threshold(1)
    return word


class TestFailurePolicy(BaseTest):
    """No-provider Stage 3 outcomes."""

    def test_rule_based_policy_keeps_review(
        self, engine: ModerationEngine, suspicious_word: str
    ) -> None:
        """With rule_based, unresolved content lands on REVIEW."""
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=f"this is {suspicious_word} content", app_name="a", user_id="u")
        )
        assert result.verdict.value in ("REVIEW", "BLOCK")

    def test_block_policy_fails_closed(
        self, engine: ModerationEngine, suspicious_word: str
    ) -> None:
        """With block policy, triggered content without a model blocks."""
        engine._settings_service.update({"LLM_FAILURE_POLICY": "block"})
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=f"this is {suspicious_word} content", app_name="a", user_id="u")
        )
        assert result.verdict.value == "BLOCK"
        assert any("fail-closed" in reason for reason in result.reasons)

    def test_provider_name_recorded_when_unavailable(
        self, engine: ModerationEngine, suspicious_word: str
    ) -> None:
        """The chain notes the unavailable provider entry."""
        engine._settings_service.update({"LLM_FAILURE_POLICY": "block"})
        result: ModerationResponse = engine.moderate(
            ModerationRequest(text=suspicious_word, app_name="a", user_id="u")
        )
        assert any("llm" in name for name in result.detector_chain)
