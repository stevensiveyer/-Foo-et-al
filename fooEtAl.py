#foo-et-al.py
#This program runs the (fictional) foo et al parameterization for calculating the volume of a sphere

import math
from changeRadius import convertRadius
from calculatePi import calculatePi

#constant value (4/3) used in the calculation of volume
constantX = float(4/3)

class FooEtAl:

	#defines the variables and constants of the foo et al. parametization
	def __init__(self, radius):
		#tests and makes sure that the entered radius is number and non negative, if it is it returns a error
		if not isinstance(radius, (float, int)):
			raise ValueError("Entered value is not premited, value must be a positive number.")
		if radius < 0:
			raise ValueError("Entered value is not premited, value must be a positive number.")
		#sets the variables used for the calculations of volume
		self.radius = radius
		self.radius3 = (convertRadius(float(radius)))
		self.pi = float(calculatePi())

	#returns the current radius
	def getRadius(self):
		return self.radius

	#returns the value for pi	
	def getPi(self):		
		return self.pi

	#change the value of the radius for the parametization
	def setRadius(self, radius):
		#tests and makes sure that the entered radius is number and non negative, if it is it returns a error
		if not isinstance(radius, (float, int)):
			raise ValueError("Entered value is not premited, value must be a positive number.")
		if radius < 0:
			raise ValueError("Entered value is not premited, value must be a positive number.")
		#sets the radius to new value inputted value
		self.radius = radius
		self.radius3 = convertRadius(float(radius))
		return 0

	#return the volume of the sphere
	def calculateVolume(self):
		return constantX * self.pi * self.radius3
