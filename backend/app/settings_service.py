"""Runtime settings persistence.

Settings are stored in ``settings.db`` and seeded from the ``.env``-backed
``Settings`` object on first use, so the environment file remains the fallback
for initial configuration. Every read goes through a small TTL cache; every
write is validated before it is persisted and the cache is refreshed
immediately so changes apply without a service restart.

The service also owns three auxiliary tables in the same database:

- ``config_audit`` records every change (old value, new value, actor, source).
- ``config_presets`` stores named bundles of settings that apply atomically.
- Editable secret values (``*_KEY``/``*_SECRET``) are encrypted at rest with
  AES-GCM using the application ``ENCRYPTION_KEY``.
"""

from __future__ import annotations

import base64
import hashlib
import json
import logging
import os
import sqlite3
import time
from pathlib import Path
from typing import Any

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from app.config import Settings

_LOGGER: logging.Logger = logging.getLogger(__name__)

_SECRET_SUFFIXES: tuple[str, ...] = ("_KEY", "_SECRET")
_ENCRYPTION_PREFIX: str = "enc:v1:"
_NONCE_BYTES: int = 12

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
    "ENABLE_SENSITIVE_STOP_WORDS_POLITICAL": "Enable the sensitive-stop-words political category",
    "ENABLE_SENSITIVE_STOP_WORDS_PORN": "Enable the sensitive-stop-words porn category",
    "ENABLE_SENSITIVE_STOP_WORDS_GUN": "Enable the sensitive-stop-words gun/explosive category",
    "ENABLE_SENSITIVE_STOP_WORDS_AD": "Enable the sensitive-stop-words ads category",
    "ENABLE_SENSITIVE_STOP_WORDS_URL": "Enable the sensitive-stop-words URL category",
    "ENABLE_PHRASE_DETECTOR": "Enable the severity-aware phrase detector",
    "ML_REVIEW_MODE": "Downgrade multi-language package hits from BLOCK to REVIEW",
    "SEVERITY_HARD_BLOCK_THRESHOLD": "Severity at or above which a phrase hard-blocks",
    "REVIEW_ESCALATION_THRESHOLD": "Suspicion score at or above which REVIEW escalates to the LLM",
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
    "LLM_PROVIDER": "Active LLM provider serving Stage 3 classifications",
    "BACKUP_LLM_PROVIDER": "Provider used when the active one fails health checks",
    "LLM_FAILURE_POLICY": "Stage 3 behavior when no provider is healthy (rule_based or block)",
    "OLLAMA_BASE_URL": "Base URL of the Ollama HTTP API",
    "OLLAMA_MODEL": "Ollama model tag used for classification",
    "OPENAI_BASE_URL": "Base URL of the OpenAI-compatible chat completions API",
    "OPENAI_MODEL": "OpenAI-compatible model name used for classification",
    "OPENAI_API_KEY": "API key for the OpenAI-compatible provider",
    "ANTHROPIC_BASE_URL": "Base URL of the Anthropic-compatible messages API",
    "ANTHROPIC_MODEL": "Anthropic-compatible model name used for classification",
    "ANTHROPIC_API_KEY": "API key for the Anthropic-compatible provider",
    "EXTERNAL_LLAMACPP_BASE_URL": "Base URL of an external llama.cpp server",
    "EXTERNAL_LLAMACPP_MODEL": "Optional model name passed to the external llama.cpp server",
    "MODEL_HEALTH_INTERVAL_SECONDS": "Seconds between provider health probes",
    "MODEL_HEALTH_FAILURE_THRESHOLD": "Consecutive failures before failing over to the backup",
    "CALIBRATION_ENABLED": "Blend the suspicion score into the LLM confidence value",
    "CALIBRATION_BLOCK_CONFIDENCE": "Confidence reported when the LLM replies BLOCK",
    "CALIBRATION_ALLOW_CONFIDENCE": "Confidence reported when the LLM replies ALLOW",
    "ACTIVE_GGUF_PATH": "Absolute path of the GGUF file selected in the model registry",
}

_READ_ONLY_KEYS: frozenset[str] = frozenset(
    {
        "APP_HOST",
        "APP_PORT",
        "WORKERS",
        "FRONTEND_DIST_PATH",
        "LOG_FILE_PATH",
        "MODEL_DIR",
        "HF_ENDPOINT",
        "HF_MIRROR",
        "MODELSCOPE_ENDPOINT",
        "REDIS_URI",
        "MODEL_PATH",
        "FEEDBACK_DB_PATH",
        "EXPORT_TEMP_DIR",
        "ADMIN_API_KEY",
        "WEBUI_API_KEY",
        "SECRET_KEY",
        "ENCRYPTION_KEY",
    }
)

