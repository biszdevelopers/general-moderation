"""FastAPI application entry point.

The engine is constructed at import time so Gunicorn's ``preload_app`` loads
the llama.cpp model once before forking workers. Public endpoints are async
and offload CPU-bound detection to the thread pool; all admin routes are
guarded by the constant-time API key dependency.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from starlette.concurrency import run_in_threadpool

from app.admin import create_admin_router
from app.config import Settings
from app.engine.moderation_engine import ModerationEngine
from app.models.request import BatchModerationRequest, ModerationRequest
from app.models.response import BatchModerationResponse, ModerationResponse
from app.security.auth import RequireAdminApiKey
from app.security.headers import SecurityHeadersMiddleware
from app.security.ratelimit import RateLimiter
from app.utils.logger import ModerationLogger
from app.wordbank.manager import WordBankManager
from app.wordbank.storage import create_storage

load_dotenv()
SETTINGS: Settings = Settings()
SETTINGS.validate_security()
SETTINGS.ensure_directories()

LOGGER: ModerationLogger = ModerationLogger(
    file_path=SETTINGS.log_file_path,
    level=SETTINGS.log_level,
    max_bytes=SETTINGS.log_max_bytes,
    backup_count=SETTINGS.log_backup_count,
)

STORAGE = create_storage(SETTINGS.custom_words_storage, SETTINGS.custom_words_path)
WORD_BANK: WordBankManager = WordBankManager(
    storage=STORAGE,
    bloom_capacity=SETTINGS.bloom_filter_capacity,
    bloom_error_rate=SETTINGS.bloom_filter_error_rate,
    logger=LOGGER,
)
ENGINE: ModerationEngine = ModerationEngine(SETTINGS, WORD_BANK, LOGGER)

RATE_LIMITER: RateLimiter = RateLimiter(
    requests=SETTINGS.rate_limit_requests,
    period_seconds=SETTINGS.rate_limit_period,
)

ADMIN_AUTH = Depends(RequireAdminApiKey(SETTINGS.admin_api_key))


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Yield control to the application then release resources.

    :param app: the FastAPI application
    """
    yield
    ENGINE.shutdown()


app: FastAPI = FastAPI(
    title="Multi-Language Moderation Service",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=SETTINGS.allowed_origins,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "X-API-Key"],
    allow_credentials=False,
    max_age=600,
)
app.add_middleware(SecurityHeadersMiddleware)

app.state.limiter = RATE_LIMITER.limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(create_admin_router(ENGINE, WORD_BANK, SETTINGS.log_file_path, ADMIN_AUTH))


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded) -> ORJSONResponse:
    """Return a 429 and record the violation.

    :param request: the rate-limited request
    :param exc: the raised exception
    :return: a 429 JSON response
    """
    ENGINE.record_rate_limit_hit()
    return ORJSONResponse({"detail": "Rate limit exceeded"}, status_code=429)


@app.get("/")
def root() -> dict[str, str]:
    """Return a lightweight liveness response.

    :return: service name and status
    """
    return {"service": "multi-language-moderation", "status": "ok"}


@app.post("/moderate", response_model=ModerationResponse)
@RATE_LIMITER.limit()
async def moderate(request: Request, payload: ModerationRequest) -> ModerationResponse:
    """Moderate a single message.

    :param request: the ASGI request (used for rate limiting)
    :param payload: the message to moderate
    :return: the moderation verdict
    """
    return await run_in_threadpool(ENGINE.moderate, payload)


@app.post("/moderate/batch", response_model=BatchModerationResponse)
@RATE_LIMITER.limit()
async def moderate_batch(
    request: Request, payload: BatchModerationRequest
) -> BatchModerationResponse:
    """Moderate a batch of messages.

    :param request: the ASGI request (used for rate limiting)
    :param payload: the batch of messages to moderate
    :return: per-item verdicts and the total latency
    """
    return await run_in_threadpool(ENGINE.moderate_batch, payload)
