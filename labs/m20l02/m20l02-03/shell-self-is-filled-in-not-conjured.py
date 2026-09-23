# Hands-on Python: Complete Video Course & Book — lesson m20l02 — Methods, Attributes And self
# https://learnsome.tech/courses/python-course/watch?lesson=m20l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

class Dog:
    def speak(self):
        return 'woof'
d = Dog()
d.speak()
#   'woof'
Dog.speak(d)
#   'woof'
type(Dog.speak).__name__
#   'function'
type(d.speak).__name__
#   'method'
Dog.speak()
#   Traceback (most recent call last):
#   TypeError: Dog.speak() missing 1 required positional argument: 'self'
