import unittest
from python.src import largest_number_finder

class test_largest_number_finder(unittest.TestCase):

	def test_a_largest(self):
		self.assertEqual(5, largest_number_finder.find(5,2,3)