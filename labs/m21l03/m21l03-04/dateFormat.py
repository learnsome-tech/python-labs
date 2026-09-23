# Hands-on Python: Complete Video Course & Book — lesson m21l03 — Dates, Times And Random
# https://learnsome.tech/courses/python-course/watch?lesson=m21l03
# © LearnSome.tech
from datetime import date, datetime, timedelta

launch = datetime(2026, 3, 14, 9, 30)
print(launch)
print(launch.strftime('%d %B %Y at %H:%M'))

back = datetime.strptime('2026-12-25 18:00', '%Y-%m-%d %H:%M')
gap = back - launch
print(gap)
print(gap.days, gap.total_seconds())

today = date(2026, 3, 14)
print(today + timedelta(days=30), today.weekday(), today.isoformat())
