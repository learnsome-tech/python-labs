# Hands-on Python: Complete Video Course & Book — lesson m13l05 — Compound Boolean Expressions
# https://learnsome.tech/courses/python-course/watch?lesson=m13l05
# © LearnSome.tech
    msg.draw(win)
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
