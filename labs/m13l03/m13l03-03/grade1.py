# Hands-on Python: Complete Video Course & Book — lesson m13l03 — If Elif Chains
# https://learnsome.tech/courses/python-course/watch?lesson=m13l03
# © LearnSome.tech
def letterGrade(score):
    if score >= 90:
        letter = 'A'
    elif score >= 80:
        letter = 'B'
    elif score >= 70:
        letter = 'C'
    elif score >= 60:
        letter = 'D'
    else:
        letter = 'F'
    return letter
