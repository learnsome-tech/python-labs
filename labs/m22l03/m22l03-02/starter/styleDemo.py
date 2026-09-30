import math

MAX_ANGLE = 360


def sector_area(radius, degrees):
    fraction = degrees / MAX_ANGLE
    return math.pi * radius**2 * fraction


class ClockFace:
    def __init__(self, radius):
        self.radius = radius

    def wedge(self, degrees):
        return sector_area(self.radius, degrees)


print(round(sector_area(2, 90), 3))
print(round(ClockFace(2).wedge(180), 3))
