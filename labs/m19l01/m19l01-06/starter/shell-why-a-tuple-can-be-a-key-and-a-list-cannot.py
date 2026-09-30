# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

grid = {}
grid[(0, 0)] = 'start'
grid[(2, 3)] = 'treasure'
grid[(0, 0)]
#   'start'
grid[[0, 0]] = 'oops'
#   Traceback (most recent call last):
#   TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
hash((0, 0)) == hash((0, 0))
#   True
sorted(grid)
#   [(0, 0), (2, 3)]
