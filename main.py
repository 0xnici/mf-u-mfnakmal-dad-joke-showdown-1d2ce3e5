#!/usr/bin/env python3
"""Dad Joke Showdown: write one joke to entry.txt in the output directory."""

import os
from pathlib import Path

JOKE = (
    "I never win an argument with my wife, so I bring a pencil to the "
    "table. At least I make a point."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(text):
    """Mirror the gate: UTF-8, 1-200 characters, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError("joke must be 1-200 characters")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    return text.encode("utf-8")


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    payload = validate(JOKE)
    target = out_dir / "entry.txt"
    with open(target, "wb") as handle:
        handle.write(payload)


if __name__ == "__main__":
    main()
