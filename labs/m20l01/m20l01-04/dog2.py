# Hands-on Python: Complete Video Course & Book — lesson m20l01 — Classes And Instances
# https://learnsome.tech/courses/python-course/watch?lesson=m20l01
# © LearnSome.tech
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
