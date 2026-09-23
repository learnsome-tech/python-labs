# Hands-on Python: Complete Video Course & Book — lesson m14l04 — Any Type As A Condition
# https://learnsome.tech/courses/python-course/watch?lesson=m14l04
# © LearnSome.tech
'''Display use of the OR operator with nonboolean operands.'''

defaultColor = 'red'
userColor = input('Enter a color, or just press Enter for the default: ')
color = userColor or defaultColor
print('The color is', color)
