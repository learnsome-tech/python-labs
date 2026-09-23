# Hands-on Python: Complete Video Course & Book — lesson m17l01 — Exceptions: try, except, else, finally
# https://learnsome.tech/courses/python-course/watch?lesson=m17l01
# © LearnSome.tech
try:
    age = int(input('Your age: '))
    print('Next year you will be', age + 1)
except ValueError:
    print('That was not a whole number.')
