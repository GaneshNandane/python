# Demonstrating the use of a class method to modify a class variable.

class Employee:

    # Class variable shared by all objects of the Employee class.
    Company = "Apple"

    # Instance method to display the employee's name and company.
    def show(self):
        print(f"The name is {self.name} and Company is {self.Company}")

    # Class method to change the value of the class variable.
    @classmethod
    def changeCompany(cls, newCompany):
        cls.Company = newCompany

# Creating an Employee object.
e1 = Employee()

# Assigning a name to the employee.
e1.name = "Harry"

# Displaying the employee's details.
e1.show()

# Changing the company for all Employee objects.
e1.changeCompany("Tesla")

# Displaying the updated employee details.
e1.show()

# Printing the updated value of the class variable.
print(Employee.Company)
