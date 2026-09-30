form = cgi.FieldStorage()
numStr1 = form.getfirst('x', '0')
toppings = form.getlist('topping')
