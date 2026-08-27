# Simple program to demonstrate the use of the super() function
# to call the parent class constructor

# Define the parent class
class Employee:

    # Define the constructor of the parent class
    def __init__(self, name, id):
        self.name = name
        self.id = id

# Define the child class that inherits from Employee
class Programmer(Employee):

    # Define the constructor of the child class
    def __init__(self, name, id, lang):

        # Call the parent class constructor using super()
        # This initializes the name and id attributes inherited from Employee
        super().__init__(name, id)

        # Initialize the additional attribute of the Programmer class
        self.lang = lang

# Create an object of the Employee class
rohan = Employee("Rohan Das", "420")

# Create an object of the Programmer class
harry = Programmer("Harry", "2345", "python")

# Print the name inherited from the Employee class
print(harry.name)

# Print the ID inherited from the Employee class
print(harry.id)

# Print the programming language of the Programmer class
print(harry.lang)
