try:
    age = int(input('Your age: '))
    print('Next year you will be', age + 1)
except ValueError:
    print('That was not a whole number.')
