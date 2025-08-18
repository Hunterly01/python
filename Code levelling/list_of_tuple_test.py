import unittest
import list_of_tuple


class TestForListOfTuple(unittest.TestCase):
	def test_if_function_exist(self):
		list_of_tuple.get_first_tuple_greater_than_two((1, 'A'),)


	def test_function(self):
		lst = (4, 'B')
		result = list_of_tuple.get_first_tuple_greater_than_two((4, 'B'),)
		self.assertTrue(result, True)



class TestForFilterTuple(unittest.TestCase):
	def test_if_function_exist(self):
		list_of_tuple.fiter_tuple([(1, 'A'), (4, 'B'), (2, 'C')])

	def test_function(self):
		information = [(1, 'A'), (4, 'B'), (2, 'C')]
		expected = (4, 'B')
		result = list_of_tuple.get_first_tuple_greater_than_two( [(1, 'A'), (4, 'B'), (2, 'C')])
		self.assertEqual(result, expected)