# Simple program to demonstrate the use of the __dict__ attribute

# Define a class named Person
class Person:

    # Define the constructor of the class
    def __init__(self, name, age):
        # Create an instance variable to store the person's name
        self.name = name

        # Create an instance variable to store the person's age
        self.age = age

# Create an object of the Person class
P = Person("John", 30)

# Display the object's instance attributes in the form of a dictionary
print(P.__dict__)
