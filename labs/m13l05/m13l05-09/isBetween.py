# Hands-on Python: Complete Video Course & Book — lesson m13l05 — Compound Boolean Expressions
# https://learnsome.tech/courses/python-course/watch?lesson=m13l05
# © LearnSome.tech
def isBetween(val, end1, end2): 
    '''Return True if val is between the ends. 
    The ends do not need to be in increasing order.'''     
    if end1 <= val <= end2 or end2 <= val <= end1: 
        return True 
    else: 
        return False
