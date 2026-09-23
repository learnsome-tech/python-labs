# Hands-on Python: Complete Video Course & Book — lesson m18l01 — Modules And The Import System
# https://learnsome.tech/courses/python-course/watch?lesson=m18l01
# © LearnSome.tech
'''Greetings in two languages.'''

def hello(name):
    return 'Hello, ' + name + '!'

def bonjour(name):
    return 'Bonjour, ' + name + '!'

print('loading greetings, name is', __name__)

if __name__ == '__main__':
    print(hello('Ada'))
