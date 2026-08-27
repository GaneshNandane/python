# Simple program to demonstrate the use of the super() function
# with simple inheritance

# Define the parent class
class ParentClass:

    # Define a method of the parent class
    def parent_method(self):
        print("This is the parent method.")

# Define the child class that inherits from the parent class
class ChildClass(ParentClass):

    # Define a method of the child class
    def child_method(self):

        # Call the parent class method using the super() function
        super().parent_method()

        # Print a message from the child class method
        print("This is the child method.")

# Create an object of the child class
child_object = ChildClass()

# Call the child class method using the child class object
child_object.child_method()
