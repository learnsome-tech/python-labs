'''Two instances of one class keep their own data'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

fido = Dog('Fido', 3)
rex = Dog('Rex', 7)
print(fido.name, fido.age)
print(rex.name, rex.age)
fido.age = 4
print(fido.age, rex.age)
print(fido is rex)
print(type(fido) is type(rex))
