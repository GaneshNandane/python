# simple program to calculate the total numbers of list

from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use reduce() to repeatedly add the numbers and combine them into a single value
# The lambda function takes two values at a time and adds them together
total = reduce(lambda x, y: x + y, numbers)

# Print the final sum of all the numbers
print(total)
