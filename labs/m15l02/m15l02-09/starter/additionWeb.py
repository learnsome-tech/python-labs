def processInput(numStr1, numStr2):  # NEW
    '''Process input parameters and return the final page as a string.'''
    num1 = int(numStr1) # transform input to output data
    num2 = int(numStr2)
    total = num1+num2
    return fileToStr('additionTemplate.html').format(**locals())

def main(): # NEW
    numStr1 = input('Enter an integer: ')  # obtain input
    numStr2 = input('Enter another integer: ')  
    contents = processInput(numStr1, numStr2)   # process input into a page
    browseLocal(contents) # display page
