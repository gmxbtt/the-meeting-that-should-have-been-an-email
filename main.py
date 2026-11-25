#!/usr/bin/env python3
"""Entry for make.fun's "The Meeting That Should Have Been an Email".

The whole entry is a single joke line. This program writes that line to
/output/entry.txt, where the sealed scorer reads it (1-200 UTF-8 chars,
one line, no setup, no second line).
"""

from pathlib import Path

LINE = "I brought snacks to the meeting that should have been an email \u2014 the chips were the only ones with anything to say."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "entry must be a single line"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
