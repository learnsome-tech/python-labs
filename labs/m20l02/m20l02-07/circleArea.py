# Hands-on Python: Complete Video Course & Book — lesson m20l02 — Methods, Attributes And self
# https://learnsome.tech/courses/python-course/watch?lesson=m20l02
# © LearnSome.tech
'''A property: behaviour behind a plain attribute name'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        '''The area, recomputed from the radius on every read.'''
        return 3.14159 * self.radius ** 2

c = Circle(2)
print(c.area)
c.radius = 3
print(c.area)
try:
    c.area = 100
except AttributeError as e:
    print('AttributeError:', e)
