# Hands-on Python: Complete Video Course & Book — lesson m19l03 — Sorting, Keys And Lambdas
# https://learnsome.tech/courses/python-course/watch?lesson=m19l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

words = ['pear', 'Fig', 'banana', 'kiwi']
sorted(words, key=len)
#   ['Fig', 'pear', 'kiwi', 'banana']
sorted(words, key=str.lower)
#   ['banana', 'Fig', 'kiwi', 'pear']
sorted(words, key=len, reverse=True)
#   ['banana', 'pear', 'kiwi', 'Fig']
sorted(words, key=lambda w: w[-1])
#   ['banana', 'Fig', 'kiwi', 'pear']
