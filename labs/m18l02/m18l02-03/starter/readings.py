'''Temperature readings, in degrees Celsius.'''

READINGS = [12, 15, 19, 14]

def highest():
    return max(READINGS)

def average():
    return sum(READINGS) / len(READINGS)
