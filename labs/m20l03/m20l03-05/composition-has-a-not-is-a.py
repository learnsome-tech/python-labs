# Hands-on Python: Complete Video Course & Book — lesson m20l03 — Inheritance And Composition
# https://learnsome.tech/courses/python-course/watch?lesson=m20l03
# © LearnSome.tech
class Car(Engine):        # a car IS an engine?  no
    ...

class Car:                # a car HAS an engine
    def __init__(self, engine):
        self.engine = engine
