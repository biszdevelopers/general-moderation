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


class TestDownloadScenarios(BaseTest):
    """DownloadScenarios scenarios."""

    def test_download_50_5113(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_51_5114(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_52_5115(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_53_5116(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_54_5117(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_55_5118(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_56_5119(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_57_5120(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_58_5121(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_59_5122(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_60_5123(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_61_5124(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_62_5125(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_63_5126(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_64_5127(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_65_5128(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_66_5129(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_67_5130(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_68_5131(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_69_5132(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_70_5133(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_71_5134(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_72_5135(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_73_5136(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_74_5137(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_75_5138(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_76_5139(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_77_5140(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_78_5141(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_79_5142(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_80_5143(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_81_5144(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_82_5145(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_83_5146(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_84_5147(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_85_5148(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_86_5149(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_87_5150(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_88_5151(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_89_5152(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_90_5153(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_91_5154(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_92_5155(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_93_5156(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_94_5157(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_95_5158(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_96_5159(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_97_5160(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_98_5161(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_99_5162(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_100_5163(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_101_5164(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_102_5165(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_103_5166(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_104_5167(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_105_5168(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_106_5169(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_107_5170(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_108_5171(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_109_5172(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_110_5173(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_111_5174(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_112_5175(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_113_5176(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_114_5177(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_115_5178(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_116_5179(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_117_5180(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_118_5181(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_119_5182(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_120_5183(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_121_5184(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_122_5185(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_123_5186(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_124_5187(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_125_5188(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_126_5189(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_127_5190(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_128_5191(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_129_5192(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_130_5193(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_131_5194(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_132_5195(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_133_5196(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_134_5197(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_135_5198(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_136_5199(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_137_5200(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_138_5201(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_139_5202(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_140_5203(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_141_5204(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_142_5205(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_143_5206(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_144_5207(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_145_5208(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_146_5209(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_147_5210(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_148_5211(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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

    def test_download_149_5212(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
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
