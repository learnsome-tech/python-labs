# Hands-on Python: Complete Video Course & Book — lesson m20l04 — Dunder Methods, And Making Objects Pythonic
# https://learnsome.tech/courses/python-course/watch?lesson=m20l04
# © LearnSome.tech
'''__eq__ decides equality, and takes hashability with it'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

a = Point(1, 2)
b = Point(1, 2)
print(a == b, a is b)
print(a in [Point(0, 0), Point(1, 2)])
try:
    print({a, b})
except TypeError as e:
    print('TypeError:', e)
