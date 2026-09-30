with open('cafe.txt', 'w', encoding='utf-8') as out:
    out.write('café\n')

with open('cafe.txt', 'rb') as f:
    raw = f.read()
print(raw)
print(type(raw), len(raw))

with open('cafe.txt', encoding='utf-8') as f:
    print(repr(f.read()))

try:
    open('cafe.txt', encoding='ascii').read()
except UnicodeDecodeError:
    print('ascii cannot read this file')
