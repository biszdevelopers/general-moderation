"""Export an SBOM of the active virtual environment.

Runs ``pip list --format=json`` against the active interpreter, attaches a
best-effort license per package via ``importlib.metadata``, and writes a
compact JSON SBOM to ``backend/exports/sbom.json``.

Run with ``npm run sbom`` (from the repository root) or
``uv run python tools/sbom.py`` (from ``backend/``).
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import UTC, datetime
from importlib.metadata import PackageNotFoundError, metadata
from pathlib import Path


def _license(name: str) -> str:
    """Return the package license text, falling back to classifier metadata."""
    try:
        meta = metadata(name)
    except PackageNotFoundError:
        return ""
    license_text: str = (meta.get("License") or "").strip()
    if license_text and license_text.upper() != "UNKNOWN":
        return license_text
    for classifier in meta.get_all("Classifier") or []:
        if classifier.startswith("License :: "):
            return classifier.rsplit(" :: ", 1)[-1]
    return ""


def main() -> int:
    """Write the SBOM and print its location."""
    installed: list[dict[str, str]] = json.loads(
        subprocess.run(
            [sys.executable, "-m", "pip", "list", "--format=json"],
            check=True,
            capture_output=True,
            text=True,
        ).stdout
    )
    packages: list[dict[str, str]] = [
        {
            "name": item["name"],
            "version": item["version"],
            "license": _license(item["name"]),
        }
        for item in installed
    ]
    packages.sort(key=lambda item: item["name"].lower())
    sbom: dict[str, object] = {
        "generated_at": datetime.now(UTC).isoformat(),
        "generated_by": "pip list --format=json + importlib.metadata",
        "environment": "backend/.venv",
        "package_count": len(packages),
        "packages": packages,
    }
    output: Path = Path(__file__).resolve().parent.parent / "exports" / "sbom.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(sbom, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote SBOM with {len(packages)} packages to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
