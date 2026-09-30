import re

line = 'Order 1234 shipped on 2026-03-14 to Ada'

print(re.findall(r'\d+', line))

match = re.search(r'(\d{4})-(\d{2})-(\d{2})', line)
print(match.group(0), match.group(1))

print(re.sub(r'\d', 'X', line))

pattern = re.compile(r'^Order (\d+)')
found = pattern.match(line)
print(found.group(1))
print(pattern.match('no order here'))
