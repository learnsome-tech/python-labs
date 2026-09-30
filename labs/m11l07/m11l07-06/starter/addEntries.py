    entry2 = Entry(Point(win.getWidth()/2, 180),25)
    entry2.setText('0')
    entry2.draw(win)

    Text(Point(win.getWidth()/2, 210),'Second Number:').draw(win)

    win.getMouse()  # To know the user is finished with the text.

    numStr1 = entry1.getText()
    num1 = int(numStr1)

    numStr2 = entry2.getText()
    num2 = int(numStr2)
    sum = num1 + num2
