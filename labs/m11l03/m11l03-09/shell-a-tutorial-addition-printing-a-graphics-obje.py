# Hands-on Python: Complete Video Course & Book — lesson m11l03 — Reading The graphics.py Documentation
# https://learnsome.tech/courses/python-course/watch?lesson=m11l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

from graphics import *
pt = Point(30, 50)
print(pt)
#   Point(30, 50)
ln = Line(pt, Point(100, 150))
print(ln)
#   Line(Point(30, 50), Point(100, 150))
