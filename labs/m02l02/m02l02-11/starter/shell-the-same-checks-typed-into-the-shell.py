# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

import sys, platform
sys.version_info
#   sys.version_info(major=3, minor=14, micro=7, releaselevel='final', serial=0)
sys.platform
#   'darwin'
platform.machine()
#   'arm64'
sys.prefix
#   '/opt/homebrew/opt/python@3.14/Frameworks/Python.framework/Versions/3.14'
import tkinter
#   ModuleNotFoundError: No module named '_tkinter'
