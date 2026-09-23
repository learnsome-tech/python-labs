# Hands-on Python: Complete Video Course & Book — lesson m02l03 — Installing Python On Linux
# https://learnsome.tech/courses/python-course/watch?lesson=m02l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import sys, venv, ensurepip
sys.version_info.minor
#   14
sys.version_info >= (3, 9)
#   True
sys.prefix == sys.base_prefix
#   True
