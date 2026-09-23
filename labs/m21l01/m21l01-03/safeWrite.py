# Hands-on Python: Complete Video Course & Book — lesson m21l01 — Paths And Files The Modern Way
# https://learnsome.tech/courses/python-course/watch?lesson=m21l01
# © LearnSome.tech
try:
    with open('report.txt', 'w') as out:
        out.write('half a report')
        raise ValueError('the data ran out')
except ValueError as problem:
    print('caught:', problem)

print('file closed:', out.closed)
print('on disk:', repr(open('report.txt').read()))
