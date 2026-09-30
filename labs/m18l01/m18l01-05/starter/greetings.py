'''Greetings in two languages.'''

def hello(name):
    return 'Hello, ' + name + '!'

def bonjour(name):
    return 'Bonjour, ' + name + '!'

print('loading greetings, name is', __name__)

if __name__ == '__main__':
    print(hello('Ada'))
