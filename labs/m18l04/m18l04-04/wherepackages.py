# Hands-on Python: Complete Video Course & Book — lesson m18l04 — pip, requirements, and installing packages
# https://learnsome.tech/courses/python-course/watch?lesson=m18l04
# © LearnSome.tech
'''Where would an installed package land for this interpreter?'''

import os
import sys

print('last folder searched:', os.path.basename(sys.path[-1]))
print('inside a virtual environment:', sys.prefix != sys.base_prefix)
