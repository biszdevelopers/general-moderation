"""Gunicorn configuration for the moderation service."""

import multiprocessing
import os


def _default_workers() -> int:
    """Return the configured worker count, defaulting to one per core."""
    configured: str = os.getenv("WORKERS", "")
    if configured.isdigit() and int(configured) > 0:
        return int(configured)
    return multiprocessing.cpu_count()


bind = f"{os.getenv('HOST', '127.0.0.1')}:{os.getenv('PORT', '8080')}"
workers = _default_workers()
worker_class = "uvicorn.workers.UvicornWorker"
max_requests = 10000
max_requests_jitter = 1000
preload_app = True
timeout = 30
keepalive = 5
graceful_timeout = 30
accesslog = "-"
errorlog = "-"
