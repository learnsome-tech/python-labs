# Hands-on Python: Complete Video Course & Book — lesson m11l07 — Entry Objects
# https://learnsome.tech/courses/python-course/watch?lesson=m11l07
# © LearnSome.tech
    win.getMouse()  # To know the user is finished with the text.

    name = entry1.getText()

    greeting1 = 'Hello, ' + name + '!'
    Text(Point(win.getWidth()/3, 150), greeting1).draw(win)

    greeting2 = 'Bonjour, ' + name + '!'
    Text(Point(2*win.getWidth()/3, 100), greeting2).draw(win)

    win.promptClose(instructions)

main()
