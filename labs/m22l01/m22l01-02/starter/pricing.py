def discount(price, percent):
    """Return price with percent taken off, rounded to the penny."""
    if not 0 <= percent <= 100:
        raise ValueError('percent must be between 0 and 100')
    return round(price * (1 - percent / 100), 2)


print(discount(20.0, 10))
print(discount(19.99, 0))
