# Hands-on Python: Complete Video Course & Book — lesson m17l04 — Debugging: print, breakpoint, and the debugger
# https://learnsome.tech/courses/python-course/watch?lesson=m17l04
# © LearnSome.tech
def running_max(numbers):
    best = 0
    for value in numbers:
        if value > best:
            best = value
    return best

breakpoint()
print(running_max([-5, -2, -9]))
