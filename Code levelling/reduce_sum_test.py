import unittest
import reduce_sum


class TestReduceSum(unittest.TestCase):
	def test_if_function_exist(self):
		reduce_sum.add(2, 3)

	def test_function(self):
		number = 2
		value = 3
		result = reduce_sum.add(number, value)
		self.assertEqual(result, 5)


class TestReduceSumq(unittest.TestCase):
	def test_if_function_exist(self):
		reduce_sum.reduce_sum()

	def test_function(self):
		expected = 1275
		result = reduce_sum.reduce_sum()
		self.assertEqual(result, expected)


