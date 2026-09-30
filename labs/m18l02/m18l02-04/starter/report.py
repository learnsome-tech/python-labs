'''Turn readings into a sentence.'''

from weather.readings import average, highest

def summary():
    return 'high {}, average {:.1f}'.format(highest(), average())

if __name__ == '__main__':
    print(summary())
