# say this out loud and see how far you get
result = [f(x, y) for x in xs if ok(x) for y in g(x) if y]

# a comprehension is for building a value, not for doing
for line in lines:
    print(line)
