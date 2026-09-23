# Hands-on Python: Complete Video Course & Book — lesson m13l06 — More String Methods
# https://learnsome.tech/courses/python-course/watch?lesson=m13l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

'2397'.isdigit()
#   True
'23a'.isdigit()
#   False
''.isdigit()
#   False
'-123'.isdigit()
#   False
'-123'[1:].isdigit()
#   True
'3.14'.count('.')
#   1
'3.14'.find('.')
#   1
