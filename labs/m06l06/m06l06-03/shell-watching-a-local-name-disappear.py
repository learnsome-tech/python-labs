# Hands-on Python: Complete Video Course & Book — lesson m06l06 — Local Scope And Global Constants
# https://learnsome.tech/courses/python-course/watch?lesson=m06l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

def f():
    y = 5
    print(y)
f()
#   5
y
#   Traceback (most recent call last):
#   NameError: name 'y' is not defined
