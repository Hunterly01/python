import unittest
import exchange_rate

class TestExchangeRateFunction(unittest.TestCase):
	def test_exchange_rate_exist(self):
		exchange_rate.get_exchange_rate(1550)
	def test_exchange_rate_function_equivalent_correct_equivalent(self):
		equivalent = exchange_rate.get_exchange_rate(2)
		self.assertEqual(equivalent, 3100)

		
	
		