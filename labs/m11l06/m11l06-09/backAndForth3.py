# Hands-on Python: Complete Video Course & Book — lesson m11l06 — Animation: Loops, Bouncing, Flushing
# https://learnsome.tech/courses/python-course/watch?lesson=m11l06
# © LearnSome.tech
def makeFace(center, win):
    '''display face centered at center in window win.
    Return a list of the shapes in the face.
    '''

    head = Circle(center, 25)
    head.setFill("yellow")
    head.draw(win)

    eye1Center = center.clone() # face positions are relative to the center
