numbers = [2, 4, 9]
try:
    total = 0
    for n in numbers:
        total = total + n
    print('average is', total / lenght(numbers))
except:
    print('something went wrong')
