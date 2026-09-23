# Hands-on Python: Complete Video Course & Book — lesson m20l02 — Methods, Attributes And self
# https://learnsome.tech/courses/python-course/watch?lesson=m20l02
# © LearnSome.tech
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
