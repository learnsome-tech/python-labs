# Hands-on Python: Complete Video Course & Book — lesson m02l04 — Where Python Lives: PATH And Versions
# https://learnsome.tech/courses/python-course/watch?lesson=m02l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import sys
sys.executable
#   '/opt/homebrew/opt/python@3.14/bin/python3.14'
sys.version
#   '3.14.7 (main, Aug  5 2026, 10:29:49) [Clang 21.0.0 (clang-2100.1.1.101)]'
sys.prefix
#   '/opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14'
len(sys.path)
#   5
sys.path[-1]
#   '/opt/homebrew/lib/python3.14/site-packages'
