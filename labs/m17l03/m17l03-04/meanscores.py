# Hands-on Python: Complete Video Course & Book — lesson m17l03 — Reading A Traceback Like A Professional
# https://learnsome.tech/courses/python-course/watch?lesson=m17l03
# © LearnSome.tech
import statistics

def average(scores):
    return statistics.mean(scores)

def report(scores):
    print('average is', average(scores))

report([7, 11, 3])
report([])
