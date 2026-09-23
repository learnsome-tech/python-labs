# Hands-on Python: Complete Video Course & Book — lesson m21l03 — Dates, Times And Random
# https://learnsome.tech/courses/python-course/watch?lesson=m21l03
# © LearnSome.tech
from datetime import datetime

now = datetime.now()
print(type(now))
print(now.year >= 2026)
print(0 <= now.hour <= 23, 1 <= now.month <= 12)

stamp = now.strftime('%Y-%m-%d')
print(len(stamp), stamp == str(now.date()))
