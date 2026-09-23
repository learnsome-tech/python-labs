# Hands-on Python: Complete Video Course & Book — lesson m13l04 — Nesting Control Flow Statements
# https://learnsome.tech/courses/python-course/watch?lesson=m13l04
# © LearnSome.tech
def getRandomPoint(xLow, xHigh, yLow, yHigh):
    '''Return a random Point with coordinates in the range specified.'''
    x = random.randrange(xLow, xHigh+1)
    y = random.randrange(yLow, yHigh+1)
    return Point(x, y)
