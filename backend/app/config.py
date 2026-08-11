"""Application settings loaded from environment variables.

All settings map 1:1 to the variables documented in ``.env.example``.
Security-critical values are validated before the service starts.
"""

from __future__ import annotations

import os
from pathlib import Path

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Typed access to every environment variable used by the service."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    host: str = "127.0.0.1"
    port: int = 8080

    workers: int = 7

    model_path: str = "/var/lib/moderation/models/mistral-7b-instruct.Q4_K_M.gguf"
    model_context_size: int = 4096
    model_threads: int = 4
    model_batch_size: int = 512
    model_max_tokens: int = 10

    bloom_filter_capacity: int = 1_000_000
    bloom_filter_error_rate: float = 0.001
    spam_cache_size: int = 10_000
    spam_cache_ttl_seconds: int = 60
    fuzzy_max_distance: int = 2
    minhash_num_perm: int = 128
    minhash_jaccard_threshold: float = 0.85

    enable_badwords_py: bool = True
    enable_profanite: bool = True
    enable_glin_profanity: bool = True
    enable_safetext: bool = True
    enable_sensitive_word_filter_cn: bool = True
    enable_profanity_filter: bool = True
    enable_gangajal: bool = True
    enable_scheckbl: bool = True
    enable_valx: bool = True
    enable_sensitive_word_filter: bool = True
    enable_pyprofane: bool = True

    admin_api_key: str = "CHANGE_ME_SUPER_SECRET_KEY"
    secret_key: str = "CHANGE_ME_SECRET_KEY_FOR_SESSION"
    encryption_key: str = "CHANGE_ME_32_BYTE_HEX"

    rate_limit_requests: int = 100
    rate_limit_period: int = 60

    allowed_origins: list[str] = Field(default_factory=lambda: [])

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
        """Refuse to start with default or empty security secrets.

        :raises RuntimeError: when a secret still carries its placeholder value.
        """
        placeholders: dict[str, str] = {
            "admin_api_key": self.admin_api_key,
            "secret_key": self.secret_key,
            "encryption_key": self.encryption_key,
        }
        for field_name, value in placeholders.items():
            if not value or value.startswith("CHANGE_ME"):
                raise RuntimeError(
                    f"Refusing to start: {field_name} must be set in the environment. "
                    f"Copy .env.example to .env and assign a real secret."
                )

    def ensure_directories(self) -> None:
        """Create the data and log directories if they do not exist."""
        for raw_path in (self.custom_words_path, self.log_file_path):
            path: Path = Path(raw_path).parent
            if raw_path.startswith("."):
                path = Path(os.getcwd()) / path
            path.mkdir(parents=True, exist_ok=True)
