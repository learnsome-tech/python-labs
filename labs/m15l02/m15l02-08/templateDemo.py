# Hands-on Python: Complete Video Course & Book — lesson m15l02 — Composing Web Pages In Python
# https://learnsome.tech/courses/python-course/watch?lesson=m15l02
# © LearnSome.tech
def fileToStr(fileName):
    """Return a string containing the contents of the named file."""
    fin = open(fileName)
    contents = fin.read()
    fin.close()
    return contents

person = 'Alice'
print(fileToStr('www/helloTemplate.html').format(**locals()))
