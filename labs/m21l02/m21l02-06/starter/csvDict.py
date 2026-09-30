import csv

with open('people.csv', 'w', newline='', encoding='utf-8') as out:
    out.write('name,city,visits\n')
    out.write('Ada,London,3\n')
    out.write('Grace,"New York, NY",7\n')

with open('people.csv', newline='', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        print(row['name'], row['city'], int(row['visits']) * 2)

line = 'Grace,"New York, NY",7'
print(line.split(','))
