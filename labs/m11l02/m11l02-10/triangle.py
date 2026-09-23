# Hands-on Python: Complete Video Course & Book — lesson m11l02 — Sample Graphics Programs
# https://learnsome.tech/courses/python-course/watch?lesson=m11l02
# © LearnSome.tech
    # Use Polygon object to draw the triangle
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)

    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()
