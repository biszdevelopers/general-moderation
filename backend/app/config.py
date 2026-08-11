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

    host: str = "127.0.0.1"
    port: int = 8080

    workers: int = 3

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

    admin_api_key: str = "CHANGE_ME_SUPER_SECRET_KEY"
    secret_key: str = "CHANGE_ME_SECRET_KEY_FOR_SESSION"
    encryption_key: str = "CHANGE_ME_32_BYTE_HEX"

    rate_limit_requests: int = 100
    rate_limit_period: int = 60

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
        fields: tuple[str, ...] = ("admin_api_key", "secret_key", "encryption_key")
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
        """Create the data, log, and model directories if they do not exist."""
        for raw_path in (self.custom_words_path, self.log_file_path):
            path: Path = Path(raw_path).parent
            if raw_path.startswith("."):
                path = Path(os.getcwd()) / path
            path.mkdir(parents=True, exist_ok=True)
        model_dir: Path = Path(self.model_dir)
        if self.model_dir.startswith("."):
            model_dir = Path(os.getcwd()) / model_dir
        model_dir.mkdir(parents=True, exist_ok=True)
