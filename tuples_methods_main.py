# Simple program to demonstrate tuple methods

# Define a tuple
tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)

# Use the count() method to find how many times
# the value 3 occurs in the tuple
res = tuple1.count(3)

# Print the number of times 3 occurs in the tuple
print("Count of 3 in tuple1 is:", res)

# Use the index() method to find the first occurrence of 3
res = tuple1.index(3)

# Print the index of the first occurrence of 3
print("Index of the first 3 is:", res)

# Find the first occurrence of 3 between index 4 and index 7
# The ending index 8 is not included
res = tuple1.index(3, 4, 8)

# Print the index where 3 is found
print("Finding the first 3 from index 4 to 7:", res)

# Use the len() function to find the number of elements in the tuple
res = len(tuple1)

# Print the length of the tuple
print("Length of tuple is:", res)
