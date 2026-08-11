"""Admin REST endpoints for word banks, logs, and service control."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import APIRouter

from app.admin.logs import create_logs_router
from app.admin.wordbank import create_wordbank_router
from app.admin.wordlist import create_wordlist_router


def create_admin_router(
    engine: Any, word_bank: Any, log_file_path: str, auth_dependency: Any
) -> APIRouter:
    """Compose every admin router into one APIRouter.

    :param engine: the moderation engine
    :param word_bank: the shared word bank manager
    :param log_file_path: path to the audit log file
    :param auth_dependency: FastAPI dependency guarding the routes
    :return: the combined admin router
    """
    router: APIRouter = APIRouter()
    router.include_router(create_wordlist_router(word_bank, auth_dependency))
    router.include_router(create_wordbank_router(engine, word_bank, log_file_path, auth_dependency))
    router.include_router(create_logs_router(str(Path(log_file_path).parent), auth_dependency))
    return router
