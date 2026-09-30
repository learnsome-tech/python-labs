win.promptClose(win.getWidth()/2, 30) # specify x, y of prompt

msg = Text(Point(100, 50), 'Original message...')
msg.draw(win)
# ...
# ... just important that there is a drawn Text object
win.promptClose(msg)  # use existing Text object
