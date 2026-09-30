#!/usr/bin/env python3
"""Count the words in each file named on the command line."""
import sys
from pathlib import Path

for name in sys.argv[1:]:
    print(name, len(Path(name).read_text(encoding='utf-8').split()))
