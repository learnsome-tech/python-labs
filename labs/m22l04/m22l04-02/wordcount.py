#!/usr/bin/env python3
# Hands-on Python: Complete Video Course & Book — lesson m22l04 — Shipping: scripts, entry points and git
# https://learnsome.tech/courses/python-course/watch?lesson=m22l04
# © LearnSome.tech
"""Count the words in each file named on the command line."""
import sys
from pathlib import Path

for name in sys.argv[1:]:
    print(name, len(Path(name).read_text(encoding='utf-8').split()))
