# Hands-on Python: Complete Video Course & Book — lesson m06l05 — Returning Values
# https://learnsome.tech/courses/python-course/watch?lesson=m06l05
# © LearnSome.tech
'''A function returning a string and using a local variable'''

def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('Benjamin', 'Franklin'))
print(lastFirst('Andrew', 'Harrington'))
