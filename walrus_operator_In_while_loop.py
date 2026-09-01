# Simple program to demonstrate the use of the walrus operator (:=)

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Get the length of the list and assign it to 'n'
# using the walrus operator while checking if the length is greater than 0
while (n := len(numbers)) > 0:

    # Remove and print the last element of the list
    print(numbers.pop())
