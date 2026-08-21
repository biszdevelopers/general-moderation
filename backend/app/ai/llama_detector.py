"""Level 2 AI detector backed by llama.cpp (C++ inference engine).

The GGUF model is auto-downloaded on first use from the configured Hugging
Face repositories, with automatic fallback to China mirrors (hf-mirror.com,
ModelScope) and manual-download instructions when every endpoint fails.

Performance features: Q8_0 KV cache quantization, flash attention, memory
locking, auto thread detection, idle unloading, and lazy loading so the
service starts even while the model is still downloading.

User input is strictly sanitized before reaching the model to prevent prompt
injection: chat control tokens are stripped with C regex and XML metacharacters
are escaped. The prompt is rendered through the model's own Jinja2 chat
template with ``enable_thinking=False`` so the Qwen reasoning model replies
with a single classification token instead of a long ``<think>`` block. The
engine runs at ``temperature=0.0`` and must reply with a BLOCK or ALLOW token.
"""

from __future__ import annotations

import os
import re
import threading
import time
import xml.sax.saxutils
from pathlib import Path
from typing import Any

import requests

try:
    import regex as _compiled_regex
except ImportError:  # pragma: no cover - regex is the C-backed primary
    _compiled_regex = None

try:
    from huggingface_hub import hf_hub_download
except ImportError:  # pragma: no cover - huggingface_hub is a declared dependency
    hf_hub_download = None

from app.ai.prompt import SYSTEM_PROMPT, build_classification_prompt
from app.detectors.interface import DetectorInterface
from app.models.verdict import DetectionResult

# Pre-compiled at module level (C-backed where available).
_CONTROL_TOKEN_PATTERN = re.compile(r"<\|im_start\|>|<\|im_end\|>|<\|endoftext\|>")
_TOKEN_PREFIX_PATTERN = re.compile(r"^(system|user|assistant):", re.IGNORECASE)
_GGUF_PATTERN = re.compile(r"\.gguf$", re.IGNORECASE)

_MAX_DOWNLOAD_RETRIES = 3


