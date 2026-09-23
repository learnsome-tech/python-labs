# Hands-on Python: Complete Video Course & Book — lesson m13l07 — Loops And Tuples
# https://learnsome.tech/courses/python-course/watch?lesson=m13l07
# © LearnSome.tech
    pt = win.getMouse()

    if isInside(pt, redButton):
        color = 'red'
    elif isInside(pt, yellowButton):
        color = 'yellow'
    elif isInside(pt, blueButton):
        color = 'blue'
    else :
        color = 'white'
    house.setFill(color)
