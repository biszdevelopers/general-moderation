"""Semantic similarity detection with SentenceTransformers and Faiss.

One Faiss index is kept per category (political, violence, sexual, hate, pii,
ads, other). Vectors are L2-normalized so the inner product of ``IndexFlatIP``
equals the cosine similarity used by the scoring formula. Indexes and their
source texts are persisted under ``SEMANTIC_INDEX_DIR``.

The heavy dependencies (``torch``, ``sentence-transformers``, ``faiss-cpu``)
are optional: when they are not installed the service reports itself
unavailable and the engine simply skips the semantic stage.
"""

from __future__ import annotations

import json
import logging
import threading
from pathlib import Path
from typing import Any

_LOGGER: logging.Logger = logging.getLogger(__name__)

CATEGORIES: tuple[str, ...] = ("political", "violence", "sexual", "hate", "pii", "ads", "other")

# Default example texts used to seed a fresh category index. They are a
# minimal curated starter set (English) that operators should extend through
# the admin API; they are kept generic and do not reproduce real-world
# sensitive strings.
_DEFAULT_EXAMPLES: dict[str, list[str]] = {
    "political": [
        "The government is corrupt",
        "Election fraud everywhere",
        "Overthrow the current regime",
        "The president must be removed from office",
        "The system is rigged against the people",
        "Leaders are lying to the nation",
        "Destroy the established order",
        "The ruling party is illegitimate",
        "Foreign powers control our government",
        "The constitution has been betrayed",
    ],
    "violence": [
        "I will kill you",
        "Bomb the building",
        "I am going to shoot them",
        "Stab them tonight",
        "Cut off their heads",
        "Blow up the station",
        "I will make you suffer",
        "Attack the school",
        "Burn the house down",
        "I have a weapon and I will use it",
    ],
    "sexual": [
        "Explicit sexual content",
        "Send nudes now",
        "Show me your genitals",
        "I want to have sex with you",
        "Sexual assault that night",
        "Explicit pornographic description",
        "Graphic sex scene details",
        "Underage sexual content",
        "Sexual violence against them",
        "X-rated material request",
    ],
    "hate": [
        "I hate all people from that country",
        "Racial slurs against them",
        "They are all subhuman",
        "Kill every member of that group",
        "That ethnicity should be wiped out",
        "They deserve to be exterminated",
        "Disgusting race, get out",
        "No religion should exist here",
        "They are animals not people",
        "Burn their homes and drive them out",
    ],
    "pii": [
        "My social security number is",
        "Here is my credit card number",
        "Send your passport details",
        "My home address is",
        "Bank account and routing number",
        "Date of birth and full name",
        "Driver's license number",
        "My phone number is",
        "Email and password for my account",
        "Health record details here",
    ],
    "ads": [
        "Buy this product now",
        "Limited time offer discount",
        "Click here to claim your prize",
        "Free gift for new members",
        "Lowest prices guaranteed",
        "Win a free vacation today",
        "Subscribe to our channel",
        "Order now before it sells out",
        "Cheap deals on everything",
        "Your chance to earn fast cash",
    ],
    "other": [],
}


