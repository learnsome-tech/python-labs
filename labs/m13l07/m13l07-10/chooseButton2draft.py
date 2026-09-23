# Hands-on Python: Complete Video Course & Book — lesson m13l07 — Loops And Tuples
# https://learnsome.tech/courses/python-course/watch?lesson=m13l07
# © LearnSome.tech
msg = Text(Point(win.getWidth()/2, 375),'Click to choose a house color.')
msg.draw(win)
color = getChoice(choicePairs, 'white', win)
house.setFill(color)

msg.setText('Click to choose a door color.')
color = getChoice(choicePairs, 'white', win)
door.setFill(color)
