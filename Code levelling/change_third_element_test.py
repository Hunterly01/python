import unittest
import change_third_element


class TestToChangeThirdNumberInIndexOne(unittest.TestCase):
	def test_if_function_exist(self):
		change_third_element.change_third_element_element_second_value( (1, 2, [3, 4], 5), 99)
	def test_for_positive_tuple(self):
		original = (1, 2, [3, 4], 5)
		expected = (1, 2, [3, 99], 5)
		result = change_third_element.change_third_element_element_second_value(original, 99)
		self.assertEqual(result, expected)

	def test_for_negative_tuple(self):
		original = (-1, -2, [-3, -4], -5)
		expected = (-1, -2, [-3, -99], -5)
		result = change_third_element.change_third_element_element_second_value(original, -99)
		self.assertEqual(result, expected)

	
