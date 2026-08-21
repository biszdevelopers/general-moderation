"""Admin REST endpoints for word banks, logs, settings, and service control."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from fastapi import APIRouter

from app.admin.appconfig_router import create_appconfig_router
from app.admin.export_router import create_export_router
from app.admin.feedback_router import create_feedback_router
from app.admin.logs import create_logs_router
from app.admin.models_router import create_models_router
from app.admin.phrases_router import create_phrases_router
from app.admin.prompt_router import create_prompt_router
from app.admin.semantic_router import create_semantic_router
from app.admin.settings_router import create_settings_router
from app.admin.stats_router import create_stats_router
from app.admin.wordbank import create_wordbank_router
from app.admin.wordlist import create_wordlist_router


def create_admin_router(
    engine: Any,
    word_bank: Any,
    log_file_path: str,
    auth_dependency: Any,
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
    router.include_router(
        create_settings_router(engine._settings_service, auth_dependency, engine=engine)
    )
    router.include_router(create_feedback_router(engine._feedback, auth_dependency))
    router.include_router(
        create_appconfig_router(engine._app_config, auth_dependency, engine=engine)
    )
    router.include_router(create_semantic_router(engine._semantic, auth_dependency))
    router.include_router(create_phrases_router(engine._phrases, auth_dependency, engine=engine))
    router.include_router(
        create_export_router(
            engine._export,
            engine,
            engine._semantic,
            engine._settings_service,
            auth_dependency,
        )
    )
    router.include_router(
        create_stats_router(engine, word_bank, engine._feedback, log_file_path, auth_dependency)
    )
    router.include_router(
        create_models_router(
            engine._model_registry,
            engine._model_router,
            engine._settings.model_dir,
            auth_dependency,
        )
    )
    router.include_router(
        create_prompt_router(
            engine._prompt_store,
            engine.apply_prompt,
            auth_dependency,
        )
    )
    return router
