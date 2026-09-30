def running_max(numbers):
    best = numbers[0]
    for value in numbers[1:]:
        if value > best:
            best = value
    return best

print(running_max([3, 9, 4]))
print(running_max([-5, -2, -9]))
