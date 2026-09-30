msg = Text(Point(win.getWidth()/2, 375),'Click to choose a house color.')
msg.draw(win)
color = getChoice(choicePairs, 'white', win)
house.setFill(color)

msg.setText('Click to choose a door color.')
color = getChoice(choicePairs, 'white', win)
door.setFill(color)
