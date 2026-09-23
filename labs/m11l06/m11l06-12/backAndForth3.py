# Hands-on Python: Complete Video Course & Book — lesson m11l06 — Animation: Loops, Bouncing, Flushing
# https://learnsome.tech/courses/python-course/watch?lesson=m11l06
# © LearnSome.tech
def main():
    win = GraphWin('Back and Forth', 300, 300)
    win.yUp() # make right side up coordinates!

    rect = Rectangle(Point(200, 90), Point(220, 100))
    rect.setFill("blue")
    rect.draw(win)

    faceList = makeFace(Point(40, 100), win)
    faceList2 = makeFace(Point(150,125), win)

    stepsAcross = 46
    dx = 5
    dy = 3
    wait = .05
    for i in range(3):
        moveAllOnLine(faceList, dx, 0, stepsAcross, wait)
        moveAllOnLine(faceList, -dx, dy, stepsAcross//2, wait)
        moveAllOnLine(faceList, -dx, -dy, stepsAcross//2, wait)

    win.promptClose(win.getWidth()/2, 20)
