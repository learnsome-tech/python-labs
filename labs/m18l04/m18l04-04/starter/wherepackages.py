'''Where would an installed package land for this interpreter?'''

import os
import sys

print('last folder searched:', os.path.basename(sys.path[-1]))
print('inside a virtual environment:', sys.prefix != sys.base_prefix)
