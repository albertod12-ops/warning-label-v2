#!/usr/bin/env python3
"""Warning Label for Humans — v2.

Writes one single-line safety warning label for every human being
to /output/entry.txt. The joke is one idea: the human as a sealed
appliance, in real label language — the turn lands in the last words,
when feelings turn out to be the forbidden maintenance.
"""

import os

LABEL = "WARNING: This human contains no user-serviceable parts. Do not open, poke, or ask it how it feels."


def main():
    assert "\n" not in LABEL, "label must be a single line"
    assert 1 <= len(LABEL.encode("utf-8")) <= 160, "label must be 1-160 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LABEL)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
