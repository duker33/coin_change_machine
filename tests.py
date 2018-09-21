import pytest

from machine import get_coins_to_give


def test_main_case():
    result = get_coins_to_give({5: 10, 3: 2, 2: 12, 1: 3}, 16)
    assert result == {5: 3, 1: 1}


def test_no_coins_to_give():
    result = get_coins_to_give({5: 1000}, 1)
    assert result == 0


def test_no_coins_in_machine():
    result = get_coins_to_give({1: 0}, 1)
    assert result == 0

	
# test from repo https://github.com/markshevchenko/coin-change-machine-csharp
	
@pytest.mark.xfail
def test_no_coins_to_give_special_case():
    result = get_coins_to_give({5: 3, 3: 1, 2: 4, }, 11)
    assert result == {5: 1, 2: 3}

	
def test_no_coins_to_give_mark():
    result = get_coins_to_give({5: 2, 3: 2}, 4)
    assert result == 0

	
def test_no_coins_to_give_has_to_give_mark():
    result = get_coins_to_give({5: 4, 2: 6}, 10)
    assert result == {5: 2}
