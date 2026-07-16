# This is a simple example of a generator function.

# Defining a generator function that generates numbers from 0 to 49999
def My_Generator():

    # Looping from 0 to 49999
    for i in range(50000):

        # Yielding one value at a time instead of returning all values at once
        yield i

# Creating a generator object
gen = My_Generator()

# Getting the first generated value
print(next(gen))

# Getting the second generated value
print(next(gen))

# Getting the third generated value
print(next(gen))

# Iterating over the remaining values in the generator
for j in gen:
    print(j)
