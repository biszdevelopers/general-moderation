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


_DETECT_REPLY_MATRIX_CASES: tuple[tuple[str, str, bool, int], ...] = (
    (
        "BLOCK",
        "user message number 0",
        True,
        5313,
    ),
    (
        "ALLOW",
        "user message number 1",
        False,
        5314,
    ),
    (
        "PASS",
        "user message number 2",
        False,
        5315,
    ),
    (
        "REVIEW",
        "user message number 3",
        False,
        5316,
    ),
    (
        "<think>reasoning</think> BLOCK",
        "user message number 4",
        True,
        5317,
    ),
    (
        "<think>x</think> ALLOW",
        "user message number 5",
        False,
        5318,
    ),
    (
        "BLOCK the content",
        "user message number 6",
        True,
        5319,
    ),
    (
        "the answer is PASS",
        "user message number 7",
        False,
        5320,
    ),
    (
        "VERDICT: BLOCK",
        "user message number 8",
        True,
        5321,
    ),
    (
        "moderation: ALLOW",
        "user message number 9",
        False,
        5322,
    ),
    (
        "BLOCK",
        "user message number 10",
        True,
        5323,
    ),
    (
        "ALLOW",
        "user message number 11",
        False,
        5324,
    ),
    (
        "PASS",
        "user message number 12",
        False,
        5325,
    ),
    (
        "REVIEW",
        "user message number 13",
        False,
        5326,
    ),
    (
        "<think>reasoning</think> BLOCK",
        "user message number 14",
        True,
        5327,
    ),
    (
        "<think>x</think> ALLOW",
        "user message number 15",
        False,
        5328,
    ),
    (
        "BLOCK the content",
        "user message number 16",
        True,
        5329,
    ),
    (
        "the answer is PASS",
        "user message number 17",
        False,
        5330,
    ),
    (
        "VERDICT: BLOCK",
        "user message number 18",
        True,
        5331,
    ),
    (
        "moderation: ALLOW",
        "user message number 19",
        False,
        5332,
    ),
    (
        "BLOCK",
        "user message number 20",
        True,
        5333,
    ),
    (
        "ALLOW",
        "user message number 21",
        False,
        5334,
    ),
    (
        "PASS",
        "user message number 22",
        False,
        5335,
    ),
    (
        "REVIEW",
        "user message number 23",
        False,
        5336,
    ),
    (
        "<think>reasoning</think> BLOCK",
        "user message number 24",
        True,
        5337,
    ),
    (
        "<think>x</think> ALLOW",
        "user message number 25",
        False,
        5338,
    ),
    (
        "BLOCK the content",
        "user message number 26",
        True,
        5339,
    ),
    (
        "the answer is PASS",
        "user message number 27",
        False,
        5340,
    ),
    (
        "VERDICT: BLOCK",
        "user message number 28",
        True,
        5341,
    ),
    (
        "moderation: ALLOW",
        "user message number 29",
        False,
        5342,
    ),
    (
        "BLOCK",
        "user message number 30",
        True,
        5343,
    ),
    (
        "ALLOW",
        "user message number 31",
        False,
        5344,
    ),
    (
        "PASS",
        "user message number 32",
        False,
        5345,
    ),
    (
        "REVIEW",
        "user message number 33",
        False,
        5346,
    ),
    (
        "<think>reasoning</think> BLOCK",
        "user message number 34",
        True,
        5347,
    ),
    (
        "<think>x</think> ALLOW",
        "user message number 35",
        False,
        5348,
    ),
    (
        "BLOCK the content",
        "user message number 36",
        True,
        5349,
    ),
    (
        "the answer is PASS",
        "user message number 37",
        False,
        5350,
    ),
    (
        "VERDICT: BLOCK",
        "user message number 38",
        True,
        5351,
    ),
    (
        "moderation: ALLOW",
        "user message number 39",
        False,
        5352,
    ),
    (
        "BLOCK",
        "user message number 40",
        True,
        5353,
    ),
    (
        "ALLOW",
        "user message number 41",
        False,
        5354,
    ),
    (
        "PASS",
        "user message number 42",
        False,
        5355,
    ),
    (
        "REVIEW",
        "user message number 43",
        False,
        5356,
    ),
    (
        "<think>reasoning</think> BLOCK",
        "user message number 44",
        True,
        5357,
    ),
    (
        "<think>x</think> ALLOW",
        "user message number 45",
        False,
        5358,
    ),
    (
        "BLOCK the content",
        "user message number 46",
        True,
        5359,
    ),
    (
        "the answer is PASS",
        "user message number 47",
        False,
        5360,
    ),
    (
        "VERDICT: BLOCK",
        "user message number 48",
        True,
        5361,
    ),
    (
        "moderation: ALLOW",
        "user message number 49",
        False,
        5362,
    ),
)


class TestDetectReplyMatrix(BaseTest):
    """Model replies reproduce the golden matched flag."""

    @pytest.mark.parametrize(
        (
            "reply",
            "text",
            "expected",
            "uid",
        ),
        _DETECT_REPLY_MATRIX_CASES,
    )
    def test_detect_reply_matrix(
        self, tmp_path: Path, reply: str, text: str, expected: bool, uid: int
    ) -> None:
        """Model replies reproduce the golden matched flag."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._model = _FakeModel(reply)
        assert detector.detect(text).matched is expected
        detector.shutdown()
