# Simple program to demonstrate the use of the return statement inside a function

# Define a function that accepts the first, middle, and last names as arguments
def name(fname, mname, lname):

    # Return a greeting containing the complete name
    return "Hello, " + fname + " " + mname + " " + lname

# Call the function with the given names and print the returned value
print(name("James", "Buchanan", "Barnes"))
