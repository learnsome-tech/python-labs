# Hands-on Python: Complete Video Course & Book — lesson m13l03 — If Elif Chains
# https://learnsome.tech/courses/python-course/watch?lesson=m13l03
# © LearnSome.tech
'''Test if-elif-...-else determining a letter grade.'''

def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter

def main():
    x = float(input('Enter a numerical grade: '))
    letter = letterGrade(x)
    print('Your grade is ' + letter + '.') 

main()
