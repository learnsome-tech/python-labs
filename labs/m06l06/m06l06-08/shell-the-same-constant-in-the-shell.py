# Hands-on Python: Complete Video Course & Book — lesson m06l06 — Local Scope And Global Constants
# https://learnsome.tech/courses/python-course/watch?lesson=m06l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

PI = 3.14159265358979
def circleArea(radius):
    return PI*radius*radius
circleArea(5)
#   78.53981633974475
def circleCircumference(radius):
    return 2*PI*radius
circleCircumference(5)
#   31.4159265358979
