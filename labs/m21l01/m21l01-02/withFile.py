# Hands-on Python: Complete Video Course & Book — lesson m21l01 — Paths And Files The Modern Way
# https://learnsome.tech/courses/python-course/watch?lesson=m21l01
# © LearnSome.tech
with open('notes.txt', 'w') as out:
    out.write('first line\n')
    out.write('second line\n')

print(out.closed)
print(open('notes.txt').read())
