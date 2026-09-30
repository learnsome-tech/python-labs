    while isInside(pt, rect):
        vertices.append(pt) 
        poly = Polygon(vertices)  
        poly.draw(win)
        pt = win.getMouse()
        poly.undraw()
