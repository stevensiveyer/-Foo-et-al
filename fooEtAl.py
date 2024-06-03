#foo-et-al.py
#This program runs the (fictional) foo et al parameterization for calculating the volume of a sphere

import math
from changeRadius import convertRadius
from calculatePi import calculatePi

constantX = float(4/3)

class FooEtAl:

	def __init__(self, radius):
		#defines the variables and constants of the foo et al. parametization
		if not isinstance(radius, (float, int)):
			raise ValueError("Entered value is not premited, value must be a positive number.")
		if radius < 0:
			raise ValueError("Entered value is not premited, value must be a positive number.")
		self.radius = (convertRadius(float(radius)))
		self.pi = float(calculatePi())

	def getRadius(self):
		#returns the current radius
		return self.radius

	def getPi(self):
		#returns the value for pi
		return self.pi

	def setRadius(self, radius):
		#change the value of the radius for the parametization
		if not isinstance(radius, (float, int)):
			raise ValueError("Entered value is not premited, value must be a positive number.")
		if radius < 0:
			raise ValueError("Entered value is not premited, value must be a positive number.")
		self.radius = convertRadius(radius)
		return 0

	def calculateVolume(self):
		#return the volume of the sphere
		return constantX * self.pi * self.radius
