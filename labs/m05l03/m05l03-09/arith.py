# Hands-on Python: Complete Video Course & Book — lesson m05l03 — The String Format Method
# https://learnsome.tech/courses/python-course/watch?lesson=m05l03
# © LearnSome.tech
'''Fancier format string example with 
parameter identification numbers
-- useful when some parameters are used several times.'''

x = int(input('Enter an integer: '))
y = int(input('Enter another integer: '))
formatStr = '{0} + {1} = {2}; {0} * {1} = {3}.'
equations = formatStr.format(x, y, x+y, x*y)
print(equations)
