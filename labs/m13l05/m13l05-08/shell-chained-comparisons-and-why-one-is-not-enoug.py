# Hands-on Python: Complete Video Course & Book — lesson m13l05 — Compound Boolean Expressions
# https://learnsome.tech/courses/python-course/watch?lesson=m13l05
# © LearnSome.tech
# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

end1 = 200
end2 = 100
val = 120
end1 <= val <= end2
#   False
200 <= 120 <= 100
#   False
end2 <= val <= end1
#   True
end1 <= val <= end2 or end2 <= val <= end1
#   True
end1 <= val and val <= end2
#   False
