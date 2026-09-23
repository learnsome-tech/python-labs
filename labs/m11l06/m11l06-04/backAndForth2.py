# Hands-on Python: Complete Video Course & Book — lesson m11l06 — Animation: Loops, Bouncing, Flushing
# https://learnsome.tech/courses/python-course/watch?lesson=m11l06
# © LearnSome.tech
    mouth = Oval(Point(30, 90), Point(50, 85))
    mouth.setFill("red")
    mouth.draw(win)

    faceList = [head, eye1, eye2, mouth]

    cir2 = Circle(Point(150,125), 25)
    cir2.setFill("red")
    cir2.draw(win)

    moveAllOnLine(faceList, 5, 0, 46, .05)
    moveAllOnLine(faceList, -5, 0, 46, .05)

    win.promptClose(win.getWidth()/2, 20)

main()
