# Hands-on Python: Complete Video Course & Book — lesson m19l04 — Iterators And Generators
# https://learnsome.tech/courses/python-course/watch?lesson=m19l04
# © LearnSome.tech
'''What a for loop does underneath.'''

nums = [10, 20, 30]

for value in nums:
    print(value)

it = iter(nums)
while True:
    try:
        value = next(it)
    except StopIteration:
        break
    print(value)
