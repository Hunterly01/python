import unittest
import square_number



class TestForSquareNumber(unittest.TestCase):
	def test_if_function_exist(self):
		square_number.isSquare(2)

	def test_function(self):
		number = 2
		result = square_number.isSquare(number)
		self.assertEqual(result, 4)

		
class TestForCheckSquareNumber(unittest.TestCase):
	def test_if_function_exist(self):
		square_number.check_square()

	def test_function(self):
		expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
		result = square_number.check_square()
		self.assertEqual(result, expected)

		