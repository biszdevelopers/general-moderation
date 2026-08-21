"""Headless load-test runner for the moderation pipeline.

Builds an isolated engine (like the eval harness) and runs the same load-test
simulation as ``/test/load-test``, printing the aggregated result as JSON so
operators can script throughput checks:

    uv run python -m tools.load_test_cli --users 20 --requests 50
    uv run python -m tools.load_test_cli --users 5 --requests 10 --json
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
import tempfile
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_ROOT))

from app.config import Settings  # noqa: E402
from app.engine.moderation_engine import ModerationEngine  # noqa: E402
from app.settings_service import SettingsService  # noqa: E402
from app.test.load_test import LoadTestConfig, run_load_test  # noqa: E402
from app.utils.logger import ModerationLogger  # noqa: E402
from app.wordbank.manager import WordBankManager  # noqa: E402
from app.wordbank.storage import create_storage  # noqa: E402


def _build_engine() -> tuple[ModerationEngine, WordBankManager, ModerationLogger]:
    """Construct an isolated engine with clean temporary storage."""
    tmp: Path = Path(tempfile.mkdtemp(prefix="loadtest-"))
    settings: Settings = Settings(
        critical_phrases_db_path=str(tmp / "critical_phrases.db"),
        log_file_path=str(tmp / "loadtest.log"),
        sensitive_stop_words_dir=str(_ROOT / "data" / "sensitive-stop-words"),
        sensitive_word_data_dict=str(
            _ROOT / "data" / "sensitive-word-data" / "src" / "main" / "resources" / "sensitive_word_dict.txt"
        ),
        sensitive_lexicon_dir=str(_ROOT / "data" / "sensitive-lexicon" / "Vocabulary"),
        sensitive_dict_path=str(_ROOT / "data" / "sensitive" / "dict" / "dict.txt"),
        auto_tuning_enabled=False,
    )
    settings_service: SettingsService = SettingsService(settings)
    settings_service.all()
    logger: ModerationLogger = ModerationLogger(str(tmp / "loadtest.log"), level="WARNING")
    word_bank: WordBankManager = WordBankManager(
        storage=create_storage("sqlite", str(tmp / "words.db")),
        bloom_capacity=settings.bloom_filter_capacity,
        bloom_error_rate=settings.bloom_filter_error_rate,
        logger=logger,
    )
    engine: ModerationEngine = ModerationEngine(settings, word_bank, logger, settings_service=settings_service)
    return engine, word_bank, logger


async def _run(engine: ModerationEngine, config: LoadTestConfig) -> dict[str, object]:
    """Run the load test and return the final result payload."""
    result: dict[str, object] = {}
    async for _name, payload in run_load_test(engine, config):
        if isinstance(payload, dict) and "requests_per_second" in payload:
            result = payload
    return result


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    :param argv: CLI arguments
    :return: exit code (0 ok, 1 error)
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--users", type=int, default=10)
    parser.add_argument("--requests", type=int, default=10)
    parser.add_argument("--json", action="store_true", help="emit a single JSON result")
    args: argparse.Namespace = parser.parse_args(argv)

    config: LoadTestConfig = LoadTestConfig(
        concurrent_users=args.users, requests_per_user=args.requests
    )
    engine, word_bank, logger = _build_engine()
    try:
        result: dict[str, object] = asyncio.run(_run(engine, config))
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print("=" * 50)
            print(f"Requests:    {result.get('total_requests')} "
                  f"({result.get('successful_requests')} ok, "
                  f"{result.get('failed_requests')} failed)")
            print(f"Throughput:  {result.get('requests_per_second')} req/s")
            print(f"Latency p50  {result.get('latency_percentiles', {}).get('p50')} ms")
            print(f"Latency p95  {result.get('latency_percentiles', {}).get('p95')} ms")
            print(f"Latency p99  {result.get('latency_percentiles', {}).get('p99')} ms")
            print(f"LLM calls:   {result.get('llm_invocation_count')}")
            print(f"Verdicts:    {result.get('verdicts')}")
            print("=" * 50)
        return 0
    finally:
        word_bank.close()
        logger.close()


if __name__ == "__main__":
    if sys.stdout and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    sys.exit(main())
