def shipping_cost(weight_kg, express=False):
    """Return the postage in pounds for a parcel.

    weight_kg: the mass of the parcel, a float
    express: True for next day delivery, which doubles the price
    """
    price = 2.5 + 0.75 * weight_kg
    return price * 2 if express else price


print(shipping_cost(4))
print(shipping_cost(4, express=True))
print(shipping_cost.__doc__.splitlines()[0])
