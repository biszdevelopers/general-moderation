"""Standalone model download entry point.

Run with ``uv run python -m app.ai.download`` (or ``npm run download`` from
the repository root) to fetch the configured GGUF model on demand instead of
waiting for the first-request auto-download.
"""

from __future__ import annotations

import sys
from typing import Any


class _ConsoleLogger:
    """Minimal logger printing detector messages to the console."""

    def log(self, level: int, message: str, **fields: Any) -> None:
        """Print a structured message, skipping debug noise.

        :param level: logging level of the message
        :param message: the message text
        :param fields: structured fields
        """
        if level < 20:  # DEBUG and below
            return
        prefix: str = "INFO" if level < 30 else "WARN" if level < 40 else "ERROR"
        detail: str = f" {fields}" if fields else ""
        print(f"[{prefix}] {message}{detail}")


def main(argv: list[str] | None = None) -> int:
    """Download the model and print its local path.

    :param argv: command-line arguments, defaults to ``sys.argv[1:]``
    :return: process exit code
    """
    from app.ai.llama_detector import LlamaCppDetector
    from app.config import Settings

    settings: Settings = Settings()
    settings.validate_security()
    detector: LlamaCppDetector = LlamaCppDetector(settings, logger=_ConsoleLogger())
    try:
        path: str = detector.download_model()
    except (FileNotFoundError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        print(
            "Manual download instructions:\n"
            "  Primary: https://huggingface.co/bartowski/Qwen_Qwen3.5-9B-GGUF\n"
            "  Fallback: https://huggingface.co/lmstudio-community/Qwen3.5-9B-GGUF\n"
            "  Mirror: https://hf-mirror.com\n"
            "Place the .gguf file in the configured MODEL_DIR.",
            file=sys.stderr,
        )
        return 1
    print(f"Model ready at: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
