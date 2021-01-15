import sys
import unittest

sys.path.append('../simple_calculator')

import calculator as clc

class TestCalculator(unittest.TestCase):
	"""docstring for TestCalculator"""
	def test_add(self):
		self.assertEqual(clc.add(1,2),3)
		self.assertEqual(clc.add(-1,-1),-2)
		self.assertEqual(clc.add(1,2,3,4,5),15)
	def test_multiply(self):
		self.assertEqual(clc.multiply(1,3),3)
		self.assertEqual(clc.multiply(-1,3),-3)
		self.assertEqual(clc.multiply(1,2,3,4,5),120)

if __name__=='__main__':
	unittest.main()