class LlamaCppDetector(DetectorInterface):
    """Classifies borderline content with a locally hosted GGUF model."""

    def __init__(self, settings: Any, logger: Any | None = None) -> None:
        """Configure the detector without blocking on the model.

        The model is loaded lazily on first use and preloaded in the
        background so the service starts immediately.

        :param settings: application settings with MODEL_* variables
        :param logger: optional logger for load failures
        """
        self._settings: Any = settings
        self._logger: Any = logger
        self._model: Any | None = None
        self._chat_template: Any | None = None
        self._last_used: float = 0.0
        self._loading: bool = False
        self._load_lock: threading.Lock = threading.Lock()
        self._infer_lock: threading.Lock = threading.Lock()
        self._shutdown: bool = False
        self._last_prompt: str | None = None
        self._last_reply: str | None = None
        self._system_prompt: str = SYSTEM_PROMPT

    def set_system_prompt(self, template: str) -> None:
        """Replace the system prompt used in classification prompts.

        :param template: the new system prompt text
        """
        if template.strip():
            self._system_prompt = template

    def start_preload(self) -> None:
        """Kick off a background download-and-load of the model.

        Called from the application startup event, after workers fork, so a
        running thread is never inherited across a fork.
        """
        if self._model is not None or self._shutdown:
            return
        thread: threading.Thread = threading.Thread(
            target=self._safe_load, name="model-preload", daemon=True
        )
        thread.start()

    def _safe_load(self) -> None:
        """Acquire the load lock and load the model.

        Never blocks: when another thread is already loading, this returns
        immediately.
        """
        if self._model is not None or self._shutdown or self._loading:
            return
        if not self._load_lock.acquire(blocking=False):
            return
        self._loading = True
        try:
            self._load_model()
        finally:
            self._loading = False
            self._load_lock.release()

    def _kv_cache_type(self, raw: str) -> int:
        """Map a KV cache type string (e.g. ``q8_0``) to the llama.cpp enum.

        :param raw: the configured cache type name
        :return: the matching ``GGML_TYPE_*`` integer, defaulting to Q8_0
        """
        from llama_cpp import llama_cpp as _llama_cpp

        value: int | None = getattr(_llama_cpp, f"GGML_TYPE_{raw.strip().upper()}", None)
        if value is None:
            return _llama_cpp.GGML_TYPE_Q8_0
        return int(value)

    def _load_model(self) -> None:
        """Download if needed and load the GGUF model with all flags.

        Callers hold the load lock. Never raises: failures leave the detector
        unavailable so the rest of the pipeline keeps working.
        """
        if self._model is not None or self._shutdown:
            return
        try:
            try:
                from llama_cpp import Llama
            except ImportError as exc:
                self._record_failure("llama_cpp_import_failed", str(exc))
                return
            try:
                model_path: str = self._ensure_model_downloaded()
                threads: int = self._get_optimal_threads()
                self._log_info(
                    "Loading model",
                    path=model_path,
                    context_size=self._settings.model_context_size,
                    threads=threads,
                    kv_cache_type=self._settings.model_cache_type_k,
                    flash_attn=self._settings.model_flash_attn,
                    mlock=self._settings.model_mlock,
                )
                start: float = time.time()
                self._model = Llama(
                    model_path=model_path,
                    n_ctx=self._settings.model_context_size,
                    n_threads=threads,
                    n_batch=self._settings.model_batch_size,
                    n_gpu_layers=0,
                    type_k=self._kv_cache_type(self._settings.model_cache_type_k),
                    type_v=self._kv_cache_type(self._settings.model_cache_type_v),
                    flash_attn=self._settings.model_flash_attn,
                    mlock=self._settings.model_mlock,
                    logits_all=False,
                    embedding=False,
                )
                self._last_used = time.time()
                self._chat_template = self._compile_chat_template()
                self._log_info("Model loaded", load_seconds=round(time.time() - start, 2))
                self._warm_up()
            except Exception as exc:  # pragma: no cover - varies by platform
                self._model = None
                self._record_failure("model_load_failed", str(exc))
        finally:
            self._loading = False

    def _compile_chat_template(self) -> Any | None:
        """Compile the model's Jinja2 chat template, if it exposes one.

        :return: a compiled template, or None when unavailable
        """
        assert self._model is not None
        raw: str = str(self._model.metadata.get("tokenizer.chat_template", ""))
        if not raw:
            return None
        try:
            from jinja2 import Template
        except ImportError:  # pragma: no cover - jinja2 is a llama-cpp-python dep
            return None
        return Template(raw)

    def _warm_up(self) -> None:
        """Run a tiny generation to force model initialization."""
        if self._model is not None:
            with self._infer_lock:
                self._model(self._build_prompt("warmup"), temperature=0.0, max_tokens=1)

    def _ensure_model_downloaded(self) -> str:
        """Return the local model path, downloading it when configured as auto.

        :return: the path to the GGUF file
        :raises FileNotFoundError: when an explicit path is missing
        :raises RuntimeError: when every download source fails
        """
        model_dir: Path = Path(self._settings.model_dir)
        model_dir.mkdir(parents=True, exist_ok=True)

        # Model registry selection: when a runtime view exposes an explicit
        # active GGUF path it wins over both the static MODEL_PATH and the
        # auto-download flow.
        active_path: str = str(getattr(self._settings, "active_gguf_path", "") or "")
        if active_path:
            selected: Path = Path(active_path)
            if selected.is_file():
                return str(selected)
            raise FileNotFoundError(f"Active model not found at {selected}")

        if self._settings.model_path != "auto":
            explicit: Path = Path(self._settings.model_path)
            if explicit.exists():
                return str(explicit)
            raise FileNotFoundError(f"Model not found at {explicit}")

        local_path: Path = model_dir / self._settings.model_filename
        if local_path.exists():
            self._log_info("Model found locally", path=str(local_path))
            return str(local_path)

        self._log_info(
            "Model not present, starting download",
            filename=self._settings.model_filename,
            repo=self._settings.model_primary_repo,
        )
        endpoint: str = self._get_working_endpoint()
        if "modelscope" in endpoint:
            try:
                return self._download_from_modelscope(model_dir)
            except Exception:
                return self._download_with_retry(
                    self._settings.model_primary_repo,
                    self._settings.model_filename,
                    model_dir,
                    self._settings.hf_mirror,
                )
        return self._download_with_retry(
            self._settings.model_primary_repo,
            self._settings.model_filename,
            model_dir,
            endpoint,
        )

    def _get_working_endpoint(self) -> str:
        """Probe configured endpoints and return the first reachable one.

        :return: a reachable endpoint, defaulting to the primary
        """
        endpoints: list[str] = [
            self._settings.hf_endpoint,
            self._settings.hf_mirror,
            self._settings.modelscope_endpoint,
        ]
        for endpoint in endpoints:
            try:
                response = requests.head(f"{endpoint}/api/models", timeout=5, allow_redirects=True)
                if response.status_code < 500:
                    self._log_info("Using model endpoint", endpoint=endpoint)
                    return endpoint
            except Exception:
                continue
        self._log_warning("No reachable model endpoint found, using primary", endpoint=endpoints[0])
        return endpoints[0]

    def _download_with_retry(self, repo: str, filename: str, model_dir: Path, endpoint: str) -> str:
        """Download with exponential backoff (1s, 2s, 4s).

        :param repo: Hugging Face repository id
        :param filename: file to download
        :param model_dir: local cache directory
        :param endpoint: base endpoint to download from
        :return: the local file path
        """
        last_error: Exception | None = None
        for attempt in range(_MAX_DOWNLOAD_RETRIES):
            try:
                return self._download_from_huggingface(repo, filename, model_dir, endpoint)
            except Exception as exc:
                last_error = exc
                if attempt == _MAX_DOWNLOAD_RETRIES - 1:
                    break
                delay: float = float(2**attempt)
                self._log_warning(
                    "Download attempt failed, retrying",
                    attempt=attempt + 1,
                    delay_seconds=delay,
                    error=str(exc),
                )
                time.sleep(delay)
        raise RuntimeError(
            f"Failed to download model {filename} after {_MAX_DOWNLOAD_RETRIES} "
            f"attempts: {last_error}"
        )

    def _download_from_huggingface(
        self, repo: str, filename: str, model_dir: Path, endpoint: str
    ) -> str:
        """Download a file from Hugging Face, trying the fallback repository.

        :param repo: primary repository id
        :param filename: file to download
        :param model_dir: local cache directory
        :param endpoint: base endpoint to download from
        :return: the local file path
        """
        if hf_hub_download is None:
            raise ImportError("huggingface_hub is not installed")
        os.environ["HF_ENDPOINT"] = endpoint
        try:
            local_path: str = hf_hub_download(
                repo_id=repo,
                filename=filename,
                local_dir=str(model_dir),
                etag_timeout=30,
            )
            self._log_info("Download complete", path=local_path)
            return local_path
        except Exception as primary_error:
            fallback_repo: str = self._settings.model_fallback_repo
            self._log_warning(
                "Primary repository failed, trying fallback",
                repo=repo,
                fallback_repo=fallback_repo,
                error=str(primary_error),
            )
            local_path = hf_hub_download(
                repo_id=fallback_repo,
                filename=filename,
                local_dir=str(model_dir),
                etag_timeout=30,
            )
            self._log_info("Download complete from fallback", path=local_path)
            return local_path

    def _download_from_modelscope(self, model_dir: Path) -> str:
        """Download from ModelScope, mapping the Hugging Face repo id.

        :param model_dir: local cache directory
        :return: the local GGUF file path
        """
        try:
            from modelscope.hub.snapshot_download import snapshot_download
        except ImportError as exc:
            raise RuntimeError("modelscope is not installed") from exc

        repo: str = self._settings.model_primary_repo
        ms_repo: str = repo.replace("bartowski/", "Qwen/", 1)
        self._log_info("Downloading from ModelScope", repo=ms_repo)
        snapshot_download(model_id=ms_repo, cache_dir=str(model_dir), revision="master")
        gguf_files: list[Path] = [
            path
            for path in model_dir.rglob("*")
            if path.is_file() and _GGUF_PATTERN.search(path.name)
        ]
        if not gguf_files:
            raise FileNotFoundError(f"GGUF file not found in {model_dir}")
        return str(gguf_files[0])

    def _get_optimal_threads(self) -> int:
        """Compute the thread count for inference.

        ``auto`` uses one fewer thread than the CPU core count, leaving a core
        free for I/O.

        :return: the thread count
        """
        configured: str = str(self._settings.model_threads)
        if configured.isdigit() and int(configured) > 0:
            return int(configured)
        cpu_count: int = os.cpu_count() or 4
        return max(1, cpu_count - 1)

    @property
    def name(self) -> str:
        """Return the detector name."""
        return "llama_cpp"

    @property
    def last_prompt(self) -> str | None:
        """Return the most recent prompt sent to the model."""
        return self._last_prompt

    @property
    def last_reply(self) -> str | None:
        """Return the most recent raw model reply."""
        return self._last_reply

    @property
    def priority(self) -> int:
        """Return the pipeline position."""
        return 8

    @property
    def language(self) -> str:
        """Return the language scope."""
        return "any"

    @property
    def blocking(self) -> bool:
        """Model verdicts are decisive at Level 2."""
        return True

    def is_available(self) -> bool:
        """Whether the model loaded successfully."""
        return self._model is not None

    def download_model(self) -> str:
        """Download the configured model and return its local path.

        :return: the path to the GGUF file
        :raises RuntimeError: when every download source fails
        """
        return self._ensure_model_downloaded()

    @staticmethod
    def sanitize(text: str) -> str:
        """Sanitize text against prompt injection before inference.

        Removes chat control tokens, strips leading system/user/assistant
        prefixes, and XML-escapes metacharacters.

        :param text: raw user text
        :return: a safe payload for the model
        """
        cleaned: str = _CONTROL_TOKEN_PATTERN.sub("", text)
        cleaned = _TOKEN_PREFIX_PATTERN.sub("", cleaned)
        return xml.sax.saxutils.escape(cleaned, {'"': "&quot;"})

    def _build_prompt(self, text: str) -> str:
        """Compose the classification prompt from the model chat template.

        Thinking is disabled through the template (``enable_thinking=False``)
        so the model replies with a verdict token instead of a long reasoning
        block. Falls back to a hand-built ChatML prompt when the model has no
        usable template.

        :param text: raw user text
        :return: the full prompt with the sanitized payload
        """
        payload: str = LlamaCppDetector.sanitize(text)
        if self._chat_template is not None:
            return self._chat_template.render(
                messages=[
                    {"role": "system", "content": self._system_prompt},
                    {"role": "user", "content": payload},
                ],
                add_generation_prompt=True,
                enable_thinking=False,
            )
        return build_classification_prompt(payload, system_prompt=self._system_prompt)

    def _check_idle_unload(self) -> None:
        """Unload the model after the idle timeout to free memory."""
        if self._model is None or self._last_used == 0:
            return
        idle_seconds: float = time.time() - self._last_used
        if idle_seconds > self._settings.model_idle_timeout_seconds:
            self._log_info("Model idle, unloading", idle_seconds=round(idle_seconds, 1))
            self.shutdown()

    def _ensure_loaded(self) -> None:
        """Load the model if it is not loaded and no load is in progress."""
        self._safe_load()

    def detect(self, text: str) -> DetectionResult:
        """Classify the text with the local model.

        The llama.cpp ``Llama`` object is not safe for concurrent generation,
        so every inference (including the idle check and lazy load) runs under
        a dedicated lock. This serializes model calls across the worker thread
        pool, preventing the KV-cache corruption and native stack panics that
        concurrent generation can trigger on newer Python releases.

        :param text: normalized input text
        :return: a positive result when the model replies BLOCK
        """
        with self._infer_lock:
            return self._detect_locked(text)

    def _detect_locked(self, text: str) -> DetectionResult:
        """Run one classification while holding the inference lock.

        :param text: normalized input text
        :return: a positive result when the model replies BLOCK
        """
        self._check_idle_unload()
        self._ensure_loaded()
        if self._model is None:
            return DetectionResult(matched=False)
        self._last_used = time.time()
        try:
            prompt: str = self._build_prompt(text)
            output: dict[str, Any] = self._model(
                prompt,
                temperature=0.0,
                max_tokens=self._settings.model_max_tokens,
            )
            reply: str = output["choices"][0]["text"].strip().upper()
            self._last_prompt = prompt
            self._last_reply = reply
        except Exception:
            return DetectionResult(matched=False)
        if "</think>" in reply:
            reply = reply.split("</think>")[-1].strip().upper()
        blocked: bool = "BLOCK" in reply
        return DetectionResult(
            matched=blocked,
            reason="LLM classified the text as BLOCK" if blocked else None,
            confidence_score=0.9 if blocked else None,
        )

    def reload(self) -> None:
        """No-op: the model is independent of the word bank."""

    def shutdown(self) -> None:
        """Release the model and its memory."""
        if self._model is not None:
            try:
                self._model.close()
            except Exception:
                pass
            self._model = None
        self._shutdown = True

    def _record_failure(self, event: str, detail: str) -> None:
        """Emit a structured warning when the model cannot be used.

        :param event: short event name
        :param detail: failure detail
        """
        self._log_warning(f"llama:{event}", detail=detail)

    def _log_info(self, message: str, **fields: Any) -> None:
        """Emit a structured info record.

        :param message: log message
        :param fields: structured fields
        """
        if self._logger is not None:
            self._logger.log(20, f"llama:{message}", **fields)

    def _log_warning(self, message: str, **fields: Any) -> None:
        """Emit a structured warning record.

        :param message: log message
        :param fields: structured fields
        """
        if self._logger is not None:
            self._logger.log(30, f"llama:{message}", **fields)
