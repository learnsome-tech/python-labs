def load(text):
    print('opening the file')
    try:
        return int(text)
    finally:
        print('closing the file')

print(load('7'))
print(load('seven'))
