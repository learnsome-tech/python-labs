# Hands-on Python: Complete Video Course & Book — lesson m20l03 — Inheritance And Composition
# https://learnsome.tech/courses/python-course/watch?lesson=m20l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

class Animal: pass
class Dog(Animal): pass
d = Dog()
isinstance(d, Dog)
#   True
isinstance(d, Animal)
#   True
isinstance(d, str)
#   False
type(d) is Animal
#   False
issubclass(Dog, Animal)
#   True
[c.__name__ for c in Dog.__mro__]
#   ['Dog', 'Animal', 'object']
