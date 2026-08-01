# Employee class
class Employee:

    # Constructor to initialize the employee's name
    def __init__(self, name):
        self.name = name

    # Function to display the employee's name
    def show(self):
        print(f"The name is {self.name}")

# Dancer class
class Dancer:

    # Constructor to initialize the dance style
    def __init__(self, dance):
        self.dance = dance

    # Function to display the dance style
    def show(self):
        print(f"The dance is {self.dance}")

# DancerEmployee class inherits from both Employee and Dancer
# (Example of Multiple Inheritance)
class DancerEmployee(Employee, Dancer):

    # Constructor to initialize both the dance style and the name
    def __init__(self, dance, name):

        # Storing the dance style
        self.dance = dance

        # Storing the employee's name
        self.name = name

# Creating an object of the DancerEmployee class
o = DancerEmployee("Kathak", "Shivani")

# Printing the employee's name
print(o.name)

# Printing the dance style
print(o.dance)

# Calling the show() function
# Since Employee is listed first in the inheritance list,
# Employee's show() method is called instead of Dancer's.
o.show()

# Printing the Method Resolution Order (MRO)
# MRO tells Python the order in which it searches for methods.
print(DancerEmployee.mro())
