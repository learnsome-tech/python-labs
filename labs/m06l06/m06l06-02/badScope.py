# Hands-on Python: Complete Video Course & Book — lesson m06l06 — Local Scope And Global Constants
# https://learnsome.tech/courses/python-course/watch?lesson=m06l06
# © LearnSome.tech
'''program causing an error with an undefined variable'''

def main():
    x = 3
    f()

def f():
    print(x)  # error: f does not know about the x defined in main

main()
