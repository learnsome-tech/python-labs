# Hands-on Python: Complete Video Course & Book — lesson m19l04 — Iterators And Generators
# https://learnsome.tech/courses/python-course/watch?lesson=m19l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

nums = [10, 20, 30]
it = iter(nums)
next(it)
#   10
next(it)
#   20
next(it)
#   30
next(it)
#   Traceback (most recent call last):
#   StopIteration
type(it).__name__
#   'list_iterator'
iter(nums) is iter(nums)
#   False
