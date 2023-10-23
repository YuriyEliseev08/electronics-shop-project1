import pytest
from src.item import Item

@pytest.fixture
def item_test():
    return Item("test",10_000, 10)
