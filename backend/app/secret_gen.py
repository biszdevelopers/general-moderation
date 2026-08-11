"""Generate or regenerate security secrets in ``.env``.

Run with ``uv run python -m app.secret_gen`` (or ``npm run generate:secrets``
from the repository root). By default only missing or placeholder secrets are
replaced; pass ``--force`` to regenerate every secret.
"""

from __future__ import annotations

import sys


def main(argv: list[str] | None = None) -> int:
    """Generate security secrets and report what changed.

    :param argv: command-line arguments, defaults to ``sys.argv[1:]``
    :return: process exit code
    """
    from app.config import Settings

    arguments: list[str] = list(sys.argv[1:] if argv is None else argv)
    force: bool = "--force" in arguments
    settings: Settings = Settings()
    generated: dict[str, str] = settings.ensure_secrets(force=force)
    if not generated:
        print("All security secrets are already set in .env.")
        return 0
    for name in generated:
        print(f"Generated {name.upper()} in .env")
    return 0


if __name__ == "__main__":
    sys.exit(main())
