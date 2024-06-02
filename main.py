#main.py


from foo-et-al import FooEtAl


if __name__ == "__main__":

	circleVolume = FooEtAl(float(input("Enter the radius of the sphere")))
	print("The volume of the sphere is " + circleVolume.calculateVolume())