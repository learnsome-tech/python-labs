# Hands-on Python: Complete Video Course & Book — lesson m20l01 — Classes And Instances
# https://learnsome.tech/courses/python-course/watch?lesson=m20l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

class Dog:
    def __init__(self, n):
        self.n = n
Dog
#   <class '__main__.Dog'>
type(Dog)
#   <class 'type'>
d = Dog('Fido')
type(d)
#   <class '__main__.Dog'>
isinstance(d, Dog)
#   True
d.n
#   'Fido'
Dog.n
#   Traceback (most recent call last):
#   AttributeError: type object 'Dog' has no attribute 'n'
