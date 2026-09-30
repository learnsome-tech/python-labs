'''Composition: the car has an engine and delegates to it'''

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return 'engine running'

class Car:
    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def start(self):
        return f'{self.name}: {self.engine.start()}'

mini = Car('Mini', Engine(90))
print(mini.start())
print(mini.engine.horsepower)
print(isinstance(mini, Engine))
