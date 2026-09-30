counts = {'ana': 7}

def count_for(name):
    try:
        return counts[name]
    except KeyError:
        return counts[name.lower()]

print(count_for('ana'))
print(count_for('Bo'))
