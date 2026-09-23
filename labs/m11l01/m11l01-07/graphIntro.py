# Hands-on Python: Complete Video Course & Book — lesson m11l01 — A Graphics Introduction
# https://learnsome.tech/courses/python-course/watch?lesson=m11l01
# © LearnSome.tech
'''Starts with same graphics as graphIntroSteps.py
Also adds illustrations of debugging print statements at the end.
'''

from graphics import *
win = GraphWin()

pt = Point(100, 50)

pt.draw(win)

cir = Circle(pt, 25) 
cir.draw(win) 

cir.setOutline('red') 
cir.setFill('blue')
