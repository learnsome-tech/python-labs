# Hands-on Python: Complete Video Course & Book — lesson m19l03 — Sorting, Keys And Lambdas
# https://learnsome.tech/courses/python-course/watch?lesson=m19l03
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

people = [('Ada', 36), ('Alan', 41), ('Grace', 36)]
sorted(people)
#   [('Ada', 36), ('Alan', 41), ('Grace', 36)]
sorted(people, key=lambda p: p[1])
#   [('Ada', 36), ('Grace', 36), ('Alan', 41)]
ages = {'ada': 36, 'alan': 41, 'grace': 36}
sorted(ages)
#   ['ada', 'alan', 'grace']
sorted(ages.items(), key=lambda pair: pair[1])
#   [('ada', 36), ('grace', 36), ('alan', 41)]
