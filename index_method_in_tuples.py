# Example of using the index() method with a tuple

# Creating a tuple containing integer values
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)

# Finding the index (position) of the first occurrence of the value 3
# Even though 3 appears multiple times, index() returns the index of its first occurrence.
res = Tuple.index(3)

# Printing the result
print("First occurrence of 3 is:", res)
