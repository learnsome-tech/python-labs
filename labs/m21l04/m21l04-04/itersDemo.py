# Hands-on Python: Complete Video Course & Book — lesson m21l04 — A Standard Library Tour
# https://learnsome.tech/courses/python-course/watch?lesson=m21l04
# © LearnSome.tech
from itertools import combinations, count, cycle, islice

for n in islice(count(10, 5), 4):
    print(n, end=' ')
print()

colours = cycle(['red', 'green'])
print([next(colours) for _ in range(5)])

for pair in combinations('abc', 2):
    print(pair)
