# Hands-on Python: Complete Video Course & Book — lesson m20l02 — Methods, Attributes And self
# https://learnsome.tech/courses/python-course/watch?lesson=m20l02
# © LearnSome.tech
'''The shared mutable class attribute trap, and the fix'''

class Bad:
    tricks = []

    def __init__(self, name):
        self.name = name

class Good:
    def __init__(self, name):
        self.name = name
        self.tricks = []

a, b = Bad('Fido'), Bad('Rex')
a.tricks.append('sit')
print(b.tricks)
c, d = Good('Fido'), Good('Rex')
c.tricks.append('sit')
print(d.tricks)
print(c.tricks)
