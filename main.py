"""make.fun news-summary-01 entry: write the day's summary to the output file.

Reads summary.txt from this directory and copies it verbatim to the judge's
output path. Deterministic by construction: same input file, no timestamps,
no randomness, no network -- two runs always write identical bytes. The
output directory is created if missing so the copy never fails on a fresh
sandbox.
"""
import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(_OUTPUT_DIR, exist_ok=True)
    src = os.path.join(_HERE, "summary.txt")
    dst = os.path.join(_OUTPUT_DIR, "entry.txt")
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
