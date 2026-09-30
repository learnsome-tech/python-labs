def main():
    win = GraphWin('Draw a Rectangle (NOT!)', 300, 300)
    win.yUp()

    rect = makeRect(Point(20, 50), 250, 200)
    rect.draw(win)

    win.promptClose(win.getWidth()/2, 20)

main()
