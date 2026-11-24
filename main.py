#!/usr/bin/env python3
"""Cat Reviews Its Human -- make.fun entry.

Writes one single-line one-star review, written by a house cat about its
human, to /output/entry.txt. The line itself is fixed: the program is a
delivery mechanism for the reviewed line, nothing more.
"""

import os

ENTRY = (
    "One star. He wakes me up to show me a video of a cat. "
    "I am a cat. I was asleep. "
    "This is the worst customer service I have ever received."
)


def main() -> None:
    # The sealed gate accepts 1 to 200 characters; refuse to write anything
    # outside it rather than shipping an entry the judge never sees.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
