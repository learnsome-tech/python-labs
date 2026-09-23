# Hands-on Python: Complete Video Course & Book — lesson m18l02 — Packages, And Your Own Library
# https://learnsome.tech/courses/python-course/watch?lesson=m18l02
# © LearnSome.tech
'''Turn readings into a sentence.'''

from weather.readings import average, highest

def summary():
    return 'high {}, average {:.1f}'.format(highest(), average())

if __name__ == '__main__':
    print(summary())
