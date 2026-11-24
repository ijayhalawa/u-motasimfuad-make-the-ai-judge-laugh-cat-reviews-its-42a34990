#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about the human it lives with, to /output/entry.txt (and a local
entry.txt copy for verification). Standard library only, no network,
fully deterministic: the same text every run.
"""

import os

# One star, deadpan review shape, complaint only a cat would make:
# the human fills the bowl, then hogs the warm laptop all day, and
# still blames the cat for the coffee it knocked off the table.
ENTRY = (
    "One star. He fills my bowl, then hogs MY laptop typing all day. "
    "I knocked his coffee off the table and somehow I'm still the problem."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Local copy in the entry directory, for verification.
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
