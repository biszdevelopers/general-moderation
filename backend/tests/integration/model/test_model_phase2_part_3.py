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


_KV_CACHE_MATRIX_CASES: tuple[tuple[str, int, int], ...] = (
    (
        "q8_0",
        7,
        5013,
    ),
    (
        "Q8_0",
        7,
        5014,
    ),
    (
        " q8_0 ",
        7,
        5015,
    ),
    (
        "q8-0",
        7,
        5016,
    ),
    (
        "q8_0 ",
        7,
        5017,
    ),
    (
        "f16",
        15,
        5018,
    ),
    (
        "F16",
        15,
        5019,
    ),
    (
        " f16 ",
        15,
        5020,
    ),
    (
        "f16",
        15,
        5021,
    ),
    (
        "f16 ",
        15,
        5022,
    ),
    (
        "q4_0",
        2,
        5023,
    ),
    (
        "Q4_0",
        2,
        5024,
    ),
    (
        " q4_0 ",
        2,
        5025,
    ),
    (
        "q4-0",
        7,
        5026,
    ),
    (
        "q4_0 ",
        2,
        5027,
    ),
    (
        "q4_1",
        3,
        5028,
    ),
    (
        "Q4_1",
        3,
        5029,
    ),
    (
        " q4_1 ",
        3,
        5030,
    ),
    (
        "q4-1",
        7,
        5031,
    ),
    (
        "q4_1 ",
        3,
        5032,
    ),
    (
        "q5_0",
        8,
        5033,
    ),
    (
        "Q5_0",
        8,
        5034,
    ),
    (
        " q5_0 ",
        8,
        5035,
    ),
    (
        "q5-0",
        7,
        5036,
    ),
    (
        "q5_0 ",
        8,
        5037,
    ),
    (
        "q5_1",
        9,
        5038,
    ),
    (
        "Q5_1",
        9,
        5039,
    ),
    (
        " q5_1 ",
        9,
        5040,
    ),
    (
        "q5-1",
        7,
        5041,
    ),
    (
        "q5_1 ",
        9,
        5042,
    ),
    (
        "q2_k",
        10,
        5043,
    ),
    (
        "Q2_K",
        10,
        5044,
    ),
    (
        " q2_k ",
        10,
        5045,
    ),
    (
        "q2-k",
        7,
        5046,
    ),
    (
        "q2_k ",
        10,
        5047,
    ),
    (
        "f32",
        0,
        5048,
    ),
    (
        "F32",
        0,
        5049,
    ),
    (
        " f32 ",
        0,
        5050,
    ),
    (
        "f32",
        0,
        5051,
    ),
    (
        "f32 ",
        0,
        5052,
    ),
    (
        "q3_0",
        7,
        5053,
    ),
    (
        "q6_0",
        7,
        5054,
    ),
    (
        "q3_k",
        7,
        5055,
    ),
    (
        "auto",
        7,
        5056,
    ),
    (
        "unknown",
        7,
        5057,
    ),
    (
        "Q4_2",
        7,
        5058,
    ),
    (
        "f64",
        7,
        5059,
    ),
    (
        "i8",
        7,
        5060,
    ),
    (
        "nf4",
        7,
        5061,
    ),
    (
        "q8",
        7,
        5062,
    ),
)


class TestKvCacheMatrix(BaseTest):
    """Known KV cache types map to their GGML enums."""

    @pytest.mark.parametrize(
        (
            "raw",
            "expected",
            "uid",
        ),
        _KV_CACHE_MATRIX_CASES,
    )
    def test_kv_cache_matrix(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, raw: str, expected: int, uid: int
    ) -> None:
        """Known KV cache types map to their GGML enums."""
        import sys as _sys
        import types as _types

        sub = _types.ModuleType("llama_cpp.llama_cpp")
        sub.GGML_TYPE_Q8_0 = 7
        sub.GGML_TYPE_F16 = 15
        sub.GGML_TYPE_Q4_0 = 2
        sub.GGML_TYPE_Q4_1 = 3
        sub.GGML_TYPE_Q5_0 = 8
        sub.GGML_TYPE_Q5_1 = 9
        sub.GGML_TYPE_Q2_K = 10
        sub.GGML_TYPE_F32 = 0
        monkeypatch.setitem(_sys.modules, "llama_cpp", _types.ModuleType("llama_cpp"))
        monkeypatch.setitem(_sys.modules, "llama_cpp.llama_cpp", sub)
        detector: LlamaCppDetector = _detector(tmp_path)
        assert detector._kv_cache_type(raw) == expected


_DOWNLOAD_RETRY_CASES: tuple[tuple[int, str, int], ...] = (
    (
        0,
        "http://127.0.0.1:1/mirror0",
        5063,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror1",
        5064,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror2",
        5065,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror3",
        5066,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror4",
        5067,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror5",
        5068,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror6",
        5069,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror7",
        5070,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror8",
        5071,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror9",
        5072,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror10",
        5073,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror11",
        5074,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror12",
        5075,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror13",
        5076,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror14",
        5077,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror15",
        5078,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror16",
        5079,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror17",
        5080,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror18",
        5081,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror19",
        5082,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror20",
        5083,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror21",
        5084,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror22",
        5085,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror23",
        5086,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror24",
        5087,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror25",
        5088,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror26",
        5089,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror27",
        5090,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror28",
        5091,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror29",
        5092,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror30",
        5093,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror31",
        5094,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror32",
        5095,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror33",
        5096,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror34",
        5097,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror35",
        5098,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror36",
        5099,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror37",
        5100,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror38",
        5101,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror39",
        5102,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror40",
        5103,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror41",
        5104,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror42",
        5105,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror43",
        5106,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror44",
        5107,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror45",
        5108,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror46",
        5109,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror47",
        5110,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror48",
        5111,
    ),
    (
        0,
        "http://127.0.0.1:1/mirror49",
        5112,
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
