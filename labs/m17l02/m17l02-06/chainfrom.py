# Hands-on Python: Complete Video Course & Book — lesson m17l02 — Raising, And Writing Your Own Exception
# https://learnsome.tech/courses/python-course/watch?lesson=m17l02
# © LearnSome.tech
settings = {'host': 'localhost'}

def port():
    try:
        return settings['port']
    except KeyError as err:
        raise RuntimeError('the settings file is incomplete') from err

print(port())
