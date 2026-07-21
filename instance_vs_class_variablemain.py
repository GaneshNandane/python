# Creating a class named Employee
class Employee:

    # Class variables (shared by all Employee objects)
    companyName = "Apple"
    noOfEmployees = 0

    # Constructor: called automatically whenever a new Employee object is created
    def __init__(self, name):

        # Instance variable to store the employee's name
        self.name = name

        # Instance variable to store the default raise amount
        self.raise_amount = 0.02

        # Increment the total number of employees
        Employee.noOfEmployees += 1

    # Method to display employee details
    def showDetails(self):

        # self.companyName:
        # - Uses the object's companyName if it exists.
        # - Otherwise, uses the class variable companyName.
        #
        # self.noOfEmployees:
        # - Since the object doesn't have this variable,
        #   Python uses the class variable noOfEmployees.
        print(
            f"The name of the Employee is {self.name} "
            f"and the raise amount in {self.noOfEmployees} sized "
            f"{self.companyName} is {self.raise_amount}"
        )

# ---------------- Creating the first employee ----------------

# Creates an Employee object named "Harry"
emp1 = Employee("Harry")

# Changes only emp1's raise amount (instance variable)
emp1.raise_amount = 0.3

# Creates an instance variable companyName for emp1.
# This hides the class variable companyName for this object only.
emp1.companyName = "Apple India"

# Display details of emp1
emp1.showDetails()

# ---------------- Changing the class variable ----------------

# Changes the companyName for the entire Employee class.
# This affects only objects that do NOT have their own companyName.
Employee.companyName = "Google"

# Prints the class variable
print(Employee.companyName)

# ---------------- Creating the second employee ----------------

# Creates another Employee object
emp2 = Employee("Rohan")

# Creates an instance variable companyName for emp2.
# This overrides the class variable only for emp2.
emp2.companyName = "Nestle"

# Display details of emp2
emp2.showDetails()
