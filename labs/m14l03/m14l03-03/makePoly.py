# Hands-on Python: Complete Video Course & Book — lesson m14l03 — Graphical Applications With While
# https://learnsome.tech/courses/python-course/watch?lesson=m14l03
# © LearnSome.tech
    while isInside(pt, rect):
        vertices.append(pt) 
        poly = Polygon(vertices)  
        poly.draw(win)
        pt = win.getMouse()
        poly.undraw()
