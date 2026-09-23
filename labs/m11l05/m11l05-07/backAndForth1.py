# Hands-on Python: Complete Video Course & Book — lesson m11l05 — Animation: Moving One Shape
# https://learnsome.tech/courses/python-course/watch?lesson=m11l05
# © LearnSome.tech
def moveOnLine(shape, dx, dy, repetitions, delay):
    for i in range(repetitions):
        shape.move(dx, dy)
        time.sleep(delay)
