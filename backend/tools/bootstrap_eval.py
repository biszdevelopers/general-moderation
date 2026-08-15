"""Bootstrap eval cases from production audit decisions.

Reads the JSONL audit log (``moderation_decision`` records), deduplicates by
text hash, and emits a labeled eval-corpus file that operators can review and
grow. The log deliberately stores only a 50-character text preview plus a
SHA-256 hash, so the generated cases inherit that built-in redaction: the
full message text never reaches the corpus.

Usage:
    uv run python -m tools.bootstrap_eval --log ./logs/moderation.log --out ./eval/generated/live.json
    uv run python -m tools.bootstrap_eval --limit 200
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

_ROOT = Path(__file__).resolve().parents[1]


def _verdict_to_expected(verdict: str, severity: int) -> str:
    """Map a stored verdict to the binary eval label.

    REVIEW verdicts never hard-blocked, so they behave like pass for the
    corpus's block/pass table; the original verdict is kept in the note.
    """
    if verdict == "BLOCK":
        return "block"
    return "pass"


def _load_decisions(log_path: Path) -> list[dict[str, Any]]:
    """Parse ``moderation_decision`` records from a JSONL audit log."""
    if not log_path.is_file():
        return []
    decisions: list[dict[str, Any]] = []
    for line in log_path.read_text(encoding="utf-8").splitlines():
        try:
            record: dict[str, Any] = json.loads(line)
        except json.JSONDecodeError:
            continue
        if record.get("message") != "moderation_decision":
            continue
        text_hash: str = str(record.get("textHash", ""))
        if not text_hash:
            continue
        decisions.append(record)
    return decisions


def _redact(case: dict[str, Any], record: dict[str, Any]) -> dict[str, Any]:
    """Apply built-in log redaction and mark sensitive cases.

    The audit log already truncates the message to a 50-character preview, so
    the emitted case text is that preview. Cases that triggered a match are
    flagged so operators review them before committing to the corpus.
    """
    severity: int = int(record.get("severity") or 0)
    matched: bool = bool(record.get("matchedWord"))
    case["redact"] = matched or severity >= 5
    case["note"] = (
        f"bootstrap from production log {datetime.now(UTC).strftime('%Y-%m-%d')}"
        + ("; original verdict " + str(record.get("verdict")) if matched else "")
    )
    return case


def bootstrap(
    log_path: Path,
    *,
    limit: int = 200,
    min_severity: int = 0,
) -> list[dict[str, Any]]:
    """Convert production audit decisions into labeled eval cases.

    :param log_path: path to the JSONL audit log
    :param limit: maximum number of cases to emit (most recent first)
    :param min_severity: only keep decisions at or above this severity
    :return: the serializable eval-corpus cases
    """
    decisions: list[dict[str, Any]] = _load_decisions(log_path)
    seen: set[str] = set()
    cases: list[dict[str, Any]] = []
    for record in reversed(decisions):
        text_hash: str = str(record.get("textHash", ""))
        severity: int = int(record.get("severity") or 0)
        if severity < min_severity:
            continue
        if text_hash in seen:
            continue
        seen.add(text_hash)
        case: dict[str, Any] = {
            "text": str(record.get("textPreview") or ""),
            "expected": _verdict_to_expected(str(record.get("verdict")), severity),
            "category": str(record.get("category") or "other"),
            "language": str(record.get("matchedLanguage") or "any"),
            "note": "",
        }
        if not case["text"]:
            continue
        cases.append(_redact(case, record))
        if len(cases) >= limit:
            break
    return cases


def _corpus_digest(cases: list[dict[str, Any]]) -> str:
    """Return a short content hash for the generated file."""
    payload: bytes = json.dumps(cases, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()[:12]


def main(argv: list[str] | None = None) -> int:
    """CLI entry point.

    :param argv: CLI arguments
    :return: exit code (0 ok, 1 error)
    """
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", default=str(_ROOT / "logs" / "moderation.log"))
    parser.add_argument("--out", default=str(_ROOT / "eval" / "generated" / "live_corpus.json"))
    parser.add_argument("--limit", type=int, default=200)
    parser.add_argument("--min-severity", type=int, default=0)
    args: argparse.Namespace = parser.parse_args(argv)

    log_path: Path = Path(args.log)
    out_path: Path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    cases: list[dict[str, Any]] = bootstrap(
        log_path, limit=args.limit, min_severity=args.min_severity
    )
    if not cases:
        print(f"No moderation decisions found in {log_path}")
        return 1
    document: dict[str, Any] = {
        "generated_at": datetime.now(UTC).isoformat(),
        "source": str(log_path),
        "count": len(cases),
        "digest": _corpus_digest(cases),
        "cases": cases,
    }
    out_path.write_text(json.dumps(document, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(cases)} bootstrapped cases to {out_path}")
    print(f"  digest={document['digest']}")
    return 0


if __name__ == "__main__":
    if sys.stdout and hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    sys.exit(main())
