import unittest
import palindrome


class TestForParlindrome(unittest.TestCase):
	def test_if_function_exist(self):
		palindrome.isPalindrome('level')

	def test_function(self):
		word = 'level'
		result = palindrome.isPalindrome(word)
		self.assertTrue(result, True)


class TestCheckParlindrome(unittest.TestCase):
	def test_if_function_exist(self):
		palindrome.check_for_palindrome(['level', 'world', 'madam', 'python'])

	def test_function(self):
		lst = ['level', 'world', 'madam', 'python']
		expected = ['level', 'madam']
		result = palindrome.check_for_palindrome(lst)
		self.assertEqual(result, expected)
