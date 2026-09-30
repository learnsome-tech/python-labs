import csv

rows = [['name', 'city', 'visits'],
        ['Ada', 'London', '3'],
        ['Grace', 'New York, NY', '7']]

with open('people.csv', 'w', newline='', encoding='utf-8') as out:
    csv.writer(out).writerows(rows)

print(open('people.csv', encoding='utf-8').read(), end='')

with open('people.csv', newline='', encoding='utf-8') as f:
    for row in csv.reader(f):
        print(row)
