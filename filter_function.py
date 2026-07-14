# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use the filter() function to keep only the even numbers.The lambda function returns True for even numbers (x % 2 == 0) and False for odd numbers.
evens = filter(lambda x: x % 2 == 0, numbers)

# Convert the filter object into a list and print it.
print(list(evens))
