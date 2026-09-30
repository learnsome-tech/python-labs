class Car(Engine):        # a car IS an engine?  no
    ...

class Car:                # a car HAS an engine
    def __init__(self, engine):
        self.engine = engine
