# Hands-on Python: Complete Video Course & Book — lesson m17l03 — Reading A Traceback Like A Professional
# https://learnsome.tech/courses/python-course/watch?lesson=m17l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

total
#   NameError: name 'total' is not defined
'3' + 4
#   TypeError: can only concatenate str (not "int") to str
int('3.5')
#   ValueError: invalid literal for int() with base 10: '3.5'
[10, 20, 30][3]
#   IndexError: list index out of range
{'a': 1}['b']
#   KeyError: 'b'
'hello'.push('x')
#   AttributeError: 'str' object has no attribute 'push'
7 / 0
#   ZeroDivisionError: division by zero
import cgi
#   ModuleNotFoundError: No module named 'cgi'
open('nosuch.txt')
#   FileNotFoundError: [Errno 2] No such file or directory: 'nosuch.txt'
