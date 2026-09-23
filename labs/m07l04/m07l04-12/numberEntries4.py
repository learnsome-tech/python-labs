# Hands-on Python: Complete Video Course & Book — lesson m07l04 — Repeat Loops And Successive Modification
# https://learnsome.tech/courses/python-course/watch?lesson=m07l04
# © LearnSome.tech
''' use a function to number the entries in any list'''

def numberList(items):
    '''Print each item in a list items, numbered in order.'''
    number = 1
    for item in items:
        print(number, item)
        number = number + 1

def main():
    numberList(['red', 'orange', 'yellow', 'green'])
    print()
    numberList(['apples', 'pears', 'bananas'])

main()
