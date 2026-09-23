# Hands-on Python: Complete Video Course & Book — lesson m10l02 — Mad Libs Revisited: The Whole Program
# https://learnsome.tech/courses/python-course/watch?lesson=m10l02
# © LearnSome.tech
def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys.
    Return a set containing all the keys from the format string.'''

    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1 # pass the '{'
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key) # may add duplicates

    return set(keyList) # removes duplicates: no duplicates in a set
