"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
def test_init(item_test):
    assert item_test.name == "test"
    assert item_test.price == 10_000
    assert item_test.quantity == 10

def test_calculate_total_price(item_test):
    assert item_test.calculate_total_price

def test_apply_discount(item_test):
    assert item_test.quantity







