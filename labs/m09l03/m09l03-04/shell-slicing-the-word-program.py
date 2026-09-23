# Hands-on Python: Complete Video Course & Book — lesson m09l03 — String Slices
# https://learnsome.tech/courses/python-course/watch?lesson=m09l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

word = 'program'
word[2:4]
#   'og'
word[1:-3]
#   'rog'
word[3:]
#   'gram'
word[3:3]
#   ''
word[:1] + word[4:]
#   'pram'
