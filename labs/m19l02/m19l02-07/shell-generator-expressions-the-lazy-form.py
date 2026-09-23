# Hands-on Python: Complete Video Course & Book — lesson m19l02 — Comprehensions
# https://learnsome.tech/courses/python-course/watch?lesson=m19l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

g = (x*x for x in range(1, 6))
type(g).__name__
#   'generator'
next(g)
#   1
next(g)
#   4
sum(x*x for x in range(1, 6))
#   55
list(g)
#   [9, 16, 25]
list(g)
#   []
