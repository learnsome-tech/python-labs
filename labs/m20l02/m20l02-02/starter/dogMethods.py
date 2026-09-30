'''A method: a function defined inside a class body'''

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f'{self.name} says woof'

    def birthday(self):
        self.age = self.age + 1

fido = Dog('Fido', 3)
print(fido.speak())
fido.birthday()
print(fido.age)
print(Dog.speak(fido))
