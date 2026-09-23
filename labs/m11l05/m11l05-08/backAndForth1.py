# Hands-on Python: Complete Video Course & Book — lesson m11l05 — Animation: Moving One Shape
# https://learnsome.tech/courses/python-course/watch?lesson=m11l05
# © LearnSome.tech
def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.yUp() # make right side up coordinates!

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    cir1 = Circle(Point(40,100), 25)
    cir1.setFill("yellow")
    cir1.draw(win)

    cir2 = Circle(Point(150,125), 25)
    cir2.setFill("red")
    cir2.draw(win)

    moveOnLine(cir1, 5, 0, 46, .05)
    moveOnLine(cir1, -5, 0, 46, .05)

    win.promptClose(win.getWidth()/2, 20)

main()
