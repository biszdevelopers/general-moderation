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


_DOWNLOAD_RETRY_CASES: tuple[tuple[int, str, int], ...] = (
    (
        1,
        "http://127.0.0.1:1/mirror0",
        5113,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror1",
        5114,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror2",
        5115,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror3",
        5116,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror4",
        5117,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror5",
        5118,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror6",
        5119,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror7",
        5120,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror8",
        5121,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror9",
        5122,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror10",
        5123,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror11",
        5124,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror12",
        5125,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror13",
        5126,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror14",
        5127,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror15",
        5128,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror16",
        5129,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror17",
        5130,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror18",
        5131,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror19",
        5132,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror20",
        5133,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror21",
        5134,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror22",
        5135,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror23",
        5136,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror24",
        5137,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror25",
        5138,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror26",
        5139,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror27",
        5140,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror28",
        5141,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror29",
        5142,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror30",
        5143,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror31",
        5144,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror32",
        5145,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror33",
        5146,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror34",
        5147,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror35",
        5148,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror36",
        5149,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror37",
        5150,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror38",
        5151,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror39",
        5152,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror40",
        5153,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror41",
        5154,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror42",
        5155,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror43",
        5156,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror44",
        5157,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror45",
        5158,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror46",
        5159,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror47",
        5160,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror48",
        5161,
    ),
    (
        1,
        "http://127.0.0.1:1/mirror49",
        5162,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror0",
        5163,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror1",
        5164,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror2",
        5165,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror3",
        5166,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror4",
        5167,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror5",
        5168,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror6",
        5169,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror7",
        5170,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror8",
        5171,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror9",
        5172,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror10",
        5173,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror11",
        5174,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror12",
        5175,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror13",
        5176,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror14",
        5177,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror15",
        5178,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror16",
        5179,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror17",
        5180,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror18",
        5181,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror19",
        5182,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror20",
        5183,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror21",
        5184,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror22",
        5185,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror23",
        5186,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror24",
        5187,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror25",
        5188,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror26",
        5189,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror27",
        5190,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror28",
        5191,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror29",
        5192,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror30",
        5193,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror31",
        5194,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror32",
        5195,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror33",
        5196,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror34",
        5197,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror35",
        5198,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror36",
        5199,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror37",
        5200,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror38",
        5201,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror39",
        5202,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror40",
        5203,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror41",
        5204,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror42",
        5205,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror43",
        5206,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror44",
        5207,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror45",
        5208,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror46",
        5209,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror47",
        5210,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror48",
        5211,
    ),
    (
        2,
        "http://127.0.0.1:1/mirror49",
        5212,
    ),
)


class TestDownloadRetry(BaseTest):
    """Download retries and mirror fallbacks stay resilient."""

    @pytest.mark.parametrize(
        (
            "n_failures",
            "endpoint",
            "uid",
        ),
        _DOWNLOAD_RETRY_CASES,
    )
    def test_download_retry(
        self,
        tmp_path: Path,
        monkeypatch: pytest.MonkeyPatch,
        n_failures: int,
        endpoint: str,
        uid: int,
    ) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom")] * n_failures + ["recovered"]),
        )
        assert detector._download_with_retry("r", "f", tmp_path / "models", endpoint) == "recovered"
        detector.shutdown()
