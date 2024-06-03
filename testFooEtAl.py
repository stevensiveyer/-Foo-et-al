#testFooEtAl.py

import unittest
import math
from fooEtAl import FooEtAl

class testFooEtAl(unittest.TestCase):

	def test_calculateVolume_CorrectInt(self):
		fooTest = FooEtAl(2)
		expected = float((4/3) * math.pi * (2**3))
		self.assertEqual(fooTest.calculateVolume(), expected)

	def  test_calculateVolume_CorrectFloat(self):
		fooTest = FooEtAl(2.2)
		expected = float((4/3) * math.pi * (2.2**3))
		self.assertEqual(fooTest.calculateVolume(), expected)

	def test_calculateVolume_Zero(self):
		fooTest = FooEtAl(0)
		expected = float((4/3) * math.pi * (0**3))
		self.assertEqual(fooTest.calculateVolume(), expected)

	def test_negativeNumberInput(self):
		with self.assertRaises(ValueError):
			FooEtAl(-2)

	def test_nonNumberInput(self):
		with self.assertRaises(ValueError):
			FooEtAl("test")

	def test_setAndGetRadius(self):
		fooTest = FooEtAl(2)
		fooTest.setRadius(4)
		self.assertEqual(fooTest.getRadius(), 4)

	def test_setRadius_NegativeNumberInput(self):
		with self.assertRaises(ValueError):
			fooTest = FooEtAl(2)
			fooTest.setRadius(-2)

	def test_setRadius_NonNumberInput(self):
		with self.assertRaises(ValueError):
			fooTest = FooEtAl(2)
			fooTest.setRadius("test")

	def test_getPi(self):
		fooTest = FooEtAl(2)
		self.assertEqual(fooTest.getPi(), math.pi)

if __name__ == "__main__":
	unittest.main()
