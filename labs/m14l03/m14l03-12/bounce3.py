# Hands-on Python: Complete Video Course & Book — lesson m14l03 — Graphical Applications With While
# https://learnsome.tech/courses/python-course/watch?lesson=m14l03
# © LearnSome.tech
def moveInBox(shape, stopHeight, xLow, xHigh, yLow, yHigh, win): #NEW
    '''Shape bounces in win so its center stays within the low and high
    x and y coordinates, and changes direction based on mouse clicks,
    terminating when there is a click above stopHeight.'''

    scale = 0.01 
    pt = shape.getCenter() # starts motionless
    while pt.getY() < stopHeight:
       (dx, dy) = getShift(shape.getCenter(), pt)
       pt = bounceInBox(shape, dx*scale, dy*scale,
                        xLow, xHigh, yLow, yHigh, win)
