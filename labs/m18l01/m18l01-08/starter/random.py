'''Name this file random.py and the real random module is hidden.'''

import random

if __name__ == '__main__':
    print(random.__name__)
    print(random.__file__.endswith('random.py'))
    print(hasattr(random, 'randint'))
