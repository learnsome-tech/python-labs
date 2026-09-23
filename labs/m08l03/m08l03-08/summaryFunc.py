# Hands-on Python: Complete Video Course & Book — lesson m08l03 — Chapter One In One Sitting
# https://learnsome.tech/courses/python-course/watch?lesson=m08l03
# © LearnSome.tech
'''Summary example: define, call, return.'''

TAX = 0.2

def withTax(price):
    '''Return the price with tax added.'''
    return price * (1 + TAX)

def main():
    for price in [10, 25]:
        print(price, 'costs', format(withTax(price), '.2f'))

main()
