import unittest;
import map_square;

class TestforMapSquare(unittest.TestCase):
	def test_that_the_fuction_exist(self):
		map_square.squaresNumber(1)
	
	def test_for_zeros(self):
		self.assertRaises(ValueError,map_square.squaresNumber, 0)
	def test_for_string(self):
		self.assertRaises(ValueError,map_square.squaresNumber, "Tayo")