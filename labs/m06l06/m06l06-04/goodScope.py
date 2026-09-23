# Hands-on Python: Complete Video Course & Book — lesson m06l06 — Local Scope And Global Constants
# https://learnsome.tech/courses/python-course/watch?lesson=m06l06
# © LearnSome.tech
'''A change to badScope.py avoiding any error by passing a parameter'''

def main():
    x = 3
    f(x)

def f(x):
    print(x)  

main()
