# Hands-on Python: Complete Video Course & Book — lesson m17l03 — Reading A Traceback Like A Professional
# https://learnsome.tech/courses/python-course/watch?lesson=m17l03
# © LearnSome.tech
def parse_row(row):
    name, score = row.split(',')
    return (name, int(score))

def total_score(text):
    rows = [parse_row(row) for row in text.split(';')]
    return sum(score for name, score in rows)

def report(text):
    print('total is', total_score(text))

report('ana,7;bo,11')
report('ana,7;bo,eleven')
