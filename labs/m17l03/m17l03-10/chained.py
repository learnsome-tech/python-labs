# Hands-on Python: Complete Video Course & Book — lesson m17l03 — Reading A Traceback Like A Professional
# https://learnsome.tech/courses/python-course/watch?lesson=m17l03
# © LearnSome.tech
counts = {'ana': 7}

def count_for(name):
    try:
        return counts[name]
    except KeyError:
        return counts[name.lower()]

print(count_for('ana'))
print(count_for('Bo'))
