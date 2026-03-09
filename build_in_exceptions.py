# this is a simple example of the build in exception error
# here value should be checked wether it is between 5 and 9 if not build in exception error occurs 

# this line displays the message enter any value 
number = int(input("Enter any value: "))

# this line checks wether entered value is between 5 and 9 if not then gives us value error saying value should be between 5 and 9 
if (number<5 or number>9):
  raise ValueError("value should be between 5 and 9")
