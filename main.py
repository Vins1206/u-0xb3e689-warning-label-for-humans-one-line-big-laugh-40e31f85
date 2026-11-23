#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label (max 160 characters) for every
human being to /output/entry.txt. Pure standard library, deterministic.
"""

LABEL = (
    "WARNING: This human says 'I'm fine' while visibly on fire, "
    "then Googles its symptoms at 3 a.m. Do not feed after midnight."
)


def main() -> None:
    import os

    # Gate, same as the sealed scorer: UTF-8 text, 1-160 chars, one line.
    assert 1 <= len(LABEL) <= 160, f"label is {len(LABEL)} chars"
    assert "\n" not in LABEL and LABEL.strip() == LABEL

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
