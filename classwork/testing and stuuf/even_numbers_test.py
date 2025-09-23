import unittest;
import even_numbers;

class TestforEvenNumbersFunction(unittest.TestCase):
	def test_that_the_fuction_exist(self):
		even_numbers.check_even_number(1)


	def test_for_number(self):
		self.assertRaises(ValueError,even_numbers.check_even_number, 0)

	def test_for_string_(self):
		self.assertRaises(ValueError,even_numbers.check_even_number, "ola")
