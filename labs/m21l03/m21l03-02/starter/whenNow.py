from datetime import datetime

now = datetime.now()
print(type(now))
print(now.year >= 2026)
print(0 <= now.hour <= 23, 1 <= now.month <= 12)

stamp = now.strftime('%Y-%m-%d')
print(len(stamp), stamp == str(now.date()))
