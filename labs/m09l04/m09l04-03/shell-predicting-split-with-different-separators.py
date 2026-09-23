# Hands-on Python: Complete Video Course & Book — lesson m09l04 — Split And Join
# https://learnsome.tech/courses/python-course/watch?lesson=m09l04
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

line = 'Go:  Tear some strings apart!'
seq = line.split()
seq
#   ['Go:', 'Tear', 'some', 'strings', 'apart!']
line.split(':')
#   ['Go', '  Tear some strings apart!']
line.split('ar')
#   ['Go:  Te', ' some strings ap', 't!']
lines = 'This includes\nsome new\nlines.'
print(lines)
#   This includes
#   some new
#   lines.
lines.split()
#   ['This', 'includes', 'some', 'new', 'lines.']
