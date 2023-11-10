from src.phone import Phone
import pytest


def test_init_phone(phone_test):
    assert phone_test.name == 'iPhone 14'
    assert phone_test.price == 120_000
    assert phone_test.quantity == 5
    assert phone_test.number_of_sim == 2


@pytest.fixture
def phone_test():
    return Phone('iPhone 14', 120_000, 5, 2)


def test_number_of_sim_phone(phone_test):
    phone_test.number_of_sim = 1
    assert phone_test.number_of_sim == 1
    with pytest.raises(ValueError):
        phone_test.number_of_sim = 0