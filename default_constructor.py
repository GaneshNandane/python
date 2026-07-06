# Default Constructor Example

# A default constructor is a constructor that does not take any arguments other than 'self'. It performs the same initialization for every object created
class Details:

    # Default constructor
    def __init__(self):

        # This statement executes automatically whenever an object of the class is created.
        print("Animal Crab belongs to Crustaceans group")

# Create an object of the Details class As soon as this object is created Python automatically calls __init__().
obj1 = Details()
