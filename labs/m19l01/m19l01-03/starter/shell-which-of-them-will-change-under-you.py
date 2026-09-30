# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

nums = [3, 1, 4]
nums.append(9)
nums
#   [3, 1, 4, 9]
point = (2, 5)
point[0] = 7
#   Traceback (most recent call last):
#   TypeError: 'tuple' object does not support item assignment
point + (9,)
#   (2, 5, 9)
seen = {1, 3, 4}
seen.add(4)
seen
#   {1, 3, 4}
