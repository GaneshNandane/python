# checking if we can drive or not through conditional operators using with if else structure 
# we are taking input from the user and checking if the input is greater or smaller based on the condition 

age= int(input("Enter your age: "))
print("Your age is:",age)
# conditional operators
# performing all conditions on the variable (number)
# > < >= <= == !=
print(age>18)
print(age<=18)
print(age==18)
print(age!=18)

# checking if the age is greater or smaller if the age is greater then you can drive if not then you can not 
if(age>18):
    print("You can drive")
    print("Yes")
else:
    print("You cannot drive")
    print("No")
    print("Yay!")
