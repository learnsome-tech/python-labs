# Hands-on Python: Complete Video Course & Book — lesson m22l01 — Testing With pytest
# https://learnsome.tech/courses/python-course/watch?lesson=m22l01
# © LearnSome.tech
def discount(price, percent):
    """Return price with percent taken off, rounded to the penny."""
    if not 0 <= percent <= 100:
        raise ValueError('percent must be between 0 and 100')
    return round(price * percent / 100, 2)
