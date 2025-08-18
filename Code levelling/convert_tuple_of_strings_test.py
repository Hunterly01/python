import unittest
import convert_tuple_of_strings




class TestForConvertTupleOfStrings(unittest.TestCase):
	def test_if_function_exist(self):
		convert_tuple_of_strings.convert_tuple_to_list(("apple", "banana", "cherry"),"mango")

	def test_empty_tuple(self):
		self.assertRaises(ValueError,convert_tuple_of_strings.convert_tuple_to_list,(), "mango")

	def test_for_equal_string(self):
		fruits = ("apple", "banana", "cherry")
		expected = (("apple", "banana", "cherry"), "mango")
		self.assertNotEqual(convert_tuple_of_strings.convert_tuple_to_list,(fruits), expected)