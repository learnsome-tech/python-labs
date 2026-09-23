# Hands-on Python: Complete Video Course & Book — lesson m07l04 — Repeat Loops And Successive Modification
# https://learnsome.tech/courses/python-course/watch?lesson=m07l04
# © LearnSome.tech
'''prints poorly numbered entries from the list'''

items = ['red', 'orange', 'yellow', 'green']
number = 1
for item in items:
    print(number, item)
    number = 2 # will change to 2 after printing 1
