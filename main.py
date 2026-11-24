#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt: a self-checkout till that scans one carton of milk
twice, then accuses its own customer of theft.

Fully deterministic: no network, no randomness, no clock, no files
read from outside this repository. Two runs produce byte-identical
output.
"""

import os
import sys

RANT = (
    "I scanned one carton of milk. The self-checkout scanned it twice, "
    "yelled 'unexpected item in the bagging area', and summoned a human to "
    "watch me bag my own groceries. I came to buy dinner, not to be "
    "interrogated by a till that can't count to one."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 400


def check(text: str) -> str:
    """Validate the rant against the competition gate.

    Returns the validated text unchanged. Raises ValueError with a
    precise reason (including the offending character count) on any
    failure, so a bad rant fails loudly instead of being submitted.
    """
    if not isinstance(text, str):
        raise TypeError(f"rant must be a string, got {type(text).__name__}")
    length = len(text)
    if length < MIN_LENGTH:
        raise ValueError(f"rant is empty ({length} characters)")
    if length > MAX_LENGTH:
        raise ValueError(
            f"rant is {length} characters, over the {MAX_LENGTH} limit"
        )
    if not text.strip():
        raise ValueError("rant must not be only whitespace")
    return text


def main() -> int:
    text = check(RANT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
