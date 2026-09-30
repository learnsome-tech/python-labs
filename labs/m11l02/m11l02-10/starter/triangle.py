    # Use Polygon object to draw the triangle
    triangle = Polygon(vertices)
    triangle.setFill('gray')
    triangle.setOutline('cyan')
    triangle.setWidth(4)  # width of boundary line
    triangle.draw(win)

    message.setText('Click anywhere to quit') # change text message
    win.getMouse()
    win.close() 

main()
