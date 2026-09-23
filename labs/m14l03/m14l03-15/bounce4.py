# Hands-on Python: Complete Video Course & Book — lesson m14l03 — Graphical Applications With While
# https://learnsome.tech/courses/python-course/watch?lesson=m14l03
# © LearnSome.tech
                if pt.getY() < stopHeight: # switch direction
                    (dx, dy) = getShift(center, pt)
                    (dx, dy) = (dx*scale, dy*scale)
                else:                  #NEW exit from depths of the loop
                    return             #NEW
        shape.move(dx, dy)                
        time.sleep(delay)
