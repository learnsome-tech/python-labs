# Hands-on Python: Complete Video Course & Book — lesson m17l01 — Exceptions: try, except, else, finally
# https://learnsome.tech/courses/python-course/watch?lesson=m17l01
# © LearnSome.tech
def hundred_over(text):
    try:
        return 100 / int(text)
    except ValueError:
        return 'not a number'
    except ZeroDivisionError:
        return 'cannot divide by zero'

for text in ['8', 'four', '0']:
    print(text, '->', hundred_over(text))
