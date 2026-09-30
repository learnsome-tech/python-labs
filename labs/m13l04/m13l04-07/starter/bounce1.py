def bounceBall(dx, dy):
    '''Make a ball bounce around the screen, initially moving by (dx, dy)
    at each jump.'''    
    win = GraphWin('Ball Bounce', 290, 290)
    win.yUp()

    radius = 10
