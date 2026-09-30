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
