"""Phase 2 model/LLM tests (generated).

Sanitize matrix, thread and KV-cache sweeps, download resilience and
prompt/detect behavior; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from app.ai.llama_detector import LlamaCppDetector
from app.config import Settings
from tests.base_test import BaseTest


def _detector(tmp_path: Path) -> LlamaCppDetector:
    (tmp_path / "models").mkdir(parents=True, exist_ok=True)
    settings = Settings(
        app_port=0,
        model_path="auto",
        model_dir=str(tmp_path / "models"),
        model_filename="model.gguf",
        model_primary_repo="owner/repo",
        model_fallback_repo="fallback/repo",
        hf_endpoint="http://127.0.0.1:1",
        hf_mirror="http://127.0.0.1:2",
        modelscope_endpoint="http://127.0.0.1:3",
        log_file_path=str(tmp_path / "l.log"),
    )
    return LlamaCppDetector(settings, None)


class _FakeModel:
    metadata: dict[str, str] = {}  # noqa: RUF012

    def __init__(self, reply: str) -> None:
        self._reply = reply

    def __call__(self, prompt: str, **kwargs: object) -> dict[str, object]:
        return {"choices": [{"text": self._reply}]}

    def close(self) -> None:
        return None


def _side_effect_factory(results: list[object]) -> Any:
    index: list[int] = [0]

    def _side_effect(*args: object, **kwargs: object) -> str:
        current: object = results[min(index[0], len(results) - 1)]
        index[0] += 1
        if isinstance(current, Exception):
            raise current
        return str(current)

    return _side_effect


_DETECT_REPLY_MATRIX_CASES: tuple[tuple[str, bool, int], ...] = (
    (
        "BLOCK",
        True,
        5313,
    ),
    (
        "ALLOW",
        False,
        5314,
    ),
    (
        "PASS",
        False,
        5315,
    ),
    (
        "REVIEW",
        False,
        5316,
    ),
    (
        "<think>reasoning</think> BLOCK",
        True,
        5317,
    ),
    (
        "<think>x</think> ALLOW",
        False,
        5318,
    ),
    (
        "BLOCK the content",
        True,
        5319,
    ),
    (
        "the answer is PASS",
        False,
        5320,
    ),
    (
        "VERDICT: BLOCK",
        True,
        5321,
    ),
    (
        "moderation: ALLOW",
        False,
        5322,
    ),
    (
        "BLOCK",
        True,
        5323,
    ),
    (
        "ALLOW",
        False,
        5324,
    ),
    (
        "PASS",
        False,
        5325,
    ),
    (
        "REVIEW",
        False,
        5326,
    ),
    (
        "<think>reasoning</think> BLOCK",
        True,
        5327,
    ),
    (
        "<think>x</think> ALLOW",
        False,
        5328,
    ),
    (
        "BLOCK the content",
        True,
        5329,
    ),
    (
        "the answer is PASS",
        False,
        5330,
    ),
    (
        "VERDICT: BLOCK",
        True,
        5331,
    ),
    (
        "moderation: ALLOW",
        False,
        5332,
    ),
    (
        "BLOCK",
        True,
        5333,
    ),
    (
        "ALLOW",
        False,
        5334,
    ),
    (
        "PASS",
        False,
        5335,
    ),
    (
        "REVIEW",
        False,
        5336,
    ),
    (
        "<think>reasoning</think> BLOCK",
        True,
        5337,
    ),
    (
        "<think>x</think> ALLOW",
        False,
        5338,
    ),
    (
        "BLOCK the content",
        True,
        5339,
    ),
    (
        "the answer is PASS",
        False,
        5340,
    ),
    (
        "VERDICT: BLOCK",
        True,
        5341,
    ),
    (
        "moderation: ALLOW",
        False,
        5342,
    ),
    (
        "BLOCK",
        True,
        5343,
    ),
    (
        "ALLOW",
        False,
        5344,
    ),
    (
        "PASS",
        False,
        5345,
    ),
    (
        "REVIEW",
        False,
        5346,
    ),
    (
        "<think>reasoning</think> BLOCK",
        True,
        5347,
    ),
    (
        "<think>x</think> ALLOW",
        False,
        5348,
    ),
    (
        "BLOCK the content",
        True,
        5349,
    ),
    (
        "the answer is PASS",
        False,
        5350,
    ),
    (
        "VERDICT: BLOCK",
        True,
        5351,
    ),
    (
        "moderation: ALLOW",
        False,
        5352,
    ),
    (
        "BLOCK",
        True,
        5353,
    ),
    (
        "ALLOW",
        False,
        5354,
    ),
    (
        "PASS",
        False,
        5355,
    ),
    (
        "REVIEW",
        False,
        5356,
    ),
    (
        "<think>reasoning</think> BLOCK",
        True,
        5357,
    ),
    (
        "<think>x</think> ALLOW",
        False,
        5358,
    ),
    (
        "BLOCK the content",
        True,
        5359,
    ),
    (
        "the answer is PASS",
        False,
        5360,
    ),
    (
        "VERDICT: BLOCK",
        True,
        5361,
    ),
    (
        "moderation: ALLOW",
        False,
        5362,
    ),
)


class TestDetectReplyMatrix(BaseTest):
    """Model replies reproduce the golden matched flag."""

    @pytest.mark.parametrize(
        (
            "reply",
            "expected",
            "uid",
        ),
        _DETECT_REPLY_MATRIX_CASES,
    )
    def test_detect_reply_matrix(
        self, tmp_path: Path, reply: str, expected: bool, uid: int
    ) -> None:
        """Model replies reproduce the golden matched flag."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._model = _FakeModel(reply)
        assert detector.detect("test").matched is expected
        detector.shutdown()
