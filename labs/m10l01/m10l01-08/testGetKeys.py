# Hands-on Python: Complete Video Course & Book — lesson m10l01 — Mad Libs Revisited: Finding The Cues
# https://learnsome.tech/courses/python-course/watch?lesson=m10l01
# © LearnSome.tech
def getKeys(formatString):
    '''formatString is a format string with embedded dictionary keys.
    Return a list containing all the keys from the format string.'''

    keyList = list()
    end = 0
    repetitions = formatString.count('{')
    for i in range(repetitions):
        start = formatString.find('{', end) + 1
        end = formatString.find('}', start)
        key = formatString[start : end]
        keyList.append(key)
    return keyList
