# Hands-on Python: Complete Video Course & Book — lesson m06l04 — Multiple Parameters
# https://learnsome.tech/courses/python-course/watch?lesson=m06l04
# © LearnSome.tech
'''Display any number of sum problems with a function.
Handle keyboard input separately.
'''

def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)

def main():
    sumProblem(2, 3)
    sumProblem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)

main()
