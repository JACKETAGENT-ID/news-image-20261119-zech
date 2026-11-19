"""Entry point for the news-image-20261119 bounty (zech entry).

Copies the pre-built poster entry.png (produced locally by generate.py)
into $MAKEFUN_OUTPUT_DIR/entry.png. Standard library only, deterministic:
the same input file is copied byte-for-byte on every run.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
