# Hands-on Python: Complete Video Course & Book — lesson m11l06 — Animation: Loops, Bouncing, Flushing
# https://learnsome.tech/courses/python-course/watch?lesson=m11l06
# © LearnSome.tech
    mouthCorner1 = center.clone()
    mouthCorner1.move(-10, -10)
    mouthCorner2 = mouthCorner1.clone()
    mouthCorner2.move(20, -5)

    mouth = Oval(mouthCorner1, mouthCorner2)
    mouth.setFill("red")
    mouth.draw(win)

    return [head, eye1, eye2, mouth]
