# ---------------------- MAP ----------------------

# Function to calculate the cube of a number
def cube(x):
    return x * x * x

# Calling the function directly
print(cube(2))   # Output: 8

# List of numbers
l = [1, 2, 4, 6, 4, 3]

# Creating an empty list to store cube values
newl = []

# Using a for loop to calculate the cube of each element
for item in l:
    newl.append(cube(item))

# Printing the new list containing cube values
print(newl)

# Using map() with a lambda function to calculate cubes
# map() applies the function to every element of the list
newl = list(map(lambda x: x * x * x, l))

# Printing the result
print(newl)

# ---------------------- FILTER ----------------------

# Function that returns True if the number is greater than 2
def filter_function(a):
    return a > 2

# filter() keeps only the elements for which the function returns True
newnewl = list(filter(filter_function, l))

# Printing the filtered list
print(newnewl)

# ---------------------- REDUCE ----------------------

# Importing the reduce function
from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Function to add two numbers
def mysum(x, y):
    return x + y

# reduce() repeatedly applies the function to combine
# all elements of the list into a single value
result = reduce(mysum, numbers)

# Printing the final sum
print(result)
