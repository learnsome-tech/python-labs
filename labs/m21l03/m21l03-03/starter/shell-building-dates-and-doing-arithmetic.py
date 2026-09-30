# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

from datetime import date, timedelta
payday = date(2026, 1, 30)
payday
#   datetime.date(2026, 1, 30)
print(payday)
#   2026-01-30
payday + timedelta(days=45)
#   datetime.date(2026, 3, 16)
date(2026, 3, 16) - payday
#   datetime.timedelta(days=45)
(date(2026, 3, 16) - payday).days
#   45
