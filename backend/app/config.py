"""Application settings loaded from environment variables.

All settings map 1:1 to the variables documented in ``.env.example``.
Security-critical values are validated before the service starts.
"""

from __future__ import annotations

import logging
import os
import secrets
import shutil
from pathlib import Path
from typing import Annotated

from atomicwrites import atomic_write
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    """Typed access to every environment variable used by the service."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_host: str = "0.0.0.0"
    app_port: int = 18427
    frontend_dist_path: str = "../frontend/dist"

    workers: int = 3

    # Stage 1: fast path
    safe_word_list_path: str = "./data/safe_words.txt"
    safe_word_enabled: bool = True

    model_path: str = "auto"
    model_primary_repo: str = "bartowski/Qwen_Qwen3.5-9B-GGUF"
    model_fallback_repo: str = "lmstudio-community/Qwen3.5-9B-GGUF"
    model_filename: str = "Qwen_Qwen3.5-9B-Q4_K_M.gguf"
    model_dir: str = "./models"
    model_context_size: int = 16384
    model_threads: str = "auto"
    model_batch_size: int = 512
    model_max_tokens: int = 10
    model_cache_type_k: str = "q8_0"
    model_cache_type_v: str = "q8_0"
    model_flash_attn: bool = True
    model_mlock: bool = True
    model_idle_timeout_seconds: int = 300

    hf_endpoint: str = "https://huggingface.co"
    hf_mirror: str = "https://hf-mirror.com"
    modelscope_endpoint: str = "https://www.modelscope.cn"

    cache_max_size: int = 500
    cache_ttl_seconds: int = 60
    detector_thread_pool_size: int = 4

    bloom_filter_capacity: int = 1_000_000
    bloom_filter_error_rate: float = 0.001
    spam_cache_size: int = 10_000
    spam_cache_ttl_seconds: int = 60
    fuzzy_max_distance: int = 2

    enable_badwords_py: bool = True
    enable_profanite: bool = True
    enable_glin_profanity: bool = True
    enable_safetext: bool = True
    enable_sensitive_word_filter_cn: bool = True
    enable_profanity_filter: bool = True
    enable_gangajal: bool = True
    enable_pyprofane: bool = True
    enable_sensitive_stop_words: bool = True
    sensitive_stop_words_dir: str = "./data/sensitive-stop-words"
    # Per-category toggles for the sensitive-stop-words submodule blocking lists.
    enable_sensitive_stop_words_political: bool = True
    enable_sensitive_stop_words_porn: bool = True
    enable_sensitive_stop_words_gun: bool = True
    enable_sensitive_stop_words_ad: bool = True
    enable_sensitive_stop_words_url: bool = True
    # Additional raw Chinese sensitive-word lists (newline-delimited txt).
    # Wired into the same detector so the service's own algorithms match them.
    sensitive_word_data_dict: str = (
        "./data/sensitive-word-data/src/main/resources/sensitive_word_dict.txt"
    )
    sensitive_lexicon_dir: str = "./data/sensitive-lexicon/Vocabulary"
    sensitive_dict_path: str = "./data/sensitive/dict/dict.txt"
    # Minimum term length for a sensitive-list match to hard-block. Single
    # CJK characters appear in benign text (祝, 你, 请, ...), so the lists'
    # ~528 one-char terms are excluded from decisive blocking.
    sensitive_min_word_length: int = 2

    # Stage 2 detector toggles (runtime-editable through the admin API)
    enable_detector_bloom_filter: bool = True
    enable_detector_rolling_hash: bool = True
    enable_detector_aho_corasick: bool = True
    enable_detector_bk_tree: bool = True
    enable_detector_double_metaphone: bool = True
    enable_detector_multi_language: bool = True

    # Benign words that multi-language packages misflag (e.g. Turkish "cok"
    # = "very", flagged as profanity after diacritic stripping). A package hit
    # is suppressed when the entire text consists of excluded words.
    ml_benign_word_exclusions: str = "cok"

    # Detector weights (Stage 2 suspicion scoring)
    weight_detector_badwords: int = 25
    weight_detector_profanite: int = 20
    weight_detector_glin: int = 20
    weight_detector_aho: int = 30
    weight_detector_bktree: int = 20
    weight_detector_metaphone: int = 15

    # Stage 2: semantic similarity
    semantic_enabled: bool = True
    semantic_model: str = "paraphrase-multilingual-MiniLM-L12-v2"
    semantic_index_dir: str = "./semantic/"
    semantic_similarity_threshold: float = 0.65
    semantic_force_llm_threshold: float = 0.80
    semantic_top_k: int = 5
    weight_semantic_political: int = 35
    weight_semantic_violence: int = 40
    weight_semantic_sexual: int = 30
    weight_semantic_hate: int = 35
    weight_semantic_pii: int = 25
    weight_semantic_ads: int = 15

    # Stage 2: user profiling (91-day rolling window with archive)
    user_profiling_enabled: bool = True
    user_db_path: str = "./data/users.db"
    user_archive_db_path: str = "./data/archive.db"
    user_ratio_threshold: float = 0.3
    user_score_modifier: int = 20
    user_window_days: int = 91

    # Stage 2: suspicion scoring
    weight_user: int = 20
    score_weights_cache_ttl_seconds: int = 300

    # Stage 2: severity-aware phrase detection
    critical_phrases_db_path: str = "./data/critical_phrases.db"
    enable_phrase_detector: bool = True
    severity_hard_block_threshold: int = 5
    review_escalation_threshold: int = 40

    # Stage 2: multi-language package handling
    ml_review_mode: bool = False

    # Stage 3: LLM trigger policy
    ai_target_percentage: int = 5
    force_llm_on_semantic_high: bool = True
    force_llm_on_user_ratio_high: bool = True
    llm_response_timeout_seconds: int = 30

    # Stage 3: provider selection and remote endpoints. The active provider is
    # switched at runtime through the admin API; these values seed settings.db.
    llm_provider: str = "local_llama_cpp"
    backup_llm_provider: str = ""
    llm_failure_policy: str = "rule_based"
    ollama_base_url: str = "http://127.0.0.1:11434"
    ollama_model: str = "qwen3.5:9b"
    openai_base_url: str = "https://api.openai.com/v1"
    openai_model: str = "gpt-4o-mini"
    openai_api_key: str = ""
    anthropic_base_url: str = "https://api.anthropic.com"
    anthropic_model: str = "claude-3-5-haiku-latest"
    anthropic_api_key: str = ""
    external_llamacpp_base_url: str = "http://127.0.0.1:8080"
    external_llamacpp_model: str = ""

    # Stage 3: model health monitoring and verdict confidence calibration.
    model_health_interval_seconds: int = 30
    model_health_failure_threshold: int = 3
    calibration_enabled: bool = True
    calibration_block_confidence: float = 0.90
    calibration_allow_confidence: float = 0.35

    # Model registry (GGUF versions managed through the admin UI)
    model_registry_db_path: str = "./data/models.db"

    # Feedback and auto-tuning
    feedback_db_path: str = "./data/feedback.db"
    auto_tuning_enabled: bool = True
    weight_decay_half_life_days: int = 30
    auto_tuning_batch_hour: int = 0

    # Runtime settings persistence
    settings_db_path: str = "./data/settings.db"
    settings_cache_ttl_seconds: int = 60
    app_config_db_path: str = "./data/config.db"

    # Data export
    export_temp_dir: str = "./exports"
    export_retention_days: int = 7

    admin_api_key: str = "CHANGE_ME_SUPER_SECRET_KEY"
    secret_key: str = "CHANGE_ME_SECRET_KEY_FOR_SESSION"
    encryption_key: str = "CHANGE_ME_32_BYTE_HEX"

    rate_limit_requests: int = 100
    rate_limit_period: int = 60
    # Optional Redis URI for cross-worker rate limiting (slowapi storage) and
    # cross-worker result-cache invalidation (pub/sub). Empty disables both.
    redis_uri: str = ""

    allowed_origins: Annotated[list[str], NoDecode] = Field(default_factory=lambda: [])

    log_file_path: str = "./logs/moderation.log"
    log_level: str = "INFO"
    log_max_bytes: int = 104_857_600
    log_backup_count: int = 10
    log_retention_days: int = 30

    custom_words_storage: str = "sqlite"
    custom_words_path: str = "./data/custom_words.db"

    request_timeout_seconds: int = 30
    max_batch_size: int = 100

    webui_enabled: bool = True
    webui_host: str = "127.0.0.1"
    webui_port: int = 5173
    webui_api_key: str = "CHANGE_ME_WEBUI_API_KEY"

    metrics_enabled: bool = True
    metrics_port: int = 9090

    @field_validator("allowed_origins", mode="before")
    @classmethod
    def _split_origins(cls, value: object) -> object:
        """Parse a comma-separated CORS origin list into a Python list."""
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value

    def validate_security(self) -> None:
        """Bootstrap security secrets on first run.

        Placeholder or empty secrets are replaced with cryptographically
        strong values persisted to ``.env``.
        """
        self.ensure_secrets()

    def ensure_secrets(self, force: bool = False) -> dict[str, str]:
        """Generate and persist security secrets.

        Without ``force`` only missing or placeholder secrets are replaced,
        preserving any real values already set.

        :param force: regenerate every secret, even already-set ones
        :return: mapping of generated field names to their new values
        """
        fields: tuple[str, ...] = (
            "admin_api_key",
            "webui_api_key",
            "secret_key",
            "encryption_key",
        )
        current: dict[str, str] = {name: getattr(self, name) for name in fields}
        targets: dict[str, str]
        if force:
            targets = current
        else:
            targets = {
                name: value
                for name, value in current.items()
                if not value or value.startswith("CHANGE_ME")
            }
        if not targets:
            return {}
        generated: dict[str, str] = {}
        for name in targets:
            if name == "encryption_key":
                generated[name] = secrets.token_hex(32)
            else:
                generated[name] = secrets.token_urlsafe(32)
        self._persist_env(generated)
        for name, value in generated.items():
            setattr(self, name, value)
        logging.warning(f"Generated {len(generated)} security secret(s) and wrote them to .env")
        return generated

    def _persist_env(self, generated: dict[str, str]) -> None:
        """Write generated secrets into the ``.env`` file.

        Creates ``.env`` from the example template when it does not exist,
        then updates or appends the three secret variables.

        :param generated: field name to value mapping for the new secrets
        """
        env_path: Path = Path(".env")
        if not env_path.exists():
            example: Path = Path(".env.example")
            if example.exists():
                shutil.copy(example, env_path)
            else:
                env_path.touch()
        lines: list[str] = env_path.read_text(encoding="utf-8").splitlines()
        updated: set[str] = set()
        for index, line in enumerate(lines):
            for name, value in generated.items():
                key: str = name.upper()
                if line.startswith(f"{key}="):
                    lines[index] = f"{key}={value}"
                    updated.add(name)
        for name, value in generated.items():
            if name not in updated:
                lines.append(f"{name.upper()}={value}")
        with atomic_write(str(env_path), encoding="utf-8", overwrite=True) as handle:
            handle.write("\n".join(lines) + "\n")

    def ensure_directories(self) -> None:
        """Create the data, log, model, semantic, and export directories."""
        db_paths: tuple[str, ...] = (
            self.custom_words_path,
            self.user_db_path,
            self.user_archive_db_path,
            self.feedback_db_path,
            self.settings_db_path,
            self.critical_phrases_db_path,
            self.log_file_path,
        )
        for raw_path in db_paths:
            path: Path = Path(raw_path).parent
            if raw_path.startswith("."):
                path = Path(os.getcwd()) / path
            path.mkdir(parents=True, exist_ok=True)
        for raw_dir in (self.semantic_index_dir, self.export_temp_dir):
            directory: Path = Path(raw_dir)
            if raw_dir.startswith("."):
                directory = Path(os.getcwd()) / directory
            directory.mkdir(parents=True, exist_ok=True)
        safe_words: Path = Path(self.safe_word_list_path)
        if self.safe_word_list_path.startswith("."):
            safe_words = Path(os.getcwd()) / safe_words
        safe_words.parent.mkdir(parents=True, exist_ok=True)
        model_dir: Path = Path(self.model_dir)
        if self.model_dir.startswith("."):
            model_dir = Path(os.getcwd()) / model_dir
        model_dir.mkdir(parents=True, exist_ok=True)
