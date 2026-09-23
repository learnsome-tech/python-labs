# Hands-on Python: Complete Video Course & Book — lesson m11l02 — Sample Graphics Programs
# https://learnsome.tech/courses/python-course/watch?lesson=m11l02
# © LearnSome.tech
def main():
    win = GraphWin('Balloons', 200, 300)
    win.yUp() # right side up coordinates

    base = Point(100, 50)

    for center in [Point(50, 200), Point(150, 220), Point(100, 225)]:
        line = Line(base, center)
        line.draw(win)
        balloon = Circle(center, 40)
        balloon.setOutline('red')
        balloon.setFill('pink')
        balloon.draw(win)

    win.promptClose(win.getWidth()/2, 20)

main()
