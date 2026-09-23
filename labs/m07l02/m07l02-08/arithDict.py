# Hands-on Python: Complete Video Course & Book — lesson m07l02 — Dictionaries And String Formatting
# https://learnsome.tech/courses/python-course/watch?lesson=m07l02
# © LearnSome.tech
'''Fancier format string example, with locals().'''

x = 20
y = 30
sum = x + y
prod = x * y
formatStr = '{x} + {y} = {sum}; {x} * {y} = {prod}.'
equations = formatStr.format(**locals())
print(equations)
