#!/usr/bin/env python3
"""Fortune in a Pot -- make.fun entry.

Writes one kind, funny fortune for the houseplant on the windowsill
to $MAKEFUN_OUTPUT_DIR/entry.txt: a single line of at most 120
characters, exactly as the competition's gate requires.
"""

import os
import sys

# The grader runs `python3 -P -s main.py`, which leaves the script's own
# directory off sys.path; bootstrap it so local imports keep working.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

FORTUNE = (
    "You will bask in the perfect sunbeam this week, and your keeper "
    "will brag about you to guests who never asked."
)

MAX_CHARS = 120


def resolve_output_dir():
    """Return the grader's output directory, falling back to ./output."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out:
        return out
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output")


def validate(text):
    """Enforce the competition gate: 1-120 chars, one line, not blank."""
    if not isinstance(text, str):
        raise ValueError("fortune must be text")
    if not text.strip():
        raise ValueError("fortune must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "fortune is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("fortune must not contain control characters")
    return text


def main():
    text = validate(FORTUNE)
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
