# Hands-on Python: Complete Video Course & Book — lesson m17l01 — Exceptions: try, except, else, finally
# https://learnsome.tech/courses/python-course/watch?lesson=m17l01
# © LearnSome.tech
def ask_number(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print('Please type a whole number.')

age = ask_number('Your age: ')
print('Next year you will be', age + 1)
