# function to double the value 

def double (x):
    return x*2

# printing the doubled value 
print(double(5))

# lambda (anonymous) function to double the value 
double=lambda x:x*2

# printing the doubled value using the lambda (anonymous) function
print(double(5))

# lambda (anonymous) function to calculate the cube of the value 
cube=lambda x:x*x*x

# printing the cube value using the lambda (anonymous) function
print(cube(5))

# lambda (anonymous) function to calculate the average of three numbers
avg=lambda x, y, z:(x+y+z)/3

# printing the average of three numbers using the lambda (anonymous) function
print(avg(3,5,10))

# it is a higher order function means that we are providing the another function as a parameter to the main function 
# here fx is the function and the value is that functions value 
    # here fx function is a anonymous lambda function that is defined in the print statement that calculates the square of the value provided by the user 
    
def appl(fx,value):
    return 6 + fx(value)
print(appl(lambda x: x*x,2))
