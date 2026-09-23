# Hands-on Python: Complete Video Course & Book — lesson m19l02 — Comprehensions
# https://learnsome.tech/courses/python-course/watch?lesson=m19l02
# © LearnSome.tech
lengths = []
for word in words:
    lengths.append(len(word))

lengths = [len(word) for word in words]
