import unittest
import unpack_tuple



class TestUnpackTuple(unittest.TestCase):
	def test_if_fuction_exist(self):
		unpack_tuple.unpack_tuple_into_variables((10, 20, 30, 40))

	def test_for_empty_tuple(self):
		self.assertRaises(ValueError, unpack_tuple.unpack_tuple_into_variables,())

	def test_for_unpack_tuple(self):
		numbers = (10, 20, 30, 40)
		a, b, last = unpack_tuple.unpack_tuple_into_variables(numbers)
		self.assertEqual(a, 10)
		self.assertEqual(b, 20)
		self.assertEqual(last,[30, 40])		