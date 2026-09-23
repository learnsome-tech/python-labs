# Hands-on Python: Complete Video Course & Book — lesson m07l02 — Dictionaries And String Formatting
# https://learnsome.tech/courses/python-course/watch?lesson=m07l02
# © LearnSome.tech
'''Hello to you!  Illustrates locals() for formating in print.
'''

person = input('Enter your name: ')
greeting = 'Hello, {person}!'.format(**locals())
print(greeting)
