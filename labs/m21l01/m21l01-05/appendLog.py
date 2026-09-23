# Hands-on Python: Complete Video Course & Book — lesson m21l01 — Paths And Files The Modern Way
# https://learnsome.tech/courses/python-course/watch?lesson=m21l01
# © LearnSome.tech
with open('log.txt', 'w') as out:
    out.write('started\n')

with open('log.txt', 'a') as out:
    out.write('finished\n')

with open('log.txt') as f:
    print(f.read(), end='')

with open('log.txt') as f:
    print(f.readlines())
