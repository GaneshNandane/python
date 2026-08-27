# Simple program to demonstrate the use of the super() function
# with multiple inheritance

# Define the first parent class
class ParentClass1:

    # Define a method of ParentClass1
    def parent_method(self):
        print("This is the parent method of ParentClass1.")

# Define the second parent class
class ParentClass2:

    # Define a method of ParentClass2
    def parent_method(self):
        print("This is the parent method of ParentClass2.")

# Define the child class that inherits from both parent classes
class ChildClass(ParentClass1, ParentClass2):

    # Define a method of the child class
    def child_method(self):
        print("This is the Child method.")

        # Call the parent method using super()
        # Python follows the Method Resolution Order (MRO)
        # and calls parent_method() from ParentClass1 first
        super().parent_method()

# Create an object of the ChildClass
child_object = ChildClass()

# Call the child method using the child class object
child_object.child_method()
