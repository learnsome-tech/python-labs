import pytest

from pricing import discount


def test_ten_percent_off():
    assert discount(20.0, 10) == 18.0


def test_nothing_off_leaves_the_price():
    assert discount(19.99, 0) == 19.99


def test_a_silly_percent_is_refused():
    with pytest.raises(ValueError):
        discount(10.0, 150)
