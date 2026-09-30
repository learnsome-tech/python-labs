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
