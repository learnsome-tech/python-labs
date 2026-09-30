def ask_number(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print('Please type a whole number.')

age = ask_number('Your age: ')
print('Next year you will be', age + 1)