_PROVIDER_CHOICES: tuple[str, ...] = (
    "local_llama_cpp",
    "external_llama_cpp",
    "ollama",
    "openai_compatible",
    "anthropic_compatible",
)

_CHOICES: dict[str, tuple[str, ...]] = {
    "LLM_PROVIDER": _PROVIDER_CHOICES,
    "BACKUP_LLM_PROVIDER": ("", *_PROVIDER_CHOICES),
    "LLM_FAILURE_POLICY": ("rule_based", "block"),
}

# Provider credentials are secrets but must be editable at runtime; every
# other *_KEY/*_SECRET value stays read-only and is redacted on read.
_EDITABLE_SECRET_KEYS: frozenset[str] = frozenset(
    {
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
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
    "SEVERITY_HARD_BLOCK_THRESHOLD": (1, 10),
    "REVIEW_ESCALATION_THRESHOLD": (1, 100),
    "MODEL_HEALTH_INTERVAL_SECONDS": (5, 600),
    "MODEL_HEALTH_FAILURE_THRESHOLD": (1, 20),
    "CALIBRATION_BLOCK_CONFIDENCE": (0, 1),
    "CALIBRATION_ALLOW_CONFIDENCE": (0, 1),
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
        "ENABLE_SENSITIVE_STOP_WORDS_POLITICAL",
        "ENABLE_SENSITIVE_STOP_WORDS_PORN",
        "ENABLE_SENSITIVE_STOP_WORDS_GUN",
        "ENABLE_SENSITIVE_STOP_WORDS_AD",
        "ENABLE_SENSITIVE_STOP_WORDS_URL",
        "ENABLE_PHRASE_DETECTOR",
        "ML_REVIEW_MODE",
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
        "CALIBRATION_BLOCK_CONFIDENCE",
        "CALIBRATION_ALLOW_CONFIDENCE",
    }
)

_INT_KEYS: frozenset[str] = frozenset(set(_RANGES) - _FLOAT_KEYS)

# Category rules evaluated in order; the first matching rule wins. The
# provider-specific prefixes must be tested before the generic MODEL_ prefix.
_CATEGORY_RULES: tuple[tuple[str, str], ...] = (
    ("EXTERNAL_LLAMACPP_", "Models & Providers"),
    ("MODEL_HEALTH_", "Models & Providers"),
    ("LLM_PROVIDER", "Models & Providers"),
    ("BACKUP_LLM_PROVIDER", "Models & Providers"),
    ("OLLAMA_", "Models & Providers"),
    ("OPENAI_", "Models & Providers"),
    ("ANTHROPIC_", "Models & Providers"),
    ("MODEL_", "Model"),
    ("SAFE_WORD_", "Stage 1 Fast Path"),
    ("WEIGHT_DETECTOR_", "Detector Weights"),
    ("WEIGHT_SEMANTIC_", "Semantic Weights"),
    ("SEMANTIC_", "Semantic Similarity"),
    ("USER_", "User Profiling"),
    ("WEIGHT_USER", "Suspicion Scoring"),
    ("SCORE_WEIGHTS", "Suspicion Scoring"),
    ("AI_", "LLM"),
    ("FORCE_LLM_", "LLM"),
    ("LLM_FAILURE_POLICY", "LLM"),
    ("LLM_RESPONSE_TIMEOUT", "LLM"),
    ("CALIBRATION_", "LLM"),
    ("AUTO_TUNING_", "Feedback & Auto-Tuning"),
    ("WEIGHT_DECAY", "Feedback & Auto-Tuning"),
    ("CACHE_", "Performance"),
    ("DETECTOR_THREAD", "Performance"),
    ("REQUEST_", "Performance"),
    ("MAX_BATCH", "Performance"),
    ("RATE_LIMIT_", "Security"),
    ("ALLOWED_ORIGINS", "Security"),
    ("LOG_LEVEL", "Logging"),
    ("LOG_MAX_BYTES", "Logging"),
    ("LOG_BACKUP_COUNT", "Logging"),
    ("LOG_RETENTION_DAYS", "Logging"),
    ("EXPORT_", "Export"),
)


