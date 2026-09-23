# Hands-on Python: Complete Video Course & Book — lesson m05l03 — The String Format Method
# https://learnsome.tech/courses/python-course/watch?lesson=m05l03
# © LearnSome.tech
'''Two numeric inputs, explicit sum'''

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))
sum = x+y
sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
print(sentence)
