"""Global pytest fixtures.

Session-scoped where the object is read-only and expensive, function-scoped
where each test needs isolation (SQLite files, word bank state, profile rows).
All paths point into a per-test temporary directory so the suite never touches
real ``data/``, ``logs/``, or ``models/``.
"""

from __future__ import annotations

import shutil
import sys
from collections.abc import Callable, Generator, Iterator
from pathlib import Path
from typing import Any

import pytest
from fastapi import Depends, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
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


def _build_settings(root: Path) -> Settings:
    """Create settings whose every data path lives under ``root``."""
    data: Path = root / "data"
    for directory in ("models", "logs", "exports", "semantic", "data"):
        (root / directory).mkdir(parents=True, exist_ok=True)
    return Settings(
        app_host="127.0.0.1",
        app_port=0,
        frontend_dist_path=str(root / "nodist"),
        safe_word_list_path=str(data / "safe_words.txt"),
        model_dir=str(root / "models"),
        model_path=str(root / "models/none.gguf"),
        model_context_size=2048,
        model_batch_size=32,
        model_max_tokens=2,
        model_idle_timeout_seconds=60,
        hf_endpoint="http://127.0.0.1:1",
        hf_mirror="http://127.0.0.1:2",
        modelscope_endpoint="http://127.0.0.1:3",
        cache_max_size=10,
        cache_ttl_seconds=60,
        bloom_filter_capacity=100_000,
        bloom_filter_error_rate=0.01,
        user_db_path=str(data / "users.db"),
        user_archive_db_path=str(data / "archive.db"),
        feedback_db_path=str(data / "feedback.db"),
        settings_db_path=str(data / "settings.db"),
        app_config_db_path=str(data / "config.db"),
        custom_words_path=str(data / "custom_words.db"),
        log_file_path=str(root / "logs" / "moderation.log"),
        export_temp_dir=str(root / "exports"),
        semantic_index_dir=str(root / "semantic"),
        sensitive_stop_words_dir=str(root / "none"),
        admin_api_key="test-admin-key",
        webui_api_key="test-webui-key",
        secret_key="test-secret-key",
        encryption_key="0" * 64,
        rate_limit_requests=100_000,
        rate_limit_period=60,
        allowed_origins=["http://localhost:3000", "https://mod.example.com"],
        log_max_bytes=1_000_000,
    )


@pytest.fixture(scope="session")
def db_template(tmp_path_factory: pytest.TempPathFactory) -> Path:
    """Pre-seeded SQLite database files shared by every test.

    Creating and seeding the settings, app-config, profiler, feedback and
    custom-words databases costs ~130 ms per test. This fixture builds them
    once for the whole session; the per-test ``settings`` fixture copies the
    files into its sandbox, so services open existing, schema-complete
    databases instead of creating and seeding them from scratch. Isolation is
    unchanged: each test still gets its own copy.
    """
    from app.appconfig.app_config_service import AppConfigService
    from app.feedback.feedback_service import FeedbackService
    from app.profiling.user_profiler import UserProfiler
    from app.settings_service import SettingsService
    from app.utils.logger import ModerationLogger

    root: Path = tmp_path_factory.mktemp("db_template")
    template_settings: Settings = _build_settings(root)
    logger: ModerationLogger = ModerationLogger(
        str(root / "logs" / "template.log"), max_bytes=100_000
    )
    settings_service: SettingsService = SettingsService(template_settings)
    app_config: AppConfigService = AppConfigService(template_settings.app_config_db_path)
    profiler: UserProfiler = UserProfiler(
        template_settings.user_db_path,
        template_settings.user_archive_db_path,
        template_settings.user_window_days,
    )
    feedback: FeedbackService = FeedbackService(
        template_settings, settings_service, app_config, logger
    )
    storage: Any = create_storage("sqlite", template_settings.custom_words_path)
    settings_service.close()
    app_config.close()
    profiler.close()
    feedback.close()
    storage.close()
    logger.close()
    return root / "data"


def _copy_db_template(tmp_path: Path, template: Path) -> None:
    """Copy the pre-seeded database files into a test sandbox.

    :param tmp_path: the per-test temporary directory
    :param template: the session template ``data`` directory
    """
    for source in template.iterdir():
        if source.is_file():
            shutil.copy2(source, tmp_path / "data" / source.name)


