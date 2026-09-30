def set_age(years):
    if years < 0:
        raise ValueError('age cannot be negative: ' + str(years))
    return years

print(set_age(30))
print(set_age(-3))
