# Hands-on Python: Complete Video Course & Book — lesson m19l04 — Iterators And Generators
# https://learnsome.tech/courses/python-course/watch?lesson=m19l04
# © LearnSome.tech
'''A list of a million squares, and a generator of the same squares.'''

import sys

square_list = [x*x for x in range(1000000)]
square_gen = (x*x for x in range(1000000))

print('list megabytes:', round(sys.getsizeof(square_list) / 1000000))
print('generator under a kilobyte:', sys.getsizeof(square_gen) < 1000)
print('both add up to the same total:', sum(square_list) == sum(square_gen))
