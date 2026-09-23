# Hands-on Python: Complete Video Course & Book — lesson m14l03 — Graphical Applications With While
# https://learnsome.tech/courses/python-course/watch?lesson=m14l03
# © LearnSome.tech
def polyHere(rect, win):
    '''  Draw a polygon interactively in Rectangle rect, in GraphWin win. 
    Collect mouse clicks inside rect into the vertices of a Polygon,
    and always draw the Polygon created so far.
    When a click goes outside rect, stop and return the final polygon. 
    The Polygon ends up drawn.  The method draws and undraws rect.
    ''' 
    rect.setOutline("red")
    rect.draw(win)
    vertices = list()
    pt = win.getMouse()
    while isInside(pt, rect):
        vertices.append(pt) 
        poly = Polygon(vertices)  
        poly.draw(win)
        pt = win.getMouse()
        poly.undraw() 
    poly.draw(win)
    rect.undraw()
    return poly
