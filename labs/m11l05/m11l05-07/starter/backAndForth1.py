def moveOnLine(shape, dx, dy, repetitions, delay):
    for i in range(repetitions):
        shape.move(dx, dy)
        time.sleep(delay)
