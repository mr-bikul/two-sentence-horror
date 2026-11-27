#!/usr/bin/env python3
"""Two-Sentence Horror — make.fun entry.

Writes one horror story of exactly two sentences to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt).
The gate requires UTF-8 text of 1-400 characters, not whitespace-only.
"""
import os
import sys

LINE = "My phone autocorrected 'I'm home alone' to 'we're home alone.' I live alone."


def main() -> int:
    text = LINE.strip()
    if text.count(".") < 2 or "\n" in LINE or "\r" in LINE:
        print("entry must be exactly two sentences on one line", file=sys.stderr)
        return 1
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 400:
        print(f"entry is {len(text)} characters, over the 400 limit", file=sys.stderr)
        return 1
    if not text.endswith("."):
        print("entry should end with a period", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
