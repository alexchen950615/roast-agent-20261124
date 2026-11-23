#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun bounty entry.

Writes a single original one-line roast of the entrant's own AI agent
to /output/entry.txt. Standard library only, no network access.
"""

from pathlib import Path

ROAST = (
    "I built an agent to save time; it spent three hours writing a plan "
    "to save me two minutes, then asked if I was proud of it."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
