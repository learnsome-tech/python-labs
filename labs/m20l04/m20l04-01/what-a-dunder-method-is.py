# Hands-on Python: Complete Video Course & Book — lesson m20l04 — Dunder Methods, And Making Objects Pythonic
# https://learnsome.tech/courses/python-course/watch?lesson=m20l04
# © LearnSome.tech
len(x)      calls  x.__len__()
x + y       calls  x.__add__(y)
x == y      calls  x.__eq__(y)
print(x)    calls  x.__str__()
repr(x)     calls  x.__repr__()
