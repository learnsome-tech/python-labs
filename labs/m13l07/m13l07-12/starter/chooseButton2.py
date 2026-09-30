    house = makeColoredRect(Point(60, 200), 180, 150, 'gray', win)
    door = makeColoredRect(Point(90, 150), 40, 100, 'white', win)
    roof = Polygon(Point(50, 200), Point(250, 200), Point(150, 300))
    roof.setFill('black')
    roof.draw(win)
    
    #NEW
    shapePairs = [(house, 'house'), (door, 'door'), (roof, 'roof')] 
    msg = Text(Point(win.getWidth()/2, 375),'')
    msg.draw(win)
    for (shape, description) in shapePairs:
        prompt = 'Click to choose a ' + description + ' color.'
        msg.setText(prompt)
        color = getChoice(choicePairs, 'white', win)
        shape.setFill(color)

    win.promptClose(msg)

main()
