def running_max(numbers):
    best = 0
    for value in numbers:
        if value > best:
            best = value
    return best

breakpoint()
print(running_max([-5, -2, -9]))
