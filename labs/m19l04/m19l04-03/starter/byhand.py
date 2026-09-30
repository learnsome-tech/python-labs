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
