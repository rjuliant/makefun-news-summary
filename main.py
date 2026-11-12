"""make.fun news-summary-01 entry: copy the day's summary to the output file.

The summary sits in summary.txt beside this file; the judge reads exactly the
bytes we copy. Two runs must write identical bytes, and they do: we copy the
same file, no timestamps, no randomness, no network.
"""
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
shutil.copyfile(os.path.join(here, "summary.txt"), os.path.join(out, "entry.txt"))