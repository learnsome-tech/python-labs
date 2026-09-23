# Hands-on Python: Complete Video Course & Book — lesson m11l04 — Mutable Objects And Aliases
# https://learnsome.tech/courses/python-course/watch?lesson=m11l04
# © LearnSome.tech
def main():
    win = GraphWin('Draw a Rectangle (NOT!)', 300, 300)
    win.yUp()

    rect = makeRect(Point(20, 50), 250, 200)
    rect.draw(win)

    win.promptClose(win.getWidth()/2, 20)

main()
