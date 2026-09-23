# Hands-on Python: Complete Video Course & Book — lesson m19l02 — Comprehensions
# https://learnsome.tech/courses/python-course/watch?lesson=m19l02
# © LearnSome.tech
'''The loop a list comprehension replaces.'''

words = ['pear', 'fig', 'banana', 'kiwi']

lengths = []
for word in words:
    lengths.append(len(word))

print(lengths)
print([len(word) for word in words])
