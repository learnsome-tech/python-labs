'''A first class, and a first instance made from it'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

fido = Dog('Fido', 3)
print(fido.name)
print(fido.age)
print(type(fido).__name__)
print(vars(fido))
