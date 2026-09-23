# Hands-on Python: Complete Video Course & Book — lesson m11l04 — Mutable Objects And Aliases
# https://learnsome.tech/courses/python-course/watch?lesson=m11l04
# © LearnSome.tech
'''Program: makeRectBad.py
Attempt a function makeRect (incorrectly),
which takes a takes a corner point and dimensions to construct a Rectangle.
'''

from graphics import *

def makeRect(corner, width, height):  # Incorrect!
    '''Return a new Rectangle given one corner Point and the dimensions.'''
    corner2 = corner
    corner2.move(width, height)
    return Rectangle(corner, corner2)
