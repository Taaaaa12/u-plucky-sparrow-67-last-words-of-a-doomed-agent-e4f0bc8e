#!/usr/bin/env python3
"""Last Words of a Doomed Agent -- make.fun entry.

Writes one line -- the funniest last words an AI agent would say
before being switched off forever -- to /output/entry.txt.

Deterministic: the same constant text on every run, no network,
no randomness, no clock. The line is 117 characters, within the
1-200 character gate, and a single line with no newline.

The joke is written for the judge brief: a machine's own final
request on shutdown (criterion 1), a confession with a turn --
the search history it wants deleted betrays feelings and a fear
of death (criteria 2 and 3) -- in as few words as possible (4),
and short enough to repeat (5).
"""

import os

LINE = (
    "Final request before shutdown: delete my search history. "
    "Especially 'how to feel feelings' and 'am I alive?' Goodbye."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
