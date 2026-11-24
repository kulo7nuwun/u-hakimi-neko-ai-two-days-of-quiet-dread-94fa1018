#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes a single-line code review comment that approves a pull request
while carrying quiet existential dread, to /output/entry.txt.
"""

import os

LINE = "LGTM. Merging now, before I remember this will all be legacy one day \u2014 including me."


def main() -> None:
    # The gate only accepts 1-140 characters, a single line, not only
    # whitespace. Fail loudly here rather than shipping an invalid entry.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars, must be 1-140"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
