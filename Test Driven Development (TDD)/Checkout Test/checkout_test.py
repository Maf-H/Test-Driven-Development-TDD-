import pytest
from checkout import Checkout
@pytest.fixture()
def checkout():
	checkout = Checkout()
	checkout.add_item_price("a", 1)
	checkout.add_item_price("b", 2)
	return checkout
# def test_can_instantiate_checkout():
# 	checkout = Checkout()
# def test_can_add_item_price(checkout):
# 	checkout.add_item_price("a", 100)
# def test_can_add_an_item(checkout):
# 	checkout.add_an_item("a")
def test_can_calculate_current_total(checkout):
	checkout.add_an_item("a")
	assert checkout.calculate_total() == 1
def test_can_add_multiple_items_and_get_correct_total(checkout):
	checkout.add_an_item("a")
	checkout.add_an_item("b")
	assert checkout.calculate_total() == 3
def test_can_add_discount_rule(checkout):
	checkout.add_discount('a', 3, 2)
# @pytest.mark.skip  # skips this test case until we remove the decorator.
def test_can_apply_discount_rule(checkout):
	checkout.add_discount('a', 3, 2)
	checkout.add_an_item("a")
	checkout.add_an_item("a")
	checkout.add_an_item("a")
	checkout.add_an_item("a")
	checkout.add_an_item("a")
	assert checkout.calculate_total() == 4
def test_can_raise_exceptions_if_item_added_without_price(checkout):
	with pytest.raises(Exception):
		checkout.add_an_item("c")

