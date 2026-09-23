# Hands-on Python: Complete Video Course & Book — lesson m14l03 — Graphical Applications With While
# https://learnsome.tech/courses/python-course/watch?lesson=m14l03
# © LearnSome.tech
def getShift(point1, point2): # NEW utility function
    '''Returns a tuple (dx, dy) which is the shift from point1 to point2.'''
    dx = point2.getX() - point1.getX()
    dy = point2.getY() - point1.getY()
    return (dx, dy)

def getUserShift(point, prompt, win): #NEW direction selection
    '''Return the change in position from the point to a mouse click in win.
    First display the prompt string under point.'''
    
    text = Text(Point(point.getX(), 60), prompt)
    text.draw(win)
    userPt = win.getMouse()
    text.undraw()
    return getShift(point, userPt)
