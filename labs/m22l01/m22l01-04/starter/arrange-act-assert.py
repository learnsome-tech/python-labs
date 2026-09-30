def test_basket_total():
    basket = [2.50, 3.00]      # arrange
    total = sum(basket)        # act
    assert total == 5.50       # assert
