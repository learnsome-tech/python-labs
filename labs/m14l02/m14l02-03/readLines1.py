# Hands-on Python: Complete Video Course & Book — lesson m14l02 — Interactive While Loops
# https://learnsome.tech/courses/python-course/watch?lesson=m14l02
# © LearnSome.tech
'''Interactive loop with verbose prompt each time.'''

lines = list()
testAnswer = input('Press y if you want to enter more lines: ')
while testAnswer == 'y':
    line = input('Next line: ')
    lines.append(line)
    testAnswer = input('Press y if you want to enter more lines: ')

print('Your lines were:')
for line in lines:
    print(line)
