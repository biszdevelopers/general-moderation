"""Runtime settings persistence.

Settings are stored in ``settings.db`` and seeded from the ``.env``-backed
``Settings`` object on first use, so the environment file remains the fallback
for initial configuration. Every read goes through a small TTL cache; every
write is validated before it is persisted and the cache is refreshed
immediately so changes apply without a service restart.
"""

from __future__ import annotations

import json
import logging
import sqlite3
import time
from pathlib import Path
from typing import Any

from app.config import Settings

_LOGGER: logging.Logger = logging.getLogger(__name__)

_SECRET_SUFFIXES: tuple[str, ...] = ("_KEY", "_SECRET")

_DESCRIPTIONS: dict[str, str] = {
    "MODEL_CONTEXT_SIZE": "LLM context window size in tokens",
    "MODEL_THREADS": "Number of inference threads (auto = cores - 1)",
    "MODEL_BATCH_SIZE": "LLM prompt batch size",
    "MODEL_MAX_TOKENS": "Maximum tokens in the LLM reply",
    "MODEL_CACHE_TYPE_K": "Key KV cache quantization type",
    "MODEL_CACHE_TYPE_V": "Value KV cache quantization type",
    "MODEL_FLASH_ATTN": "Enable flash attention",
    "MODEL_MLOCK": "Lock model memory to prevent swapping",
    "MODEL_IDLE_TIMEOUT_SECONDS": "Seconds of idle time before the model unloads",
    "SAFE_WORD_LIST_PATH": "Path to the safe word list file",
    "SAFE_WORD_ENABLED": "Enable the Stage 1 fast path",
    "ENABLE_BADWORDS_PY": "Enable the badwords-py detector",
    "ENABLE_PROFANITE": "Enable the profanite detector",
    "ENABLE_GLIN_PROFANITY": "Enable the glin-profanity detector",
    "ENABLE_SAFETEXT": "Enable the safetext detector",
    "ENABLE_SENSITIVE_WORD_FILTER_CN": "Enable the sensitive-word-filter-cn detector",
    "ENABLE_PROFANITY_FILTER": "Enable the profanity-filter2 detector",
    "ENABLE_GANGAJAL": "Enable the gangajal detector",
    "ENABLE_PYPROFANE": "Enable the PyProfane detector",
    "ENABLE_SENSITIVE_STOP_WORDS": "Enable the sensitive-stop-words submodule detector",
    "ENABLE_DETECTOR_BLOOM_FILTER": "Enable the Bloom filter fast-negative detector",
    "ENABLE_DETECTOR_ROLLING_HASH": "Enable the rolling hash spam detector",
    "ENABLE_DETECTOR_AHO_CORASICK": "Enable the Aho-Corasick exact matcher",
    "ENABLE_DETECTOR_BK_TREE": "Enable the BK-tree fuzzy matcher",
    "ENABLE_DETECTOR_DOUBLE_METAPHONE": "Enable the Double Metaphone phonetic matcher",
    "ENABLE_DETECTOR_MULTI_LANGUAGE": "Enable the multi-language package detector",
    "WEIGHT_DETECTOR_BADWORDS": "Suspicion weight contributed by badwords-py",
    "WEIGHT_DETECTOR_PROFANITE": "Suspicion weight contributed by profanite",
    "WEIGHT_DETECTOR_GLIN": "Suspicion weight contributed by glin-profanity",
    "WEIGHT_DETECTOR_AHO": "Suspicion weight contributed by Aho-Corasick",
    "WEIGHT_DETECTOR_BKTREE": "Suspicion weight contributed by the BK-tree",
    "WEIGHT_DETECTOR_METAPHONE": "Suspicion weight contributed by Metaphone",
    "SEMANTIC_ENABLED": "Enable semantic similarity detection",
    "SEMANTIC_MODEL": "SentenceTransformer model name",
    "SEMANTIC_INDEX_DIR": "Directory holding the per-category Faiss indexes",
    "SEMANTIC_SIMILARITY_THRESHOLD": "Similarity above which a category contributes weight",
    "SEMANTIC_FORCE_LLM_THRESHOLD": "Similarity above which the LLM is forced",
    "SEMANTIC_TOP_K": "Nearest neighbors returned per category index",
    "WEIGHT_SEMANTIC_POLITICAL": "Suspicion weight for the political category",
    "WEIGHT_SEMANTIC_VIOLENCE": "Suspicion weight for the violence category",
    "WEIGHT_SEMANTIC_SEXUAL": "Suspicion weight for the sexual category",
    "WEIGHT_SEMANTIC_HATE": "Suspicion weight for the hate category",
    "WEIGHT_SEMANTIC_PII": "Suspicion weight for the PII category",
    "WEIGHT_SEMANTIC_ADS": "Suspicion weight for the ads category",
    "USER_PROFILING_ENABLED": "Enable per-user behavior profiling",
    "USER_RATIO_THRESHOLD": "Bad-content ratio above which a user is boosted",
    "USER_SCORE_MODIFIER": "Points added to the suspicion score for boosted users",
    "USER_WINDOW_DAYS": "Length of the rolling profiling window",
    "WEIGHT_USER": "Suspicion weight contributed by the user ratio",
    "SCORE_WEIGHTS_CACHE_TTL_SECONDS": "TTL of the score weight cache in seconds",
    "AI_TARGET_PERCENTAGE": "Target percentage of traffic handled by the LLM",
    "FORCE_LLM_ON_SEMANTIC_HIGH": "Force the LLM when semantic similarity is high",
    "FORCE_LLM_ON_USER_RATIO_HIGH": "Force the LLM when the user ratio is high",
    "LLM_RESPONSE_TIMEOUT_SECONDS": "Timeout for a single LLM response",
    "AUTO_TUNING_ENABLED": "Enable the daily weight and threshold tuning batch",
    "WEIGHT_DECAY_HALF_LIFE_DAYS": "Half-life for decaying old feedback influence",
    "AUTO_TUNING_BATCH_HOUR": "UTC hour at which the tuning batch runs",
    "SCORE_WEIGHTS_CACHE_TTL_SECONDS_LEGACY": "Unused legacy key",
    "CACHE_MAX_SIZE": "Maximum number of cached moderation results",
    "CACHE_TTL_SECONDS": "TTL of cached moderation results",
    "DETECTOR_THREAD_POOL_SIZE": "Worker threads for the parallel detectors",
    "REQUEST_TIMEOUT_SECONDS": "Maximum request processing time",
    "MAX_BATCH_SIZE": "Maximum items per batch moderation request",
    "RATE_LIMIT_REQUESTS": "Allowed requests per rate limit window",
    "RATE_LIMIT_PERIOD": "Rate limit window length in seconds",
    "ALLOWED_ORIGINS": "Comma-separated CORS origin allowlist",
    "LOG_LEVEL": "Logging verbosity",
    "LOG_MAX_BYTES": "Maximum log file size before rotation",
    "LOG_BACKUP_COUNT": "Number of rotated log files to keep",
    "LOG_RETENTION_DAYS": "Days to retain rotated log files",
    "EXPORT_RETENTION_DAYS": "Days to retain generated export archives",
}

