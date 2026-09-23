# Hands-on Python: Complete Video Course & Book — lesson m18l01 — Modules And The Import System
# https://learnsome.tech/courses/python-course/watch?lesson=m18l01
# © LearnSome.tech
'''Name this file random.py and the real random module is hidden.'''

import random

if __name__ == '__main__':
    print(random.__name__)
    print(random.__file__.endswith('random.py'))
    print(hasattr(random, 'randint'))
