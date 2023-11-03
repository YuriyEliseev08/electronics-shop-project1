import pytest
from src.item import Item


@pytest.fixture
def item_test():
    return Item("test", 10_000, 10)


@pytest.fixture
def instantiate_from_csv():
    Item.all.clear()
    Item.instantiate_from_csv('C:/Users/Юрий/PycharmProjects/electronics-shop-project1/src/items.csv')
    return Item.all
