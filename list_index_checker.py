# Simple program to handle different types of errors
# and access a value using an index in a list

# The try block contains code that may cause an exception
try:
    # Take an integer input from the user
    num = int(input("Enter an integer: "))
    
    # Define a list
    a = [6, 3]

    # Access and print the list element at the index provided by the user
    print(a[num])

# Handle the ValueError if the user enters a value
# that cannot be converted into an integer
except ValueError:
    print("Number entered is not an integer.")

# Handle the IndexError if the user enters an index
# that is outside the valid range of the list
except IndexError:
    print("Index Error")
