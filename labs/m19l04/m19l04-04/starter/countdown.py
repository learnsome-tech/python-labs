'''A generator function counts without building a list.'''

def countdown(n):
    while n > 0:
        yield n
        n = n - 1

for number in countdown(3):
    print(number)

print(list(countdown(5)))
print(sum(countdown(100)))
