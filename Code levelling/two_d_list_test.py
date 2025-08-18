import unittest
import two_d_list


class TestForTwoDList(unittest.TestCase):
	def test_if_function_exist(self):
		two_d_list.sum_inner_two_d_list_index([[2, 3, 4],  [1, 5, 7],  [4, 6, 8] ])
	
	def test_for_empty_list(self):
		self.assertRaises(ValueError,two_d_list.sum_inner_two_d_list_index,[])

	def test_for_positive(self):
		lst =  [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
		expected = [7, 14, 19]
		result = two_d_list.sum_inner_two_d_list_index(lst)
		self.assertEqual(result,expected)