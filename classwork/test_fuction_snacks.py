import unittest
import function_snacks

class TestCaseDivideOrSquareFunction(unittest.TestCase):
	def test_divide_or_square_exist(self):
		function_snacks.get_divide_or_square(5)
	def test_that_divide_or_square_is_valid_for_negative(self):
		self.assertRaises(ValueError, function_snacks.get_divide_or_square, -1)
	def test_that_divide_or_square_is_valid_for_float(self):
		self.assertRaises(ValueError, function_snacks.get_divide_or_square, 4.8233)
	def test_that_divide_or_square_is_valid_for_string(self):
		self.assertRaises(ValueError, function_snacks.get_divide_or_square, "ola")
	def test_that_divide_or_square_correct_result(self):
		result = function_snacks.get_divide_or_square(25)
		self.assertEqual(result, 5)
	def test_that_divide_or_square_correct_result2(self):
		result = function_snacks.get_divide_or_square(7)
		self.assertNotEqual(result, 1.4)


class TestCaseFutureAmount(unittest.TestCase):
	def test_future_amount_exist(self):
		function_snacks.get_future_amount(100, 10, 2)
	def test_that_future_amount_is_valid1(self):
		self.assertRaises(ValueError, function_snacks.get_future_amount, 9.9877, 0.77, 0.084)
	def test_that_future_amount_is_valid2(self):
		self.assertRaises(ValueError, function_snacks.get_future_amount, "ola", "ola", "ola")
	def test_that_future_amount_is_valid3(self):
		self.assertRaises(ValueError, function_snacks.get_future_amount, -1, -2, -3)
	def test_that_future_amount_is_correct_future_amount(self):
		future_amount = function_snacks.get_future_amount(100, 10, 2)
		self.assertEqual(future_amount,  221)




	