"""Manual, idempotent seeding of first-run moderation data.

Run explicitly with ``npm run seed`` (or ``python seed.py`` in ``backend/``).
It is intentionally NOT invoked at startup: the seed only fills data that is
missing and never overwrites operator edits, so running it repeatedly is safe.

Seeds three things:
1. The critical-phrases table from ``data/seed/critical_phrases.json``.
2. The semantic example indexes (only when the semantic stage is installed and
   a category index is empty).
3. A minimal safe-word starter list (only when the list file is empty).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

load_dotenv()

from app.config import Settings  # noqa: E402
from app.fastpath.safe_word_filter import SafeWordFilter  # noqa: E402
from app.phrases.manager import CriticalPhraseManager  # noqa: E402
from app.semantic.semantic_service import CATEGORIES, SemanticService  # noqa: E402
from app.utils.logger import ModerationLogger  # noqa: E402
from app.utils.unicode_utils import UnicodeUtils  # noqa: E402

_SEED_PATH = Path(__file__).parent / "seed_data" / "critical_phrases.json"
_SAFE_WORDS = ("hello", "thanks", "thank", "please", "yes", "no", "ok", "good", "morning", "nice")


def _seed_phrases(manager: CriticalPhraseManager) -> int:
    """Insert seed phrases that are not already present.

    :param manager: the critical phrase manager
    :return: the number of phrases added
    """
    if not _SEED_PATH.is_file():
        print(f"seed: no critical-phrases seed file at {_SEED_PATH}")
        return 0
    payload: dict[str, Any] = json.loads(_SEED_PATH.read_text(encoding="utf-8"))
    existing: set[str] = {item.phrase for item in manager.list_all()}
    added: int = 0
    for entry in payload.get("phrases", []):
        phrase: str = UnicodeUtils.prepare(str(entry["phrase"])).lower()
        if phrase in existing:
            continue
        manager.add(
            phrase=phrase,
            category=str(entry["category"]),
            severity=int(entry["severity"]),
            language=str(entry.get("language", "any")),
        )
        added += 1
    return added


def _seed_semantic(semantic: SemanticService) -> int:
    """Persist the default example texts into empty category indexes.

    :param semantic: the semantic service
    :return: the number of categories seeded
    """
    if not semantic.is_available():
        print("seed: semantic stage unavailable (optional dependencies not installed)")
        return 0
    seeded: int = 0
    stats: dict[str, Any] = semantic.stats()
    for category in CATEGORIES:
        current: int = int(stats.get("categories", {}).get(category, 0) or 0)
        if current > 0:
            continue
        from app.semantic.semantic_service import _DEFAULT_EXAMPLES

        for example in _DEFAULT_EXAMPLES.get(category, []):
            semantic.add(category, example)
        seeded += 1
    return seeded


def _seed_safe_words(safe_word: SafeWordFilter) -> int:
    """Write the starter safe-word list only when the list is empty.

    :param safe_word: the safe word filter
    :return: the number of words written
    """
    if safe_word.words():
        return 0
    added: int = 0
    for word in _SAFE_WORDS:
        if safe_word.add_word(word):
            added += 1
    return added


def main() -> int:
    """Run the seed and report what was added."""
    settings: Settings = Settings()
    logger: ModerationLogger = ModerationLogger(
        settings.log_file_path, level="INFO", max_bytes=settings.log_max_bytes
    )
    phrases: CriticalPhraseManager = CriticalPhraseManager(settings.critical_phrases_db_path)
    safe_word: SafeWordFilter = SafeWordFilter(settings, logger)
    semantic: SemanticService = SemanticService(settings, logger)

    phrases_added: int = _seed_phrases(phrases)
    semantic_seeded: int = _seed_semantic(semantic)
    safe_added: int = _seed_safe_words(safe_word)

    print(f"seed: added {phrases_added} critical phrase(s)")
    print(f"seed: seeded {semantic_seeded} semantic category/categories")
    print(f"seed: added {safe_added} safe word(s)")

    phrases.close()
    safe_word.reload()
    semantic.close() if hasattr(semantic, "close") else None
    logger.close()
    print("seed: complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
