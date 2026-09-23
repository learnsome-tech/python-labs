# Hands-on Python: Complete Video Course & Book — lesson m22l02 — Type Hints
# https://learnsome.tech/courses/python-course/watch?lesson=m22l02
# © LearnSome.tech
def double(n: int) -> int:
    return n * 2


print(double(21))
print(double('ab'))
print(double.__annotations__)
