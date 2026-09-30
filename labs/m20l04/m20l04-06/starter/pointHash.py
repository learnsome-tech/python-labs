'''Adding __hash__ back so the object can go in a set'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

print(len({Point(1, 2), Point(1, 2), Point(3, 4)}))
print({Point(1, 2): 'home'}[Point(1, 2)])
