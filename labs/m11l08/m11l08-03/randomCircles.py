# Hands-on Python: Complete Video Course & Book — lesson m11l08 — Colours, Custom And Random
# https://learnsome.tech/courses/python-course/watch?lesson=m11l08
# © LearnSome.tech
"""Draw random circles.
"""
from graphics import *
import random, time

def main():
    win = GraphWin("Random Circles", 300, 300)
    for i in range(75):
        r = random.randrange(256)
        b = random.randrange(256)
        g = random.randrange(256)
        color = color_rgb(r, g, b)
