"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_init(item_test):
    assert item_test.name == "test"
    assert item_test.price == 10_000
    assert item_test.quantity == 10


def test_calculate_total_price(item_test):
    assert item_test.calculate_total_price() == 100_000


def test_apply_discount(item_test):
    item_test.pay_rate = 0.8
    item_test.apply_discount()
    assert item_test.price == 8_000


def test_string_to_number(item_test):
    assert item_test.string_to_number("5") == 5
    assert item_test.string_to_number("5.0") == 5
    assert item_test.string_to_number("5.5") == 5


def test_repr(item_test):
    assert item_test.__repr__() == "Item('test', 10000, 10)"

def test_str(item_test):
    assert item_test.__str__() == "test"
