choicePairs = list()
buttonSetup = [(310, 350, 'red'), (310, 310, 'yellow'),
               (310, 270, 'blue')]
for (x, y, color) in buttonSetup:
   button = makeColoredRect(Point(x, y), 80, 30, color, win)
   choicePairs.append((button, color))
