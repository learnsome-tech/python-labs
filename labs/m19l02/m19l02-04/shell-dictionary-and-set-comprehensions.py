# Hands-on Python: Complete Video Course & Book — lesson m19l02 — Comprehensions
# https://learnsome.tech/courses/python-course/watch?lesson=m19l02
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

words = ['pear', 'fig', 'banana', 'kiwi']
{w: len(w) for w in words}
#   {'pear': 4, 'fig': 3, 'banana': 6, 'kiwi': 4}
{len(w) for w in words}
#   {3, 4, 6}
ages = {'ada': 36, 'alan': 41}
{value: key for key, value in ages.items()}
#   {36: 'ada', 41: 'alan'}
sorted({w[0] for w in words})
#   ['b', 'f', 'k', 'p']
