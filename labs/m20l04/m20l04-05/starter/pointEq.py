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
