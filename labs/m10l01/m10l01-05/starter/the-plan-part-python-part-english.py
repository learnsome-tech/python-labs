def getKeys(formatString):
    keyList = list()
    ?? other initializations ??
    repetitions = formatString.count('{')
    for i in range(repetitions):
        find the start and end of the next key
        key = formatString[start : end]
        keyList.append(key)
    return keyList
