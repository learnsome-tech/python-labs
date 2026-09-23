# Hands-on Python: Complete Video Course & Book — lesson m11l02 — Sample Graphics Programs
# https://learnsome.tech/courses/python-course/watch?lesson=m11l02
# © LearnSome.tech
'''Program: triangle.py or triangle.pyw (best name for Windows)
Interactive graphics program to draw a triangle,
with prompts in a Text object and feedback via mouse clicks.
'''

from graphics import *

def main():
    win = GraphWin('Draw a Triangle', 350, 350)
    win.yUp() # right side up coordinates
    win.setBackground('yellow')
    message = Text(Point(win.getWidth()/2, 30), 'Click on three points')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)
