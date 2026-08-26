# Simple program to demonstrate string length and string slicing

# Define a string
fruit = "Mango"

# Find the length of the string using the len() function
mangoLen = len(fruit)

# Print the length of the string
print(mangoLen)

# Print characters from index 0 up to, but not including, index 4
print(fruit[0:4])

# Print characters from index 1 up to, but not including, index 4
print(fruit[1:4])

# Print characters from the beginning up to, but not including, index 5
print(fruit[:5])

# Print characters from index 0 up to the index calculated as -3
print(fruit[0:-3])

# Print characters from the beginning up to, but not including, the last 3 characters
print(fruit[:len(fruit)-3])

# Try to print characters from index -3 up to, but not including, index 1
# Since the starting index comes after the ending index, this returns an empty string
print(fruit[-3:1])

# Quick Quiz

# Define a string
nm = "Harry"

# Print characters from index -4 up to, but not including, index -2
print(nm[-4:-2])
