# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

words = ['pear', 'fig', 'banana', 'kiwi']
[w.upper() for w in words if len(w) > 3]
#   ['PEAR', 'BANANA', 'KIWI']
[w for w in words if 'a' in w]
#   ['pear', 'banana']
[x for x in range(20) if x % 3 == 0]
#   [0, 3, 6, 9, 12, 15, 18]
['long' if len(w) > 3 else 'short' for w in words]
#   ['long', 'short', 'long', 'long']
