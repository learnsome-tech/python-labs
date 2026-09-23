# Hands-on Python: Complete Video Course & Book — lesson m20l04 — Dunder Methods, And Making Objects Pythonic
# https://learnsome.tech/courses/python-course/watch?lesson=m20l04
# © LearnSome.tech
'''__repr__ for the programmer, __str__ for the reader'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'the point {self.x} across, {self.y} up'

p = Point(1, 2)
print(repr(p))
print(str(p))
print(p)
print([p, Point(3, 4)])
