#main.py


from fooEtAl import FooEtAl

yesList = ["y", "yes"]

if __name__ == "__main__":
	keepGoing = True 
	while keepGoing:
	#Loop asking for radius and returning the result
	#try is used when taking input as when converting to float if it errors we know its because they entered a non-number and give another opportunity to enter a value
		try: 
			#take input from user
			r = float(input("Enter the radius of the sphere: "))
			#if makes sure the number is a positive number
			if r >= 0:
				#send to FooEtAl and calculate and return the volume to the user
				circleVolume = FooEtAl(r)
				circleVolume = circleVolume.calculateVolume()
				print("The volume of the sphere is: ", circleVolume)

				#ask to continue doing calculations
				answer = input("Would you like to calculate another volume? (Y or N)").lower()

				#Itterate over possible yes answers
				for x in range(len(yesList)):
					if yesList[x] == answer:
						#if found a entered yes, continue asking for radius measurements
						keepGoing = True
						break
					else: 
						#If not given a yes, program ends
						keepGoing = False
			else: 
				#if got here the number entered was negative
				print("Entered value is not premited, value must be a positive number.")
		except:
			#if got here the entered value was not a number
			print("Entered value is not premited, value must be a positive number.")