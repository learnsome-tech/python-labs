# Hands-on Python: Complete Video Course & Book — lesson m17l02 — Raising, And Writing Your Own Exception
# https://learnsome.tech/courses/python-course/watch?lesson=m17l02
# © LearnSome.tech
def set_age(years):
    if years < 0:
        raise ValueError('age cannot be negative: ' + str(years))
    return years

print(set_age(30))
print(set_age(-3))
