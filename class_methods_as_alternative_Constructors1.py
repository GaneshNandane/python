# Demonstrating the use of class methods as alternative constructors.

class Employee:

    # Constructor to initialize the employee's name and salary.
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Class method that creates an Employee object from a string.
    # The string should be in the format: "name-salary".
    @classmethod
    def fromStr(cls, string):
        name, salary = string.split("-")
        return cls(name, int(salary))


# Creating an Employee object using the regular constructor.
e1 = Employee("Harry", 12000)

print(e1.name)
print(e1.salary)

# Creating an Employee object using the class method.
string = "John-12000"
e2 = Employee.fromStr(string)

print(e2.name)
print(e2.salary)
