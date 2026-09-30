    numStr2 = form.getfirst("y", "0") # similarly for name 'y'
    contents = processInput(numStr1, numStr2)   # process input into a page
    print(contents)
    
def processInput(numStr1, numStr2):  
    '''Process input parameters and return the final page as a string.'''
    num1 = int(numStr1) # transform input to output data
    num2 = int(numStr2)
    total = num1+num2
    return fileToStr('additionTemplate.html').format(**locals())
