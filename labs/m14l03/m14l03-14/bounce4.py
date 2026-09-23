# Hands-on Python: Complete Video Course & Book — lesson m14l03 — Graphical Applications With While
# https://learnsome.tech/courses/python-course/watch?lesson=m14l03
# © LearnSome.tech
def moveInBox(shape, stopHeight, xLow, xHigh, yLow, yHigh, win):
    ''' Animate a shape moving toward any mouse click below stopHeight and
    bouncing when its center reaches the low or high x or y coordinates.
    The animation stops when the mouse is clicked at stopHeight or above.'''
    
    scale = 0.01 
    delay = .001
    dx = 0                      #NEW dx and dy are no longer parameters
    dy = 0                      #NEW
    while True:                 #NEW exit loop at return statement
        center = shape.getCenter()
        x = center.getX()
        y = center.getY()
        isInside = True
        if x < xLow or x > xHigh:
            dx = -dx
            isInside = False
        if y < yLow or y > yHigh:
            dy = -dy            
            isInside = False
        if isInside:
            pt = win.checkMouse()
