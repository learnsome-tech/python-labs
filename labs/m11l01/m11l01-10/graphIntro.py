# Hands-on Python: Complete Video Course & Book — lesson m11l01 — A Graphics Introduction
# https://learnsome.tech/courses/python-course/watch?lesson=m11l01
# © LearnSome.tech
cir = Circle(pt, 25) 
cir.draw(win) 

cir.setOutline('red') 
cir.setFill('blue') 

line = Line(pt, Point(150, 100)) 
line.draw(win) 

rect = Rectangle(Point(20, 10), pt) 
rect.draw(win) 

line.move(10, 40)
