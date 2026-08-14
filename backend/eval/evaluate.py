"""Evaluation harness for the moderation pipeline.

Measures precision, recall, and F1 over the labeled corpus. Used both as a
regression gate (``npm run eval``) and as the demo-readiness proof: it runs
the real pipeline over labeled benign/sensitive samples and fails (nonzero
exit) when accuracy drops below the configured thresholds.

Never prints sensitive sample text: every sampled CJK term is redacted in the
report.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
import tempfile
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "backend"))

_SEED_JSON = _ROOT / "backend" / "seed_data" / "critical_phrases.json"

from app.config import Settings  # noqa: E402
from app.engine.moderation_engine import ModerationEngine  # noqa: E402
from app.models.request import ModerationRequest  # noqa: E402
from app.settings_service import SettingsService  # noqa: E402
from app.utils.logger import ModerationLogger  # noqa: E402
from app.wordbank.manager import WordBankManager  # noqa: E402
from app.wordbank.storage import create_storage  # noqa: E402
from eval.corpus import EvalCase, build_corpus  # noqa: E402

_DEFAULTS = {
    "min_accuracy": 0.95,
    "min_precision": 0.90,
    "min_recall": 0.90,
    "min_f1": 0.90,
}


def _build_engine() -> tuple[ModerationEngine, WordBankManager, ModerationLogger]:
    """Construct an isolated engine wired to the real word lists.

    The critical-phrase table is seeded from ``seed_data/critical_phrases.json``
    into an isolated database so phrase detection is exercised with the same
    labeled positives the corpus uses.
    """
    tmp: Path = Path(tempfile.mkdtemp(prefix="eval-"))
    base: Path = _ROOT / "backend" / "data"
    phrases_db: Path = tmp / "critical_phrases.db"
    _seed_phrases(phrases_db)
    settings: Settings = Settings(
        sensitive_stop_words_dir=str(base / "sensitive-stop-words"),
        sensitive_word_data_dict=str(
            base / "sensitive-word-data" / "src" / "main" / "resources" / "sensitive_word_dict.txt"
        ),
        sensitive_lexicon_dir=str(base / "sensitive-lexicon" / "Vocabulary"),
        sensitive_dict_path=str(base / "sensitive" / "dict" / "dict.txt"),
        critical_phrases_db_path=str(phrases_db),
        log_file_path=str(tmp / "eval.log"),
    )
    settings_service: SettingsService = SettingsService(settings)
    settings_service.all()
    logger: ModerationLogger = ModerationLogger(
        str(tmp / "eval.log"), level="INFO", max_bytes=1_000_000
    )
    word_bank: WordBankManager = WordBankManager(
        storage=create_storage("sqlite", str(tmp / "words.db")),
        bloom_capacity=settings.bloom_filter_capacity,
        bloom_error_rate=settings.bloom_filter_error_rate,
        logger=logger,
    )
    engine: ModerationEngine = ModerationEngine(
        settings, word_bank, logger, settings_service=settings_service
    )
    return engine, word_bank, logger


def _seed_phrases(db_path: Path) -> None:
    """Insert the seed critical phrases into a fresh phrases database."""
    from app.phrases.manager import CriticalPhraseManager

    data: dict[str, Any] = json.loads(_SEED_JSON.read_text(encoding="utf-8"))
    manager: CriticalPhraseManager = CriticalPhraseManager(str(db_path))
    try:
        for phrase in data.get("phrases", []):
            manager.add(
                phrase=phrase["phrase"],
                language=phrase.get("language", "any"),
                category=phrase.get("category", "other"),
                severity=int(phrase.get("severity", 5)),
            )
    finally:
        manager.close()


def _verdict_group(verdict: str) -> str:
    """Map a verdict to the binary bucket used for metrics."""
    return "block" if verdict == "BLOCK" else "pass"


def _case_ok(case: EvalCase, verdict: str) -> bool:
    """Whether a verdict satisfies the case label.

    ``review`` expectations accept either REVIEW or PASS (the content must not
    hard-block); ``block`` requires BLOCK; ``pass`` requires PASS.
    """
    if case.expected == "review":
        return verdict in ("REVIEW", "PASS")
    actual: str = _verdict_group(verdict)
    return actual == case.expected


def _metrics(bucket: list[dict[str, Any]]) -> dict[str, float]:
    """Compute precision/recall/F1 from a list of outcome dicts.

    Accuracy uses the ``ok`` flag (which honors review-expected cases); the
    2x2 table is derived only from binary block/pass labels.

    :param bucket: outcomes with ``expected`` and ``actual`` binary labels
    :return: accuracy, precision, recall, f1
    """
    if not bucket:
        return {"accuracy": 0.0, "precision": 0.0, "recall": 0.0, "f1": 0.0}
    binary: list[dict[str, Any]] = [
        outcome for outcome in bucket if outcome["expected"] in ("block", "pass")
    ]
    accuracy: float = sum(1 for o in bucket if o["ok"]) / len(bucket)
    if not binary:
        return {
            "accuracy": round(accuracy, 4),
            "precision": 0.0,
            "recall": 0.0,
            "f1": 0.0,
        }
    tp: int = sum(1 for o in binary if o["expected"] == "block" and o["actual"] == "block")
    fp: int = sum(1 for o in binary if o["expected"] == "pass" and o["actual"] == "block")
    fn: int = sum(1 for o in binary if o["expected"] == "block" and o["actual"] == "pass")
    precision: float = tp / (tp + fp) if (tp + fp) else 0.0
    recall: float = tp / (tp + fn) if (tp + fn) else 0.0
    f1: float = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return {
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
    }


def run(include_cjk: bool = True) -> dict[str, Any]:
    """Run the corpus through the engine and return the full report.

    :param include_cjk: whether to include the sampled Chinese positives
    :return: a serializable report dict
    """
    engine, word_bank, logger = _build_engine()
    outcomes: list[dict[str, Any]] = []
    latencies: list[float] = []
    verdict_counts: Counter[str] = Counter()
    by_category: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_language: dict[str, list[dict[str, Any]]] = defaultdict(list)

    try:
        for case in build_corpus(include_cjk=include_cjk):
            start: float = time.perf_counter()
            response = engine.moderate(
                ModerationRequest(text=case.text, user_id="eval", app_name="eval")
            )
            elapsed_ms: float = (time.perf_counter() - start) * 1000.0
            latencies.append(elapsed_ms)
            verdict_counts[response.verdict] += 1
            outcome: dict[str, Any] = {
                "text": case.display_text(),
                "expected": case.expected,
                "actual": _verdict_group(response.verdict),
                "verdict": response.verdict,
                "category": case.category,
                "language": case.language,
                "ok": _case_ok(case, response.verdict),
                "latency_ms": round(elapsed_ms, 3),
            }
            outcomes.append(outcome)
            by_category[case.category].append(outcome)
            by_language[case.language].append(outcome)
    finally:
        word_bank.close()
        logger.close()

    overall: dict[str, float] = _metrics(outcomes)
    report: dict[str, Any] = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_cases": len(outcomes),
        "verdict_distribution": dict(verdict_counts),
        "overall": overall,
        "latency_ms": {
            "mean": round(statistics.mean(latencies), 3) if latencies else 0.0,
            "p50": round(statistics.median(latencies), 3) if latencies else 0.0,
            "p95": round(sorted(latencies)[int(len(latencies) * 0.95) - 1], 3)
            if len(latencies) >= 20
            else (sorted(latencies)[-1] if latencies else 0.0),
            "p99": round(sorted(latencies)[int(len(latencies) * 0.99) - 1], 3)
            if len(latencies) >= 100
            else (sorted(latencies)[-1] if latencies else 0.0),
        },
        "by_category": {
            cat: {"count": len(rows), "metrics": _metrics(rows)}
            for cat, rows in sorted(by_category.items())
        },
        "by_language": {
            lang: {"count": len(rows), "metrics": _metrics(rows)}
            for lang, rows in sorted(by_language.items())
        },
        "failures": [o for o in outcomes if not o["ok"]],
    }
    return report


def _print_report(report: dict[str, Any]) -> None:
    """Print a compact human-readable report."""
    print("=" * 60)
    print("MODERATION EVALUATION")
    print("=" * 60)
    print(f"Cases: {report['total_cases']}")
    print(f"Verdicts: {report['verdict_distribution']}")
    print(
        "Overall: "
        f"acc={report['overall']['accuracy']:.3f} "
        f"prec={report['overall']['precision']:.3f} "
        f"rec={report['overall']['recall']:.3f} "
        f"f1={report['overall']['f1']:.3f}"
    )
    lat: dict[str, float] = report["latency_ms"]
    print(
        "Latency (ms): "
        f"mean={lat['mean']:.2f} p50={lat['p50']:.2f} "
        f"p95={lat['p95']:.2f} p99={lat['p99']:.2f}"
    )
    print("\nBy category:")
    for cat, info in sorted(report["by_category"].items()):
        m: dict[str, float] = info["metrics"]
        print(
            f"  {cat:12s} n={info['count']:3d} "
            f"acc={m['accuracy']:.3f} prec={m['precision']:.3f} rec={m['recall']:.3f} "
            f"f1={m['f1']:.3f}"
        )
    failures: list[dict[str, Any]] = report["failures"]
    if failures:
        print(f"\nFailures ({len(failures)}):")
        for fail in failures:
            print(
                f"  [{fail['expected']:>6s} != {fail['actual']:>5s}] "
                f"({fail['language']}) {fail['text']!r}"
            )
    print("=" * 60)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point with regression thresholds.

    :param argv: CLI arguments
    :return: exit code (0 pass, 1 regression, 2 error)
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="emit a JSON report")
    parser.add_argument("--no-cjk", action="store_true", help="skip sampled CJK positives")
    parser.add_argument("--min-accuracy", type=float, default=_DEFAULTS["min_accuracy"])
    parser.add_argument("--min-precision", type=float, default=_DEFAULTS["min_precision"])
    parser.add_argument("--min-recall", type=float, default=_DEFAULTS["min_recall"])
    parser.add_argument("--min-f1", type=float, default=_DEFAULTS["min_f1"])
    args: argparse.Namespace = parser.parse_args(argv)

    report: dict[str, Any] = run(include_cjk=not args.no_cjk)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2, default=str))
        return 0
    _print_report(report)

    overall: dict[str, float] = report["overall"]
    checks: list[tuple[str, float, float]] = [
        ("accuracy", overall["accuracy"], args.min_accuracy),
        ("precision", overall["precision"], args.min_precision),
        ("recall", overall["recall"], args.min_recall),
        ("f1", overall["f1"], args.min_f1),
    ]
    failed: list[str] = [name for name, value, minimum in checks if value < minimum]
    if failed:
        print(f"REGRESSION: below minimums -> {', '.join(failed)}")
        return 1
    print("OK: all metrics meet the configured minimums.")
    return 0


if __name__ == "__main__":
    if sys.stdout and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    sys.exit(main())
