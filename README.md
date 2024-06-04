#  Foo et al
 The fictional Foo et al parameterization for calculating the volume of a sphere 

there are five python files part of this software package
1. foo-et-al.py
2. changeRadius.py
3. calculatePi.py
4. main.py
5. testFooEtAl.py

foo-et-al.py is where the initialization of all the variables necessary for the volume of the sphere are created and the calculation using the Foo et al parameterization occurs to calculte the volume of the sphere. This is the main code that will be used and imported when being used in other projects with 

changeRadius.py has a function that given the radius of the sphere makes the necessary changes that are defined by the Foo et al. parameterization (converting) and returns that value.

calculatePi.py has a function where calculations to find pi are done and returned

main.py is the driver code for anyone to use the program to calculate. It involves a looping request to enter a radius and returning the result and asking if they want to continue looping. If a yes answer is given it will continue otherwise it will not and the code will end. The idea of checking if no was entered correctly was considered but the decision not to was made to save a minor amount of storage and this only affects random answers and incorrect spellings of yes or y

testFooEtAl.py does unit tests on fooEtAl.py to make sure that it is still working as intended 


The main idea behind this software package is to allow for easy use of the Foo Et Al. software in other packages just by adding this folder in the directory of another piece of software and import as well as access to the other variables used in the paramerterization when more scientific discoveries are made. 