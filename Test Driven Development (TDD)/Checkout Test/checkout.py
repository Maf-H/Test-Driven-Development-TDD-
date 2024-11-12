class Checkout:
	class Discount:
		def __init__(self, number_of_items, price):
			self.number_of_items = number_of_items
			self.price = price

	def __init__(self):
		self.prices = {}
		self.discounts = {}
		self.items = {}

	def add_item_price(self, item_name,  item_price):
		self.prices[item_name] = item_price

	def add_an_item(self, item):
		if item not in self.prices:
			raise Exception(f"'{item}' Unknown Item!")
		if item in self.items:
			self.items[item] += 1
		else:
			self.items[item] = 1

	def add_discount(self, item, number_of_items, discount_price):
		discount = self.Discount(number_of_items, discount_price)
		self.discounts[item] = discount

	def calculate_total(self):
		total = 0
		for item, number_of_items in self.items.items():
			total = self.check_and_apply_discount(item, number_of_items, total)
		return total

	def check_and_apply_discount(self, item, number_of_items, total):
		if item in self.discounts:
			discount = self.discounts[item]
			discounted_items = discount.number_of_items
			if number_of_items >= discounted_items:
				total += self.apply_discounted_total(discount, item, number_of_items)
			else:
				total += self.prices[item] * number_of_items
		else:
			total += self.prices[item] * number_of_items
		return total

	def apply_discounted_total(self, discount, item, number_of_items):
		total = 0
		discounted_items = discount.number_of_items
		non_discounted_items = number_of_items % discount.number_of_items
		non_discounted_total_price = self.prices[item] * non_discounted_items
		total += ((number_of_items // discounted_items) * discount.price + non_discounted_total_price)
		return total
