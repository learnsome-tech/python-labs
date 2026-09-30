def hundred_over(text):
    try:
        return 100 / int(text)
    except ValueError:
        return 'not a number'
    except ZeroDivisionError:
        return 'cannot divide by zero'

for text in ['8', 'four', '0']:
    print(text, '->', hundred_over(text))
