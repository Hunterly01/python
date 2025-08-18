import unittest
import convert_to_upper



class TestForConvertToUpper(unittest.TestCase):
	def test_if_function_exist(self):
		convert_to_upper.convert_string_to_upper(['python', 'java', 'c++'])


	def test_function(self):
		lst = ['python', 'java', 'c++']
		expected = ['PYTHON', 'JAVA', 'C++']
		result = convert_to_upper.convert_string_to_upper(lst)
		self.assertEqual(result, expected)