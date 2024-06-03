#testFooEtAl.py

import unittest
import math
from fooEtAl import FooEtAl

class testFooEtAl(unittest.TestCase):

	#tests when given a Int returns the expected value
	def test_calculateVolume_CorrectInt(self):
		fooTest = FooEtAl(2)
		expected = float((4/3) * math.pi * (2**3))
		self.assertEqual(fooTest.calculateVolume(), expected)

	#tests when given a Float returns the expected value
	def  test_calculateVolume_CorrectFloat(self):
		fooTest = FooEtAl(2.2)
		expected = float((4/3) * math.pi * (2.2**3))
		self.assertEqual(fooTest.calculateVolume(), expected)

	#tests when given a value of 0 returns the expected value(0)
	def test_calculateVolume_Zero(self):
		fooTest = FooEtAl(0)
		expected = float((4/3) * math.pi * (0**3))
		self.assertEqual(fooTest.calculateVolume(), expected)

	#tests given a negative number that it raises a ValueError which is expceted since negative radius can not exist
	def test_negativeNumberInput(self):
		with self.assertRaises(ValueError):
			FooEtAl(-2)

	#tests if a non number value is entered if it errors out correctly
	def test_nonNumberInput(self):
		with self.assertRaises(ValueError):
			FooEtAl("test")

	#tests both the setRadius correctly sets the radius as well as getRadius
	def test_setAndGetRadius(self):
		fooTest = FooEtAl(2)
		fooTest.setRadius(4)
		self.assertEqual(fooTest.getRadius(), 4)

	#tests to make sure setRadius still doesnt allow negative numbers
	def test_setRadius_NegativeNumberInput(self):
		with self.assertRaises(ValueError):
			fooTest = FooEtAl(2)
			fooTest.setRadius(-2)

	#tests to make sure setRadius still doesnt allow non numbers
	def test_setRadius_NonNumberInput(self):
		with self.assertRaises(ValueError):
			fooTest = FooEtAl(2)
			fooTest.setRadius("test")

	#tests the getPi value returns the expected value
	def test_getPi(self):
		fooTest = FooEtAl(2)
		self.assertEqual(fooTest.getPi(), math.pi)

if __name__ == "__main__":
	unittest.main()
