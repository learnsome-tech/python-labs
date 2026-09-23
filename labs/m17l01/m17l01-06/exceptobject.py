# Hands-on Python: Complete Video Course & Book — lesson m17l01 — Exceptions: try, except, else, finally
# https://learnsome.tech/courses/python-course/watch?lesson=m17l01
# © LearnSome.tech
try:
    count = int('12x')
except ValueError as err:
    print('type is', type(err).__name__)
    print('message is', err)
    print('args is', err.args)
