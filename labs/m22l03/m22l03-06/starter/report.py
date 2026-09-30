import json
import statistics


def average_age(people):
    ages = [p['age'] for p in people]
    count = len(ages)
    return statistics.mean(ags)
