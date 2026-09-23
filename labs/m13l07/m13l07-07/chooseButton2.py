# Hands-on Python: Complete Video Course & Book — lesson m13l07 — Loops And Tuples
# https://learnsome.tech/courses/python-course/watch?lesson=m13l07
# © LearnSome.tech
def getChoice(choicePairs, default, win):     #NEW
    '''Given a list choicePairs of tuples with each tuple in the form
    (rectangle, choice), return the choice that goes with the rectangle
    in win where the mouse gets clicked, or return default if the click
    is in none of the rectangles.'''

    point = win.getMouse()
    for (rectangle, choice) in choicePairs:
        if isInside(point, rectangle):
            return choice
    return default
