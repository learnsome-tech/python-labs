# Hands-on Python: Complete Video Course & Book — lesson m09l05 — Appending To Lists, Sets, Constructors
# https://learnsome.tech/courses/python-course/watch?lesson=m09l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

strList = ['z', 'zz', 'c', 'z', 'bb', 'z', 'a', 'c']
aSet = set(strList)
len(aSet)
#   5
sorted(aSet)
#   ['a', 'bb', 'c', 'z', 'zz']
dupes = ['animal', 'food', 'animal', 'food', 'food', 'city']
len(set(dupes))
#   3
sorted(set(dupes))
#   ['animal', 'city', 'food']
