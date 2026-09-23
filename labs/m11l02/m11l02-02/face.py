# Hands-on Python: Complete Video Course & Book — lesson m11l02 — Sample Graphics Programs
# https://learnsome.tech/courses/python-course/watch?lesson=m11l02
# © LearnSome.tech
'''A simple graphics example constructs a face from basic shapes.
'''

from graphics import *


def main():
    win = GraphWin('Face', 200, 150) # give title and dimensions
    win.yUp() # make right side up coordinates!
