# Hands-on Python: Complete Video Course & Book — lesson m07l05 — Accumulation Loops
# https://learnsome.tech/courses/python-course/watch?lesson=m07l05
# © LearnSome.tech
def sumList(nums):
    '''Return the sum of the numbers in the list nums.'''
    sum = 0
    for num in nums:
        sum = sum + num
    return sum

print(sumList([5, 2, 4, 7]))
