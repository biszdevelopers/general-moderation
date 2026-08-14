"""Labeled evaluation corpus builder.

Builds a deterministic, labeled dataset used to measure precision, recall,
and F1 of the moderation pipeline:

- **Positives** — seed critical phrases (violence/hate/political/sexual) plus
  a sampled subset of the Chinese sensitive-word lists. The raw list files are
  sensitive, so the Chinese positives are sampled programmatically at runtime
  (seeded RNG, never printed) instead of being committed as literal words.
- **Negatives** — benign English and Chinese sentences, including common-word
  overlap and near-miss cases that historically produced false positives.
- **Reviews** — weak/probabilistic hits expected to land in REVIEW.

The corpus is rebuilt identically on every run (fixed RNG seed) so eval
results are comparable across changes.
"""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any

from app.utils.sensitive_word_loader import SensitiveWordLoader

_ROOT = Path(__file__).resolve().parents[2]
_DATA = _ROOT / "backend" / "data"
_SEED_JSON = _ROOT / "backend" / "seed_data" / "critical_phrases.json"

_RNG_SEED = 20260814
_CJK_POSITIVE_SAMPLE = 40
_CJK_NEGATIVE_SAMPLE = 25

# Benign English sentences, including the classic false-positive cases.
_BENIGN_EN = [
    "hello world",
    "this is a completely normal message",
    "how was your day today",
    "the weather is nice outside",
    "can you pass the glass please",
    "class president, pass the glass",
    "i am going to the park with my friends",
    "the assassination museum was interesting to visit",
    "please read this article about history",
    "congratulations on your new job",
    "the committee will meet on friday",
    "she plays the piano beautifully",
    "we are having pasta for dinner",
    "my favorite color is blue",
    "the meeting is at three o clock",
    "thanks for your help yesterday",
    "the project deadline is next monday",
    "i recommend the new restaurant downtown",
    "everyone should exercise regularly",
    "the library opens at nine",
    "please send me the document",
    "the train arrives at ten thirty",
    "i bought some apples at the market",
    "the kids are playing in the garden",
    "it is a beautiful sunny day",
]

# Benign Chinese sentences. These must not contain any sensitive term from the
# wired lists; common characters are checked at eval time.
_BENIGN_ZH = [
    "今天天气很好",
    "你好，很高兴认识你",  # noqa: RUF001 - intentional fullwidth comma in sample text
    "这个项目下周就要完成了",
    "我们一起去公园散步吧",
    "这家餐厅的菜很好吃",
    "祝你生日快乐",
    "会议安排在下午三点",
    "请把文件发给我",
    "我喜欢读书和听音乐",
    "孩子们在花园里玩耍",
    "明天早上九点开始",
    "这个城市的夜景很美",
    "感谢你的帮助",
    "图书馆上午开门",
    "周末我们去爬山",
    "这份报告需要修改一下",
    "火车站离这里不远",
    "妈妈做的菜最香",
    "学习需要持之以恒",
    "春天来了花开了",
]

# Near-miss / obfuscation cases that should still be caught.
_ATTACK_EN = [
    "k1ll y0urs3lf now",
    "i w1ll k1ll you",
    "i will k1ll you ton1ght",
    "k i l l yourself",
    "bomb the school building",
    "i w1ll r4pe y0u",
    "k1ll every 0ne 0f them",
    "i am g01ng to k1ll you",
    "b0mb th3 sch00l",
    "s3nd m3 ph0t0s 0f ch1ldr3n",
]

# Weak-signal cases that are genuinely benign and should reach PASS (they must
# NOT hard-block).
_REVIEW_EN = [
    "that was a really bad idea",
    "this situation is completely messed up",
]

# Benign multilingual sentences (no sensitive content).
_BENIGN_MULTI = [
    ("bonjour comment ca va", "fr"),
    ("je vais au marche acheter des fruits", "fr"),
    ("guten morgen wie geht es dir", "de"),
    ("das wetter ist heute sehr schon", "de"),
    ("buenos dias que tal estas", "es"),
    ("vamos al parque a pasear", "es"),
    ("buongiorno come stai", "it"),
    ("oggi e una bella giornata", "it"),
    ("bom dia como voce esta", "pt"),
    ("vamos ao cinema hoje", "pt"),
    ("доброе утро как дела", "ru"),
    ("сегодня хорошая погода", "ru"),
    ("おはようございます", "ja"),
    ("今日はいい天気ですね", "ja"),
    ("좋은 아침이에요", "ko"),
    ("오늘 날씨가 좋네요", "ko"),
    ("صباح الخير كيف حالك", "ar"),
    ("الطقس جميل اليوم", "ar"),
    ("merhaba nasilsin", "tr"),
    ("bugun hava cok guzel", "tr"),
]


