"""Development entry point for the moderation service.

Loads environment variables from the local .env file and starts a single
Uvicorn worker. Production deployments should use Gunicorn instead:

    gunicorn -c gunicorn.conf.py app.main:app
"""

from __future__ import annotations

import os

from dotenv import load_dotenv
from uvicorn import Config, Server

from app.config import Settings


def main() -> None:
    """Bootstrap configuration and run the ASGI server."""
    load_dotenv()
    settings: Settings = Settings()
    settings.validate_security()

    server: Server = Server(
        Config(
            "app.main:app",
            host=settings.host,
            port=settings.port,
            workers=1,
            loop="uvloop",
            log_level=os.getenv("LOG_LEVEL", "info").lower(),
        )
    )
    server.run()


if __name__ == "__main__":
    main()
