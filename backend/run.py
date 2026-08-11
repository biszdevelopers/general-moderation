"""Development and single-worker production entry point for the service.

Loads environment variables from the local .env file and starts a single
Uvicorn worker. On Linux the uvloop event loop is used when available; on
platforms without uvloop (Windows) the asyncio loop is used instead.

Production deployments on Linux should use Gunicorn for multi-worker runs:

    gunicorn -c gunicorn.conf.py app.main:app
"""

from __future__ import annotations

import importlib.util
import os

from dotenv import load_dotenv
from uvicorn import Config, Server

from app.config import Settings


def main() -> None:
    """Bootstrap configuration and run the ASGI server."""
    load_dotenv()
    settings: Settings = Settings()
    settings.validate_security()

    loop: str = "asyncio"
    if importlib.util.find_spec("uvloop") is not None:
        loop = "uvloop"

    server: Server = Server(
        Config(
            "app.main:app",
            host=settings.app_host,
            port=settings.app_port,
            workers=1,
            loop=loop,
            log_level=os.getenv("LOG_LEVEL", "info").lower(),
        )
    )
    server.run()


if __name__ == "__main__":
    main()
