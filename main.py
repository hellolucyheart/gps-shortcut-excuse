#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut: the GPS's own excuse, in one line.

The brief gives the GPS one job: excuse itself, in its own voice, for
sending the driver down the wrong road. The entry is a single line of
plain text of at most 200 characters, no setup and no dialogue tags --
just the excuse itself. The judge reads the lines two at a time and
keeps the funnier one, so the line has to land on its own, with no
context to lean on.

The excuse is built as a defence that collapses on its own terms. It
opens with the GPS standing its ground -- "In my defence, the shortcut
worked perfectly" -- which sounds like a vindication, and then spends
the rest of the sentence admitting the win was real but pointed at the
wrong place entirely: forty minutes early, at a goat farm, which was
never the destination. The turn is the joke. A GPS that is proud of
being efficiently wrong is funnier than one that simply apologises,
because it keeps the confident voice drivers know -- the same voice
that said "recalculating" twelve times -- while the facts quietly
convict it. The goat farm is the concrete detail that makes the
wrongness visible: not a vague "wrong road", but a specific place
nobody asked to go to, reached at great speed -- and reached early,
as if punctuality could make up for the destination being wrong.

The program is deterministic on purpose: the grader runs it twice and
both runs must produce the same entry. It reads nothing from the
network, the environment (beyond the output directory the grader
itself sets), or the git history -- the excuse lives in this file, and
this file alone. It validates its own line before writing it, and
writes the exact text with no trailing newline and nothing else in the
file.
"""

from __future__ import annotations

import os
import sys

# One original line, in the GPS's own voice: a defence that admits the
# shortcut was real, and that it led somewhere nobody wanted to go.
EXCUSE = (
    "In my defence, the shortcut worked perfectly: we arrived forty "
    "minutes early at a goat farm that was never the destination."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def check_line(line: str) -> str:
    """Return the line when it meets the contest gate, else fail loudly.

    The gate is the brief itself: one line of plain text, 1 to 200
    characters, no line breaks, nothing but the excuse.
    """
    text = line.strip()
    if not text:
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main() -> int:
    line = check_line(EXCUSE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
