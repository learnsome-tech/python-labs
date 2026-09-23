# Hands-on Python: Complete Video Course & Book — lesson m10l01 — Mad Libs Revisited: Finding The Cues
# https://learnsome.tech/courses/python-course/watch?lesson=m10l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

story = 'blah {animal} blah blah {food} ...'
story.count('{')
#   2
story.find('{')
#   5
story.find('{') + 1
#   6
story.find('}')
#   12
story[6 : 12]
#   'animal'
story.find('{', 12) + 1
#   25
story.find('}', 25)
#   29
story[25 : 29]
#   'food'
