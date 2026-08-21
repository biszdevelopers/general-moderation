"""Model management admin endpoints.

Backs the admin Models page: registry CRUD, GGUF upload and download,
activation, and provider health reporting.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import APIRouter, HTTPException, UploadFile, status
from pydantic import BaseModel

_GGUF_SUFFIX: str = ".gguf"


class RegisterModelRequest(BaseModel):
    """Register a GGUF that already exists on the server disk.

    :param name: display name for the admin UI
    :param path: absolute path of the GGUF file
    """

    name: str
    path: str


class DownloadModelRequest(BaseModel):
    """Register and download a GGUF from Hugging Face.

    :param name: display name for the admin UI
    :param repo: Hugging Face repository id
    :param filename: GGUF file name inside the repository
    """

    name: str
    repo: str
    filename: str


def create_models_router(  # noqa: C901 - one handler per endpoint, many typed branches
    registry: Any,
    router: Any,
    model_dir: str,
    auth_dependency: Any,
) -> APIRouter:
    """Build the model management admin router.

    :param registry: the ModelRegistryService
    :param router: the ModelRouter providing health status
    :param model_dir: directory where uploaded GGUF files are stored
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the configured APIRouter
    """
    api: APIRouter = APIRouter(
        prefix="/admin/models", tags=["admin"], dependencies=[auth_dependency]
    )

    @api.get("")
    def list_models() -> dict[str, Any]:
        """Return every registered model plus provider health.

        :return: models list and routed provider status
        """
        return {"models": registry.list_models(), "providers": router.status()}

    @api.get("/health")
    def health() -> dict[str, Any]:
        """Probe the active and backup providers.

        :return: per-provider availability summary
        """
        return router.status()

    @api.post("/register", status_code=status.HTTP_201_CREATED)
    def register(payload: RegisterModelRequest) -> dict[str, Any]:
        """Register a GGUF file already present on the server.

        :param payload: name and absolute server-side path
        :return: the created model row
        :raises HTTPException: 400 for invalid names or missing files
        """
        try:
            model_id: int = registry.register_path(payload.name, payload.path)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"status": "ok", "model": registry.get_model(model_id)}

    @api.post("/download", status_code=status.HTTP_202_ACCEPTED)
    def download(payload: DownloadModelRequest) -> dict[str, Any]:
        """Start a background Hugging Face download.

        :param payload: display name, repository id, and GGUF file name
        :return: the created model row in downloading state
        :raises HTTPException: 400 for duplicate names
        """
        try:
            model_id: int = registry.register_download(payload.name, payload.repo, payload.filename)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"status": "downloading", "model": registry.get_model(model_id)}

    @api.post("/upload", status_code=status.HTTP_201_CREATED)
    async def upload(name: str, file: UploadFile) -> dict[str, Any]:
        """Upload a GGUF file and register it.

        :param name: display name for the admin UI
        :param file: the uploaded GGUF file
        :return: the created model row
        :raises HTTPException: 400 for a missing or non-GGUF upload
        """
        filename: str = Path(file.filename or "").name
        if not filename.lower().endswith(_GGUF_SUFFIX):
            raise HTTPException(status_code=400, detail="Only .gguf files can be uploaded")
        destination: Path = Path(model_dir) / filename
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("wb") as handle:
            while True:
                chunk: bytes = await file.read(1024 * 1024)
                if not chunk:
                    break
                handle.write(chunk)
        try:
            model_id: int = registry.attach_upload(name, str(destination))
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        return {"status": "ok", "model": registry.get_model(model_id)}

    @api.post("/{model_id}/activate")
    def activate(model_id: int) -> dict[str, Any]:
        """Point the local provider at a registered model.

        :param model_id: the model row id
        :return: the activated model row
        :raises HTTPException: 400 for unknown ids or missing files
        """
        try:
            model: dict[str, Any] = registry.activate(model_id)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        router.refresh()
        return {"status": "ok", "model": model}

    @api.delete("/{model_id}")
    def delete(model_id: int) -> dict[str, Any]:
        """Remove a registration without deleting the file on disk.

        :param model_id: the model row id
        :return: deletion confirmation
        :raises HTTPException: 400 for unknown ids
        """
        was_active: bool = bool(
            registry.get_model(model_id) and registry.get_model(model_id)["active"]
        )
        try:
            registry.delete(model_id)
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        if was_active:
            router.refresh()
        return {"status": "ok"}

    return api
