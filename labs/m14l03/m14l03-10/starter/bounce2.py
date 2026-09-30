    ball = makeDisk(center, radius, win)

    #NEW interactive direction and speed setting
    prompt = '''                            
Click to indicate the direction and
speed of the ball:  The further you
click from the ball, the faster it starts.'''
    (dx, dy) = getUserShift(center, prompt, win)
    scale = 0.01 # to reduce the size of animation steps    
    bounceInBox(ball, dx*scale, dy*scale, xLow, xHigh, yLow, yHigh, win)
