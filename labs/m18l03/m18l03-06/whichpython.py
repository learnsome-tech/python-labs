# Hands-on Python: Complete Video Course & Book — lesson m18l03 — Virtual Environments
# https://learnsome.tech/courses/python-course/watch?lesson=m18l03
# © LearnSome.tech
'''Is this interpreter running inside a virtual environment?'''

import sys

print('prefix and base prefix agree:', sys.prefix == sys.base_prefix)
print('so this is not a virtual environment')
