# Hands-on Python: Complete Video Course & Book — lesson m18l02 — Packages, And Your Own Library
# https://learnsome.tech/courses/python-course/watch?lesson=m18l02
# © LearnSome.tech
'''Temperature readings, in degrees Celsius.'''

READINGS = [12, 15, 19, 14]

def highest():
    return max(READINGS)

def average():
    return sum(READINGS) / len(READINGS)
