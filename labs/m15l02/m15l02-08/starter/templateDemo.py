def fileToStr(fileName):
    """Return a string containing the contents of the named file."""
    fin = open(fileName)
    contents = fin.read()
    fin.close()
    return contents

person = 'Alice'
print(fileToStr('www/helloTemplate.html').format(**locals()))
