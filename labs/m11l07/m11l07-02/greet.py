# Hands-on Python: Complete Video Course & Book — lesson m11l07 — Entry Objects
# https://learnsome.tech/courses/python-course/watch?lesson=m11l07
# © LearnSome.tech
"""Simple example with Entry objects.
Enter your name, click the mouse, and see greetings.
"""

from graphics import *

def main():
    win = GraphWin("Greeting", 300, 300)
    win.yUp()

    instructions = Text(Point(win.getWidth()/2, 40),
                     "Enter your name.\nThen click the mouse.")
    instructions.draw(win)

    entry1 = Entry(Point(win.getWidth()/2, 200),10)
    entry1.draw(win)
