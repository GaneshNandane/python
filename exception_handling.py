# exceptions in python are used to handle risky codes that might terminate the whole system or other code bases
# note: exceptions handling handles runtime errors
# it's syntax is 
        # try:
        #      #statements which could generate 
        #      #exception
        # except:
        #    #Soloution of generated exception

# code for the value error 
# here the user might enter some float value to the console by accidentlly or by curiosity and if our code is large below and uses that values it might be risky to be handle this value it might get some unexpected output for this reason the exception handling is there in the python 
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")


# code for zero division error
# here the user enters the number according to the value result is get calculated to the console there is one conditon where user might enter zero but logically zero cant divide any number so the error might occur in the program and the script we are running might give us unexpected errors 
try:
  num = int(input("Enter an number: "))
  print(100/num)
except:
  print("An error occured")

# using multiple exceptions in one block
# we can use multiple exceptions in one block by seperating it with the quama (,) here the both conditions are get checked
try:
  num = int(input("Enter an number: "))
  print(100/num)
except(ValueError, ZeroDivisionError):
  print(" value entered by the user is invalid input or divide by zero")
