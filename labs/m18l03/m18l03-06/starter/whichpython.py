'''Is this interpreter running inside a virtual environment?'''

import sys

print('prefix and base prefix agree:', sys.prefix == sys.base_prefix)
print('so this is not a virtual environment')