_READ_ONLY_KEYS: frozenset[str] = frozenset(
    {
        "APP_PORT",
        "WORKERS",
        "MODEL_PATH",
        "FEEDBACK_DB_PATH",
        "EXPORT_TEMP_DIR",
        "ADMIN_API_KEY",
        "WEBUI_API_KEY",
        "SECRET_KEY",
        "ENCRYPTION_KEY",
    }
)

_RANGES: dict[str, tuple[int, int]] = {
    "MODEL_CONTEXT_SIZE": (1024, 262144),
    "MODEL_BATCH_SIZE": (16, 8192),
    "MODEL_MAX_TOKENS": (1, 4096),
    "MODEL_IDLE_TIMEOUT_SECONDS": (10, 86400),
    "WEIGHT_DETECTOR_BADWORDS": (5, 50),
    "WEIGHT_DETECTOR_PROFANITE": (5, 50),
    "WEIGHT_DETECTOR_GLIN": (5, 50),
    "WEIGHT_DETECTOR_AHO": (5, 50),
    "WEIGHT_DETECTOR_BKTREE": (5, 50),
    "WEIGHT_DETECTOR_METAPHONE": (5, 50),
    "WEIGHT_SEMANTIC_POLITICAL": (5, 50),
    "WEIGHT_SEMANTIC_VIOLENCE": (5, 50),
    "WEIGHT_SEMANTIC_SEXUAL": (5, 50),
    "WEIGHT_SEMANTIC_HATE": (5, 50),
    "WEIGHT_SEMANTIC_PII": (5, 50),
    "WEIGHT_SEMANTIC_ADS": (5, 50),
    "WEIGHT_USER": (5, 50),
    "SEMANTIC_SIMILARITY_THRESHOLD": (0, 1),
    "SEMANTIC_FORCE_LLM_THRESHOLD": (0, 1),
    "SEMANTIC_TOP_K": (1, 100),
    "USER_RATIO_THRESHOLD": (0, 1),
    "USER_SCORE_MODIFIER": (0, 100),
    "USER_WINDOW_DAYS": (7, 365),
    "AI_TARGET_PERCENTAGE": (0, 100),
    "LLM_RESPONSE_TIMEOUT_SECONDS": (1, 300),
    "WEIGHT_DECAY_HALF_LIFE_DAYS": (1, 365),
    "AUTO_TUNING_BATCH_HOUR": (0, 23),
    "CACHE_MAX_SIZE": (1, 100000),
    "CACHE_TTL_SECONDS": (1, 86400),
    "DETECTOR_THREAD_POOL_SIZE": (1, 64),
    "REQUEST_TIMEOUT_SECONDS": (1, 300),
    "MAX_BATCH_SIZE": (1, 1000),
    "RATE_LIMIT_REQUESTS": (1, 100000),
    "RATE_LIMIT_PERIOD": (1, 86400),
    "LOG_MAX_BYTES": (1024, 1073741824),
    "LOG_BACKUP_COUNT": (0, 100),
    "LOG_RETENTION_DAYS": (1, 365),
    "EXPORT_RETENTION_DAYS": (1, 365),
    "SCORE_WEIGHTS_CACHE_TTL_SECONDS": (1, 3600),
}

