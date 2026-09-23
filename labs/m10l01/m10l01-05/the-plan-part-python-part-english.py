# Hands-on Python: Complete Video Course & Book — lesson m10l01 — Mad Libs Revisited: Finding The Cues
# https://learnsome.tech/courses/python-course/watch?lesson=m10l01
# © LearnSome.tech
def getKeys(formatString):
    keyList = list()
    ?? other initializations ??
    repetitions = formatString.count('{')
    for i in range(repetitions):
        find the start and end of the next key
        key = formatString[start : end]
        keyList.append(key)
    return keyList
