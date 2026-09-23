# Hands-on Python: Complete Video Course & Book — lesson m20l04 — Dunder Methods, And Making Objects Pythonic
# https://learnsome.tech/courses/python-course/watch?lesson=m20l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

len('hello')
#   5
'hello'.__len__()
#   5
2 + 3
#   5
(2).__add__(3)
#   5
[1, 2] + [3]
#   [1, 2, 3]
[1, 2].__add__([3])
#   [1, 2, 3]
'ab'.__class__
#   <class 'str'>
