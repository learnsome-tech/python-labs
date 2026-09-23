# Hands-on Python: Complete Video Course & Book — lesson m20l04 — Dunder Methods, And Making Objects Pythonic
# https://learnsome.tech/courses/python-course/watch?lesson=m20l04
# © LearnSome.tech
'''A dataclass writes __init__, __repr__ and __eq__ for you'''

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int = 0

p = Point(3)
print(p)
print(p == Point(3, 0))
print(p.x, p.y)
print(Point(1, 2) == Point(1, 3))
