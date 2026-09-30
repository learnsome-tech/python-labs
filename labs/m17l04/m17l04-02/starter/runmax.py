def running_max(numbers):
    best = 0
    for value in numbers:
        if value > best:
            best = value
    return best

print(running_max([3, 9, 4]))
print(running_max([-5, -2, -9]))