@pytest.fixture()
def settings(tmp_path: Path, db_template: Path) -> Settings:
    """Per-test settings isolated under a temporary directory.

    The pre-seeded databases from ``db_template`` are copied into the sandbox
    so the services these settings point at initialize without re-seeding.
    """
    settings_instance: Settings = _build_settings(tmp_path)
    _copy_db_template(tmp_path, db_template)
    return settings_instance


@pytest.fixture()
def logger(settings: Settings) -> Iterator[ModerationLogger]:
    """Per-test JSONL audit logger writing under the sandbox."""
    instance: ModerationLogger = ModerationLogger(
        settings.log_file_path,
        level="INFO",
        max_bytes=settings.log_max_bytes,
        backup_count=2,
    )
    yield instance
    instance.close()


@pytest.fixture()
def word_bank(settings: Settings, logger: ModerationLogger) -> Iterator[WordBankManager]:
    """Per-test word bank with an isolated SQLite storage file."""
    manager: WordBankManager = WordBankManager(
        storage=create_storage("sqlite", settings.custom_words_path),
        bloom_capacity=settings.bloom_filter_capacity,
        bloom_error_rate=settings.bloom_filter_error_rate,
        logger=logger,
    )
    yield manager
    manager.close()


@pytest.fixture()
def engine(
    settings: Settings, word_bank: WordBankManager, logger: ModerationLogger
) -> Iterator[ModerationEngine]:
    """Per-test moderation engine sharing the isolated word bank."""
    instance: ModerationEngine = ModerationEngine(settings, word_bank, logger)
    yield instance
    instance.shutdown()


@pytest.fixture(scope="session")
def settings_factory() -> Generator:
    """Factory that builds settings rooted at an arbitrary path."""
    yield _build_settings


@pytest.fixture()
def fake_semantic_modules(monkeypatch: pytest.MonkeyPatch) -> None:  # noqa: C901
    """Inject lightweight fake ``faiss`` and ``sentence_transformers`` modules.

    The real packages pull torch (hundreds of MB) and are optional; the fakes
    give ``SemanticService`` a deterministic embedding so its full add/query/
    delete surface can be exercised.

    :param monkeypatch: pytest monkeypatch fixture
    """
    import types

    import numpy as np

    class _IndexFlatIP:
        """In-memory inner-product index with L2-normalized vectors."""

        def __init__(self, dim: int) -> None:
            self.dim: int = dim
            self.ntotal: int = 0
            self._vectors: list[np.ndarray] = []

        def add(self, vectors: object) -> None:
            """Append normalized vectors.

            :param vectors: array-like of vectors
            """
            array = np.asarray(vectors, dtype="float32")
            if array.ndim == 1:
                array = array[None, :]
            self._vectors.append(array)
            self.ntotal += array.shape[0]

        def search(self, query: object, k: int) -> tuple[Any, Any]:
            """Return top-k scores and indices.

            :param query: the query vector
            :param k: number of neighbors
            :return: (scores, indices)
            """
            q = np.asarray(query, dtype="float32")
            if q.ndim == 1:
                q = q[None, :]
            all_vectors = np.vstack(self._vectors)
            scores = q @ all_vectors.T
            indices = np.argsort(-scores, axis=1)[:, :k]
            rows = []
            for row, row_idx in zip(scores, indices, strict=True):
                rows.append([float(row[i]) for i in row_idx])
            return np.array(rows, dtype="float32"), indices

    class _FakeSentenceTransformer:
        """Deterministic char-code embedder standing in for the real model."""

        def __init__(self, model_name: str) -> None:
            self._name: str = model_name

        def encode(
            self,
            texts: list[str],
            normalize_embeddings: bool = False,
            show_progress_bar: bool = False,
        ) -> Any:
            """Encode texts into L2-normalized 384-dim vectors.

            :param texts: input strings
            :param normalize_embeddings: unused, kept for signature parity
            :param show_progress_bar: unused, kept for signature parity
            :return: a stacked float32 array
            """
            vectors: list[np.ndarray] = []
            for text in texts:
                vector = np.zeros(384, dtype="float32")
                for index, char in enumerate(text[:384]):
                    vector[index] = ord(char) % 251
                norm: float = float(np.linalg.norm(vector))
                vectors.append(vector / norm if norm > 0 else vector)
            return np.stack(vectors)

    faiss_module = types.ModuleType("faiss")
    faiss_module.IndexFlatIP = _IndexFlatIP
    faiss_module.normalize_L2 = lambda vectors: vectors
    faiss_module.write_index = lambda index, path: Path(str(path)).write_bytes(b"index")
    faiss_module.read_index = lambda path: _IndexFlatIP(384)

    st_module = types.ModuleType("sentence_transformers")
    st_module.SentenceTransformer = _FakeSentenceTransformer

    monkeypatch.setitem(sys.modules, "faiss", faiss_module)
    monkeypatch.setitem(sys.modules, "sentence_transformers", st_module)


