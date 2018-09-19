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
