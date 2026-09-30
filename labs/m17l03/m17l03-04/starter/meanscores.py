import statistics

def average(scores):
    return statistics.mean(scores)

def report(scores):
    print('average is', average(scores))

report([7, 11, 3])
report([])
