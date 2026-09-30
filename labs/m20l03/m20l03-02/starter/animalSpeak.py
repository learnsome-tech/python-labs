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