_BOOL_KEYS: frozenset[str] = frozenset(
    {
        "SAFE_WORD_ENABLED",
        "ENABLE_BADWORDS_PY",
        "ENABLE_PROFANITE",
        "ENABLE_GLIN_PROFANITY",
        "ENABLE_SAFETEXT",
        "ENABLE_SENSITIVE_WORD_FILTER_CN",
        "ENABLE_PROFANITY_FILTER",
        "ENABLE_GANGAJAL",
        "ENABLE_PYPROFANE",
        "ENABLE_SENSITIVE_STOP_WORDS",
        "ENABLE_DETECTOR_BLOOM_FILTER",
        "ENABLE_DETECTOR_ROLLING_HASH",
        "ENABLE_DETECTOR_AHO_CORASICK",
        "ENABLE_DETECTOR_BK_TREE",
        "ENABLE_DETECTOR_DOUBLE_METAPHONE",
        "ENABLE_DETECTOR_MULTI_LANGUAGE",
        "SEMANTIC_ENABLED",
        "USER_PROFILING_ENABLED",
        "FORCE_LLM_ON_SEMANTIC_HIGH",
        "FORCE_LLM_ON_USER_RATIO_HIGH",
        "AUTO_TUNING_ENABLED",
        "MODEL_FLASH_ATTN",
        "MODEL_MLOCK",
    }
)

_FLOAT_KEYS: frozenset[str] = frozenset(
    {
        "SEMANTIC_SIMILARITY_THRESHOLD",
        "SEMANTIC_FORCE_LLM_THRESHOLD",
        "USER_RATIO_THRESHOLD",
    }
)

_INT_KEYS: frozenset[str] = frozenset(set(_RANGES) - _FLOAT_KEYS)


