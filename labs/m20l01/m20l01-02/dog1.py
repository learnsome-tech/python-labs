# Hands-on Python: Complete Video Course & Book — lesson m20l01 — Classes And Instances
# https://learnsome.tech/courses/python-course/watch?lesson=m20l01
# © LearnSome.tech
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
