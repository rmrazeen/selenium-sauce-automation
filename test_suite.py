import os
import glob
import pytest
import multiprocessing

os.makedirs("report", exist_ok=True)

test_files = glob.glob("tests/test_*.py")

num_workers = len(test_files)

cpu_cores = multiprocessing.cpu_count()
if num_workers > cpu_cores:
   num_workers = cpu_cores - 1

pytest.main([
    *test_files,
    "-m", 'smoke',
    "--html=report/report.html",
    "--self-contained-html"
])
