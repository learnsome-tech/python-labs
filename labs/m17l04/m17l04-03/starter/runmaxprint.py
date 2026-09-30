def running_max(numbers):
    best = 0
    for value in numbers:
        print('value is', value, 'and best is', best)
        if value > best:
            best = value
    return best

print(running_max([-5, -2, -9]))
