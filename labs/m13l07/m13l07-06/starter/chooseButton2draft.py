def getChoice(choicePairs, default, win):
    '''Given a list choicePairs of tuples, with each tuple in the form
    (rectangle, choice), return the choice that goes with the rectangle
    in win where the mouse gets clicked, or return default if the click
    is in none of the rectangles.'''

    point = win.getMouse()
    for (rectangle, choice) in choicePairs:
        #....
