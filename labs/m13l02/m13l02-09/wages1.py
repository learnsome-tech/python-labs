# Hands-on Python: Complete Video Course & Book — lesson m13l02 — If Else, And Conditional Expressions
# https://learnsome.tech/courses/python-course/watch?lesson=m13l02
# © LearnSome.tech
    if totalHours <= 40:
        regularHours = totalHours
        overtime = 0
    else:
        overtime = totalHours - 40
        regularHours = 40
    return hourlyWage*regularHours + (1.5*hourlyWage)*overtime
