# Example of using a constructor (__init__) in a class

# Defining a class named MyClass
class MyClass:

    # Constructor that is automatically called
    # whenever a new object is created
    def __init__(self, name):

        # Storing the value of 'name' in the object's instance variable
        self.name = name

    # Method to print the name stored in the object
    def print_name(self):
        print(self.name)

# Creating the first object and passing "John" to the constructor
obj1 = MyClass("John")

# Creating the second object and passing "Jane" to the constructor
obj2 = MyClass("Jane")

# Calling the print_name() method for the first object
obj1.print_name()

# Calling the print_name() method for the second object
obj2.print_name()
