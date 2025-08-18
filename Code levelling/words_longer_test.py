import unittest
import words_longer


class TestWordsLonger(unittest.TestCase):
	def test_if_function_exist(self):
		words_longer.long_word('lion')
	
	def test_function_is_true(self):
		word = 'lion'
		result = words_longer.long_word(word)
		self.assertFalse(result, word)




class TestWordsLongerww(unittest.TestCase):
	def test_if_function_exist(self):
		words_longer.extract_words_thats_longer(['cat', 'elephant', 'tiger', 'lion'])

	def test_function(self):
		words =  ['cat', 'elephant', 'tiger', 'lion']
		expected = ['elephant']
		result = words_longer.extract_words_thats_longer(words)
		self.assertEqual(result, expected)
