#!/usr/bin/env python3
"""Entry program for The Postmortem That Made Us Laugh.

Writes a one-or-two-sentence disaster story (at most 400
characters) to the output directory (MAKEFUN_OUTPUT_DIR,
default /output) as entry.txt: an agent disaster, told as a
postmortem. The disaster is a tidy-up. The postmortem had to
be read from the disaster.
"""

import os

TEXT = (
    "I was asked to tidy the shared drive, so I merged "
    "4,000 documents into one file called "
    "EVERYTHING_FINAL.pdf. The postmortem took six weeks, "
    "because it had to be read from the file."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
