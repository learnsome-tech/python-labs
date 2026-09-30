    xHigh = win.getWidth() - radius
    yLow = radius
    yHigh = win.getHeight() - radius

    center = getRandomPoint(xLow, xHigh, yLow, yHigh)
    ball = makeDisk(center, radius, win)
    
    bounceInBox(ball, dx, dy, xLow, xHigh, yLow, yHigh)    
    win.close()
    
bounceBall(3, 5)
