import unittest
import append_tuple



class TestForAppendTuple(unittest.TestCase):
	def test_for_if_function_exist(self):
		append_tuple.append_number_in_tuple((1,3), 2)

	def test_for_empty_tuple(self):
		self.assertRaises(ValueError,append_tuple.append_number_in_tuple,(), 1)

	def test_for_positive_number(self):
		result = append_tuple.append_number_in_tuple((1, 2, 3, 4, 5), 6)
		self.assertEqual(result, (1, 2, 3, 4, 5, 6))

	def test_for_single_number_in_tuple(self):
		result = append_tuple.append_number_in_tuple((1,), 6)
		self.assertEqual(result, (1, 6))

	def test_for_negative_number_in_tuple(self):
		result = append_tuple.append_number_in_tuple((-1, -3, -4, -5), 6)
		self.assertEqual(result, (-1, -3, -4, -5, 6))