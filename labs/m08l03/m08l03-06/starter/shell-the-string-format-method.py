# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

fmt = 'word: {}, int: {}, formatted float: {:.3f}.'
fmt.format('Joe', 23, 2.1357)
#   'word: Joe, int: 23, formatted float: 2.136.'
defs = {'name':'Joe', 'num':23, 'dec':2.13579}
f2 = 'word: {name}, int: {num}, formatted float: {dec:.3f}.'
f2.format(**defs)
#   'word: Joe, int: 23, formatted float: 2.136.'