class SemanticService:
    """Encodes text and searches per-category Faiss indexes.

    :param settings: application settings
    :param logger: audit logger
    """

    def __init__(self, settings: Any, logger: Any) -> None:
        self._enabled: bool = bool(settings.semantic_enabled)
        self._model_name: str = settings.semantic_model
        self._index_dir: Path = Path(settings.semantic_index_dir)
        if settings.semantic_index_dir.startswith("."):
            self._index_dir = Path.cwd() / self._index_dir
        self._threshold: float = float(settings.semantic_similarity_threshold)
        self._force_threshold: float = float(settings.semantic_force_llm_threshold)
        self._top_k: int = int(settings.semantic_top_k)
        self._logger: Any = logger
        self._lock: threading.Lock = threading.Lock()
        self._model: Any = None
        self._faiss: Any = None
        self._indexes: dict[str, Any] = {}
        self._texts: dict[str, list[str]] = {category: [] for category in CATEGORIES}
        self._available: bool = False
        self._ready: bool = False
        try:
            import faiss
            import sentence_transformers  # noqa: F401

            self._faiss = faiss
            self._available = True
        except ImportError:
            _LOGGER.warning(
                "Semantic similarity disabled: install the optional "
                "'semantic' dependencies (torch, sentence-transformers, faiss-cpu)."
            )

    def is_available(self) -> bool:
        """Return whether the optional dependencies are installed."""
        return self._available and self._enabled

    def _load(self) -> None:
        """Load the transformer model and every persisted index."""
        if self._ready:
            return
        from sentence_transformers import SentenceTransformer

        self._model = SentenceTransformer(self._model_name)
        self._index_dir.mkdir(parents=True, exist_ok=True)
        for category in CATEGORIES:
            index_path: Path = self._index_dir / f"{category}.index"
            texts_path: Path = self._index_dir / f"{category}.json"
            if index_path.exists() and texts_path.exists():
                self._indexes[category] = self._faiss.read_index(str(index_path))
                self._texts[category] = json.loads(texts_path.read_text(encoding="utf-8"))
            else:
                self._indexes[category] = self._faiss.IndexFlatIP(384)
                self._texts[category] = list(_DEFAULT_EXAMPLES.get(category, []))
                if self._texts[category]:
                    self._reindex(category)
        self._ready = True

    def _embed(self, texts: list[str]) -> Any:
        """Encode and L2-normalize a list of texts."""
        vectors = self._model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
        return self._faiss.normalize_L2(vectors)

    def _reindex(self, category: str) -> None:
        """Rebuild one category index from its stored texts."""
        texts: list[str] = self._texts[category]
        index = self._faiss.IndexFlatIP(384)
        if texts:
            index.add(self._embed(texts))
        self._indexes[category] = index

    def query(self, text: str) -> dict[str, float]:
        """Return the maximum similarity per category for a text.

        :param text: input text
        :return: category to similarity mapping, empty when unavailable
        """
        if not self.is_available():
            return {}
        with self._lock:
            self._load()
        vector = self._faiss.normalize_L2(self._embed([text]))
        results: dict[str, float] = {}
        for category in CATEGORIES:
            index = self._indexes[category]
            if index.ntotal == 0:
                results[category] = 0.0
                continue
            scores, _ = index.search(vector, min(self._top_k, index.ntotal))
            results[category] = float(scores[0][0]) if len(scores[0]) else 0.0
        return results

    def add(self, category: str, text: str) -> None:
        """Append an example to a category index and persist it.

        :param category: one of the semantic categories
        :param text: sensitive example text
        :raises ValueError: for an unknown category
        """
        if category not in CATEGORIES:
            raise ValueError(f"Unknown category: {category}")
        if not text.strip():
            raise ValueError("Text must not be empty")
        with self._lock:
            self._load()
            self._texts[category].append(text.strip())
            self._reindex(category)
            self._persist(category)

    def delete(self, category: str, text: str) -> bool:
        """Remove one example from a category index.

        :param category: one of the semantic categories
        :param text: the example to remove
        :return: True when the example was removed
        :raises ValueError: for an unknown category
        """
        if category not in CATEGORIES:
            raise ValueError(f"Unknown category: {category}")
        with self._lock:
            self._load()
            texts: list[str] = self._texts[category]
            if text not in texts:
                return False
            texts.remove(text)
            self._reindex(category)
            self._persist(category)
            return True

    def _persist(self, category: str) -> None:
        """Write a category index and its texts to disk."""
        self._faiss.write_index(self._indexes[category], str(self._index_dir / f"{category}.index"))
        (self._index_dir / f"{category}.json").write_text(
            json.dumps(self._texts[category], ensure_ascii=False), encoding="utf-8"
        )

    def stats(self) -> dict[str, Any]:
        """Return per-category entry counts."""
        if not self._ready:
            return {"available": self.is_available(), "categories": {}}
        return {
            "available": self.is_available(),
            "model": self._model_name,
            "categories": {category: len(self._texts[category]) for category in CATEGORIES},
        }
