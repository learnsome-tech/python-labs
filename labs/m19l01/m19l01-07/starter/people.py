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
