# Define a function that prints a greeting message
def hello():
    print("Hello")

# Call the function
hello()

# -------------------- Without OOP --------------------

# Storing data for multiple people using separate variables
# becomes repetitive and difficult to manage as the program grows.

Sales1 = 6000
profit1 = 2000
ad1 = 1000
# Data for Rajeev

Sales2 = 6000
profit2 = 2000
ad2 = 1000
# # Data for Vikrant

Sales3 = 6000
profit3 = 2000
ad3 = 1000
# # Data for another employee

# -------------------- With OOP --------------------

# A class acts as a blueprint for creating objects.
# It defines the attributes (data) and methods (behavior)
# that every object created from it will have.

# RailwayForm --> Class (Blueprint)

# Objects are individual instances of a class.
# Each object stores its own data while sharing the
# structure and behavior defined in the class.

# harry   --> Object (contains Harry's information)
# tom     --> Object (contains Tom's information)
# shubham --> Object (contains Shubham's information)

# Objects can also call methods defined inside the class.
# Example:
# shubham.changeName("Shubhi")
# This calls the 'changeName()' method to update
# the name stored in the 'shubham' object.
