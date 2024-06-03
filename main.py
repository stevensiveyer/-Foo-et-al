#main.py


from fooEtAl import FooEtAl


if __name__ == "__main__":
	keepGoing = True 
	while keepGoing:
	#Loop asking for radius and returning the result
		try: 
			r = float(input("Enter the radius of the sphere: "))
			if r > 0:
				circleVolume = FooEtAl(r)
				circleVolume = circleVolume.calculateVolume()
				print("The volume of the sphere is: ", circleVolume)

				#ask to continue doing calculations
				if "Y" != input("Would you like to calculate another volume? (Y or N)"):
					keepGoing = False
			else: 
				print("Entered value is not premited, value must be a positive number.")
		except:
			print("Entered value is not premited, value must be a positive number.")