"""GGUF model registry backing the admin model management page.

Multiple GGUF files coexist under ``MODEL_DIR``; administrators register
them by server-side path, browser upload, or Hugging Face download, and
activate one at a time. Activation writes ``ACTIVE_GGUF_PATH`` through the
runtime settings service so the local provider picks the file up without
a restart.
"""

from __future__ import annotations

import os
import sqlite3
import threading
import time
from pathlib import Path
from typing import Any

import requests

try:
    from huggingface_hub import hf_hub_download
except ImportError:  # pragma: no cover - huggingface_hub is a declared dependency
    hf_hub_download = None

_GGUF_SUFFIX: str = ".gguf"
_DOWNLOAD_RETRIES: int = 3


class ModelRegistryService:
    """Tracks registered GGUF models and the active selection.

    :param settings: application settings holding MODEL_DIR and repo defaults
    :param settings_service: runtime settings used for activation
    :param logger: optional structured logger
    """

    _SCHEMA = """
        CREATE TABLE IF NOT EXISTS models (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE,
            path TEXT,
            repo TEXT,
            filename TEXT,
            size_bytes INTEGER DEFAULT 0,
            status TEXT DEFAULT 'registered',
            detail TEXT DEFAULT '',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """

    def __init__(self, settings: Any, settings_service: Any, logger: Any | None = None) -> None:
        self._settings: Any = settings
        self._settings_service: Any = settings_service
        self._logger: Any = logger
        self._db_path: str = settings.model_registry_db_path
        Path(self._db_path).parent.mkdir(parents=True, exist_ok=True)
        self._connection: sqlite3.Connection = sqlite3.connect(
            self._db_path, check_same_thread=False
        )
        self._connection.execute("PRAGMA journal_mode=WAL")
        self._connection.executescript(ModelRegistryService._SCHEMA)
        self._connection.commit()

    def list_models(self) -> list[dict[str, Any]]:
        """Return every registered model.

        :return: model rows ordered newest first
        """
        rows = self._connection.execute(
            "SELECT id, name, path, repo, filename, size_bytes, status, detail, created_at "
            "FROM models ORDER BY id DESC"
        ).fetchall()
        active_path: str = str(self._settings_service.get("ACTIVE_GGUF_PATH", "") or "")
        return [
            {
                "id": row[0],
                "name": row[1],
                "path": row[2],
                "repo": row[3],
                "filename": row[4],
                "size_bytes": row[5],
                "status": row[6],
                "detail": row[7],
                "created_at": row[8],
                "exists": bool(row[2]) and Path(str(row[2])).exists(),
                "active": bool(row[2]) and str(row[2]) == active_path,
            }
            for row in rows
        ]

    def get_model(self, model_id: int) -> dict[str, Any] | None:
        """Return one registered model.

        :param model_id: the model row id
        :return: the model mapping, or None when unknown
        """
        models: list[dict[str, Any]] = [m for m in self.list_models() if m["id"] == model_id]
        return models[0] if models else None

    def register_path(self, name: str, path: str) -> int:
        """Register a GGUF file that already exists on the server disk.

        :param name: display name for the admin UI
        :param path: absolute path of the GGUF file
        :return: the new model id
        :raises ValueError: when the name is taken or the file is invalid
        """
        self._ensure_name_free(name)
        file_path: Path = Path(path)
        if not file_path.is_file():
            raise ValueError(f"Model file not found: {path}")
        if not file_path.name.lower().endswith(_GGUF_SUFFIX):
            raise ValueError("Only .gguf files can be registered")
        cursor = self._connection.execute(
            "INSERT INTO models (name, path, size_bytes, status) VALUES (?, ?, ?, 'ready')",
            (name, str(file_path), file_path.stat().st_size),
        )
        self._connection.commit()
        return int(cursor.lastrowid)

    def register_download(self, name: str, repo: str, filename: str) -> int:
        """Register a model and start a background Hugging Face download.

        :param name: display name for the admin UI
        :param repo: Hugging Face repository id
        :param filename: GGUF file name inside the repository
        :return: the new model id
        :raises ValueError: when the name is taken
        """
        self._ensure_name_free(name)
        cursor = self._connection.execute(
            "INSERT INTO models (name, repo, filename, status) VALUES (?, ?, ?, 'downloading')",
            (name, repo, filename),
        )
        self._connection.commit()
        model_id: int = int(cursor.lastrowid)
        thread: threading.Thread = threading.Thread(
            target=self._run_download, args=(model_id, repo, filename), daemon=True
        )
        thread.start()
        return model_id

    def attach_upload(self, name: str, path: str) -> int:
        """Register an uploaded GGUF written to MODEL_DIR by the API layer.

        :param name: display name for the admin UI
        :param path: server-side path where the upload was saved
        :return: the new model id
        """
        return self.register_path(name, path)

    def delete(self, model_id: int) -> None:
        """Remove a registration; clears the active pointer when needed.

        The underlying file is never deleted from disk.

        :param model_id: the model row id
        :raises ValueError: when the id is unknown
        """
        model: dict[str, Any] | None = self.get_model(model_id)
        if model is None:
            raise ValueError(f"Unknown model: {model_id}")
        with self._connection:
            self._connection.execute("DELETE FROM models WHERE id = ?", (model_id,))
        if model["active"]:
            self._settings_service.update({"ACTIVE_GGUF_PATH": ""}, source="model_registry")

    def activate(self, model_id: int) -> dict[str, Any]:
        """Point the local provider at a registered, ready model.

        :param model_id: the model row id
        :return: the activated model mapping
        :raises ValueError: when the id is unknown or the file is missing
        """
        model: dict[str, Any] | None = self.get_model(model_id)
        if model is None:
            raise ValueError(f"Unknown model: {model_id}")
        if not model["path"] or not Path(str(model["path"])).is_file():
            raise ValueError(f"Model file is not available: {model['path']}")
        self._settings_service.update(
            {"ACTIVE_GGUF_PATH": str(model["path"])}, source="model_registry"
        )
        return model

    def _ensure_name_free(self, name: str) -> None:
        """Raise when a model name is already registered.

        :param name: candidate display name
        :raises ValueError: when the name exists
        """
        row = self._connection.execute("SELECT id FROM models WHERE name = ?", (name,)).fetchone()
        if row is not None:
            raise ValueError(f"Model name already registered: {name}")

    def _set_status(self, model_id: int, status: str, detail: str = "", path: str = "") -> None:
        """Update a model row's status, detail, and optionally its path.

        :param model_id: the model row id
        :param status: new status value
        :param detail: human-readable detail (error message on failure)
        :param path: local file path once the download finished
        """
        if path:
            self._connection.execute(
                "UPDATE models SET status = ?, detail = ?, path = ?, size_bytes = ? WHERE id = ?",
                (
                    status,
                    detail,
                    path,
                    Path(path).stat().st_size if Path(path).is_file() else 0,
                    model_id,
                ),
            )
        else:
            self._connection.execute(
                "UPDATE models SET status = ?, detail = ? WHERE id = ?",
                (status, detail, model_id),
            )
        self._connection.commit()

    def _run_download(self, model_id: int, repo: str, filename: str) -> None:
        """Download a model in the background and record the outcome.

        :param model_id: the model row id
        :param repo: Hugging Face repository id
        :param filename: GGUF file name inside the repository
        """
        try:
            path: str = self._download(repo, filename)
            self._set_status(model_id, "ready", "", path)
            self._log(20, "download_complete", model_id=model_id, path=path)
        except Exception as exc:
            self._set_status(model_id, "failed", str(exc))
            self._log(30, "download_failed", model_id=model_id, error=str(exc))

    def _download(self, repo: str, filename: str) -> str:
        """Download one GGUF from Hugging Face with mirror fallback.

        ModelScope is intentionally not used here: registry downloads target
        explicit repo/file pairs that the HF endpoints serve directly.

        :param repo: primary Hugging Face repository id
        :param filename: GGUF file name inside the repository
        :return: the local file path
        :raises RuntimeError: when every attempt fails
        """
        if hf_hub_download is None:
            raise RuntimeError("huggingface_hub is not installed")
        model_dir: Path = Path(self._settings.model_dir)
        model_dir.mkdir(parents=True, exist_ok=True)
        last_error: Exception | None = None
        for endpoint in self._endpoints():
            os.environ["HF_ENDPOINT"] = endpoint
            for attempt in range(_DOWNLOAD_RETRIES):
                try:
                    return str(
                        hf_hub_download(
                            repo_id=repo,
                            filename=filename,
                            local_dir=str(model_dir),
                            etag_timeout=30,
                        )
                    )
                except Exception as exc:
                    last_error = exc
                    time.sleep(2**attempt)
        raise RuntimeError(f"Failed to download {filename}: {last_error}")

    def _endpoints(self) -> list[str]:
        """Return the configured HF endpoints in probe order."""
        return [self._settings.hf_endpoint, self._settings.hf_mirror]

    def _log(self, level: int, message: str, **fields: Any) -> None:
        """Emit a structured log record when a logger is attached.

        :param level: numeric logging level
        :param message: log message
        :param fields: structured fields
        """
        if self._logger is not None:
            self._logger.log(level, f"registry:{message}", **fields)

    @staticmethod
    def probe_url(url: str, timeout: float = 5.0) -> bool:
        """Return whether a URL answers with a non-server-error status.

        Exposed for tests and health tooling.

        :param url: the URL to probe
        :param timeout: request timeout in seconds
        :return: reachability flag
        """
        try:
            response = requests.head(url, timeout=timeout, allow_redirects=True)
            return response.status_code < 500
        except Exception:
            return False

    def close(self) -> None:
        """Close the underlying database connection."""
        self._connection.close()
