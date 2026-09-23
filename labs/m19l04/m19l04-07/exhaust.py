# Hands-on Python: Complete Video Course & Book — lesson m19l04 — Iterators And Generators
# https://learnsome.tech/courses/python-course/watch?lesson=m19l04
# © LearnSome.tech
'''A generator can be walked through once.'''

def countdown(n):
    while n > 0:
        yield n
        n = n - 1

c = countdown(3)
print(list(c))
print(list(c))

for number in countdown(3):
    print(number)
