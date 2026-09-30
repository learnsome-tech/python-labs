with open('log.txt', 'w') as out:
    out.write('started\n')

with open('log.txt', 'a') as out:
    out.write('finished\n')

with open('log.txt') as f:
    print(f.read(), end='')

with open('log.txt') as f:
    print(f.readlines())
