with open('notes.txt', 'w') as out:
    out.write('first line\n')
    out.write('second line\n')

print(out.closed)
print(open('notes.txt').read())
