# shorthand if else statement is used in the context of the normal if else statement but for simple conditions 
# note: shorthand if else statement should be used in the small conditions because of the readability

# simple calculation of the person if the he can vote or not 
age = int(input("Enter your age: "))
print("you can vote. ") if age>=18 else print("you can not vote. ")

# printing the largest value in both the variable 
a = 300
b = 600
print("a is greater than b") if a>b else print("b is greater than a")
