# documenting the code and printing the square name of the square function

# documenting the function with the docstrings imidialtelly after function definition 
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

# printing the documentation of the function 
print(square.__doc__)

# Printing the function's name 
print(square.__name__)
