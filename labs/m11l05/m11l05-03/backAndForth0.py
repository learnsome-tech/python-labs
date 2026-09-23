# Hands-on Python: Complete Video Course & Book — lesson m11l05 — Animation: Moving One Shape
# https://learnsome.tech/courses/python-course/watch?lesson=m11l05
# © LearnSome.tech
    for i in range(46):
        cir1.move(5, 0)
        time.sleep(.05)

    for i in range(46):
        cir1.move(-5, 0)
        time.sleep(.05)

    win.promptClose(win.getWidth()/2, 20)

main()
