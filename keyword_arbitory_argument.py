# Example of keyword arbitrary arguments (**kwargs)

# Defining a function that accepts any number of keyword arguments
# The **name parameter collects all keyword arguments into a dictionary.
def name(**name):

    # Accessing the values using their keys and printing the full name
    print("Hello,", name["fname"], name["mname"], name["lname"])

# Calling the function by passing keyword arguments
# The order of the arguments does not matter because they are identified by their keys.
name(mname="Buchanan", lname="Barnes", fname="James")
