'''The loop a list comprehension replaces.'''

words = ['pear', 'fig', 'banana', 'kiwi']

lengths = []
for word in words:
    lengths.append(len(word))

print(lengths)
print([len(word) for word in words])
