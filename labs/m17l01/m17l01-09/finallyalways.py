# Hands-on Python: Complete Video Course & Book — lesson m17l01 — Exceptions: try, except, else, finally
# https://learnsome.tech/courses/python-course/watch?lesson=m17l01
# © LearnSome.tech
def load(text):
    print('opening the file')
    try:
        return int(text)
    finally:
        print('closing the file')

print(load('7'))
print(load('seven'))
