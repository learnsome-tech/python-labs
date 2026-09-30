                if pt.getY() < stopHeight: # switch direction
                    (dx, dy) = getShift(center, pt)
                    (dx, dy) = (dx*scale, dy*scale)
                else:                  #NEW exit from depths of the loop
                    return             #NEW
        shape.move(dx, dy)                
        time.sleep(delay)
