# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

range(1000000)
#   range(0, 1000000)
type(range(5)).__name__
#   'range'
list(range(3))
#   [0, 1, 2]
z = zip([1, 2, 3], 'abc')
type(z).__name__
#   'zip'
list(z)
#   [(1, 'a'), (2, 'b'), (3, 'c')]
list(enumerate(['a', 'b']))
#   [(0, 'a'), (1, 'b')]
list(enumerate(['a', 'b'], start=1))
#   [(1, 'a'), (2, 'b')]
