# Hands-on Python: Complete Video Course & Book — lesson m19l01 — Lists, Tuples, Sets, Dicts: Choosing One
# https://learnsome.tech/courses/python-course/watch?lesson=m19l01
# © LearnSome.tech
'''Asking whether a value is present: a list against a set.'''

import timeit

setup = 'big_list = list(range(200000))\nbig_set = set(big_list)'
list_time = timeit.timeit('199999 in big_list', setup, number=200)
set_time = timeit.timeit('199999 in big_set', setup, number=200)

print('the set answered faster:', set_time < list_time)
print('by a factor of more than a hundred:', list_time > 100 * set_time)
