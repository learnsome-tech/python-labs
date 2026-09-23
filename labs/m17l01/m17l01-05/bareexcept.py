# Hands-on Python: Complete Video Course & Book — lesson m17l01 — Exceptions: try, except, else, finally
# https://learnsome.tech/courses/python-course/watch?lesson=m17l01
# © LearnSome.tech
numbers = [2, 4, 9]
try:
    total = 0
    for n in numbers:
        total = total + n
    print('average is', total / lenght(numbers))
except:
    print('something went wrong')
