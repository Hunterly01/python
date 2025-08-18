import unittest
import get_all_number



class TestForGetAllNumber(unittest.TestCase):
	def test_if_function_exist(self):
		get_all_number.get_number(15)

	def test_function(self):
		number = 15
		result = get_all_number.get_number(number)
		self.assertTrue(result, True)


class TestForGetAllNumberh(unittest.TestCase):
	def test_if_function_exist(self):
		get_all_number.filter_to_get_all_number()

	def test_function(self):
		expected = [15, 30, 45]
		result = get_all_number.filter_to_get_all_number()
		self.assertEqual(result, expected)

