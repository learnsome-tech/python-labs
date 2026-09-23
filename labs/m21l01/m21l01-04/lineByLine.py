# Hands-on Python: Complete Video Course & Book — lesson m21l01 — Paths And Files The Modern Way
# https://learnsome.tech/courses/python-course/watch?lesson=m21l01
# © LearnSome.tech
with open('shopping.txt', 'w') as out:
    out.write('bread\nmilk\napples\n')

with open('shopping.txt') as f:
    whole = f.read()
print(len(whole), whole.count('\n'))

with open('shopping.txt') as f:
    for number, line in enumerate(f, start=1):
        print(number, line.strip())