def build_app(
    engine: ModerationEngine,
    word_bank: WordBankManager,
    settings: Settings,
) -> FastAPI:
    """Assemble a FastAPI app mirroring ``app.main`` but with test components.

    Recreates the CORS, security headers, rate limiter, public endpoints, and
    the full admin router so E2E tests exercise real wiring.

    :param engine: the test moderation engine
    :param word_bank: the test word bank
    :param settings: test settings
    :return: a fully wired FastAPI app
    """
    rate_limiter: RateLimiter = RateLimiter(
        requests=settings.rate_limit_requests,
        period_seconds=settings.rate_limit_period,
    )
    auth_dependency: Any = Depends(RequireAdminApiKey(settings.admin_api_key))

    application: FastAPI = FastAPI(title="General Moderation (test)", version="1.0.0")
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Content-Type", "X-API-Key", "Authorization"],
        allow_credentials=False,
        max_age=600,
    )
    application.add_middleware(SecurityHeadersMiddleware)
    application.state.limiter = rate_limiter.limiter
    application.add_middleware(SlowAPIMiddleware)

    application.include_router(
        create_admin_router(engine, word_bank, settings.log_file_path, auth_dependency)
    )

    @application.get("/health")
    def health() -> dict[str, str]:
        """Return a lightweight health response."""
        return {"status": "healthy"}

    @application.get("/")
    def root() -> dict[str, str]:
        """Return a JSON service status when no frontend build exists."""
        return {"service": "multi-language-moderation", "status": "ok"}

    @application.get("/metrics", include_in_schema=False)
    def metrics() -> Any:
        """Return the Prometheus metrics payload."""
        from fastapi.responses import PlainTextResponse

        lines: list[str] = []
        for name, value in engine.metrics().items():
            lines.append(f"# TYPE {name} counter")
            lines.append(f"{name} {value}")
        return PlainTextResponse("\n".join(lines) + "\n", media_type="text/plain; version=0.0.4")

    @application.post("/moderate", response_model=ModerationResponse)
    @rate_limiter.limit()
    async def moderate(request: Request, payload: ModerationRequest) -> ModerationResponse:
        """Moderate a single message."""
        return await run_in_threadpool(engine.moderate, payload)

    @application.post("/moderate/batch", response_model=BatchModerationResponse)
    @rate_limiter.limit()
    async def moderate_batch(
        request: Request, payload: BatchModerationRequest
    ) -> BatchModerationResponse:
        """Moderate a batch of messages."""
        return await run_in_threadpool(engine.moderate_batch, payload)

    return application


@pytest.fixture()
def app(
    engine: ModerationEngine,
    word_bank: WordBankManager,
    settings: Settings,
) -> FastAPI:
    """Per-test FastAPI app wired to the isolated engine."""
    return build_app(engine, word_bank, settings)


@pytest.fixture()
def client(app: FastAPI) -> Iterator[Any]:
    """Per-test TestClient bound to the wired app."""
    from fastapi.testclient import TestClient

    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture()
def admin_headers(settings: Settings) -> dict[str, str]:
    """Headers carrying the valid admin API key."""
    return {"X-API-Key": settings.admin_api_key}


@pytest.fixture()
def detector_factory(word_bank: WordBankManager) -> Callable[[str], Any]:
    """Factory that instantiates a detector class bound to the word bank.

    :return: callable taking a detector class name and returning an instance
    """
    from app.detectors import aho_detector, bktree_detector, bloom_detector, metaphone_detector

    classes: dict[str, type] = {
        "aho": aho_detector.AhoCorasickDetector,
        "bk_tree": bktree_detector.BkTreeDetector,
        "bloom": bloom_detector.BloomFilterDetector,
        "metaphone": metaphone_detector.MetaphoneDetector,
    }

    def _factory(name: str, *args: object) -> Any:
        return classes[name](word_bank, *args)

    return _factory
