#main.py


from fooEtAl import FooEtAl


if __name__ == "__main__":
	keepGoing = True 
	while keepGoing:
		circleVolume = FooEtAl(float(input("Enter the radius of the sphere: ")))
		circleVolume = circleVolume.calculateVolume()
		print("The volume of the sphere is: " + str(circleVolume))
		if "N" == input("Would you like to calculate another volume? (Y or N)"):
			keepGoing = False