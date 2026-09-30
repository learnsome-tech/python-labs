import math
import statistics

print(math.sqrt(2), math.pi)
print(math.floor(3.7), math.ceil(3.2), math.factorial(5))
print(math.isclose(0.1 + 0.2, 0.3))

marks = [58, 72, 72, 91, 64]
print(statistics.mean(marks))
print(statistics.median(marks), statistics.mode(marks))
print(round(statistics.stdev(marks), 3))
