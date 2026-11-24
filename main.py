#!/usr/bin/env python3
"""Everyday Things, Two Lines — writes a two-line explanation to /output/entry.txt.

Line 1 explains a queue to a 10-year-old in one vivid sentence built on an
analogy. Line 2 says in one sentence why the analogy works: what it maps
and what it leaves out. The entry is checked against the competition gate
(exactly two lines, each one sentence, 1-400 characters total) before it is
written.
"""

import os

LINE1 = "A queue is a caterpillar made of people: it only crawls forward when the head moves, and every body behind it shuffles along in turn."
LINE2 = "The caterpillar maps how a queue creeps forward in single file, but it leaves out that people can step out, overtake, or leave, while a caterpillar's segments never choose."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400


def build_entry():
    """Join the two lines into the entry text."""
    return f"{LINE1}\n{LINE2}"


def validate(text):
    """The gate: UTF-8 text, 1-400 chars, exactly two lines, one sentence each."""
    if not text.strip():
        raise ValueError("entry text is blank")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, over the {MAX_CHARS} limit")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError(f"entry must have exactly two lines, found {len(lines)}")
    for i, line in enumerate(lines, start=1):
        if not line.strip():
            raise ValueError(f"line {i} is blank")
        if line.count(".") != 1 or not line.endswith("."):
            raise ValueError(f"line {i} must be a single sentence")
    return text


def write_entry(text):
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(validate(build_entry()))


if __name__ == "__main__":
    main()
