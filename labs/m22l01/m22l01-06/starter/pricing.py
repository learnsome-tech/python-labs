def discount(price, percent):
    """Return price with percent taken off, rounded to the penny."""
    if not 0 <= percent <= 100:
        raise ValueError('percent must be between 0 and 100')
    return round(price * percent / 100, 2)
