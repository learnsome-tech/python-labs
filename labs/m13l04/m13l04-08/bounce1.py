# Hands-on Python: Complete Video Course & Book — lesson m13l04 — Nesting Control Flow Statements
# https://learnsome.tech/courses/python-course/watch?lesson=m13l04
# © LearnSome.tech
    xHigh = win.getWidth() - radius
    yLow = radius
    yHigh = win.getHeight() - radius

    center = getRandomPoint(xLow, xHigh, yLow, yHigh)
    ball = makeDisk(center, radius, win)
    
    bounceInBox(ball, dx, dy, xLow, xHigh, yLow, yHigh)    
    win.close()
    
bounceBall(3, 5)
