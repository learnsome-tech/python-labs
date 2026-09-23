# Hands-on Python: Complete Video Course & Book — lesson m05l02 — Input, And Numbers Versus Digits
# https://learnsome.tech/courses/python-course/watch?lesson=m05l02
# © LearnSome.tech
'''Conversion of strings to int before addition'''

xString = input("Enter a number: ")
x = int(xString)
yString = input("Enter a second number: ")
y = int(yString)
print('The sum of ', x, ' and ', y, ' is ', x+y, '.', sep='')
