# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

nums = [1, 2, 3]
numsAlias = nums
nums.append(4)
numsAlias
#   [1, 2, 3, 4]
numsAlias.append(5)
nums
#   [1, 2, 3, 4, 5]
