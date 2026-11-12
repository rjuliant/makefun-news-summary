"""make.fun news-summary-01 entry.

Reads the pre-written summary.txt from this directory and copies it byte-for-byte
to the judge's output file. Deterministic by construction: no timestamps, no
randomness, and no network access, so two runs always write identical bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Create the output directory if missing so the copy works on a fresh sandbox.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "summary.txt")
    dst = os.path.join(OUTPUT_DIR, "entry.txt")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()