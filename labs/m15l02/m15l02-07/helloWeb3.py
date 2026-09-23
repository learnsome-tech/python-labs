# Hands-on Python: Complete Video Course & Book — lesson m15l02 — Composing Web Pages In Python
# https://learnsome.tech/courses/python-course/watch?lesson=m15l02
# © LearnSome.tech
def fileToStr(fileName): # NEW
    """Return a string containing the contents of the named file."""
    fin = open(fileName); 
    contents = fin.read();  
    fin.close() 
    return contents

def main():
    person = input('Enter a name: ')  
    contents = fileToStr('helloTemplate.html').format(**locals())   # NEW
    browseLocal(contents)
