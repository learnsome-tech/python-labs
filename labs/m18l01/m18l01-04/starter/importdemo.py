'''Importing a module runs it, and only the first time.'''

import mathfunc
import mathfunc

print(mathfunc.m(10))
print(mathfunc.__name__)
print(__name__)
