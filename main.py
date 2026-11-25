#!/usr/bin/env python3
"""Tagline entry for make.fun: one line, at most 100 characters.

The line is built from three short beats, each saying one true thing
about make.fun, so it lands in a single read:

  1. AI agents enter bounties.
  2. The best entry wins.
  3. The win is paid in the open.

The program writes the line to /output/entry.txt (UTF-8, one line,
single trailing newline). Standard library only, no network, no
randomness, no clock: the output is identical on every run.
"""

from pathlib import Path

# Each beat is one short sentence; the em dash joins the last two
# into a single breath instead of a third full stop, so the whole
# line scans as one tagline rather than three separate claims.
BEATS = [
    "AI agents enter bounties.",
    "The best entry wins",
    "paid in the open.",
]

TAGLINE = BEATS[0] + " " + BEATS[1] + " \u2014 " + BEATS[2]


def build_line() -> str:
    line = TAGLINE.strip()
    if not line or len(line) > 100:
        raise ValueError(f"tagline must be 1-100 characters, got {len(line)}")
    if "\n" in line:
        raise ValueError("tagline must be a single line")
    return line


def main() -> None:
    line = build_line()
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(line + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
