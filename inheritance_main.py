# Parent class (Base class)
class Employee:

    # Constructor to initialize the employee's name and ID
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # Method to display the employee's details
    def showDetails(self):
        print(f"The name of Employee {self.id} is {self.name}")

# Child class (Derived class) inheriting from Employee
class Programmer(Employee):

    # Method specific to the Programmer class
    def showLanguage(self):
        print("The default language is Python")

# Creating an object of the Employee class
e1 = Employee("Rohan Das", 400)

# Calling the Employee class method
e1.showDetails()

# Creating an object of the Programmer class
# Programmer automatically inherits the constructor (__init__)
# and showDetails() method from the Employee class.
e2 = Programmer("Harry", 4100)

# Calling the inherited method from the Employee class
e2.showDetails()

# Calling the method defined in the Programmer class
e2.showLanguage()
