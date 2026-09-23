# Hands-on Python: Complete Video Course & Book — lesson m11l08 — Colours, Custom And Random
# https://learnsome.tech/courses/python-course/watch?lesson=m11l08
# © LearnSome.tech
        radius = random.randrange(3, 40)
        x = random.randrange(5, 295)
        y = random.randrange(5, 295)

        circle = Circle(Point(x,y), radius)
        circle.setFill(color)
        circle.draw(win)
        time.sleep(.05)

    win.promptClose(win.getWidth()/2, 20)

main()
