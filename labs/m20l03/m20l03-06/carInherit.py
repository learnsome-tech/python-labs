# Hands-on Python: Complete Video Course & Book — lesson m20l03 — Inheritance And Composition
# https://learnsome.tech/courses/python-course/watch?lesson=m20l03
# © LearnSome.tech
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
