sorted(words, key=len)        # a named function, not called
sorted(words, key=str.lower)  # case insensitive

sorted(people, key=lambda p: p[1])

def second(p):   # exactly the same thing, with a name
    return p[1]
