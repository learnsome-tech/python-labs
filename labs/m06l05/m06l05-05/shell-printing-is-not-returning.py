# Hands-on Python: Complete Video Course & Book — lesson m06l05 — Returning Values
# https://learnsome.tech/courses/python-course/watch?lesson=m06l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

def printSum(x, y):
    print(x + y)
def returnSum(x, y):
    return x + y
printSum(2, 3)
#   5
returnSum(2, 3)
#   5
print(printSum(2, 3))
#   5
#   None
print(returnSum(2, 3))
#   5
returnSum(2, 3) * 10
#   50
printSum(2, 3) * 10
#   5
#   Traceback (most recent call last):
#   TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
