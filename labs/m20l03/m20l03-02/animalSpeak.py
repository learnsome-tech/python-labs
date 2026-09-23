# Hands-on Python: Complete Video Course & Book — lesson m20l03 — Inheritance And Composition
# https://learnsome.tech/courses/python-course/watch?lesson=m20l03
# © LearnSome.tech
'''Inheritance: a subclass reuses and specialises its base'''

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} makes a sound'

class Dog(Animal):
    def speak(self):
        return f'{self.name} says woof'

class Puppy(Dog):
    def speak(self):
        return super().speak() + ', quietly'

for a in [Animal('Thing'), Dog('Fido'), Puppy('Bit')]:
    print(a.speak())
