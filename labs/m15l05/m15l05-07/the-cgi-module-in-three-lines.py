# Hands-on Python: Complete Video Course & Book — lesson m15l05 — Chapter Four In One Sitting
# https://learnsome.tech/courses/python-course/watch?lesson=m15l05
# © LearnSome.tech
form = cgi.FieldStorage()
numStr1 = form.getfirst('x', '0')
toppings = form.getlist('topping')
