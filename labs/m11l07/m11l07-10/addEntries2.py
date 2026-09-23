# Hands-on Python: Complete Video Course & Book — lesson m11l07 — Entry Objects
# https://learnsome.tech/courses/python-course/watch?lesson=m11l07
# © LearnSome.tech
    entry1 = makeLabeledEntry(Point(win.getWidth()/2, 250), 25,
                              '0', 'First Number:', win)
    entry2 = makeLabeledEntry(Point(win.getWidth()/2, 180), 25,
                              '0', 'Second Number:', win)

    win.getMouse()  # To know the user is finished with the text.

    num1 = int(entry1.getText())
    num2 = int(entry2.getText())
    sum = num1 + num2
