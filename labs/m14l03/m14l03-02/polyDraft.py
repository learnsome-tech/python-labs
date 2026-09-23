# Hands-on Python: Complete Video Course & Book — lesson m14l03 — Graphical Applications With While
# https://learnsome.tech/courses/python-course/watch?lesson=m14l03
# © LearnSome.tech
rect.setOutline('red')   
rect.draw(win) 
vertices = list()         
pt = win.getMouse() 
vertices.append(pt)   
poly = Polygon(vertices)   
poly.draw(win)          # with one point 
pt = win.getMouse() 
poly.undraw()           # missing latest point 
vertices.append(pt)    
poly = Polygon(vertices)   
poly.draw(win)          # with two points 
pt = win.getMouse() 
poly.undraw()           # missing latest point 
vertices.append(pt)    
poly = Polygon(vertices)   
poly.draw(win)          # with three points 
pt = win.getMouse()  # assume outside the region 
 
rect.undraw() 
return poly
