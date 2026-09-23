# Hands-on Python: Complete Video Course & Book — lesson m19l02 — Comprehensions
# https://learnsome.tech/courses/python-course/watch?lesson=m19l02
# © LearnSome.tech
'''A nested comprehension, and the two things it can mean.'''

rows = [[1, 2, 3], [4, 5], [6]]

flat = [value for row in rows for value in row]
print(flat)

table = [[r * c for c in range(1, 4)] for r in range(1, 4)]
print(table)

pairs = [(a, b) for a in 'ab' for b in (1, 2)]
print(pairs)
