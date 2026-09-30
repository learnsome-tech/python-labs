'''A docstring on a class and on one of its methods'''

class Dog:
    '''A dog with a name and an age in years.'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        '''Return this dog's sound, with its name in front.'''
        return f'{self.name} says woof'

print(Dog.__doc__)
print(Dog.speak.__doc__)
fido = Dog('Fido', 3)
print(fido.speak.__doc__)
