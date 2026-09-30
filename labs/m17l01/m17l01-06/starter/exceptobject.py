try:
    count = int('12x')
except ValueError as err:
    print('type is', type(err).__name__)
    print('message is', err)
    print('args is', err.args)
