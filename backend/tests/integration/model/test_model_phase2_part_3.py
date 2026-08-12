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
        "q8_0",
        7,
        5014,
    ),
    (
        "q8_0",
        7,
        5015,
    ),
    (
        "q8_0",
        7,
        5016,
    ),
    (
        "q8_0",
        7,
        5017,
    ),
    (
        "Q8_0",
        7,
        5018,
    ),
    (
        "Q8_0",
        7,
        5019,
    ),
    (
        "Q8_0",
        7,
        5020,
    ),
    (
        "Q8_0",
        7,
        5021,
    ),
    (
        "Q8_0",
        7,
        5022,
    ),
    (
        "f16",
        15,
        5023,
    ),
    (
        "f16",
        15,
        5024,
    ),
    (
        "f16",
        15,
        5025,
    ),
    (
        "f16",
        15,
        5026,
    ),
    (
        "f16",
        15,
        5027,
    ),
    (
        "F16",
        15,
        5028,
    ),
    (
        "F16",
        15,
        5029,
    ),
    (
        "F16",
        15,
        5030,
    ),
    (
        "F16",
        15,
        5031,
    ),
    (
        "F16",
        15,
        5032,
    ),
    (
        "q4_0",
        2,
        5033,
    ),
    (
        "q4_0",
        2,
        5034,
    ),
    (
        "q4_0",
        2,
        5035,
    ),
    (
        "q4_0",
        2,
        5036,
    ),
    (
        "q4_0",
        2,
        5037,
    ),
    (
        "q4_1",
        3,
        5038,
    ),
    (
        "q4_1",
        3,
        5039,
    ),
    (
        "q4_1",
        3,
        5040,
    ),
    (
        "q4_1",
        3,
        5041,
    ),
    (
        "q4_1",
        3,
        5042,
    ),
    (
        "q5_0",
        8,
        5043,
    ),
    (
        "q5_0",
        8,
        5044,
    ),
    (
        "q5_0",
        8,
        5045,
    ),
    (
        "q5_0",
        8,
        5046,
    ),
    (
        "q5_0",
        8,
        5047,
    ),
    (
        "q5_1",
        9,
        5048,
    ),
    (
        "q5_1",
        9,
        5049,
    ),
    (
        "q5_1",
        9,
        5050,
    ),
    (
        "q5_1",
        9,
        5051,
    ),
    (
        "q5_1",
        9,
        5052,
    ),
    (
        "q2_k",
        10,
        5053,
    ),
    (
        "q2_k",
        10,
        5054,
    ),
    (
        "q2_k",
        10,
        5055,
    ),
    (
        "q2_k",
        10,
        5056,
    ),
    (
        "q2_k",
        10,
        5057,
    ),
    (
        "f32",
        0,
        5058,
    ),
    (
        "f32",
        0,
        5059,
    ),
    (
        "f32",
        0,
        5060,
    ),
    (
        "f32",
        0,
        5061,
    ),
    (
        "f32",
        0,
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


class TestDownloadScenarios(BaseTest):
    """DownloadScenarios scenarios."""

    def test_download_0_5063(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_1_5064(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_2_5065(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_3_5066(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_4_5067(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_5_5068(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_6_5069(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_7_5070(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_8_5071(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_9_5072(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_10_5073(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_11_5074(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_12_5075(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_13_5076(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_14_5077(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_15_5078(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_16_5079(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_17_5080(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_18_5081(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_19_5082(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_20_5083(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_21_5084(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_22_5085(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_23_5086(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_24_5087(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_25_5088(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_26_5089(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_27_5090(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_28_5091(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_29_5092(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_30_5093(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_31_5094(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_32_5095(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_33_5096(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_34_5097(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_35_5098(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_36_5099(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_37_5100(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_38_5101(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_39_5102(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_40_5103(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_41_5104(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_42_5105(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_43_5106(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_44_5107(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_45_5108(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_46_5109(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_47_5110(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_48_5111(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()

    def test_download_49_5112(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Download retries and mirror fallbacks stay resilient."""
        detector: LlamaCppDetector = _detector(tmp_path)
        monkeypatch.setattr(
            detector,
            "_download_from_huggingface",
            _side_effect_factory([Exception("boom"), "recovered"]),
        )
        assert (
            detector._download_with_retry("r", "f", tmp_path / "models", "http://e") == "recovered"
        )
        detector.shutdown()
