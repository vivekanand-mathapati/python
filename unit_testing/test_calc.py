import unittest
import calc

class TestCalc(unittest.TestCase):

	def test_add(self):
		self.assertEqual(calc.add(10,20),30)

	def test_divide(self):
		with self.assertRaises(ValueError) as err:
			calc.divide(10,0)

if __name__ == '__main__':
	unittest.main()