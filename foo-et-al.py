#foo-et-al.py
#This program runs the (fictional) foo et al parametization for calculating the volume of a sphere

import math
from changeRadius import convertRadius
from findPi import calculatePi

class FooEtAl:

	def __init__(self, radius):
		#defines the variables and constants of the foo et al. parametization
		self.radius = convertRadius(radius)
		self.pi = calculatePi()
		self.constantX = (4/3)

	def getRadius(self):
		#returns the current radius
		return self.radius

	def getPi(self):
		#returns the value for pi
		return self.pi

	def changeRadius(self, radius)
		#change the value of the radius for the parametization
		self.radius = convertRadius(radius)
		return 0

	def calculateVolume(self):
		#return the 
		return constantX * pi * radius
