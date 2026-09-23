# Hands-on Python: Complete Video Course & Book — lesson m13l07 — Loops And Tuples
# https://learnsome.tech/courses/python-course/watch?lesson=m13l07
# © LearnSome.tech
msg = Text(Point(win.getWidth()/2, 375),'')
msg.draw(win)

msg.setText('Click to choose a house color.')

shapePairs = [(house, 'house'), (door, 'door'), (roof, 'roof')]
for (shape, description) in shapePairs:
    prompt = 'Click to choose a ' + description + ' color.'
    # ....
