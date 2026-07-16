# Example of functions

# Function to calculate the arithmetic mean of two numbers
def calculateMean(a, b):
    mean = (a + b) / 2
    print(mean)

# Function to check which number is greater
def isGreater(a, b):
    if a > b:
        print("First number is greater")
    else:
        print("Second number is greater or equal")

# Defining variables and passing them to the functions
a = 9
b = 8
calculateMean(a, b)
isGreater(a, b)

# Defining another set of variables and passing them to the functions
c = 8
d = 74
calculateMean(c, d)
isGreater(c, d)
