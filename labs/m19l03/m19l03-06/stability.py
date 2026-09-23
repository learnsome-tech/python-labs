# Hands-on Python: Complete Video Course & Book — lesson m19l03 — Sorting, Keys And Lambdas
# https://learnsome.tech/courses/python-course/watch?lesson=m19l03
# © LearnSome.tech
'''Sorting twice: stability keeps the earlier order inside ties.'''

people = [('Grace', 'B'), ('Ada', 'A'), ('Alan', 'B'), ('Edsger', 'A')]

people.sort(key=lambda person: person[0])
print(people)

people.sort(key=lambda person: person[1])
print(people)
