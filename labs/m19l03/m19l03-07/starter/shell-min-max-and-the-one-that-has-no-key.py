# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

words = ['pear', 'fig', 'banana']
min(words, key=len)
#   'fig'
max(words, key=len)
#   'banana'
sum(words, key=len)
#   Traceback (most recent call last):
#   TypeError: sum() got an unexpected keyword argument 'key'
sum(len(w) for w in words)
#   13
min([], default='nothing')
#   'nothing'
