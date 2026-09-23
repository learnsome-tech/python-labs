# Hands-on Python: Complete Video Course & Book — lesson m07l01 — Dictionaries
# https://learnsome.tech/courses/python-course/watch?lesson=m07l01
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

spanish = dict()
spanish['hello'] = 'hola'
spanish['red'] = 'rojo'
spanish
#   {'hello': 'hola', 'red': 'rojo'}
spanish['red']
#   'rojo'
spanish['purple']
#   Traceback (most recent call last):
#   KeyError: 'purple'
'purple' in spanish
#   False
'red' in spanish
#   True