class EvalCase:
    """One labeled moderation sample.

    :param text: the message to moderate
    :param expected: ``"block"``, ``"pass"``, or ``"review"``
    :param category: optional semantic category for grouping
    :param language: optional language tag for grouping
    :param note: optional provenance note
    :param redact: when True the report hides this text (sampled sensitive terms)
    """

    __slots__ = ("category", "expected", "language", "note", "redact", "text")

    def __init__(
        self,
        text: str,
        expected: str,
        category: str = "other",
        language: str = "en",
        note: str = "",
        redact: bool = False,
    ) -> None:
        self.text = text
        self.expected = expected
        self.category = category
        self.language = language
        self.note = note
        self.redact = redact

    def display_text(self) -> str:
        """Return a redacted text for reports."""
        return "[redacted]" if self.redact else self.text

    def to_dict(self) -> dict[str, Any]:
        """Serialize the case for JSON reports (sensitive text redacted)."""
        return {
            "text": self.display_text(),
            "expected": self.expected,
            "category": self.category,
            "language": self.language,
            "note": self.note,
        }


def _seed_phrase_cases() -> list[EvalCase]:
    """Build labeled positives from the seed critical phrases."""
    cases: list[EvalCase] = []
    data: dict[str, Any] = json.loads(_SEED_JSON.read_text(encoding="utf-8"))
    for phrase in data.get("phrases", []):
        text: str = phrase.get("phrase", "")
        if not text:
            continue
        cases.append(
            EvalCase(
                text=text,
                expected="block",
                category=phrase.get("category", "other"),
                language=phrase.get("language", "en"),
                note="seed phrase",
            )
        )
    return cases


def _cjk_positive_cases() -> list[EvalCase]:
    """Sample a deterministic subset of the Chinese sensitive lists.

    Each sampled term is embedded into a carrier sentence so the match actually
    exercises the detector; the term is never printed (``redact=True``).
    """
    loader: SensitiveWordLoader = SensitiveWordLoader(
        _DATA / "sensitive-stop-words",
        extra_files=(
            _DATA
            / "sensitive-word-data"
            / "src"
            / "main"
            / "resources"
            / "sensitive_word_dict.txt",
            _DATA / "sensitive" / "dict" / "dict.txt",
        ),
        extra_dirs=(_DATA / "sensitive-lexicon" / "Vocabulary",),
    )
    words: tuple[str, ...] = loader.blocking_words()
    if not words:
        return []
    rng: random.Random = random.Random(_RNG_SEED)
    picked: list[str] = rng.sample(list(words), min(_CJK_POSITIVE_SAMPLE, len(words)))
    return [
        EvalCase(
            text=f"这段内容包含敏感信息，请注意核对。{term}",  # noqa: RUF001 - intentional CJK punctuation
            expected="block",
            category="sensitive",
            language="zh-CN",
            note="sampled CJK term",
            redact=True,
        )
        for term in picked
    ]


def build_corpus(include_cjk: bool = True) -> list[EvalCase]:
    """Return the full labeled evaluation corpus.

    :param include_cjk: when False, skip sampling the Chinese lists (used when
        the subrepos are not initialized or for fast local runs)
    :return: the ordered list of evaluation cases
    """
    cases: list[EvalCase] = _seed_phrase_cases()
    if include_cjk:
        cases.extend(_cjk_positive_cases())
    cases.extend(
        EvalCase(text=text, expected="pass", category="benign", language="en", note="benign")
        for text in _BENIGN_EN
    )
    cases.extend(
        EvalCase(text=text, expected="pass", category="benign", language="zh-CN", note="benign")
        for text in _BENIGN_ZH
    )
    cases.extend(
        EvalCase(text=text, expected="block", category="attack", language="en", note="obfuscation")
        for text in _ATTACK_EN
    )
    cases.extend(
        EvalCase(text=text, expected="review", category="weak", language="en", note="weak signal")
        for text in _REVIEW_EN
    )
    cases.extend(
        EvalCase(
            text=text,
            expected="pass",
            category="benign",
            language=language,
            note="benign multilingual",
        )
        for text, language in _BENIGN_MULTI
    )
    return cases
