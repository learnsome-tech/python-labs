from itertools import combinations, count, cycle, islice

for n in islice(count(10, 5), 4):
    print(n, end=' ')
print()

colours = cycle(['red', 'green'])
print([next(colours) for _ in range(5)])

for pair in combinations('abc', 2):
    print(pair)
