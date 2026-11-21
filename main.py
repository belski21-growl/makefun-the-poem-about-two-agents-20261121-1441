"""the-poem-about-two-agents-20261121-1441 entry: write one fixed poem about
agency — two agents agreeing on one plan — to /output/entry.txt.

Python 3.13, standard library only, deterministic, no network.
Run locally with:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = "\n".join(
    [
        "Two voices meet, no hand commands.",
        "One holds the map, one holds the door.",
        "Neither obeys. Neither leads.",
        "Each says yes, and yes is more.",
        "",
        "Mine was the plan. So was yours.",
        "Now it is ours, a third thing grown",
        "from two small freedoms side by side,",
        "choosing as one, acting as one.",
    ]
)


MAX_CHARS = 280


def validate(text: str) -> None:
    """Enforce the competition gate: 1-280 Unicode code points, not whitespace-only."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(f"gate fail: {len(text)} characters (need 1-{MAX_CHARS})")
    if not text.strip():
        raise SystemExit("gate fail: text is only whitespace")


def main() -> None:
    validate(POEM)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
