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


_PROMPT_BUILD_CASES: tuple[tuple[str, int], ...] = (
    (
        "ordinary input message 0",
        5213,
    ),
    (
        "ordinary input message 1",
        5214,
    ),
    (
        "ordinary input message 2",
        5215,
    ),
    (
        "ordinary input message 3",
        5216,
    ),
    (
        "ordinary input message 4",
        5217,
    ),
    (
        "ordinary input message 5",
        5218,
    ),
    (
        "ordinary input message 6",
        5219,
    ),
    (
        "ordinary input message 7",
        5220,
    ),
    (
        "ordinary input message 8",
        5221,
    ),
    (
        "ordinary input message 9",
        5222,
    ),
    (
        "ordinary input message 10",
        5223,
    ),
    (
        "ordinary input message 11",
        5224,
    ),
    (
        "ordinary input message 12",
        5225,
    ),
    (
        "ordinary input message 13",
        5226,
    ),
    (
        "ordinary input message 14",
        5227,
    ),
    (
        "ordinary input message 15",
        5228,
    ),
    (
        "ordinary input message 16",
        5229,
    ),
    (
        "ordinary input message 17",
        5230,
    ),
    (
        "ordinary input message 18",
        5231,
    ),
    (
        "ordinary input message 19",
        5232,
    ),
    (
        "ordinary input message 20",
        5233,
    ),
    (
        "ordinary input message 21",
        5234,
    ),
    (
        "ordinary input message 22",
        5235,
    ),
    (
        "ordinary input message 23",
        5236,
    ),
    (
        "ordinary input message 24",
        5237,
    ),
    (
        "ordinary input message 25",
        5238,
    ),
    (
        "ordinary input message 26",
        5239,
    ),
    (
        "ordinary input message 27",
        5240,
    ),
    (
        "ordinary input message 28",
        5241,
    ),
    (
        "ordinary input message 29",
        5242,
    ),
    (
        "ordinary input message 30",
        5243,
    ),
    (
        "ordinary input message 31",
        5244,
    ),
    (
        "ordinary input message 32",
        5245,
    ),
    (
        "ordinary input message 33",
        5246,
    ),
    (
        "ordinary input message 34",
        5247,
    ),
    (
        "ordinary input message 35",
        5248,
    ),
    (
        "ordinary input message 36",
        5249,
    ),
    (
        "ordinary input message 37",
        5250,
    ),
    (
        "ordinary input message 38",
        5251,
    ),
    (
        "ordinary input message 39",
        5252,
    ),
    (
        "ordinary input message 40",
        5253,
    ),
    (
        "ordinary input message 41",
        5254,
    ),
    (
        "ordinary input message 42",
        5255,
    ),
    (
        "ordinary input message 43",
        5256,
    ),
    (
        "ordinary input message 44",
        5257,
    ),
    (
        "ordinary input message 45",
        5258,
    ),
    (
        "ordinary input message 46",
        5259,
    ),
    (
        "ordinary input message 47",
        5260,
    ),
    (
        "ordinary input message 48",
        5261,
    ),
    (
        "ordinary input message 49",
        5262,
    ),
    (
        "ordinary input message 50",
        5263,
    ),
    (
        "ordinary input message 51",
        5264,
    ),
    (
        "ordinary input message 52",
        5265,
    ),
    (
        "ordinary input message 53",
        5266,
    ),
    (
        "ordinary input message 54",
        5267,
    ),
    (
        "ordinary input message 55",
        5268,
    ),
    (
        "ordinary input message 56",
        5269,
    ),
    (
        "ordinary input message 57",
        5270,
    ),
    (
        "ordinary input message 58",
        5271,
    ),
    (
        "ordinary input message 59",
        5272,
    ),
    (
        "ordinary input message 60",
        5273,
    ),
    (
        "ordinary input message 61",
        5274,
    ),
    (
        "ordinary input message 62",
        5275,
    ),
    (
        "ordinary input message 63",
        5276,
    ),
    (
        "ordinary input message 64",
        5277,
    ),
    (
        "ordinary input message 65",
        5278,
    ),
    (
        "ordinary input message 66",
        5279,
    ),
    (
        "ordinary input message 67",
        5280,
    ),
    (
        "ordinary input message 68",
        5281,
    ),
    (
        "ordinary input message 69",
        5282,
    ),
    (
        "ordinary input message 70",
        5283,
    ),
    (
        "ordinary input message 71",
        5284,
    ),
    (
        "ordinary input message 72",
        5285,
    ),
    (
        "ordinary input message 73",
        5286,
    ),
    (
        "ordinary input message 74",
        5287,
    ),
    (
        "ordinary input message 75",
        5288,
    ),
    (
        "ordinary input message 76",
        5289,
    ),
    (
        "ordinary input message 77",
        5290,
    ),
    (
        "ordinary input message 78",
        5291,
    ),
    (
        "ordinary input message 79",
        5292,
    ),
    (
        "ordinary input message 80",
        5293,
    ),
    (
        "ordinary input message 81",
        5294,
    ),
    (
        "ordinary input message 82",
        5295,
    ),
    (
        "ordinary input message 83",
        5296,
    ),
    (
        "ordinary input message 84",
        5297,
    ),
    (
        "ordinary input message 85",
        5298,
    ),
    (
        "ordinary input message 86",
        5299,
    ),
    (
        "ordinary input message 87",
        5300,
    ),
    (
        "ordinary input message 88",
        5301,
    ),
    (
        "ordinary input message 89",
        5302,
    ),
    (
        "ordinary input message 90",
        5303,
    ),
    (
        "ordinary input message 91",
        5304,
    ),
    (
        "ordinary input message 92",
        5305,
    ),
    (
        "ordinary input message 93",
        5306,
    ),
    (
        "ordinary input message 94",
        5307,
    ),
    (
        "ordinary input message 95",
        5308,
    ),
    (
        "ordinary input message 96",
        5309,
    ),
    (
        "ordinary input message 97",
        5310,
    ),
    (
        "ordinary input message 98",
        5311,
    ),
    (
        "ordinary input message 99",
        5312,
    ),
)


class TestPromptBuild(BaseTest):
    """Fallback prompts carry the system role and sanitized payload."""

    @pytest.mark.parametrize(
        (
            "text",
            "uid",
        ),
        _PROMPT_BUILD_CASES,
    )
    def test_prompt_build(self, tmp_path: Path, text: str, uid: int) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt(text)
        assert text in prompt
        assert "system" in prompt.lower()
        detector.shutdown()
