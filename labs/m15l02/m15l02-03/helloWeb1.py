# Hands-on Python: Complete Video Course & Book — lesson m15l02 — Composing Web Pages In Python
# https://learnsome.tech/courses/python-course/watch?lesson=m15l02
# © LearnSome.tech
def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
