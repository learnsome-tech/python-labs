# Hands-on Python: Complete Video Course & Book — lesson m22l02 — Type Hints
# https://learnsome.tech/courses/python-course/watch?lesson=m22l02
# © LearnSome.tech
def total(prices: list[float], discount: float = 0.0) -> float:
    return sum(prices) * (1 - discount)


def find_user(name: str) -> str | None:
    users = {'ada': 'ada@example.com'}
    return users.get(name)


print(total([2.50, 3.00]))
print(total([2.50, 3.00], 0.5))
print(find_user('ada'), find_user('bob'))
