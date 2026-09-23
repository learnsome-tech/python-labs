# Hands-on Python: Complete Video Course & Book — lesson m13l02 — If Else, And Conditional Expressions
# https://learnsome.tech/courses/python-course/watch?lesson=m13l02
# © LearnSome.tech
''' if-else statement example (recommending clothing)'''

def main():    
    temperature = float(input('What is the temperature? '))
    if temperature > 70:
        print('Wear shorts.')
    else:
        print('Wear long pants.')
    print('Get some exercise outside.')

main()
