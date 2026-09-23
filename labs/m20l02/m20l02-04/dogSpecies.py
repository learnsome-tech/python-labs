# Hands-on Python: Complete Video Course & Book — lesson m20l02 — Methods, Attributes And self
# https://learnsome.tech/courses/python-course/watch?lesson=m20l02
# © LearnSome.tech
'''One value shared by the class, one value per instance'''

class Dog:
    species = 'Canis familiaris'

    def __init__(self, name):
        self.name = name

fido = Dog('Fido')
rex = Dog('Rex')
print(fido.species, rex.species)
Dog.species = 'dog'
print(fido.species, rex.species)
fido.species = 'wolf'
print(fido.species, rex.species, Dog.species)
