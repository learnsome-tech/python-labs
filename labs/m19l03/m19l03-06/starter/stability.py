'''Sorting twice: stability keeps the earlier order inside ties.'''

people = [('Grace', 'B'), ('Ada', 'A'), ('Alan', 'B'), ('Edsger', 'A')]

people.sort(key=lambda person: person[0])
print(people)

people.sort(key=lambda person: person[1])
print(people)
