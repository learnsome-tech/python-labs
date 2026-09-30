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
