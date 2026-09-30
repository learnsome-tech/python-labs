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

print(getKeys('blah {animal} blah blah {food} ...'))
