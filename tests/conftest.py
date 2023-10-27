import pytest
from src.item import Item


@pytest.fixture
def item_test():
    return Item("test", 10_000, 10)


@pytest.fixture
def instantiate_from_csv():
    Item.all.clear()
    Item.instantiate_from_csv('d:\\tuting\\el_shop_yuriy\\src\\items.csv')
    return Item.all
