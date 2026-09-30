'''Summary example: define, call, return.'''

TAX = 0.2

def withTax(price):
    '''Return the price with tax added.'''
    return price * (1 + TAX)

def main():
    for price in [10, 25]:
        print(price, 'costs', format(withTax(price), '.2f'))

main()
