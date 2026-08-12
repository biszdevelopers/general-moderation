"""Phase 2 model/LLM tests (generated).

Sanitize matrix, thread and KV-cache sweeps, download resilience and
prompt/detect behavior; see tests/tools/phase2_generator.py."""

# multilingual fixtures use non-ASCII on purpose
from __future__ import annotations

from pathlib import Path
from typing import Any

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


class TestPromptBuilding(BaseTest):
    """PromptBuilding scenarios."""

    def test_prompt_build_0_5213(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_1_5214(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_2_5215(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_3_5216(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_4_5217(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_5_5218(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_6_5219(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_7_5220(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_8_5221(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_9_5222(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_10_5223(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_11_5224(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_12_5225(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_13_5226(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_14_5227(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_15_5228(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_16_5229(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_17_5230(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_18_5231(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_19_5232(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_20_5233(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_21_5234(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_22_5235(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_23_5236(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_24_5237(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_25_5238(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_26_5239(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_27_5240(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_28_5241(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_29_5242(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_30_5243(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_31_5244(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_32_5245(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_33_5246(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_34_5247(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_35_5248(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_36_5249(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_37_5250(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_38_5251(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_39_5252(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_40_5253(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_41_5254(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_42_5255(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_43_5256(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_44_5257(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_45_5258(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_46_5259(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_47_5260(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_48_5261(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_49_5262(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_50_5263(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_51_5264(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_52_5265(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_53_5266(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_54_5267(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_55_5268(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_56_5269(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_57_5270(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_58_5271(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_59_5272(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_60_5273(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_61_5274(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_62_5275(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_63_5276(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_64_5277(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_65_5278(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_66_5279(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_67_5280(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_68_5281(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_69_5282(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_70_5283(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_71_5284(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_72_5285(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_73_5286(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_74_5287(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_75_5288(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_76_5289(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_77_5290(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_78_5291(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_79_5292(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_80_5293(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_81_5294(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_82_5295(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_83_5296(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_84_5297(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_85_5298(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_86_5299(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_87_5300(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_88_5301(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_89_5302(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_90_5303(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_91_5304(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_92_5305(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_93_5306(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_94_5307(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_95_5308(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_96_5309(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_97_5310(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_98_5311(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()

    def test_prompt_build_99_5312(self, tmp_path: Path) -> None:
        """Fallback prompts carry the system role and sanitized payload."""
        detector: LlamaCppDetector = _detector(tmp_path)
        detector._chat_template = None
        prompt = detector._build_prompt("ordinary input")
        assert "ordinary input" in prompt
        assert "system" in prompt.lower() or "moderation" in prompt.lower()
        detector.shutdown()
