# in python their are two types of variables are present 
    # 1. global variable
          # global variables are the variables that are declared outside of the function body and can be access anywhere in the program 
 
    # 2. local variable
          # local variables are the variables that are declared inside the function body and can only be access inside the function body
# here is the example of the global variable
value1 = 40
print(value1)

enteredvalue = int(input("Enter any value to add into the 40: "))
def addingnumber():
# here is the example of the local variable
  value2 = 50
  # we can modify the value of the global variables in the function body by using the keyword global 
  global value1
  value1 += enteredvalue
  print(value2)

addingnumber()
print(value1)
