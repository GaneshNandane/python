# for importing any external library or module we import it by using import keyword followed by the library name 

# this line of code imports all functionalities of the math library to this file
from math import *

# this line of code imports the library math to this respective file 
import math


# this line of code imports the specific functions that are present in the math library like sqrt and pi to be able to use it in our this file
from math import sqrt, pi

# this line of code imports the library with the user defined specified name 
import math as m

# this line prints the squre root of 9
# the difference is it uses user defined name to the specified library in this case math library
print(m.sqrt(9))

# this line also prints the square root of 9
# the difference is it uses normal math library name as it is as of the name present in
print(math.sqrt(9))

# this line also prints the square root of 9 
# the difference is it does't search the whole math library for a specific function in this case sqrt it directlly serch for sqrt function definition inside the math library think of it as the asscending ordered phone directory 
print(sqrt(9))

# this line prints the value of pi
print(pi)

# this function dir is used to know more about the module or library this function displays all the function names that are present in the specified library or module
print(dir(math))










