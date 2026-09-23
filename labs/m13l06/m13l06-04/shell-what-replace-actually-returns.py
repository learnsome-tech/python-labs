# Hands-on Python: Complete Video Course & Book — lesson m13l06 — More String Methods
# https://learnsome.tech/courses/python-course/watch?lesson=m13l06
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

s = '-123'
t = s.replace('-', '', 1)
t
#   '123'
t = t.replace('-', '', 1)
t
#   '123'
u = '.2.3.4.'
u.replace('.', '', 2)
#   '23.4.'
u.replace('.', ' dot ', 5)
#   ' dot 2 dot 3 dot 4 dot '
