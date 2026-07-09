# Import the Employee class from the emp.py file.
from emp import Employee

# Create an Employee object using the constructor defined in emp.py.
e = Employee("Harry")

# Print the string representation of the object.
# This automatically calls the __str__() method defined in emp.py.
print(str(e))

# Print the official (developer-friendly) representation of the object.
# This automatically calls the __repr__() method defined in emp.py.
print(repr(e))

# Access the 'name' instance variable of the Employee object.
# The variable was initialized in the __init__() method of the Employee class.
print(e.name)

# Print the length of the Employee object.
# This automatically calls the __len__() method defined in emp.py.
print(len(e))

# Call the Employee object like a function.
# This automatically invokes the __call__() method defined in emp.py.
e()
