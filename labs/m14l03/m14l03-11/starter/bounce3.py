    delay = .001
    pt = None                        #NEW
    while  pt == None:               #NEW
        shape.move(dx, dy)
        center = shape.getCenter()
        x = center.getX()
        y = center.getY()
        isInside = True              #NEW
        if x < xLow or x > xHigh:
            dx = -dx
            isInside = False         #NEW
        if y < yLow or y > yHigh:
            dy = -dy
            isInside = False         #NEW
        time.sleep(delay)
        if isInside: # NEW  don't mess with dx, dy when outside  
            pt = win.checkMouse()    #NEW
    return pt                        #NEW
