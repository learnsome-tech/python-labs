'''super in __init__, and super in an overriding method'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        return f'{self.name} earns {self.salary}'

class Manager(Employee):
    def __init__(self, name, salary, reports):
        super().__init__(name, salary)
        self.reports = reports

    def describe(self):
        return super().describe() + f' and leads {self.reports}'

boss = Manager('Ada', 90000, 4)
print(boss.describe())
print(boss.name, boss.salary, boss.reports)
