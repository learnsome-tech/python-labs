# Hands-on Python: Complete Video Course & Book — lesson m16l01 — Reading Error Messages
# https://learnsome.tech/courses/python-course/watch?lesson=m16l01
# © LearnSome.tech
'''Program with intended error to demonstrate traceback from nested call'''

def invminus4(x):
    return 1.0/(x-4)

def main():
    print('This program is INTENDED to cause an execution error.')
    print('Ok call to invminus4(6) next:')
    print(invminus4(6))
    print('Bad call invminus4(4) next:')
    print(invminus4(4))
    print("Won't get to here!")

main()
