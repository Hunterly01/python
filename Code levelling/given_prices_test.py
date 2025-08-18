import unittest
import given_prices



class TestGivenPrices(unittest.TestCase):
	def test_if_function_exist(self):
		given_prices.check_given_prices(100)


	def test_function(self):
		number = 100
		expected = 110
		result = given_prices.check_given_prices(number)
		self.assertEqual(result, expected)


class TestGivenPricesa(unittest.TestCase):
	def test_if_function_exist(self):
		given_prices.add_percentage_to_price([100, 200, 300])

	def test_function(self):
		lst = [100, 200, 300]
		expected = [110.0, 220.0, 330.0]
		result = given_prices.add_percentage_to_price(lst)
		self.assertEqual(result, expected)