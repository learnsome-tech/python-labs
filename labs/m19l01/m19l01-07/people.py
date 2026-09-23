# Hands-on Python: Complete Video Course & Book — lesson m19l01 — Lists, Tuples, Sets, Dicts: Choosing One
# https://learnsome.tech/courses/python-course/watch?lesson=m19l01
# © LearnSome.tech
'''Nesting the four collections inside each other.'''

people = [
    {'name': 'Ada', 'langs': {'python', 'c'}},
    {'name': 'Alan', 'langs': {'python', 'c', 'go'}},
]

for person in people:
    print(person['name'], 'knows', len(person['langs']), 'languages')

by_name = {person['name']: person for person in people}
print(sorted(by_name))
print(by_name['Ada']['langs'] == {'c', 'python'})
