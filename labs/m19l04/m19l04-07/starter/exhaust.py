'''A generator can be walked through once.'''

def countdown(n):
    while n > 0:
        yield n
        n = n - 1

c = countdown(3)
print(list(c))
print(list(c))

for number in countdown(3):
    print(number)
