# this is the example of hybrid inheritance 

# Parent class
class School:

    # Method of the parent class
    def func1(self):
        print("This function is in School.")

# First child class inheriting from School
class Student1(School):

    # Method of Student1
    def func2(self):
        print("This function is in Student1.")

# Second child class inheriting from School
class Student2(School):

    # Method of Student2
    def func3(self):
        print("This function is in Student2.")

# Student3 inherits from Student1 and School
class Student3(Student1, School):

    # Method of Student3
    def func4(self):
        print("This function is in Student3.")

# Creating an object of Student3
obj = Student3()

# Calling inherited methods
obj.func1()   # Inherited from School
obj.func2()   # Inherited from Student1
