# Hands-on Python: Complete Video Course & Book — lesson m22l03 — Formatting, Linting And Style
# https://learnsome.tech/courses/python-course/watch?lesson=m22l03
# © LearnSome.tech
import json
def  total( prices,tax = 0.08 ):
    subtotal=sum( prices )
    return subtotal*(1+tax)
print( total([1.50,2.25]) )
