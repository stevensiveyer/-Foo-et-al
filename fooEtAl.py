#foo-et-al.py
#This program runs the (fictional) foo et al parameterization for calculating the volume of a sphere

import math
from changeRadius import convertRadius
from calculatePi import calculatePi

constantX = float(4/3)

class FooEtAl:

	def __init__(self, radius):
		#defines the variables and constants of the foo et al. parametization
		self.radius = convertRadius(radius)
		self.pi = calculatePi()

	def getRadius(self):
		#returns the current radius
		return self.radius

	def getPi(self):
		#returns the value for pi
		return self.pi

	def setRadius(self, radius):
		#change the value of the radius for the parametization
		self.radius = convertRadius(radius)
		return 0

	def calculateVolume(self):
		#return the volume of the sphere
		return constantX * self.pi * self.radius