def _category(key: str) -> str:
    """Return the admin UI category for a settings key.

    :param key: the settings key
    :return: the category label
    """
    for prefix, group in _CATEGORY_RULES:
        if key.startswith(prefix):
            return group
    return "Other"


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
        );
        CREATE TABLE IF NOT EXISTS config_audit (
            id INTEGER PRIMARY KEY,
            key TEXT,
            old_value TEXT,
            new_value TEXT,
            actor TEXT,
            source TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS config_presets (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            description TEXT,
            payload TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """

    _DEFAULT_PRESETS: tuple[dict[str, Any], ...] = (
        {
            "name": "High Accuracy",
            "description": "More traffic reaches the LLM and thresholds favor recall",
            "payload": {
                "AI_TARGET_PERCENTAGE": 25,
                "SEMANTIC_SIMILARITY_THRESHOLD": 0.55,
                "SEMANTIC_FORCE_LLM_THRESHOLD": 0.7,
                "REVIEW_ESCALATION_THRESHOLD": 30,
                "SEVERITY_HARD_BLOCK_THRESHOLD": 4,
                "FORCE_LLM_ON_SEMANTIC_HIGH": True,
                "FORCE_LLM_ON_USER_RATIO_HIGH": True,
                "USER_SCORE_MODIFIER": 25,
                "WEIGHT_USER": 25,
            },
        },
        {
            "name": "Low Cost",
            "description": "Rule-based verdicts only; the LLM is reserved for manual runs",
            "payload": {
                "AI_TARGET_PERCENTAGE": 0,
                "FORCE_LLM_ON_SEMANTIC_HIGH": False,
                "FORCE_LLM_ON_USER_RATIO_HIGH": False,
                "MODEL_IDLE_TIMEOUT_SECONDS": 60,
                "CACHE_TTL_SECONDS": 300,
                "CACHE_MAX_SIZE": 2000,
            },
        },
        {
            "name": "Strict",
            "description": "Aggressive blocking with fail-closed model failures",
            "payload": {
                "AI_TARGET_PERCENTAGE": 15,
                "SEVERITY_HARD_BLOCK_THRESHOLD": 3,
                "REVIEW_ESCALATION_THRESHOLD": 20,
                "ML_REVIEW_MODE": False,
                "SEMANTIC_SIMILARITY_THRESHOLD": 0.5,
                "SEMANTIC_FORCE_LLM_THRESHOLD": 0.7,
                "LLM_FAILURE_POLICY": "block",
            },
        },
    )

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
        self._aes_key: bytes = self._derive_aes_key(settings.encryption_key)
        self._seed(settings)
        self._seed_presets()
        self._load()

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
        if key in _CHOICES:
            if raw not in _CHOICES[key]:
                raise ValueError(f"{key} must be one of: {', '.join(_CHOICES[key])}")
            return
        if raw == "":
            raise ValueError(f"{key} must not be empty")

    @staticmethod
    def _derive_aes_key(raw_key: str) -> bytes:
        """Derive a 32-byte AES key from the configured encryption secret.

        Real deployments hold a 32-byte hex value; placeholder or malformed
        values are hashed so the service still starts (and tests still run).

        :param raw_key: the ENCRYPTION_KEY environment value
        :return: 32 bytes of key material
        """
        try:
            key: bytes = bytes.fromhex(raw_key)
            if len(key) == 32:
                return key
        except ValueError:
            pass
        return hashlib.sha256(raw_key.encode("utf-8")).digest()

    def _is_secret(self, key: str) -> bool:
        """Return whether the key holds an encryptable credential.

        Read-only secrets never transit this service's write path, so only
        editable provider keys are encrypted at rest.

        :param key: the settings key
        """
        return key.endswith(_SECRET_SUFFIXES) and self.is_public(key)

    def _encrypt(self, plaintext: str) -> str:
        """Encrypt a secret for storage with AES-GCM.

        :param plaintext: the secret value
        :return: the prefixed base64 nonce+ciphertext token
        """
        nonce: bytes = os.urandom(_NONCE_BYTES)
        ciphertext: bytes = AESGCM(self._aes_key).encrypt(nonce, plaintext.encode("utf-8"), None)
        return _ENCRYPTION_PREFIX + base64.b64encode(nonce + ciphertext).decode("ascii")

    def _decrypt(self, stored: str) -> str:
        """Decrypt a stored secret, passing legacy plaintext through.

        :param stored: the stored value
        :return: the plaintext secret
        """
        if not stored.startswith(_ENCRYPTION_PREFIX):
            return stored
        try:
            blob: bytes = base64.b64decode(stored[len(_ENCRYPTION_PREFIX) :])
            plaintext: bytes = AESGCM(self._aes_key).decrypt(
                blob[:_NONCE_BYTES], blob[_NONCE_BYTES:], None
            )
            return plaintext.decode("utf-8")
        except Exception:
            _LOGGER.warning("Failed to decrypt stored secret; returning empty value")
            return ""

    def _seed_presets(self) -> None:
        """Insert the built-in presets that are not already present."""
        stored: set[str] = {
            row[0] for row in self._connection.execute("SELECT name FROM config_presets").fetchall()
        }
        for preset in SettingsService._DEFAULT_PRESETS:
            if preset["name"] in stored:
                continue
            self._connection.execute(
                "INSERT INTO config_presets (name, description, payload) VALUES (?, ?, ?)",
                (
                    str(preset["name"]),
                    str(preset["description"]),
                    json.dumps(preset["payload"], sort_keys=True),
                ),
            )
        self._connection.commit()

    def cache_freshness(self) -> float:
        """Return the monotonic timestamp of the last settings load.

        Callers (the engine cache fingerprint) use this to detect that
        settings changed and drop their memoized derivation.

        :return: the monotonic time of the last ``_load``
        """
        return self._cache_loaded_at

    def _load(self) -> dict[str, str]:
        """Reload every setting from the database into the cache.

        Encrypted secret values are decrypted so callers always see plaintext.
        """
        rows = self._connection.execute("SELECT key, value FROM settings").fetchall()
        self._cache = {}
        for key, value in rows:
            self._cache[key] = (
                self._decrypt(value)
                if isinstance(value, str) and value.startswith(_ENCRYPTION_PREFIX)
                else value
            )
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
        """Return whether the key is safe to expose through the admin API.

        Editable provider credentials count as public: they are redacted in
        every read path but administrators may update them at runtime.

        :param key: the settings key
        """
        if key in _EDITABLE_SECRET_KEYS:
            return True
        return not key.endswith(_SECRET_SUFFIXES) and key not in _READ_ONLY_KEYS

    def editable_keys(self) -> list[str]:
        """Return every key an administrator may edit, in a stable order."""
        return sorted(key for key in self._cache if self.is_public(key))

    def describe(self) -> list[dict[str, Any]]:
        """Return the full metadata list for the admin settings UI.

        Secret values (``*_KEY`` and ``*_SECRET`` suffixes) are redacted so the
        catalog never exposes credentials through the admin or test APIs. Each
        entry carries the validation metadata (type, range, choices), the UI
        category, and the restart/secret flags.

        :return: metadata per setting
        """
        values: dict[str, Any] = self.all()
        catalog: list[dict[str, Any]] = []
        for key in sorted(values):
            is_secret: bool = key.endswith(_SECRET_SUFFIXES)
            entry: dict[str, Any] = {
                "key": key,
                "value": "********" if is_secret else values[key],
                "type": self._value_type(values[key]),
                "description": _DESCRIPTIONS.get(key, ""),
                "editable": self.is_public(key),
                "category": _category(key),
                "restart_required": key in _READ_ONLY_KEYS,
                "secret": is_secret,
            }
            if key in _RANGES:
                low, high = _RANGES[key]
                entry["min"] = low
                entry["max"] = high
            if key in _CHOICES:
                entry["choices"] = list(_CHOICES[key])
            catalog.append(entry)
        return catalog

    def history(self, key: str | None = None, limit: int = 100) -> list[dict[str, Any]]:
        """Return recent configuration changes from the audit table.

        Secret keys are redacted in both the old and new value columns.

        :param key: optional settings key filter
        :param limit: maximum number of rows to return
        :return: audit rows ordered newest first
        """
        query: str = "SELECT key, old_value, new_value, actor, source, created_at FROM config_audit"
        params: list[Any] = []
        if key is not None:
            query += " WHERE key = ?"
            params.append(key.upper())
        query += " ORDER BY id DESC LIMIT ?"
        params.append(max(1, min(limit, 1000)))
        rows = self._connection.execute(query, params).fetchall()
        redact: bool = self._is_secret(key) if key is not None else False

        def mask(row_key: str, value: str | None) -> str | None:
            """Redact a stored value when it belongs to a secret key."""
            if value is None or self._is_secret(row_key) or redact:
                return "********" if value else value
            return value

        return [
            {
                "key": row[0],
                "old_value": mask(row[0], row[1]),
                "new_value": mask(row[0], row[2]),
                "actor": row[3],
                "source": row[4],
                "created_at": row[5],
            }
            for row in rows
        ]

    def update(
        self,
        values: dict[str, Any],
        actor: str = "admin",
        source: str = "admin_api",
    ) -> dict[str, Any]:
        """Persist and apply validated settings.

        Every change is recorded in ``config_audit`` with its previous value;
        editable secrets are encrypted before they touch the database.

        :param values: settings key to raw value mapping
        :param actor: identity recorded in the audit trail
        :param source: change origin recorded in the audit trail
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
            old_value: str | None = self._cache.get(key)
            stored_text: str = self._encrypt(text) if self._is_secret(key) else text
            self._connection.execute(
                "UPDATE settings SET value = ?, updated_at = CURRENT_TIMESTAMP WHERE key = ?",
                (stored_text, key),
            )
            self._connection.execute(
                "INSERT INTO config_audit (key, old_value, new_value, actor, source) "
                "VALUES (?, ?, ?, ?, ?)",
                (key, old_value, stored_text if self._is_secret(key) else text, actor, source),
            )
            updated[key] = self._coerce(key, text)
        self._connection.commit()
        self._load()
        for key, value in updated.items():
            _LOGGER.info("Updated setting %s to %s", key, "***" if self._is_secret(key) else value)
        return updated

    def presets(self) -> list[dict[str, Any]]:
        """Return every configuration preset.

        :return: preset name, description, and payload mapping
        """
        rows = self._connection.execute(
            "SELECT name, description, payload FROM config_presets ORDER BY name"
        ).fetchall()
        return [
            {"name": row[0], "description": row[1], "payload": json.loads(row[2])} for row in rows
        ]

    def create_preset(self, name: str, description: str, payload: dict[str, Any]) -> None:
        """Store a new named preset after validating every payload value.

        :param name: unique preset name
        :param description: human-readable purpose
        :raises ValueError: when the name exists or a payload value is invalid
        """
        existing: set[str] = {
            row[0] for row in self._connection.execute("SELECT name FROM config_presets").fetchall()
        }
        if name in existing:
            raise ValueError(f"Preset already exists: {name}")
        for key in payload:
            if key.upper() not in self._cache:
                raise ValueError(f"Unknown setting: {key}")
            if not self.is_public(key.upper()):
                raise ValueError(f"Setting is read-only: {key}")
        self._validate_batch(payload)
        self._connection.execute(
            "INSERT INTO config_presets (name, description, payload) VALUES (?, ?, ?)",
            (name, description, json.dumps(payload, sort_keys=True)),
        )
        self._connection.commit()

    def delete_preset(self, name: str) -> None:
        """Remove a preset by name.

        :param name: the preset to delete
        :raises ValueError: when the preset does not exist
        """
        cursor = self._connection.execute("DELETE FROM config_presets WHERE name = ?", (name,))
        if cursor.rowcount == 0:
            raise ValueError(f"Unknown preset: {name}")
        self._connection.commit()

    def apply_preset(self, name: str, actor: str = "admin") -> dict[str, Any]:
        """Apply a preset as one validated batch update.

        :param name: the preset to apply
        :param actor: identity recorded in the audit trail
        :return: the keys that changed
        :raises ValueError: when the preset does not exist or a value is invalid
        """
        row = self._connection.execute(
            "SELECT payload FROM config_presets WHERE name = ?", (name,)
        ).fetchone()
        if row is None:
            raise ValueError(f"Unknown preset: {name}")
        payload: dict[str, Any] = json.loads(row[0])
        self._validate_batch(payload)
        return self.update(payload, actor=actor, source=f"preset:{name}")

    def _validate_batch(self, payload: dict[str, Any]) -> None:
        """Validate every key/value pair without persisting anything.

        :param payload: settings key to raw value mapping
        :raises ValueError: when any value fails validation
        """
        for key, raw in payload.items():
            key = key.upper()
            text: str
            if isinstance(raw, bool):
                text = "true" if raw else "false"
            else:
                text = str(raw)
            self._validate(key, text)

    def to_json(self) -> str:
        """Serialize every setting as compact JSON for export.

        Secret values (``*_KEY`` and ``*_SECRET`` suffixes) are redacted so
        export archives never contain credentials.
        """
        values: dict[str, Any] = self.all()
        redacted: dict[str, Any] = {
            key: ("********" if key.endswith(_SECRET_SUFFIXES) else value)
            for key, value in values.items()
        }
        return json.dumps(redacted, sort_keys=True)

    def close(self) -> None:
        """Close the underlying database connection."""
        self._connection.close()
