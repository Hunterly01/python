import unittest;
import words_len;

class TestforWord(unittest.TestCase):
	def test_that_the_fuction_exist(self):
		words_len.get_length(1)

	def test_for_number(self):
		self.assertRaises(ValueError,words_len.get_length, 0)

	def test_for_number_less_zero(self):
		self.assertRaises(ValueError,words_len.get_length, -1)
