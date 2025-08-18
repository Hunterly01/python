import unittest
import get_even_number


class TestForGetEvenNumber(unittest.TestCase):
	def test_for_if_function_exist(self):
		get_even_number.get_even(2)

	def test_function(self):
		number = 2
		result = get_even_number.get_even(number)
		self.assertTrue(result, True)		


class TestForGetsameEvenNumber(unittest.TestCase):
	def test_function_exist(self):
		get_even_number.get_even_number()

	def test_function(self):
		expected_answer = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
		result = get_even_number.get_even_number()
		self.assertEqual(result, expected_answer)