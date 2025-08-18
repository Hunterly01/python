import unittest
import d_list_


class TestFor2DList(unittest.TestCase):
	def test_if_function_exist(self):
		d_list_.sum_dlist([[2, 3, 4], [1, 5, 7], [4, 6, 8]])

	def test_for_empty_list(self):
		self.assertRaises(ValueError, d_list_.sum_dlist, ([]))

	def test_sum_inner_lst(self):
		lst = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
		expected = [9, 13, 18]
		result = d_list_.sum_dlist(lst)
		self.assertEqual(result , expected)