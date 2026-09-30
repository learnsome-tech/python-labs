total = 0
for n in range(1, 5):
    total = total + n
print('sum:', total)

for word in ['red', 'green']:
    print(word, end=' ')
print()

count = 1
for _ in range(3):
    print('step', count, end='; ')
    count = count * 2
print()
