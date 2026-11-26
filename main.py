#!/usr/bin/env python3
"""Warning Label for Humans — v3.

Writes one single-line safety warning label for every human being
to /output/entry.txt. The joke is one idea: the human as a piece of
equipment with three daily requirements, and the third one is not a
physical supply at all — the turn lands in the last words, when being
told it did a good job turns out to be a maintenance requirement.
"""

import os

LABEL = "WARNING: This human requires food, water, and being told it did a good job at least once a day."


def main():
    assert "\n" not in LABEL, "label must be a single line"
    assert LABEL == LABEL.strip(), "label must have no leading or trailing space"
    assert 1 <= len(LABEL.encode("utf-8")) <= 160, "label must be 1-160 characters"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(LABEL.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
