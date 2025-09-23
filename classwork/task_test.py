import unittest
import task

class TestForAppendTuple(unittest.TestCase):
	def test_for_empty_list(self):
		self.assertRaises(ValueError,task.get_student_square,[])

	def test_if_fuction_return_list(self):
		lst = [2,3,4,5,6,7,16];
		result = task.get_student_square(lst)
		self.assertEqual(result, [False, False, True, False, False, False, True])
		