class SettingsService:
    """Validated, cached access to runtime settings.

    :param settings: environment-backed settings used to seed the database
    """

    _SCHEMA = """
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            key TEXT UNIQUE,
            value TEXT,
            type TEXT,
            description TEXT,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """

    def __init__(self, settings: Settings) -> None:
        self._db_path: str = settings.settings_db_path
        Path(self._db_path).parent.mkdir(parents=True, exist_ok=True)
        self._connection: sqlite3.Connection = sqlite3.connect(
            self._db_path, check_same_thread=False
        )
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.execute("PRAGMA synchronous=NORMAL")
        self._connection.executescript(SettingsService._SCHEMA)
        self._connection.commit()
        self._cache_ttl: int = settings.settings_cache_ttl_seconds
        self._cache: dict[str, str] = {}
        self._cache_loaded_at: float = 0.0
        self._seed(settings)

    @staticmethod
    def _env_key(name: str) -> str:
        """Return the environment variable name for a Settings field."""
        return name.upper()

    def _seed(self, settings: Settings) -> None:
        """Insert any settings that are not already present.

        Existing database rows always win so a previous administrator edit is
        never overwritten by the environment fallback.

        :param settings: environment-backed settings object
        """
        stored: set[str] = {
            row[0] for row in self._connection.execute("SELECT key FROM settings").fetchall()
        }
        for field in settings.model_fields:
            key: str = self._env_key(field)
            if key in stored:
                continue
            value: Any = getattr(settings, field)
            value_type: str = self._value_type(value)
            self._connection.execute(
                "INSERT INTO settings (key, value, type, description) VALUES (?, ?, ?, ?)",
                (key, self._format(value, value_type), value_type, _DESCRIPTIONS.get(key, "")),
            )
        self._connection.commit()

    @staticmethod
    def _value_type(value: Any) -> str:
        """Map a Python value to its stored type label."""
        if isinstance(value, bool):
            return "boolean"
        if isinstance(value, int):
            return "integer"
        if isinstance(value, float):
            return "float"
        return "string"

    @staticmethod
    def _format(value: Any, value_type: str) -> str:
        """Serialize a value for storage."""
        if value_type == "boolean":
            return "true" if value else "false"
        if value_type in ("integer", "float"):
            return str(value)
        if isinstance(value, list):
            return ",".join(str(item) for item in value)
        return str(value)

    @classmethod
    def _coerce(cls, key: str, raw: str) -> Any:
        """Convert a stored string back to a typed Python value."""
        if key in _BOOL_KEYS:
            return raw.strip().lower() in ("true", "1", "yes")
        if key in _FLOAT_KEYS:
            return float(raw)
        if key in _INT_KEYS:
            return int(float(raw))
        if key == "ALLOWED_ORIGINS":
            return [origin.strip() for origin in raw.split(",") if origin.strip()]
        return raw

    @classmethod
    def _validate(cls, key: str, raw: str) -> None:  # noqa: C901 - many typed branches
        """Validate a raw value before it is persisted.

        :param key: the settings key
        :param raw: the string value to validate
        :raises ValueError: when the value fails type or range validation
        """
        if key in _BOOL_KEYS:
            if raw.strip().lower() not in ("true", "false", "1", "0", "yes", "no"):
                raise ValueError(f"{key} must be a boolean")
            return
        if key in _FLOAT_KEYS:
            try:
                value: float = float(raw)
            except ValueError as exc:
                raise ValueError(f"{key} must be a number") from exc
            if key in _RANGES:
                low, high = _RANGES[key]
                if not low <= value <= high:
                    raise ValueError(f"{key} must be between {low} and {high}")
            return
        if key in _INT_KEYS:
            try:
                int_value: int = int(float(raw))
            except ValueError as exc:
                raise ValueError(f"{key} must be an integer") from exc
            if key in _RANGES:
                low, high = _RANGES[key]
                if not low <= int_value <= high:
                    raise ValueError(f"{key} must be between {low} and {high}")
            return
        if raw == "":
            raise ValueError(f"{key} must not be empty")

    def _load(self) -> dict[str, str]:
        """Reload every setting from the database into the cache."""
        rows = self._connection.execute("SELECT key, value FROM settings").fetchall()
        self._cache = dict(rows)
        self._cache_loaded_at = time.monotonic()

    def _refresh_if_stale(self) -> None:
        """Reload the cache when its TTL has expired."""
        if time.monotonic() - self._cache_loaded_at > self._cache_ttl:
            self._load()

    def all(self) -> dict[str, Any]:
        """Return every setting as a typed key/value mapping."""
        self._refresh_if_stale()
        return {key: self._coerce(key, value) for key, value in self._cache.items()}

    def get(self, key: str, default: Any = None) -> Any:
        """Return one setting value.

        :param key: the settings key
        :param default: value returned when the key is absent
        :return: the typed value
        """
        self._refresh_if_stale()
        raw: str | None = self._cache.get(key)
        if raw is None:
            return default
        try:
            return self._coerce(key, raw)
        except (TypeError, ValueError):
            return default

    def is_public(self, key: str) -> bool:
        """Return whether the key is safe to expose through the admin API."""
        return not key.endswith(_SECRET_SUFFIXES) and key not in _READ_ONLY_KEYS

    def editable_keys(self) -> list[str]:
        """Return every key an administrator may edit, in a stable order."""
        return sorted(key for key in self._cache if self.is_public(key))

    def describe(self) -> list[dict[str, Any]]:
        """Return the full metadata list for the admin settings UI.

        :return: key, value, type, description, and editability per setting
        """
        values: dict[str, Any] = self.all()
        return [
            {
                "key": key,
                "value": values[key],
                "type": self._value_type(values[key]),
                "description": _DESCRIPTIONS.get(key, ""),
                "editable": self.is_public(key),
            }
            for key in sorted(values)
        ]

    def update(self, values: dict[str, Any]) -> dict[str, Any]:
        """Persist and apply validated settings.

        :param values: settings key to raw value mapping
        :return: the keys that were updated
        :raises ValueError: when a key is read-only, unknown, or invalid
        """
        updated: dict[str, Any] = {}
        for key, raw in values.items():
            key = key.upper()
            if key not in self._cache:
                raise ValueError(f"Unknown setting: {key}")
            if not self.is_public(key):
                raise ValueError(f"Setting is read-only: {key}")
            text: str
            if isinstance(raw, bool):
                text = "true" if raw else "false"
            else:
                text = str(raw)
            self._validate(key, text)
            self._connection.execute(
                "UPDATE settings SET value = ?, updated_at = CURRENT_TIMESTAMP WHERE key = ?",
                (text, key),
            )
            updated[key] = self._coerce(key, text)
        self._connection.commit()
        self._load()
        for key, value in updated.items():
            _LOGGER.info("Updated setting %s to %s", key, value)
        return updated

    def to_json(self) -> str:
        """Serialize every setting as compact JSON for export."""
        values: dict[str, Any] = self.all()
        return json.dumps(values, sort_keys=True)

    def close(self) -> None:
        """Close the underlying database connection."""
        self._connection.close()
