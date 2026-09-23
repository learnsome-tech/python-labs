# Hands-on Python: Complete Video Course & Book — lesson m11l03 — Reading The graphics.py Documentation
# https://learnsome.tech/courses/python-course/watch?lesson=m11l03
# © LearnSome.tech
win.promptClose(win.getWidth()/2, 30) # specify x, y of prompt

msg = Text(Point(100, 50), 'Original message...')
msg.draw(win)
# ...
# ... just important that there is a drawn Text object
win.promptClose(msg)  # use existing Text object
