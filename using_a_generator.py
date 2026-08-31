# Simple program to demonstrate the use of a generator

# Define a generator function
def My_Generator():

    # Generate numbers from 0 to 4 using a for loop
    for i in range(5):

        # Yield the current value and pause the function
        # until the next value is requested
        yield i

# Create a generator object by calling the generator function
gen = My_Generator()

# Iterate through the generator and get each value one at a time
for i in gen:

    # Print the generated value
    print(i)
