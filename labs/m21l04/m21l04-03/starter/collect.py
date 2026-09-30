from collections import Counter, defaultdict, namedtuple

words = 'the cat sat on the mat the end'.split()
counts = Counter(words)
print(counts['the'], counts.most_common(2))

groups = defaultdict(list)
for word in words:
    groups[len(word)].append(word)
print(dict(groups))

Point = namedtuple('Point', 'x y')
here = Point(3, 4)
print(here, here.x, here[1])
