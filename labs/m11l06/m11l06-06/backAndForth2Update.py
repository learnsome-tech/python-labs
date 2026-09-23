# Hands-on Python: Complete Video Course & Book — lesson m11l06 — Animation: Loops, Bouncing, Flushing
# https://learnsome.tech/courses/python-course/watch?lesson=m11l06
# © LearnSome.tech
def moveAll(shapeList, dx, dy):
    ''' Move all shapes in shapeList by (dx, dy).'''
    for shape in shapeList:
        shape.move(dx, dy)

                             #NEW update version, added win param
def moveAllOnLineUpdate(shapeList, dx, dy, repetitions, delay, win):
    '''Animate the shapes in shapeList along a line in win.
    Move by (dx, dy) each time.
    Repeat the specified number of repetitions.
    Have the specified delay (in seconds) after each repeat.
    '''
    win.autoflush = False          # NEW: set before animation
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        update()         # NEW needed to make all the changes appear
        time.sleep(delay)
    win.autoflush = True           # NEW: set after animation
