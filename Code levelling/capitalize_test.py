import unittest
import capitalize



class TestForCapitalizeFirst(unittest.TestCase):
	def test_if_function_exist(self):
		capitalize.capitalize_first_letter( ['john', 'mary', 'steve'])


	def test_function(self):
		lst = ['john', 'mary', 'steve']
		expected = ['John', 'Mary', 'Steve']
		result = capitalize.capitalize_first_letter(lst)
		self.assertEqual(result, expected)