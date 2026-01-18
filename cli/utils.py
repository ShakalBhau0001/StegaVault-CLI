import os
import sys


def ensure_file(path):
    if not os.path.isfile(path):
        print("File not found:", path)
        sys.exit(1)
