# Hands-on Python: Complete Video Course & Book — lesson m22l01 — Testing With pytest
# https://learnsome.tech/courses/python-course/watch?lesson=m22l01
# © LearnSome.tech
def test_basket_total():
    basket = [2.50, 3.00]      # arrange
    total = sum(basket)        # act
    assert total == 5.50       # assert
