def makeLabeledEntry(entryCenterPt, entryWidth, initialStr, labelText, win):
    '''Return an Entry object with specifed center, width in characters, and
    initial string value.  Also create a static label over it with
    specified text.  Draw everything in the GraphWin win.
    '''

    entry = Entry(entryCenterPt, entryWidth)
    entry.setText(initialStr)
    entry.draw(win)

    labelCenter = entryCenterPt.clone()
    labelCenter.move(0, 30)
    Text(labelCenter,labelText).draw(win)
    return entry
