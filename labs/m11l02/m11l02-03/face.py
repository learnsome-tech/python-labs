# Hands-on Python: Complete Video Course & Book — lesson m11l02 — Sample Graphics Programs
# https://learnsome.tech/courses/python-course/watch?lesson=m11l02
# © LearnSome.tech
    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("yellow")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('blue')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)
