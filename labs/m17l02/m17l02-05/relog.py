# Hands-on Python: Complete Video Course & Book — lesson m17l02 — Raising, And Writing Your Own Exception
# https://learnsome.tech/courses/python-course/watch?lesson=m17l02
# © LearnSome.tech
def parse_count(text):
    try:
        return int(text)
    except ValueError:
        print('log: bad count from the user:', repr(text))
        raise

print(parse_count('12'))
print(parse_count('a few'))
