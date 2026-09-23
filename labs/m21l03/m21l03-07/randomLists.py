# Hands-on Python: Complete Video Course & Book — lesson m21l03 — Dates, Times And Random
# https://learnsome.tech/courses/python-course/watch?lesson=m21l03
# © LearnSome.tech
import random

random.seed(42)
deck = ['ace', 'king', 'queen', 'jack']
random.shuffle(deck)
print(deck)

print(random.sample(range(1, 50), 6))
print(random.choices(['heads', 'tails'], k=5))
