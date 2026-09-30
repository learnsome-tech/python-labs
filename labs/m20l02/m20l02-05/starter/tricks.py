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
