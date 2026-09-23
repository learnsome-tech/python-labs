# Hands-on Python: Complete Video Course & Book — lesson m11l07 — Entry Objects
# https://learnsome.tech/courses/python-course/watch?lesson=m11l07
# © LearnSome.tech
"""Example with two Entry objects and type conversion.
Do addition.
"""

from graphics import *

def main():
    win = GraphWin("Addition", 300, 300)
    win.yUp()

    instructions = Text(Point(win.getWidth()/2, 30),
                     "Enter two numbers.\nThen click the mouse.")
    instructions.draw(win)

    entry1 = Entry(Point(win.getWidth()/2, 250),25)
    entry1.setText('0')
    entry1.draw(win)

    Text(Point(win.getWidth()/2, 280),'First Number:').draw(win)
