# Hands-on Python: Complete Video Course & Book — lesson m17l01 — Exceptions: try, except, else, finally
# https://learnsome.tech/courses/python-course/watch?lesson=m17l01
# © LearnSome.tech
def read(text):
    print('trying', text)
    try:
        value = int(text)
    except ValueError:
        print('- except ran')
    else:
        print('- else ran, value is', value)
    finally:
        print('- finally ran')

read('7')
read('seven')
