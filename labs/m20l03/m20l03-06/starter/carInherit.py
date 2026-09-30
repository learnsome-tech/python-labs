'''Inheritance used where it does not belong'''

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return 'engine running'

class Car(Engine):
    def __init__(self, name, horsepower):
        super().__init__(horsepower)
        self.name = name

mini = Car('Mini', 90)
print(mini.start())
print(mini.horsepower)
print(isinstance(mini, Engine))
