# Hands-on Python: Complete Video Course & Book — lesson m17l02 — Raising, And Writing Your Own Exception
# https://learnsome.tech/courses/python-course/watch?lesson=m17l02
# © LearnSome.tech
def set_age(years):
    if not isinstance(years, int):
        raise TypeError('age must be a whole number')
    if years < 0:
        raise ValueError('age cannot be negative: ' + str(years))
    return years

for candidate in [30, -3, 'forty']:
    try:
        print('accepted', set_age(candidate))
    except (ValueError, TypeError) as err:
        print('rejected', repr(candidate), '-', err)
