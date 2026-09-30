# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

strList = ['z', 'zz', 'c', 'z', 'bb', 'z', 'a', 'c']
aSet = set(strList)
len(aSet)
#   5
sorted(aSet)
#   ['a', 'bb', 'c', 'z', 'zz']
dupes = ['animal', 'food', 'animal', 'food', 'food', 'city']
len(set(dupes))
#   3
sorted(set(dupes))
#   ['animal', 'city', 'food']
